import pds_rest
import json
# Get PDS accounts
all_accounts = json.dumps(pds_rest.get_accounts())
accounts_dict = json.loads(all_accounts)
items = len(accounts_dict['data'])
print("Get count of deployments for each account the Bearer Token has access to... CSV format")
print("")
print("Account ID, Account Name, Number of Deployments")
for x in range(items):
    # each account tenant and project print how many deployments there are.
    account_id = json.dumps(accounts_dict["data"][x]["id"])
    account_name = json.dumps(accounts_dict["data"][x]["name"])
    account_id = account_id.replace('"', '')
    
    tenant_id = pds_rest.get_tenants(account_id)
    tenant_id = json.dumps(tenant_id["data"][0]["id"])
    tenant_id = tenant_id.replace('"', '')
    
    ten_proj = pds_rest.get_tenant_projects(tenant_id)
    ten_proj = json.dumps(ten_proj["data"][0]["id"])
    ten_proj = ten_proj.replace('"', '')
    
    deployments = pds_rest.get_deployments(ten_proj)
    item_dict = json.loads(json.dumps(deployments))

    num_deployments = len(item_dict["data"])
    
    print(account_id + "," + account_name + "," + str(num_deployments))
