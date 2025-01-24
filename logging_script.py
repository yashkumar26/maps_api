import googlemaps
from datetime import datetime
import pandas as pd
import os

gmaps = googlemaps.Client(key='AIzaSyCMl4ZfJ4C9-gRSeaQI_sIwDBeu6FZvjKw')


def get_distance_and_time():
    origin = 'avance business hub, Gachibowli,Hyderabad,Telangana'
    destination = 'Vasavi Nilayam apartment, Golden Tulip Estate, Kondapur, Hyderabad, Telangana'
    # waypoints = ['Intermediate Address']

    directions_result = gmaps.directions(origin,
                                         destination,
                                         mode="driving",
                                         departure_time=datetime.now())

    if directions_result:
        leg = directions_result[0]['legs'][0]
        distance = leg['distance']['text']
        duration = leg['duration']['text']
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        day_of_week = datetime.now().strftime('%A')

        data = {
            "Day": [day_of_week],
            "Timestamp": [current_time],
            "Distance": [distance],
            "Duration": [duration]
        }
        df = pd.DataFrame(data)

        file_path = "logs/distance_log.csv"
        file_exists = os.path.isfile(file_path)

        with open(file_path, "a", newline='') as log_file:
            df.to_csv(log_file, header=not file_exists, index=False)
        print(f"Logged data at {current_time}")
    else:
        print("No directions found.")


if __name__ == "__main__":
    get_distance_and_time()
