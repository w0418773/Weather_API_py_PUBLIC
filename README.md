# Weather API Service 🌤️

A modern RESTful API service built with FastAPI that provides comprehensive weather information combined with beautiful location imagery. This service integrates WeatherAPI for real-time weather data and Unsplash for stunning visual representations of locations.

## Features ✨

- **Current Weather Data**: Get real-time weather conditions for any city worldwide
- **Weather Forecasts**: Access multi-day weather forecasts (customizable duration)
- **Hourly Weather**: Retrieve detailed hourly weather predictions
- **Location Imagery**: Automatically fetched high-quality images from Unsplash based on weather location
- **CORS Enabled**: Full cross-origin resource sharing support for web applications
- **Fast & Async**: Built with FastAPI for high performance and async request handling
- **Error Handling**: Graceful error handling with fallback images and informative responses

## API Endpoints 🚀

### `GET /`
Welcome endpoint with author information and portfolio links.

### `GET /weather/{city}`
Returns current weather data along with a location-based image.
- **Parameters**: `city` (string) - Name of the city
- **Response**: Weather data + location image with photographer credits

### `GET /forecast/{city}/{days}`
Provides weather forecast for specified number of days.
- **Parameters**: 
  - `city` (string) - Name of the city
  - `days` (integer) - Number of forecast days
- **Response**: Forecast data + location image

### `GET /hourly/{city}`
Returns current weather plus next 2 hours of hourly forecasts.
- **Parameters**: `city` (string) - Name of the city
- **Response**: Current conditions + hourly predictions + location image

## Technology Stack 🛠️

- **FastAPI**: Modern, fast web framework for building APIs
- **HTTPX**: Async HTTP client for external API calls
- **WeatherAPI**: Real-time weather data provider
- **Unsplash API**: High-quality photography service
- **Python 3.7+**: Core programming language