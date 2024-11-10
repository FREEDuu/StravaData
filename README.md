# Strava Data of ALL your runs

this is a project that aim to get every avaiable data from the STRAVA API v3 and try to display everything in a friendly way just for free ( and fun :'D )

## Installation

just clone the repo with :

```bash
git clone https://github.com/FREEDuu/StravaData.git
```

change directory with : 
```bash
cd StravaData
```
and install the dependencies by : 
```bash
pip install -r requirements.txt
```
## Usage

in the file .env change 

```env
ACCESS_TOKEN=YOUR_PERSONAL_ACCESS_TOKEN
PAGES=4 #every page read max 200 runs, so with 4 you can read 800 activities
YEARS=2 #how many years in the past you want to see 
```

after change the .env file you need to populate your data_runs.json ( in the data_runs.json is just my runs for example, if you cant get your runs just rename data_runs_example.json in ---> data_runs.json and use my runs to see the results )

in order to populate the data_runs.json you just need to call a python script with ( in the StravaData directory ) : 
```bash
python3 api.py
```
or
```bash
python api.py
```

To get your personal access token, please refer to the official Strava Doc : https://developers.strava.com/

after that you just have to initialize the streamlit app by :
```bash
streamlit run app.py
```

and enjoy the charts :D

this is the results of my runs ( in the last 4 years) :

![Screenshot from 2024-11-10 19-10-09](https://github.com/user-attachments/assets/064f5ea3-dc15-4ef3-be08-b2b6bd8e382f)

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
Feel free to write me for anything
