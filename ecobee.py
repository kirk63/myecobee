###########################################################################################
#
#   Created by Kirk Sievers April 2021
#   Authorizes a custom application with ecobee
#   Once authorized an access token and refresh token can be requested
#   The access token has a time to live and must be refreshed using the refresh token
#
#
###########################################################################################
import requests
import json
import os
import datetime

cur_time = datetime.datetime.now().strftime("%a %Y-%m-%d %H:%M:%S") + " :: "

# Set to True to print just about everything
debug = True


def clean_json(text):
    clean_text = json.dumps(text)
    clean_text = clean_text.replace('"', '')
    return clean_text


def get_refresh_token(r_key):
    local_params = (
        ('grant_type', 'refresh_token'),
        ('code', r_key["refresh_token"]),
        ('client_id', key["client_id"]),
    )

    local_response = requests.get('https://api.ecobee.com/token', headers=headers, params=local_params)
    # print(local_response.json())

    r_key["access_token"] = clean_json(local_response.json()["access_token"])

    # print("Now using ACCESS_TOKEN: {}".format(r_key["access_token"]))
    save_key(r_key)
    return r_key







def save_key(s_key):
    try:
        s_key
    except NameError:
        print('{}Key not valid'.format(cur_time))
        quit()

    # todo set the permissions on the file when it is created
    if os.path.exists(key_file):
        # f = open(key_file)
        f = open(key_file, "w")
        f.write(json.dumps(s_key))
        f.close()
    else:
        print("{}File did not exist".format(cur_time))
        f = open(key_file, "w")
        f.write(json.dumps(s_key))
        f.close()

    return s_key


def get_key():
    g_key = {}

    if os.path.exists(key_file):
        f = open(key_file)
        g_key = json.loads(f.read())
        f.close()
        return g_key

    else:
        print("file did not exist")
        return False

    


key_file = "ecobee.json"

# code = 'm5dEodIjU5mORBEz9D-lEpCE'
# client_id = '9JUVO28TTSIC8iayWFPXa9MJ63guqp6X'
# access_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJFWXhNVEpDT0Rnek9UaERRelJHTkRCRlFqZEdNVGxETnpaR1JUZzRNalEwTmtWR01UQkdPQSJ9.eyJpc3MiOiJodHRwczovL2F1dGguZWNvYmVlLmNvbS8iLCJzdWIiOiJhdXRoMHxlYWEwZTEwYS1lMmFmLTQyMTctYTk1Ny0yMjE3MjI2ZmJiYTAiLCJhdWQiOlsiaHR0cHM6Ly9kZXZlbG9wZXItYXBwcy5lY29iZWUuY29tL2FwaS92MSIsImh0dHBzOi8vZWNvYmVlLXByb2QuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYxOTA1NDQxMywiZXhwIjoxNjE5MDU4MDEzLCJhenAiOiI5SlVWTzI4VFRTSUM4aWF5V0ZQWGE5TUo2M2d1cXA2WCIsInNjb3BlIjoib3BlbmlkIHNtYXJ0UmVhZCBvZmZsaW5lX2FjY2VzcyJ9.CtXUKR9LxFt1c8NX-i4r6gm__g7HhZZHvtJ93RwNIaB5aARb_l6VQdjIiYD31jQNK09l2Sf4PNpOf78NR_uSg5JVS36avVq__cEgSKAuUs9a0IPGXGDLzwq9QmJwSjmJzpk7J_o8oUfhpKWGpF11-cgHdKa6ofOL5NwDqzMrpV7BboGEnvk7m3gUJk12cyE9f3uGbddaeRFV2awjk7dSOrgDlnyw8WCcECQ-FwMlJO2h-ghn20nl5fi16M5-XglwBQT2SjxiAzPv7CB6hWDsqybFF2DHY7STC6X2-lBbL1B2GuvDg4URqyoVi-o2ENlWF9zJ7AHD-JhEf9SPSlGOvA'
#
# refresh_token = 'T0rjsDcd6JgLYBXFVPmI5jAVNEvoTNdhGy4ne3TsQyIo6'

# key = {
#     "ecobeePin": "NDRF-GTBK",
#     "code": "m5dEodIjU5mORBEz9D-lEpCE",
#     "client_id": "9JUVO28TTSIC8iayWFPXa9MJ63guqp6X",
#     "refresh_token": "T0rjsDcd6JgLYBXFVPmI5jAVNEvoTNdhGy4ne3TsQyIo6",
#     "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJFWXhNVEpDT0Rnek9UaERRelJHTkRCRlFqZEdNVGxETnpaR1JUZzRNalEwTmtWR01UQkdPQSJ9.eyJpc3MiOiJodHRwczovL2F1dGguZWNvYmVlLmNvbS8iLCJzdWIiOiJhdXRoMHxlYWEwZTEwYS1lMmFmLTQyMTctYTk1Ny0yMjE3MjI2ZmJiYTAiLCJhdWQiOlsiaHR0cHM6Ly9kZXZlbG9wZXItYXBwcy5lY29iZWUuY29tL2FwaS92MSIsImh0dHBzOi8vZWNvYmVlLXByb2QuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYxOTA1NDQxMywiZXhwIjoxNjE5MDU4MDEzLCJhenAiOiI5SlVWTzI4VFRTSUM4aWF5V0ZQWGE5TUo2M2d1cXA2WCIsInNjb3BlIjoib3BlbmlkIHNtYXJ0UmVhZCBvZmZsaW5lX2FjY2VzcyJ9.CtXUKR9LxFt1c8NX-i4r6gm__g7HhZZHvtJ93RwNIaB5aARb_l6VQdjIiYD31jQNK09l2Sf4PNpOf78NR_uSg5JVS36avVq__cEgSKAuUs9a0IPGXGDLzwq9QmJwSjmJzpk7J_o8oUfhpKWGpF11-cgHdKa6ofOL5NwDqzMrpV7BboGEnvk7m3gUJk12cyE9f3uGbddaeRFV2awjk7dSOrgDlnyw8WCcECQ-FwMlJO2h-ghn20nl5fi16M5-XglwBQT2SjxiAzPv7CB6hWDsqybFF2DHY7STC6X2-lBbL1B2GuvDg4URqyoVi-o2ENlWF9zJ7AHD-JhEf9SPSlGOvA"
# }

key = get_key()
if debug:
    print("\n\n\n")
    print(key)
    print("\n")



# Only run this once when a new app is added in the developer portal
do_authorize = False

# 
do_token = False
do_refresh = False

# This will attempt to get the current thermosate info regardless of the above settings
do_get_thermostats = True

headers = {
    'Content-Type': 'text/json'
}

# todo move authorize into a separate script
if do_authorize and get_key:
    params = (
        ('response_type', 'ecobeePin'),
        ('client_id', key["client_id"]),
        ('scope', 'smartRead'),
    )
    # scope can be one of smartRead or smartWrite

    response = requests.get('https://api.ecobee.com/authorize', headers=headers, params=params)

    print("{} Results from do_authorize {}".format(cur_time, response.json()))
    # {'ecobeePin': 'NDRF-GTBK', 'code': 'm5dEodIjU5mORBEz9D-lEpCE', 'interval': 5, 'expires_in': 900, 'scope': 'openid,offline_access,smartRead'}

    key["code"] = clean_json(response.json()["code"])


if do_token:
    params = (
        ('grant_type', 'ecobeePin'),
        ('code', key["code"]),
        ('client_id', key["client_id"]),
    )

    response = requests.post('https://api.ecobee.com/token', headers=headers, params=params)
    if debug:
        print("{} Results from do_token {}\n".format(cur_time, response.json()))

    if response.status_code == 401 and str(response.json()["error"]) == "authorization_pending":
        print("Please authorize the application and try again!")
        exit(11)
    if response.status_code == 401:
        print("Please authorize the application and try again!")
        exit(response.status_code)

    key["access_token"] = clean_json(response.json()["access_token"])

    save_key(key)
    if debug:
        print("{}{}\n".format(cur_time, key["access_token"]))

if do_get_thermostats:
    headers = {
        'Content-Type': 'text/json',
        'Authorization': 'Bearer ' + key["access_token"],
    }

    params = (
        ('body',
             '{"selection":\
                 {"selectionType":"registered","selectionMatch":"",\
                 "includeRuntime":true,\
                 "includeWeather":true,\
                 "includeSensors":true,\
                 "includeAlerts":true,\
                 "includeReminders":true}\
         }'),
    )

    response = requests.get('https://api.ecobee.com/1/thermostat', headers=headers, params=params)

    if debug:
        print(response.json())
        print("\n")


    status = clean_json(response.json()["status"])
    status_code = int(clean_json(response.json()["status"]["code"]))
    status_message = clean_json(response.json()["status"]["message"])

    # print("\nThermostat list request returned status code: {} message: {}\n".format(str(status_code), status_message))

    if status_code == 14:
        print("{}Token expired! Getting another.\n".format(cur_time))
        key = get_refresh_token(key)
        headers = {
            'Content-Type': 'text/json',
            'Authorization': 'Bearer ' + key["access_token"],
        }
        response = requests.get('https://api.ecobee.com/1/thermostat', headers=headers, params=params)

        status_code = int(clean_json(response.json()["status"]["code"]))
        status_message = clean_json(response.json()["status"]["message"])

        if debug:
            print(
              "\nThermostat list request returned status code: {} message: {}\n".format(str(status_code), status_message))

    if status_code == 0:
        t_id = 0
        while t_id < 2:
            t_name = clean_json(response.json()["thermostatList"][t_id]["name"])

            t_running_actualTemperature = \
                clean_json(response.json()["thermostatList"][t_id]["runtime"]["actualTemperature"])

            t_running_actualHumidity = \
                clean_json(response.json()["thermostatList"][t_id]["runtime"]["actualHumidity"])

            t_running_connected = \
                clean_json(response.json()["thermostatList"][t_id]["runtime"]["connected"])


            print("{}{} Temp: {}, Humidity: {} Connected: {}\n".format(cur_time,
                                                                     t_name,
                                                                     str(int(t_running_actualTemperature) / 10),
                                                                     t_running_actualHumidity,
                                                                     t_running_connected))

            t_id += 1

    else:
        print("{}Unhandled Status Code".format(cur_time))

