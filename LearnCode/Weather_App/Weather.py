import requests 
import sys , json 
#Building A CLI Weather api request app
def lat_long(city):
    response = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=10&language=en&format=json") 
    Latitude = response.json()["results"][0]["latitude"]
    Longitude = response.json()["results"][0]["longitude"]
    return Latitude , Longitude
def Temperature(city,Latitude,Longitude):
    response_Mateo = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={Latitude}&longitude={Longitude}&daily=weather_code,sunset,sunrise&hourly=temperature_2m&current=temperature_2m,precipitation,rain,showers,snowfall,is_day,apparent_temperature,relative_humidity_2m,wind_speed_10m&timezone=Asia%2FBangkok")
    temperature = response_Mateo.json()["current"]["apparent_temperature"]
    print(f"The Apparent Temparature of {city} is {temperature} degree Celcius")
    
def Day_Night(city,Latitude,Longitude):
    response1_Mateo = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={Latitude}&longitude={Longitude}&daily=weather_code,sunset,sunrise&hourly=temperature_2m&current=temperature_2m,precipitation,rain,showers,snowfall,is_day,apparent_temperature,relative_humidity_2m,wind_speed_10m&timezone=Asia%2FBangkok")
    Day_Night = response1_Mateo.json()["current"]["is_day"]
    if Day_Night == 0 :
        Day_Night = 'Night'
        print(f"Its is Currently {Day_Night} in {city}")   
    else :
        Day_Night = "Morning/Afternoon" 
        print(f"Its Currently {Day_Night} in {city}")
        
def set_city():
    try :
        city = input("Tell Me the City You Want a Weather Report About :").lower().strip()
        return city 
    except ValueError :
        print("Enter Only Valid Characters ")
def main():
    city = set_city()
    Latitude , Longitude = lat_long(city)
    Temperature(city,Latitude,Longitude)
    Day_Night(city,Latitude,Longitude)
    
if __name__  == "__main__" :
    main()

        