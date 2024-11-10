import requests
import json
from dotenv import load_dotenv
import os


def get_activities():

    load_dotenv()
    
    access_token = os.getenv('ACCESS_TOKEN')
    pages = int( os.getenv('PAGES') )
    per_page = 200

    data_dumps = []

    for page in range(1, pages+1):

        response = requests.get(
            url = f'https://www.strava.com/api/v3/athlete/activities?access_token={access_token}&per_page={per_page}&page={page}',
        )

        data_dumps.append(response.json())
    
    with open("data_runs.json", "w") as outfile:

        json.dump(data_dumps, outfile, indent=4)
        
def autorization(client_id, client_secret):

    header = {
        'client_id' : client_id,
        'client_secret' : client_secret,
        'response_type' : 'code',
        'scope' : 'activity:read_all',
        'redirect_uri' : 'localhost'
    }

    response = requests.get(
        url = f'http://www.strava.com/oauth/authorize?client_id={client_id}&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=activity:read_all',
        headers=header
    )

    

