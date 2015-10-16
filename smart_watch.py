#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# RPi_SmartWatch_MAX7219
# Created by Jonatas Freitas - https://github.com/jonatasfreitasv
# https://github.com/jonatasfreitasv/RPi_SmartWatch_MAX7219
#

import datetime, time, urllib, json
import max7219.led as led
from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT

# Start LED Matrix with 2 modules
device = led.matrix(cascaded=2)
device.brightness(15)
font = TINY_FONT

# OpenWeather
weather_city = "CITY,COUNTRY_CODE"
weather_key = "YOUR_API_KEY"
weather_url = ("http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s") % (weather_city, weather_key)

def main():

	# Get weather data
	weather_data = urllib.urlopen(weather_url)
	weather_json = json.loads(weather_data.read())

	# Variables
	city = weather_json["name"]
	temp = "Temp:%sC" % str(int(weather_json["main"]["temp"] - 273.15))
	cloudness = "Clouds:%s%%" % str(weather_json["clouds"]["all"])
	weather = weather_json["weather"][0]["main"]
	humidity = "Humidity:%s%%" % str(weather_json["main"]["humidity"])
	time = "-%s-" % str(datetime.datetime.now().strftime("%H:%M"))

	# Show variables in matrix
	device.show_message(city, font)
	device.show_message(temp, font)
	device.show_message(cloudness, font)
	device.show_message(humidity, font)
	device.show_message(weather, font)
	device.show_message(time, font)
	device.show_message("||||||||||||||||||||")

if __name__ == "__main__":
	while True:
		main()
