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
