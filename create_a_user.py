import requests
import json

# Update the values of these variables
opensearch_domain_endpoint = "domain endpoint ex. https://search-workshop-domain-xxxxxx.us-east-1.es.amazonaws.com"
user_name_auth = "<user name for the user authenticating the HTTP request"
password_auth = "<password for user authenticating the HTTP request>"
user_name_for_new_user = "<user name for OpenSearch user that will be created"
roles_to_map_user_to = ["<role_name>"]
backend_roles_to_map_user_to = ["<role_name>"]

role_type = "<backend_roles OR users>"
role_name = "<role name ex. all_access>"
user_to_map = "<user name or IAM ARN to mapp to the role name"

# Create the User
request_body = {
		"password": "<password_for_new_user_must_have_1_lower_1_upper_1_number_1_special_character>", 
		"opendistro_security_roles": role_to_map_user_to,
		"backend_roles": backend_roles_to_map_user_to
}

create_user = requests.put(
  opensearch_domain_endpoint.rstrip('/') + '/_plugins/_security/api/internalusers/' + user_name_for_new_user,
  auth = (user_name_auth, password_auth),
  headers = {'Content-type': 'application/json'},
  data = json.dumps(request_body)
)

print(create_user.text)