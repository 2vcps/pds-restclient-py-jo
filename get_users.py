import pds_rest
import json
# Get PDS accounts
all_accounts = json.dumps(pds_rest.get_accounts())
x = json.loads(all_accounts)
#print(x)

#print(json.dumps(x["data"][0]["id"], indent=4))

# #For first account find all of the users in that account
account_id = json.dumps(x["data"][0]["id"], indent=4)
account_id = account_id.replace('"', '')
users = pds_rest.get_users(account_id)
print(json.dumps(users, indent=4))
