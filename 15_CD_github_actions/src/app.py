import requests
import streamlit as st

api_key = st.secrets["api"]["OPEN_WEATHER_MAP_API"]

st.title("Weather information")

st.markdown("You will find very nice weather info from here. Such a cool weather app")

city = st.text_input("Enter city name:", "Oslo")


def get_weather_data(city, api_key):
    url = (
        "https://api.openweathermap.org/data/2.5/weather?"
        f"q={city}&appid={api_key}&units=metric"
    )
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        st.error(f"Error fetching data: {response.text}")
        return None


if city:
    weather_data = get_weather_data(city, api_key)

    if weather_data:
        st.subheader(f"Weather in {city.capitalize()}")
        st.write(f"Temperature: {weather_data['main']['temp']} °C")
        st.write(f"Humidity: {weather_data['main']['humidity']} %")
        st.write(f"Weather: {weather_data['weather'][0]['description'].capitalize()}")

        # weather icon
        icon_code = weather_data["weather"][0]["icon"]
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"
        st.image(icon_url, width=100)

        st.write(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        st.write("No data available.")
