import requests

#api key for weather

#endpoint of the website
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

#gets input from user to get city 
city = input("Enter a city name: ")

#passes in base url and query parameters 
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

#get request to retrieve data
response = requests.get(request_url)

#error checking, status code of 200 means succesful
if response.status_code == 200:
    data = response.json() # gets json data as python dictionary
    weather = data["weather"][0]["description"] #gets weather description
    temperature = round(data["main"]["temp"] - 273.15, 2) #gets temp in celsius
    feelsLike = round(data["main"]["feels_like"] - 273.15, 2) #gets the "feels like" temperature
    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")
    print("Feels like:", feelsLike)
else:
    print("An error occured")
