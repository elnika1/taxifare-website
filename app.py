import streamlit as st

# '''
# # TaxiFareModel front
# '''

# st.markdown('''
# Remember that there are several ways to output content into your web page...

# Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
# ''')

# '''
# ## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count
# '''


# '''
# ## Once we have these, let's call our API in order to retrieve a prediction

# See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

# 🤔 How could we call our API ? Off course... The `requests` package 💡
# '''

# url = 'https://taxifare.lewagon.ai/predict'

# if url == 'https://taxifare.lewagon.ai/predict':

#     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

# '''

# 2. Let's build a dictionary containing the parameters for our API...

# 3. Let's call our API using the `requests` package...

# 4. Let's retrieve the prediction from the **JSON** returned by the API...

# ## Finally, we can display the prediction to the user
# '''

import streamlit as st
import requests
from urllib.parse import urlencode

URL = "https://taxifare.lewagon.ai/predict"

def send_request(ride_params):
    try:
        # Construct the URL with query parameters
        query_parameters = urlencode(ride_params)
        full_url = f"{URL}?{query_parameters}"

        # Send a GET request to the API
        response = requests.get(full_url)

        if response.status_code == 200:
            # Successful request
            return response.json()
        else:
            st.error(f"Error: {response.status_code}, {response.text}")
    except Exception as e:
        st.error(f"Error: {str(e)}")

def main():
    st.title("Ride Parameters Selector")

    # Initialize an empty dictionary to store parameters
    ride_params = {}

    # Ask for date and time
    ride_params['pickup_datetime'] = st.text_input("1. Enter Date and Time:", "2012-10-06 12:10:20")

    # Ask for pickup and dropoff coordinates
    ride_params['pickup_longitude'] = st.number_input("2. Enter Pickup Longitude:")
    ride_params['pickup_latitude'] = st.number_input("3. Enter Pickup Latitude:")
    ride_params['dropoff_longitude'] = st.number_input("4. Enter Dropoff Longitude:")
    ride_params['dropoff_latitude'] = st.number_input("5. Enter Dropoff Latitude:")

    # Ask for passenger count
    ride_params['passenger_count'] = st.number_input("6. Enter Passenger Count:", min_value=1, value=2)

    original_string = urlencode(ride_params)
    index_of_ampersand = original_string.find('&')
    modified_string = original_string[:index_of_ampersand].replace("+", "%").replace("%", ":").replace("A", "").replace("&", "%") + original_string[index_of_ampersand:]

    # Display the selected parameters
    st.write("\n**Selected Parameters:**")
    for key, value in ride_params.items():
        st.write(f"- {key.replace('_', ' ').title()}: {value}")

    # Button to send the request
    if st.button("Send Request"):
        response = send_request(ride_params)
        if response:
            st.success("Request processed successfully!")
            answer = str(round(response['fare'], 2))
            st.write(f"\n**Your fare is : {answer}**")

if __name__ == "__main__":
    main()


# "pickup_datetime":"2012-10-06 2012:10:20"
# "pickup_longitude":40.7614327
# "pickup_latitude":-73.9798156
# "dropoff_longitude":40.6513111
# "dropoff_latitude":-73.8803331
# "passenger_count":1
