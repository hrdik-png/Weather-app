# 🌤️ PyQt5 Desktop Weather App

A sleek, desktop-based weather application built with Python and PyQt5. This app fetches real-time weather data using the OpenWeatherMap API and displays the current temperature, feels-like temperature, humidity, pressure, and dynamic weather emojis based on the forecast.

## ✨ Features
* **Real-Time Data:** Fetches live weather metrics using the OpenWeather API.
* **Modern GUI:** Built with PyQt5 featuring a clean, dark-mode interface and responsive typography.
* **Robust Error Handling:** Gracefully handles invalid city names, missing API keys, and connection timeouts without crashing.
* **Secure:** Uses `python-dotenv` to securely manage API keys outside of the source code.

## 🛠️ Tech Stack
* **Language:** Python 3.14.2
* **GUI Framework:** PyQt5
* **API:** OpenWeatherMap
* **Libraries:** `requests`, `python-dotenv`

## 🚀 Installation & Setup

**1. Clone the repository**

git clone [https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git](https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git)
cd YOUR-REPO-NAME

2. Install dependencies

pip install PyQt5 requests python-dotenv


3. Set up your API Key
You will need a free API key from OpenWeatherMap.
Create a file named exactly .env in the root directory of this project and add your key like this:

Ini, TOML
OPENWEATHER_API_KEY=your_api_key_here
(Note: Ensure your .env file is listed in your .gitignore so your key remains private!)

💻 Usage
Run the application from your terminal:

Bash
python weather.py
Type a city name into the input field and click "Get Weather" to see the current forecast.
