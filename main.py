from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

weather_API_key = "#"
weather_base_url = "http://api.weatherapi.com/v1"

upsplash_API_key = "#"
upsplash_base_url = "https://api.unsplash.com"

@app.get("/")
async def read_root():
    return {
            "Message": "Welcome to the Weather and Image API Service!",
            "Author": "Nathan Snook",
            "Portfolio": "https://w0418773.github.io/",
            "GitHub": "https://github.com/w0418773/"
            }

@app.get("/weather/{city}")
async def read_weather(city: str):
    # Simulate a weather API response
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{weather_base_url}/current.json?key={weather_API_key}&q={city}")
        weather_data = response.json()

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{upsplash_base_url}/photos/random?query={weather_data['location']['region']}&location={weather_data['location']['country']}&orientation=landscape&client_id={upsplash_API_key}")

    if response.status_code != 200:
        image_data = {"error": "Image not found"}
    else:
        image_data = response.json()

    if "error" in weather_data:
        return "Seems like the city you entered is invalid. Please try again."
    elif "error" in image_data:
        return {
                "weather": weather_data,
                "image": {
                    "url": 'https://images.unsplash.com/photo-1548475390-f6908921aaf8?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=1170',
                    "location": 'Bow Lake, Banff National Park, Canada',
                    "photographer": {
                        "username": 'dbmartin00',
                        "name": 'David Brooke Martin',
                        "link": 'https://unsplash.com/@dbmartin00',
                    },
                }
            }
    else:
        return {
            "weather": weather_data,
            "image": {
                "url": image_data['urls']['regular'],
                "location": image_data['location']['name'] if image_data.get('location') else "Unknown",
                "photographer": {
                    "username": image_data['user']['username'],
                    "name": image_data['user']['name'],
                    "link": image_data['user']['links']['html'],
                },
            }
        }
    
@app.get("/forecast/{city}/{days}")
async def read_forecast(city: str, days: int):
    # Simulate a weather API response
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{weather_base_url}/forecast.json?key={weather_API_key}&q={city}&days={days}")
        weather_data = response.json()

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{upsplash_base_url}/photos/random?query={weather_data['location']['region']}&location={weather_data['location']['country']}&orientation=landscape&client_id={upsplash_API_key}")
        
    if response.status_code != 200:
        image_data = {"error": "Image not found"}
    else:
        image_data = response.json()

    if "error" in weather_data:
        return "Seems like the city you entered is invalid. Please try again."
    elif "error" in image_data:
        return {
                "weather": weather_data,
                "image": {
                    "url": 'https://images.unsplash.com/photo-1548475390-f6908921aaf8?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=1170',
                    "location": 'Bow Lake, Banff National Park, Canada',
                    "photographer": {
                        "username": 'dbmartin00',
                        "name": 'David Brooke Martin',
                        "link": 'https://unsplash.com/@dbmartin00',
                    },
                }
            }
    else:
        return {
            "weather": weather_data,
            "image": {
                "url": image_data['urls']['regular'],
                "location": image_data['location']['name'] if image_data.get('location') else "Unknown",
                "photographer": {
                    "username": image_data['user']['username'],
                    "name": image_data['user']['name'],
                    "link": image_data['user']['links']['html'],
                },
            }
        }
    
@app.get("/hourly/{city}")
async def read_forecast(city: str):
    # Simulate a weather API response
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{weather_base_url}/forecast.json?key={weather_API_key}&q={city}&days=2")
        weather_data = response.json()

    current_time = weather_data['location']['localtime'].split(' ')[1]
    hourly_data = []
    count = 0
    for day in weather_data['forecast']['forecastday']:
        for hour in day['hour']:
            if count >= 2:
                break   
            elif hour['time'].split(' ')[1] > current_time and day['date'] == weather_data['location']['localtime'].split(' ')[0]:
                hourly_data.append(hour)
                count += 1
    # return {
    #     "weather": weather_data['current'],
    #     "hourly": hourly_data,
    # }

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{upsplash_base_url}/photos/random?query={weather_data['location']['region']}&location={weather_data['location']['country']}&orientation=landscape&client_id={upsplash_API_key}")
        
    if response.status_code != 200:
        image_data = {"error": "Image not found"}
    else:
        image_data = response.json()

    if "error" in weather_data:
        return "Seems like the city you entered is invalid. Please try again."
    elif "error" in image_data:
        return {
                "location": weather_data['location'],
                "current": weather_data['current'],
                "hourly": hourly_data,
                "image": {
                    "url": 'https://images.unsplash.com/photo-1548475390-f6908921aaf8?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&q=80&w=1170',
                    "location": 'Bow Lake, Banff National Park, Canada',
                    "photographer": {
                        "username": 'dbmartin00',
                        "name": 'David Brooke Martin',
                        "link": 'https://unsplash.com/@dbmartin00',
                    },
                }
            }
    else:
        return {
            "location": weather_data['location'],
            "current": weather_data['current'],
            "hourly": hourly_data,
            "image": {
                "url": image_data['urls']['regular'],
                "location": image_data['location']['name'] if image_data.get('location') else "Unknown",
                "photographer": {
                    "username": image_data['user']['username'],
                    "name": image_data['user']['name'],
                    "link": image_data['user']['links']['html'],
                },
            }
        }