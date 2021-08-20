
import streamlit as st
import requests
import datetime

'''
# TaxiFareModel front
'''



pickup_datetime = st.text_input('Enter pickup_datetime:'),
pickup_longitude = st.text_input('Enter pickup_longitude:'),
pickup_latitude = st.text_input('Enter pickup_latitude:'),
dropoff_longitude = st.text_input('Enter dropoff_longitude:'),
dropoff_latitude = st.text_input('Enter dropoff_latitude:'),
passenger_count=input = st.text_input('Enter passenger_count:')



url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':
    pass


# 2. Let's build a dictionary containing the parameters for our API...


params = {
   "pickup_datetime": pickup_datetime,
   "pickup_longitude": pickup_longitude,
   "pickup_latitude": pickup_latitude,
   "dropoff_longitude": dropoff_longitude,
   "dropoff_latitude": dropoff_latitude,
   "passenger_count": passenger_count
}

# 3. Let's call our API using the `requests` package...

response = requests.get(url,
    params=params
)

# 4. Let's retrieve the prediction from the **JSON** returned by the API...
st.json(response.json())
## Finally, we can display the prediction to the user
