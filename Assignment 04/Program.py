#F to C
#acres to barns
#polygon

import turtle

def temp(fahren):
	celsius = round(((fahren - 32) * 5/9), 2)
	print(str(fahren) + " degrees Fahrenheit is " + str(celsius) + " degrees Celsius.")

def area(acres):
	barns = format((acres * (4.047 * (10**31))), '.3e')
	print(str(acres) + " acres is approximately " + str(barns) + " barns.")

def polygon(shapes):
	angle = 360 / shapes 
	for i in range(shapes):
		turtle.forward(50)
		turtle.left(angle)

fahren = int(input("What temperature in Fahrenheit would you like to convert to Celsius? "))
temp(fahren)

acres = int(input("How many acres do you want to convert to barns? "))
area(acres)

shapes = int(input("How many sides do you want your polygon to be(more than two but not too many)? "))
polygon(shapes)
screen = turtle.getscreen()
screen.mainloop()
