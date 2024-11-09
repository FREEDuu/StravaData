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

        request = requests.get(
            url = f'https://www.strava.com/api/v3/athlete/activities?access_token={access_token}&per_page={per_page}&page={page}',
        )

        data_dumps.append(request.json())
    
    with open("data_runs.json", "w") as outfile:

        json.dump(data_dumps, outfile, indent=4)
        
get_activities()