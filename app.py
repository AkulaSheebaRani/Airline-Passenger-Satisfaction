
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib

# Create FastAPI application
app = FastAPI(title="Airline Passenger Satisfaction Prediction")

# Enable CORS for Vercel frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Load trained ML pipeline
model = joblib.load("airline_passenger_satisfaction_pipeline.pkl")


# Input data format
class passenger(BaseModel):
    Gender: str
    Customer_Type: str
    Age: int
    Type_of_Travel: str
    Class: str
    Flight_distance: int
    Inflight_Wifi_services: int
    Departure_Arrival_time_convenient: int
    Ease_of_Online_booking: int
    Gate_location: int
    Food_and_drink: int
    Online_boarding: int
    Seat_comfort: int
    Inflight_entertainment: int
    On_board_service: int
    Leg_room_service: int
    Baggage_handling: int
    Checkin_service: int
    Inflight_service: int
    Cleanliness: int
    Departure_Delay_in_Minutes: int
    Arrival_Delay_in_Minutes: int


# Prediction API
@app.post("/predict")
def predict(data: passenger):

    input_data = pd.DataFrame([{
        "Gender": data.Gender,
        "Customer Type": data.Customer_Type,
        "Age": data.Age,
        "Type of Travel": data.Type_of_Travel,
        "Class": data.Class,
        "Flight Distance": data.Flight_distance,
        "Inflight wifi service": data.Inflight_Wifi_services,
        "Departure/Arrival time convenient": data.Departure_Arrival_time_convenient,
        "Ease of Online booking": data.Ease_of_Online_booking,
        "Gate location": data.Gate_location,
        "Food and drink": data.Food_and_drink,
        "Online boarding": data.Online_boarding,
        "Seat comfort": data.Seat_comfort,
        "Inflight entertainment": data.Inflight_entertainment,
        "On-board service": data.On_board_service,
        "Leg room service": data.Leg_room_service,
        "Baggage handling": data.Baggage_handling,
        "Checkin service": data.Checkin_service,
        "Inflight service": data.Inflight_service,
        "Cleanliness": data.Cleanliness,
        "Departure Delay in Minutes": data.Departure_Delay_in_Minutes,
        "Arrival Delay in Minutes": data.Arrival_Delay_in_Minutes
    }])

    prediction = int(model.predict(input_data)[0])

    result = (
        "Passenger Satisfied"
        if prediction == 1
        else "Passenger Dissatisfied or Neutral"
    )

    return {
        "prediction": prediction,
        "result": result
    }
