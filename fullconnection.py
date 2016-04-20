# Author: Kadar Anwar and Brian Elliott
# Purpose: To read data from an Arduino UNO board using a serial connection
# and write the data to a text file
# Language: Python 2.7
# Date: 3/30/2016

# Import libraries
import serial	# Serial library to handle serial connection to Arduino
#import os	# OS library to handle sending Linux commands to host.
import MySQLdb # Importing mysql library
import time # importing time library
import datetime #module for importing the date and time

# Open a serial handler on the appropriate port with a
# 9600 baud connection rate
# Note: Need to modify this to automatically detect the TTY port
# Also need to look into using the os library to automatically
# chown the port to my user.
ser = serial.Serial('/dev/ttyACM0', 9600)

# creating output list variable and first and second values below
def main():
	output = []
	output.append(0)
	#getting propertyID from the user
	output.append(raw_input("What is your PropertyID?: "))
	# Loop to continously read the input
	while True:	
		print "Gathering Data..."
		endTime = time.time() + 5
		while time.time() < endTime:
			# get the input from the arduino and strip the newline chracter from it
			myData = ser.readline().strip()
			# checking to see if the \r character is in the data being read, this is an error prevention
			if '\r' not in myData and myData != '':	
				# adding output together 
				output[0] = int(myData)
				#checking the output value for bug detection
				#print output[0]
				#print output[1]

		mysqlFunc(output[1], output[0])


def mysqlFunc(PropertyID, Consumption):

	db = MySQLdb.connect(host="127.0.0.1",   # Our amazon host IP
 					 user="root",   # Our mysql username
 					 passwd="password", # our mysql password
 					 db="smarthome",    # name of our database
 					 port=3306)     # opened port for our database

	# Creating a Cursor object letting us execute our Queries :D
	cursor = db.cursor()
	cursor.execute("UPDATE water SET Consumption=%s, Rate=%s, WarningLevel=%s, TimePassed=%s WHERE PropertyID=%s", (str(Consumption), str(0.2), str(700), str(datetime.datetime.now()), str(PropertyID)))
	db.commit()
	print "Data Uploaded!"
	cursor.execute("SELECT * FROM water")
	print cursor.fetchall()
	#cursor.execute(
	#	UPDATE water SET Consumption=%s, Rate=%s, WarningLevel=%s, TimePassed=%s, PropertyID=%s
	# WHERE PropertyID = %s, (Consumption, Rate, WarningLevel, TimePassed, PropertyID, PropertyID))


	db.close()

main()
