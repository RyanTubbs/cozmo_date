#!/usr/bin/env python3

# Licensed under the MIT License. 
#
# Copyright 2017 RYAN TUBBS rmtubbs@gmail.com 
#
# Permission is hereby granted, free of charge, to any person obtaining 
# a copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions: 
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software. 
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A 
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 

#This program causes Anki's Cozmo robot to say aloud the current day of the week, month, date, and year.

import cozmo #Imports the 'cozmo' module from Cozmo's API, which enables this program to access Cozmo's core capabilities.
import datetime #Imports the Python 'datetime' module, which enables this program to work with date & time-related data.  

def day_month_date(robot: cozmo.robot.Robot): 
#The line above defines the 'day_month_date' function and initiates an instance of Cozmo for the program to act upon.

	date = datetime.datetime.now().strftime('%A'+', '+'%B'+' '+'%d' + ', ' + '%Y') 
	#The line above defines the 'date' variable as a text string in the format of "Weekday, Month Date, Year". 
	#Additional date (and time) formats can be constructed by changing the %variables within the parentheses. 
	#See https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior for a listing of available variables.

	robot.say_text("Today is " + date).wait_for_completed() 
	#Now that we have converted the date data into a text string (the 'date' variable we just defined), we can use 
	#the 'say_text' method (from the 'cozmo' module we imported above) to have Cozmo read the weekday, month, date, and year aloud. 

cozmo.run_program(day_month_date)
#This line tells Cozmo to execute the 'day_month_date' function we just defined above.