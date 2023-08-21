from datetime import datetime
import pytz
import sys 

print("Enter date in YYYY-MM-DD format:")
input_date_str = sys.stdin.readline().strip()

print("Enter time in HH:MM:SS format:") 
input_time_str = sys.stdin.readline().strip()

input_datetime = datetime.strptime(input_date_str + ' ' + input_time_str, '%Y-%m-%d %H:%M:%S')

timezones = [
    'US/Eastern', 
    'US/Central', 
    'US/Mountain',
    'US/Pacific',
    'Europe/London',
    'Europe/Paris',
    'Asia/Singapore',
    'Asia/Hong_Kong',
    'Asia/Tokyo',
    'Australia/Sydney',
    'Australia/Melbourne',
    'Australia/Brisbane',
    'Pacific/Auckland',
    'Pacific/Fiji',
    'Africa/Cairo',
    'Africa/Nairobi',
    'America/Sao_Paulo',
    'America/Mexico_City'
]

for tz in timezones:
    tz = pytz.timezone(tz)
    print(input_datetime.astimezone(tz).strftime("%Y-%m-%d %H:%M:%S %Z"))
