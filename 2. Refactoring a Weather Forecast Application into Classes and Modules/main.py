# Task 1: Identifying and Creating Classes

import weather_forecaster

def main():
    w_d = weather_forecaster.WeatherDisplayer()
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        if detailed == 'yes':
            forecast = w_d.get_detailed_forecast(city)
        else:
            forecast = w_d.display_weather(city)
        print(forecast)

if __name__ == "__main__":
    main()