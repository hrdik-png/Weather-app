import os 
import sys
from dotenv import load_dotenv
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                            QLabel, QLineEdit, QPushButton)
from PyQt5.QtCore import Qt

load_dotenv("api.env")
api_key = os.getenv("OPENWEATHER_API_KEY")
class weatherapp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather",self)
        self.temperature_label = QLabel( self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.feels_like_label = QLabel(self)
        self.temp_min_max_label = QLabel(self)
        self.extra_details_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("weather app")

        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.feels_like_label)
        vbox.addWidget(self.temp_min_max_label)
        vbox.addWidget(self.extra_details_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.feels_like_label.setAlignment(Qt.AlignCenter)
        self.extra_details_label.setAlignment(Qt.AlignCenter)
        self.temp_min_max_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.temperature_label.setObjectName("temperature_label")
        self.feels_like_label.setObjectName("feels_like_label")
        self.temp_min_max_label.setObjectName("temp_min_max_label")
        self.extra_details_label.setObjectName("extra_details_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        self.get_weather_button.setObjectName("get_weather_button")
        
        self.setStyleSheet("""
            QWidget{
                background-color: #000000;
                }
            Qlabel, QPushButton{
                font-family: Times New Roman;
                color: #fffcfc;
                }
            QLabel#city_label {
                font-size: 40px;
                font-family: Times New Roman;
                color: #fffcfc;
                }
            QLineEdit#city_input{
                font-size: 40px;
                font-family: Times New Roman;
                color: #fffcfc;
                }
            QPushButton#get_weather_button{
                font-size: 30px;
                font-weight: bold;
                font-family: Times New Roman;
                color: #fffcfc;
                background-color: #004734;
                }
            QLabel#temperature_label{
                font-size: 75px;
                font-family: Times New Roman;
                color: #fffcfc;
                }
            QLabel#emoji_label{
                font-size: 90px;
                }
            QLabel#description_label{
                font-size: 40px;
                font-family: Times New Roman;
                color: #fffcfc
                }
            QLabel#feels_like_label, QLabel#temp_min_max_label, QLabel#extra_details_label{
                font-size: 20px;
                font-style: italic;
                font-family: Times New Roman;
                color: #fffcfc
                }

        """)
        self.get_weather_button.clicked.connect(self.get_weather)
    def get_weather(self):
        api_key = os.getenv("OPENWEATHER_API_KEY")
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if data["cod"] == 200:
                self.display_weather(data)
        except requests.exceptions.HTTPError as httperror:
            match response.status_code:
                case 400:
                    self.display_error("Bad request; \n check your input")
                case 401:
                    self.display_error("Unauthorized: \n invalid API key")
                case 403:
                    self.display_error("Forbidden: \n Access denied")
                case 404:
                    self.display_error("Not Found: \n City Not Found")
                case 500:
                    self.display_error("Internal Server Error: \n Try Again")
                case 502:
                    self.display_error("Bad Gateway: \n Invalid response from server")
                case 503:
                    self.display_error("Service Unavailable: \n Server is Down")
                case 504:
                    self.display_error("Gateway timeout: \n No response from the server")
                case _:
                    self.display_error(f"HTTP error occured: \n {httperror}")
            
        except requests.exceptions.ConnectionError:
            self.display_error("Connection error")
        except requests.exceptions.Timeout:
            self.display_error("Request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error: \n {req_error}")
    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px")
        self.feels_like_label.setStyleSheet("font-size: 30px")
        
        self.temperature_label.setText(message)
        self.feels_like_label.setText(" ")
        self.emoji_label.setText(message)
        self.emoji_label.setText(" ")
        self.temp_min_max_label.setText(" ")
        self.extra_details_label.setText(" ")
        self.description_label.setText(" ")
        self.description_label.setText(" ")

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 75px")
        self.feels_like_label.setStyleSheet("font-size: 20px")
        temperature_k = data["main"]["temp"]
        feels_like_k = data["main"]["feels_like"]
        temperature_c = temperature_k - 273.15
        feels_like_c = feels_like_k - 273.15
        feels_like_f = (feels_like_k *9/5) - 459.67
        temp_min_c = data["main"]["temp_min"] - 273.15
        temp_max_c = data["main"]["temp_max"] - 273.15
        pressure = data["main"]["pressure"]
        humidity = data["main"]["humidity"]
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]
        self.temperature_label.setText(f"{temperature_c:.0f}°C")
        self.feels_like_label.setText(f"Feels like: {feels_like_c:.0f}°C")
        self.temp_min_max_label.setText(f"Min: {temp_min_c:.1f}°C  |  Max: {temp_max_c:.1f}°C")
        self.extra_details_label.setText(f"Humidity: {humidity}%  |  Pressure: {pressure} hPa")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)

    @staticmethod
    def get_weather_emoji(weather_id):
        if  200 <=weather_id <=232:
            return "🍃"
        elif 300 <= weather_id <= 321:
            return "☔🌦️"
        elif 500 <= weather_id <= 531:
            return "☔🌧️"
        elif 600 <= weather_id <= 622:
            return "🌨️❄️"
        elif 701 <= weather_id <= 741:
            return "🌫️🌁"
        elif  weather_id == 762:
            return "🌋⚱️"
        elif weather_id == 771:
            return "🌬️💨"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️/🌃"
        elif 801<= weather_id <=804:
            return "☁️🌥️"
        
if __name__ == "__main__": 
    app = QApplication(sys.argv)
    weather_app = weatherapp()
    weather_app.show()
    sys.exit(app.exec_())