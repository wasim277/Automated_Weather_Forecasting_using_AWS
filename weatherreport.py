import requests
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Your OpenWeatherMap API key
API_KEY = 'a960b5a01fa7e717a1b753937cdb5857'
# City name for which you want to fetch weather data
CITY = 'Austin'
# Base URL for the OpenWeatherMap API
BASE_URL = 'http://api.openweathermap.org/data/2.5/forecast'

def fetch_three_day_weather(city, api_key):
    url = f"{BASE_URL}?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        forecast_list = data['list']

        weather_report = f"3-Day Weather Forecast for {city} (Including Today):\n\n"

        current_date = datetime.now().date()
        day_count = 0
        added_dates = set()

        # Flag to ensure today's date is included
        today_included = False

        for forecast in forecast_list:
            dt_txt = forecast['dt_txt']
            date_time = datetime.strptime(dt_txt, '%Y-%m-%d %H:%M:%S')
            forecast_date = date_time.date()

            # Include today's forecast (at any time if not already included)
            if not today_included and forecast_date == current_date:
                today_included = True
                temperature = forecast['main']['temp']
                weather_description = forecast['weather'][0]['description']

                weather_report += f"Date: {date_time.strftime('%Y-%m-%d')} (Today)\n"
                weather_report += f"Temperature: {temperature}°C\n"
                weather_report += f"Weather: {weather_description}\n"
                weather_report += "-" * 30 + "\n"

                added_dates.add(forecast_date)
                day_count += 1
                continue

            # Include forecast data for the next 2 days at 12:00 PM
            if forecast_date not in added_dates and forecast_date > current_date and date_time.hour == 12:
                temperature = forecast['main']['temp']
                weather_description = forecast['weather'][0]['description']

                weather_report += f"Date: {date_time.strftime('%Y-%m-%d')}\n"
                weather_report += f"Temperature: {temperature}°C\n"
                weather_report += f"Weather: {weather_description}\n"
                weather_report += "-" * 30 + "\n"

                added_dates.add(forecast_date)
                day_count += 1

            # Stop after collecting data for 3 days (including today)
            if day_count >= 3:
                break

        return weather_report
    else:
        return f"Error fetching data: {response.status_code}"

def send_email_with_outlook(subject, body, sender_email, sender_password, recipient_email):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()

        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

# Main logic
weather_report = fetch_three_day_weather(CITY, API_KEY)
send_email_with_outlook(
    subject="3-Day Weather Forecast",
    body=weather_report,
    sender_email="wasimprojects@outlook.com",
    sender_password="xcvnossxilhtddxn",  # Your app password
    recipient_email="amdwasim97@gmail.com"
)
