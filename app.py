import streamlit as st
from utils import get_weeks, get_data_run, autorization
import numpy
import plotly.graph_objs as go
from dotenv import load_dotenv
import os

st.set_page_config(layout="wide")

st.title('Segui le istruzioni')
st.write('STEP 1 --> ottieni il codice di accesso')

CLIENT_ID = ( st.secrets['CLIENT_ID'] )
CLIENT_SECRET = ( st.secrets['CLIENT_SECRET'] )
link = f'http://www.strava.com/oauth/authorize?client_id={CLIENT_ID}<&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=activity:read_all'

st.write('visita la pagina ( da browser ) e clicca su AUTORIZZA .... non chiuderla dopo aver autorizzato !')
st.link_button("Login With Strava", link)

st.write('')
st.write('STEP 1 --> Copia il codice di accesso')
st.write('Dopo aver cliccato su autorizza, verrai reinderizzato ad una pagina simile, ora devi solo copiare il codice nel link ( come in figura )')
st.image("tutorial.png", caption="Codice da copiare ")

st.write('')
st.write('STEP 3 --> Incolla il codice di accesso')
st.write('')
title = st.text_input("Incolla il Codice", "")
if st.button("Ottieni Dati", use_container_width=True):
    st.title('Wait . . .')
    autorization(CLIENT_ID, CLIENT_SECRET, title)

    st.write('')
    st.write('')
    st.title('Vai alla pagina dashboard con il codice appena inserito')