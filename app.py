import streamlit as st
import datetime
import requests
'''
# TaxiFareModel front
'''
passenger_count = st.sidebar.slider("Passenger Count",1,8,3)
pickup_longitude = st.sidebar.number_input("Pickup Longitude",40.00,50.00,41.00)
pickup_latitude = st.sidebar.number_input("Pickup Latitude",-79.00,-72.00,-74.00)
dropoff_longitude = st.sidebar.number_input("Dropoff Longitude",40.00,50.00,40.50)
dropoff_latitude = st.sidebar.number_input("Dropoff Latitude",-79.00,-72.00,-73.80)
date_in = st.sidebar.date_input("Date",datetime.date(2021,5,8))
time_in = st.sidebar.time_input("Hour", datetime.time(10,00))

url = "https://joss-taxifare-api-7wgexjijda-ew.a.run.app/predict_fare?"\
    +"key=2012-10-06%2012:10:20.0000001"\
    +f"&pickup_datetime={date_in.year}-{date_in.month}-{date_in.day}%2012:10:20%20UTC"\
    +f"&pickup_longitude={pickup_longitude}"\
    +f"&pickup_latitude={pickup_latitude}"\
    +f"&dropoff_longitude={dropoff_longitude}"\
    +f"&dropoff_latitude={dropoff_latitude}"\
    +f"&passenger_count={passenger_count}"

response = requests.get(url).json()
dict_result = dict(response)
dict_result["prediction"]
