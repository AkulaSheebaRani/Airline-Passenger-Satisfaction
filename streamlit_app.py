import streamlit as st
import requests
st.title("Airline Passenger Satisfaction")

### Input Wedigets
Gender=st.radio("Select Gender",
    ["Male", "Female"]
    )

Customer_Type=st.selectbox("Select Customer Type",
                           ["Loyal Customer","disloyal Customer"]
                           )
Age=st.number_input("Age",13,80,13)
Type_of_Travel=st.selectbox("Select Type of Travel",
                            ["Personal Travel","Business travel"]
                            )
Class=st.selectbox("Select Class",
                   ["Eco Plus","Business","Eco"]
                   )
Flight_distance=st.number_input("Flight Diatnce",min_value=100,max_value=5000,value=460)

Inflight_Wifi_services=st.number_input("Inflight WiFi Services",min_value=0,max_value=5,value=3)

Departure_Arrival_time_convenient=st.number_input("Departure/Arrival time convenient",min_value=0,max_value=5,value=4)

Ease_of_Online_booking=st.number_input("Ease of Online booking",min_value=0,max_value=5,value=3)

Gate_location=st.number_input("Gate location",min_value=0,max_value=5,value=1)

Food_and_drink=st.number_input("Food and drink",min_value=0,max_value=5,value=5)

Online_boarding =st.number_input("Online boarding ",min_value=0,max_value=5,value=3)

Seat_comfort=st.number_input("Seat Comfort",min_value=0,max_value=5,value=5)

Inflight_entertainment=st.number_input("Inflight entertainment",min_value=0,max_value=5,value=5)

On_board_service=st.number_input("On-board service",min_value=0,max_value=4,value=4)

Leg_room_service=st.number_input("Leg room service",min_value=0,max_value=5,value=3)

Baggage_handling=st.number_input("Baggage handling",min_value=1,max_value=5,value=4)

Checkin_service=st.number_input("Checkin service",min_value=0,max_value=5,value=4)

Inflight_service=st.number_input("Inflight service",min_value=0,max_value=5,value=5)

Cleanliness=st.number_input("Cleanliness",min_value=0,max_value=5,value=5)

Departure_Delay_in_Minutes=st.number_input("Departure Delay in Minutes",min_value=0,max_value=1600,value=25)

Arrival_Delay_in_Minutes=st.number_input("Arrival Delay in Minutes",min_value=0,max_value=1600,value=18)

###Prediction
if st.button("Predict"):
    data={
      "Gender":Gender,
      "Customer_Type":Customer_Type,
      "Age":Age,
      "Type_of_Travel":Type_of_Travel,
      "Class":Class,
      "Flight_distance":Flight_distance,
      "Inflight_Wifi_services":Inflight_Wifi_services,
      "Departure_Arrival_time_convenient":Departure_Arrival_time_convenient,
      "Ease_of_Online_booking":Ease_of_Online_booking,
      "Gate_location":Gate_location,
      "Food_and_drink":Food_and_drink,
      "Online_boarding":Online_boarding,
      "Seat_comfort":Seat_comfort,
      "Inflight_entertainment":Inflight_entertainment,
      "On_board_service":On_board_service,
      "Leg_room_service":Leg_room_service,
      "Baggage_handling":Baggage_handling,
      "Checkin_service":Checkin_service,
      "Inflight_service":Inflight_service,
      "Cleanliness":Cleanliness,
      "Departure_Delay_in_Minutes":Departure_Delay_in_Minutes,
      "Arrival_Delay_in_Minutes":Arrival_Delay_in_Minutes
    }

    try:
        response = requests.post(
                    "http://127.0.0.1:8000/predict",
                    json=data
            )
        if response.status_code==200:
            result=response.json()

            if result["prediction"]==1:
                st.success("Passenger Satisfied")
            else:
                st.warning("Passenger Dissatisfied or neutral")

    except requests.exceptions.ConnectionError:
            st.error("FastAPI server is not running.")
    
