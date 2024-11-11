import requests
import json
from dotenv import load_dotenv
import os
import streamlit as st


def get_activities(access_token, code):

    load_dotenv()
    
    pages = int( st.secrets['PAGES'] )
    per_page = 200

    data_dumps = []

    for page in range(1, pages+1):

        response = requests.get(
            url = f'https://www.strava.com/api/v3/athlete/activities?access_token={access_token}&per_page={per_page}&page={page}',
        )

        data_dumps.append(response.json())

    with open(f"runs{code}.json", "w") as outfile:
        json.dump(data_dumps, outfile, indent=4)
        
def autorization(client_id, client_secret, code):

    response = requests.post(
        url = f'https://www.strava.com/oauth/token?client_id={client_id}&client_secret={client_secret}&code={code}&grant_type=authorization_code'
    )

    get_activities(response.json()['access_token'], code)
