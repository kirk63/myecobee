###########################################################################################
#
#   Created by Kirk Sievers May 2022
#   Retrieves authorization PIN from ecobee
#   This PIN is needed to add the custom application to your account
#
###########################################################################################

import requests
client_id="IJwiSoWgXCqW0ymCcANTL4rMVJUn1KI9"

url = "https://api.ecobee.com/authorize?response_type=ecobeePin&client_id=" + client_id + "&scope=smartwrite"

payload={}
headers={}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

# Sample response
# {
#   "ecobeePin": "NMJM-VMPL",
#   "code": "kVBer7TWljKza2o_Nt--IPa2",
#   "interval": 5,
#   "expires_in": 900,
#   "scope": "openid,offline_access,smartwrite"
# }