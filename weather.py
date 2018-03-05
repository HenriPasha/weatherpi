from flask import Flask, render_template  
from sense_hat import SenseHat  #imports sensehat packages, allowing use of the sensors
import time

app = Flask(__name__)

@app.route('/')

def index():				#returns to check definition before executing code

	#variables are defined, each being representative of a measurement derived from the sensehat
	
	sense = SenseHat()

	celcius = round(sense.get_temperature(), 1)
	fahrenheit = round(1.8 * celcius + 32, 1)
	humidity = round(sense.get_humidity(), 1)
	pressure = round(sense.get_pressure(), 1)

#returns outputs/results to the calling funtion; sends weather data to the website
	return render_template('weather.html', celcius=round(celcius * 0.75, 1), fahrenheit=round(fahrenheit * 0.8, 1), humidity=humidity, pressure=pressure) 
	#numbers multiplied to account for component heat

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')



#creates infinite loop for LED display
while True:
    ap = SenseHat()
    temp = ap.get_temperature()
    print("Temp: %s C" % temp)               # Show temp on console

    ap.set_rotation(180)        # Set LED matrix to scroll from right to left

    ap.show_message("%.1f C" % temp, scroll_speed=0.10, text_colour=[0, 0, 255])
    time.sleep(2)
