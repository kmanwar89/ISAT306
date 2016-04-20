# ISAT306 
This repo will host Python and Arduino sketches for ISAT 306 at JMU, Spring 2016.
The code contained here is to support the semester project involving using a water flow meter
and CT to measure water and electrical usage. The project's goal is to create
a cheap water and electrical meter with a web-page frontend and a mobile app
that shows the user usage statistics for different properties.

3-11-2016
Finally organized files and added everything to GitHub. Made repository public as well.

3-30-2016
Added files for new flow meter code and a Python file that handles data input and writing to text file.

4-19-2016
Old files deleted and new files added after collaboration with classmate.  Arduino code optimized, Python code completey
re-written and multiple files combined into one.  Data is no longer stored in text files and is pushed to the database after polling for 5 instances.  Brian re-wrote the code to make use of MySQL as opposed to sockets.
