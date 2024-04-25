# Weather Forecast Application Script

weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
        }

class WeatherFetcher:
    def __init__(self):
        pass

    def fetch_weather_data(self, city):
        # Simulated function to fetch weather data for a given city
        print(f"Fetching weather data for {city}...")
        return weather_data.get(city, {})

class WeatherParser:
    def __init__(self):
        pass

    def parse_weather_data(self, data, city):
        # Function to parse weather data
        if not data:
            return "Weather data not available"
        # city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

class WeatherDisplayer:
    def __init__(self):
        self.w_f = WeatherFetcher()
        self.w_p = WeatherParser()
    
    def get_detailed_forecast(self, city):
        # Function to provide a detailed weather forecast for a city
        data = self.w_f.fetch_weather_data(city)
        return self.w_p.parse_weather_data(data, city)

    def display_weather(self, city):
        # Function to display the basic weather forecast for a city
        data = self.w_f.fetch_weather_data(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            weather_report = self.w_p.parse_weather_data(data, city)
            print(weather_report)