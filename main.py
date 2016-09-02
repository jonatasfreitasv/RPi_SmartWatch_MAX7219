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

from config import Config

# Start LED Matrix with 2 modules
device = led.matrix(cascaded=Config.display["total"])
device.brightness(Config.display["brightness"])
font = TINY_FONT

# OpenWeather
weather_city = Config.openWeather["locale"]
weather_key = Config.openWeather["key"]
weather_url = ("http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s") % (weather_city, weather_key)

def main():

	# Get weather data
	weather_data = urllib.urlopen(weather_url)
	weather_json = json.loads(weather_data.read())

	# Variables
	time = "-%s-" % str(datetime.datetime.now().strftime("%Hh %Mmin"))
	temp = "T %sC" % str(int(weather_json["main"]["temp"] - 273.15))
	cloudness = "C %s%%" % str(weather_json["clouds"]["all"])
	humidity = "H %s%%" % str(weather_json["main"]["humidity"])
	weather = "now %s  " % str(weather_json["weather"][0]["main"])

	# Show variables in matrix
	device.show_message(time, font)
	device.show_message(temp, font)
	device.show_message(cloudness, font)
	device.show_message(humidity, font)
	device.show_message(weather, font)

if __name__ == "__main__":
	while True:
		try:
			main()
		except:
			continue

