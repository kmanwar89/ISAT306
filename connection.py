# Author: Kadar Anwar
# Purpose: To read data from an Arduino UNO board using a serial connection
# and write the data to a text file
# Language: Python 2.7
# Date: 3/30/2016

# Import serial library
import serial

# Open a serial handler on the appropriate port with a
# 9600 baud connection rate
# Note: Need to modify this to automatically detect the TTY port
# Also need to look into using the os library to automatically
# chown the port to my user.
ser = serial.Serial('/dev/ttyACM1', 9600)

# Loop to continously read the input
# Note: Need to modify this to be more robust
while True:
	outfile = open('data.txt', 'a')
	output = ser.readline()
	outfile.write(output)
