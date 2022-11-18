Get a token from PDS. Then add it as a shell env var so you can use the python pds_rest_client. Token can by found by clicking the user profile in the PDS ui, it is in the bottom left corner and is a "user person" icon. Create a new bearer token and copy it to your machine.
More info here:
[https://prod.pds.portworx.com/swagger/index.html](https://prod.pds.portworx.com/swagger/index.html)

```
export BEARER_TOKEN=""
```
# Example
Example this code Gets your ID information and your project, deletes any unhealthy k8s clusters and all the deployments on them. This helps cleanup the demo.
```
import pds_rest
import json
# Get PDS accounts
all_accounts = json.dumps(pds_rest.get_accounts())
x = json.loads(all_accounts)

#For first account find all of the users in that account
account_id = json.dumps(x["data"][0]["id"], indent=4)
account_id = account_id.replace('"', '')
users = pds_rest.get_users(account_id)


#get deployment targets - k8s clusters
ten_id = pds_rest.get_tenants(account_id)
ten_id = json.dumps(ten_id["data"][0]["id"])
ten_id = ten_id.replace('"', '')
targets = pds_rest.get_deploymenttargets(ten_id)
targetjson = json.dumps(targets["data"])

#Finds unhealthy clusters, deletes all deployments on them then deletes the cluster
pds_rest.clean_unhealthy_clusters(targetjson, ten_id)
```
or download the file and run:
```
export BEARER_TOKEN="yourpdstoken"
python3 clean_up_demo.py
```