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

if you're not a developer, or you dont want to follow the STRAVA api , just follow the first page of instructions !!
![image](https://github.com/user-attachments/assets/6a3fca9d-9c45-4a9c-8706-9a79d8cfbe0a)


in the file .env change 

```env
ACCESS_TOKEN=YOUR_PERSONAL_ACCESS_TOKEN
PAGES=4 #every page read max 200 runs, so with 4 you can read 800 activities
YEARS=2 #how many years in the past you want to see 
```
When you click the 'Ottieni Dati' button, the script will generate a runs{code}.json that contains all your runs

To get your personal access token, please refer to the official Strava Doc : https://developers.strava.com/

after that you just have to initialize the streamlit app by :
```bash
streamlit run app.py
```

and enjoy the charts :D

this is the results of my runs ( in the last 4 years) :

![Screenshot from 2024-11-11 13-10-44](https://github.com/user-attachments/assets/facd3d8d-09c2-4412-82ac-04895ba77fe3)



## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
Feel free to write me for anything
