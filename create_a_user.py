import requests
import json

# Update the values of these variables
opensearch_domain_endpoint = "<domain endpoint ex. https://search-workshop-domain-xxxxxx.us-east-1.es.amazonaws.com>"
user_name_auth = "<user name for the user authenticating the HTTP request>"
password_auth = "<password for the user authenticating the HTTP request>"
user_name_for_new_user = "<user name for the new user that will be created>"
password_for_new_user = "<password for the new user the will be created. Passworkd must have 1 case, 1 upper case, 1 number, 1 special character"
roles_to_map_user_to = ["<role_name>"]
backend_roles_to_map_user_to = ["<role_name>"]

# Create the User
request_body = {
		"password": password_for_new_user, 
		"opendistro_security_roles": roles_to_map_user_to,
		"backend_roles": backend_roles_to_map_user_to
}

create_user = requests.put(
  opensearch_domain_endpoint.rstrip('/') + '/_plugins/_security/api/internalusers/' + user_name_for_new_user,
  auth = (user_name_auth, password_auth),
  headers = {'Content-type': 'application/json'},
  data = json.dumps(request_body)
)

print(create_user.text)