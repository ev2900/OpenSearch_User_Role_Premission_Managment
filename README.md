## Map a users to an OpenSearch role 

The following snippet of Python code maps a user to an OpenSearch role. Users can either be mapped to an OpenSearch role as a user or backend role. To adjust which type a user is mapped as the value of the ```path``` in the request body must be either ```backend_roles``` or ```users```. 

Before running the code snippet ensure you update any valued surrounded by ```< >``` brackets

```
import requests
import json

request_body = [
	{
		"op": "add", 
		"path": "/<backend_role OR users>/-",
		"value": "arn:aws:iam::392052658792:role/ab3-databrew-service-role"
	}
]

map_user_to_IAM_role = requests.patch(
  '<open_search_domain_endpoint>/_plugins/_security/api/rolesmapping/<role_name>',
  auth = ('<user_name>', '<password>'),
  headers = {'Content-type': 'application/json'},
  data = json.dumps(request_body))

print(map_user_to_IAM_role.text)
```

