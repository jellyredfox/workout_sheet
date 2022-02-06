import requests
import datetime as dt
import os

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
WEIGHT = 72
HEIGHT = 184
date = dt.date.today().strftime("%d/%m/%Y")
time = dt.datetime.now().time().strftime("%H:%M:%S")


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

answer_about_exercise = input("Tell me which exercises you did? ")

request_settings = {
 "query": answer_about_exercise,
 "gender": "male",
 "weight_kg": WEIGHT,
 "height_cm": HEIGHT,
 "age": 31
}


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

ex_response = requests.post(url=exercise_endpoint, json=request_settings, headers=headers)
ex_data = ex_response.json()


sheety_endpoint = "https://api.sheety.co/81427601dce6294ea36d2c8b08f0d167/myWorkouts/workouts"
sheety_headers = {
    "Authorization": os.getenv("SHEETY_TOKEN"),
}
for exercise in ex_data["exercises"]:
    data_for_post = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheety_response = requests.post(url=sheety_endpoint, json=data_for_post, headers=sheety_headers)
    print(sheety_response.text)
