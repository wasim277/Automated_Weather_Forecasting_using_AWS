# Weather Forecast Script with Email Notification

## Overview

This script fetches a 3-day weather forecast (including today) for a specified city using the OpenWeatherMap API and sends the report via email using an Outlook account. The script fetches weather data, processes it to display a human-readable forecast, and sends the information in an email.

## Flow Chart
<div style="border: 2px solid #000; display: inline-block;">
  <img src="Results/Flow%20Chart.png" alt="Flow Chart" />
</div>

## Libraries Used
- `requests`: For making HTTP requests to fetch weather data from the OpenWeatherMap API.
- `smtplib`: For sending emails using the Simple Mail Transfer Protocol (SMTP).
- `datetime`: For handling date and time operations.
- `email.mime.multipart`: For creating a multipart email message.
- `email.mime.text`: For adding plain text to the email message.

## Features
- Fetches a 3-day weather forecast from the OpenWeatherMap API.
- Displays weather data including temperature and weather description.
- Sends the weather forecast via email using the Outlook SMTP service.
- Customizable city and API key.

## Summary

This Python script fetches a 3-day weather forecast for a specified city using the OpenWeatherMap API and sends it via email using Outlook's SMTP server. Below is a breakdown of the main components of the code:

1. **API Setup**:
   - An API key and the target city (Austin) is defined.
   - The base URL for the OpenWeatherMap API is specified.

2. **Weather Data Fetching**:
   - The `fetch_three_day_weather` function retrieves weather data for the specified city:
     - It constructs the API request URL and retrieves the response.
     - If the response is successful, it processes the forecast data to extract weather details for today and the next two days, focusing on forecasts at 12:00 PM for the latter days.
     - The function returns a formatted string with the weather report.

3. **Email Sending**:
   - The `send_email_with_outlook` function composes and sends an email with the weather report:
     - It creates a multipart email message and attaches the weather report.
     - It connects to the Outlook SMTP server, logs in with the sender's credentials, and sends the email.

4. **Main Logic**:
   - The script fetches the weather report and sends it via email using specified sender and recipient email addresses.

## OpenWeatherMap API Setup

1. Sign up at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) and generate an API key.
2. Replace the placeholder value of the `API_KEY` in the script with your actual API key:

   ```python
   API_KEY = 'your_openweather_api_key_here'
## Example Output

### 3-Day Weather Forecast for Austin (Including Today)

### Date: 2024-10-26 (Today)
- **Temperature**: 22°C  
- **Weather**: scattered clouds  
------------------------------

### Date: 2024-10-27
- **Temperature**: 24°C  
- **Weather**: clear sky  
------------------------------

### Date: 2024-10-28
- **Temperature**: 23°C  
- **Weather**: light rain  
------------------------------

<div style="border: 2px solid #000; display: inline-block;">
  <img src="Results/Email%20Sample.png" alt="Email Sample" />
</div>

