The Python script, datas.py is used to create the data set. It retrieves the source data set and transforms it to produce the final result.It calculates the number of sessions (valid and total) for each game in  and the average session time(only valid) from the dataset. The code takes care of missing data also to come up with total number of sessions.
The output in this repository was created by running the datas.py script using Python version 3.5.2 (2017-07-27) on Ubuntu 16.0.4 .
This script requires the datetime module.
Convert the date string into date type
Calculate the number of sessions with only the correct pair of start and stop timings, calculate the number of valid sessions from it. Ignore the session lenght less than 1 second
Keep count of the number of times there is missing data and number of times the the time difference between session stop time and session start time is less than or equal to 30 seconds. Use these to find the adjusted session count.
Print the the result.
