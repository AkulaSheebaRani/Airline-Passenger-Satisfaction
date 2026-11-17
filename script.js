
const API_URL = "https://airline-passenger-satisfaction-ntuc.onrender.com/predict";

const form = document.getElementById("prediction-form");
const button = document.getElementById("predict-button");
const resultBox = document.getElementById("result");

const textFields = [
    "Gender",
    "Customer_Type",
    "Type_of_Travel",
    "Class"
];

const numberFields = [
    "Age",
    "Flight_distance",
    "Inflight_Wifi_services",
    "Departure_Arrival_time_convenient",
    "Ease_of_Online_booking",
    "Gate_location",
    "Food_and_drink",
    "Online_boarding",
    "Seat_comfort",
    "Inflight_entertainment",
    "On_board_service",
    "Leg_room_service",
    "Baggage_handling",
    "Checkin_service",
    "Inflight_service",
    "Cleanliness",
    "Departure_Delay_in_Minutes",
    "Arrival_Delay_in_Minutes"
];

form.addEventListener("submit", async function(event) {

    event.preventDefault();

    resultBox.className = "";
    resultBox.textContent = "";

    button.disabled = true;
    button.textContent = "Predicting...";

    const data = {};

    textFields.forEach(function(key) {
        data[key] = document.getElementById(key).value;
    });

    numberFields.forEach(function(key) {
        data[key] = Number(document.getElementById(key).value);
    });

    try {

        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error("API Error: " + response.status);
        }

        const result = await response.json();

        if (result.prediction === 1) {

            resultBox.textContent = "Passenger Satisfied";
            resultBox.className = "success";

        } else if (result.prediction === 0) {

            resultBox.textContent =
                "Passenger Dissatisfied or neutral";

            resultBox.className = "warning";

        } else {

            resultBox.textContent = "Unexpected prediction response";
            resultBox.className = "error";

        }

    } catch (error) {

        console.error(error);

        resultBox.textContent =
            "Unable to connect to FastAPI server.";

        resultBox.className = "error";

    } finally {

        button.disabled = false;
        button.textContent = "Predict";

    }

});
