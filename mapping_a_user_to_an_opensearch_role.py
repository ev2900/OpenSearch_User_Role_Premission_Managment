import requests
import json

# Update the values of these variables
opensearch_domain_endpoint = "domain endpoint ex. https://search-workshop-domain-xxxxxx.us-east-1.es.amazonaws.com"
user_name_auth = "<user name for the user authenticating the HTTP request"
password_auth = "<password for user authenticating the HTTP request>"
role_type = "<backend_roles OR users>"
role_name = "<role name ex. all_access>"
user_to_map = "<user name or IAM ARN to mapp to the role name"

# Map user to role
request_body = [
	{
		"op": "add", 
		"path": "/" + role_type + "/-",
		"value": user_to_map 
	}
]

map_user_to_IAM_role = requests.patch(
  opensearch_domain_endpoint.rstrip('/') + '/_plugins/_security/api/rolesmapping/' + role_name,
  auth = (user_name_auth, password_auth),
  headers = {'Content-type': 'application/json'},
  data = json.dumps(request_body)
)

print(map_user_to_IAM_role.text)
