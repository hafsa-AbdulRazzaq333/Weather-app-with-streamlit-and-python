import streamlit as st
import requests

# -----------------------
# PAGE CONFIGURATION
# -----------------------
st.set_page_config(
    page_title="Weather App",
    page_icon="🌦",
    layout="centered",
    initial_sidebar_state="auto"
)

# -----------------------
# CUSTOM CSS FOR STYLING
# -----------------------
st.markdown(
"""
<style>
/* ---------- APP BACKGROUND ---------- */
.stApp {
    background: linear-gradient(to bottom, #87CEFA, #E0F7FA, #B3E5FC);  /* natural sky gradient */
    color: #525252;
    font-family: 'Arial', sans-serif;
}

/* ---------- WEATHER INFO BOXES ---------- */
.weather-box {
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 10px;
    color: #333333;  /* readable dark grey */
    font-size: 18px;
    background-color: rgba(255, 255, 255, 0);  
    border: 1px solid rgba(0,0,0,0.3);        
}

/* ---------- TEXT INPUT LABEL ---------- */
div.stTextInput > label {
    font-weight: bold;
    color: #2E2E2E;   
    font-size: 16px;
    padding: 5px 0;
}

/* ---------- BUTTON STYLE ---------- */
div.stButton > button {
    background-color: #58B3E0;  
    color: white;               
    font-size: 16px;
    font-weight: bold;
    padding: 8px 20px;
    border-radius: 10px;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

/* ---------- BUTTON HOVER ---------- */
div.stButton > button:hover {
    background-color: #54B8EB;  
}
</style>
""",
unsafe_allow_html=True
)

# -----------------------
# TITLE AND DESCRIPTION
# -----------------------
st.title("🌦 Weather App")
st.write("Enter a city name to get current weather information")

# -----------------------
# USER INPUT
# -----------------------
city = st.text_input("City Name")  # text input box

# -----------------------
# BUTTON CLICK EVENT
# -----------------------
if st.button("Get Weather"):

    if city.strip() == "":
        st.markdown(
        "<div style='background-color: rgba(255,223,186,0.7); color: #333333; padding: 15px; border-radius:10px;'>⚠️ Please enter a city name</div>", 
        unsafe_allow_html=True
    )

    else:
        api_key = "da24ed9aa977876400badb129b3ef4a9"  # OpenWeather API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)
        data = response.json()  

        if response.status_code == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            wind = data["wind"]["speed"]

            # -----------------------
            # DISPLAY WEATHER IN TRANSPARENT BOXES
            # -----------------------
            st.markdown(f"<div class='weather-box temp'>🌡 Temperature: {temp} °C</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='weather-box desc'>📝 Weather: {desc}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='weather-box humidity'>💧 Humidity: {humidity}%</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='weather-box pressure'>🎚️ Pressure: {pressure} hPa</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='weather-box wind'>💨 Wind Speed: {wind} m/s</div>", unsafe_allow_html=True)

        else:
           st.markdown(
           "<div style='background-color: rgba(255,128,128,0.7); color: #1F1F1F; padding: 15px; border-radius:10px;'>❌ City not found. Please check the name!</div>", 
           unsafe_allow_html=True
           )
