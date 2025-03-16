import requests
api_key = 'f70e992fec956ef283f762687b3ad5ac'
city = input('Enter city name:')  
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)  

sendReq = requests.get(url)
sendReq.raise_for_status

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp'] 
    desc = data['weather'][0]['description']
    print(f'Temperature: {temp} K') 
    print(f'Description: {desc} ')
elif response.status_code == 404:
    print("City not found") 
else:
    print('Error fetching weather data')

    