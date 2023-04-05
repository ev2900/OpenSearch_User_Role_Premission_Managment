import requests
import json

# Update the values of these variables
opensearch_domain_endpoint = "domain endpoint ex. https://search-workshop-domain-xxxxxx.us-east-1.es.amazonaws.com"
user_name_auth = "<user name for the user authenticating the HTTP request"
password_auth = "<password for user authenticating the HTTP request>"
role_type = "<backend_roles OR users>"
role_name = "<role name ex. all_access>"
user_to_delete = "<user name or IAM ARN to mapp to the role name"

# 1. Find the index position of the user
get_user_mapped_to_IAM_role = requests.get(
  opensearch_domain_endpoint.rstrip('/') + '/_plugins/_security/api/rolesmapping/' + role_name,
  auth = (user_name_auth, password_auth),
  headers = {'Content-type': 'application/json'}
)

users_or_backend_users_mapped_to_role = get_user_mapped_to_IAM_role.json()[role_name][role_type]

for index_position, name in enumerate(users_or_backend_users_mapped_to_role): 
	if name == user_to_delete:
		index_position_to_delete = index_position

# 2. Use the index position to remove the user from the role mapping
request_body = [
	{
		"op": "remove", 
		"path": "/" + role_type + "/" + str(index_position_to_delete),
		"value": ""
	}
]

map_user_to_IAM_role = requests.patch(
  opensearch_domain_endpoint.rstrip('/') + '/_plugins/_security/api/rolesmapping/' + role_name,
  auth = (user_name_auth, password_auth),
  headers = {'Content-type': 'application/json'},
  data = json.dumps(request_body)
)

print(map_user_to_IAM_role.text)