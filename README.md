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

## Quick Start 🏃‍♂️

1. **Clone the repository**
   ```bash
   git clone https://github.com/w0418773/Weather_API_py_PUBLIC.git
   cd Weather_API_py_PUBLIC
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Keys**
   - Get your free API key from [WeatherAPI](https://www.weatherapi.com/)
   - Get your free API key from [Unsplash](https://unsplash.com/developers)
   - Update the API keys in `main.py`

4. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the API**
   - Local: `http://localhost:8000`
   - Interactive docs: `http://localhost:8000/docs`

## Deployment 🚀

This project is configured for easy deployment on Vercel with serverless functions. Simply click the deploy button or connect your GitHub repository to Vercel.

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/w0418773/Weather_API_py_PUBLIC)

## Example Response 📋

```json
{
  "weather": {
    "location": { "name": "Toronto", "region": "Ontario", "country": "Canada" },
    "current": { "temp_c": 15.0, "condition": { "text": "Partly cloudy" } }
  },
  "image": {
    "url": "https://images.unsplash.com/photo-...",
    "location": "Toronto, Canada", 
    "photographer": {
      "username": "photographer_name",
      "name": "Photographer Name",
      "link": "https://unsplash.com/@photographer_name"
    }
  }
}
```

## Author 👨‍💻

**Nathan Snook**
- Portfolio: [https://w0418773.github.io/](https://w0418773.github.io/)
- GitHub: [@w0418773](https://github.com/w0418773/)

## License 📄

This project is open source and available under the [MIT License](LICENSE).

---

*Built with ❤️ using FastAPI and modern Python*
