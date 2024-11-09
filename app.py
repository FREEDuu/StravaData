import streamlit as st
from utils import get_weeks, get_data_run
import numpy
import plotly.graph_objs as go
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(layout="wide")

st.title('STRAVA PREMIUM DATA FOR FREE')

date_time, time_week_x = get_weeks( int((os.getenv('YEARS'))) )
data_run, km, min, gain = get_data_run(time_week_x)

fig_distance = go.Figure()
fig_hr = go.Figure()
fig_gain = go.Figure()

fig_distance.add_trace(go.Scatter(x = time_week_x, y = km))
fig_gain.add_trace(go.Scatter(x = time_week_x, y = gain))
fig_hr.add_trace(go.Scatter(x = time_week_x, y = min))

col1, col2 = st.columns([3,2])

with col1:
    st.write('')
    st.write('')
    st.write('Distance Chart')
    st.plotly_chart(fig_distance)

with col2:
    st.write('')
    st.write('')
    st.write('Elevation Gain Chart')
    st.plotly_chart(fig_gain)

st.write('')
st.write('')
st.write('Hour Chart')
st.plotly_chart(fig_hr)