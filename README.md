## Mapping a user to an OpenSearch role 

The following snippet of Python code maps a user to an OpenSearch role. 

Before running the code snippet ensure you update any value surrounded by ```< >``` brackets

```
import requests
import json

request_body = [
	{
		"op": "add", 
		"path": "/<backend_roles OR users>/-",
		"value": "<name_of_user OR ARN_of_IAM>"
	}
]

map_user_to_IAM_role = requests.patch(
  '<open_search_domain_endpoint>/_plugins/_security/api/rolesmapping/<role_name>',
  auth = ('<user_name>', '<password>'),
  headers = {'Content-type': 'application/json'},
  data = json.dumps(request_body)
)

print(map_user_to_IAM_role.text)
```

You can also reference [mapping_a_user_to_an_opensearch_role.py](https://github.com/ev2900/OpenSearch_User_Role_Premission_Managment/blob/main/mapping_a_user_to_an_opensearch_role.py) for a scripted version of the code sample

## Removing a user from an OpenSearch role mapping 

The following snippet of Python code removes a user from an OpenSearch role. OpenSearch stores user role mapping as separate lists for backend roles and users. Unfortunately the HTTP ```PATCH``` operation does not support removing an object from a list using the value name of the object. Instead ```PATCH``` supports deleting objects based on the index ie. position of the object in the list. Consequently the Python code snippet below has two parts. The first part finds the index position of the user. The second part uses the index position to remove the user from the role mapping.

Before running the code snippet ensure you update any value surrounded by ```< >``` brackets

```
import requests
import json

# 1. Find the index position of the user
get_user_mapped_to_IAM_role = requests.get(
  '<open_search_domain_endpoint>/_plugins/_security/api/rolesmapping/<role_name>',
  auth = ('<user_name>', '<password>'),
  headers = {'Content-type': 'application/json'}
)

users_or_backend_users_mapped_to_role = get_user_mapped_to_IAM_role.json()['<role_name>']['<backend_roles OR users>']

for index_position, name in enumerate(users_or_backend_users_mapped_to_role): 
	if name == '<name_of_user>':
		index_position_to_delete = index_position

# 2. Use the index position to remove the user from the role mapping
request_body = [
	{
		"op": "remove", 
		"path": "/<backend_role OR users>/" + str(index_position_to_delete),
		"value": ""
	}
]

map_user_to_IAM_role = requests.patch(
  'https://<open_search_domain_endpoint>/_plugins/_security/api/rolesmapping/<role_name>',
  auth = ('<user_name>', '<password>'),
  headers = {'Content-type': 'application/json'},
  data = json.dumps(request_body)
)

print(map_user_to_IAM_role.text)
```
