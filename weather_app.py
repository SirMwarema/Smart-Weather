# weather_app.py
import tkinter as tk
import requests

# Load API key from the api_key.txt file
with open("api_key.txt", "r") as file:
    api_key = file.read().strip()

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] == 200:
        weather_info = data["weather"][0]["description"].capitalize()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        return f"Weather: {weather_info}\nTemperature: {temperature}°C\nHumidity: {humidity}%"
    else:
        return "City not found."

def get_weather_button_click():
    city = city_entry.get()
    result_label.config(text=get_weather(city))

# Create the main window
root = tk.Tk()
root.title("Weather Forecast")

# Create widgets
label = tk.Label(root, text="Enter City:")
city_entry = tk.Entry(root)
get_weather_button = tk.Button(root, text="Get Weather", command=get_weather_button_click)
result_label = tk.Label(root, text="", wraplength=200)

# Layout widgets
label.pack()
city_entry.pack()
get_weather_button.pack()
result_label.pack()

# Start the GUI main loop
root.mainloop()
