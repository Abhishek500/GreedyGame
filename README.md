# GreedyGame
Calculates the number of sessions (valid and total) of a game and the average session time(only valid) from the dataset. The code takes care of missing data also to come up with total number of sessions.
The functions defined in the code are as follows:
1) unix_time_millis- Takes argument in date format and coverts to integer.
2) str2time- Shows the time with microseconds.
3) session_time-Calculates the time difference between the ggstop and previous index, while increasing the count of wrong_data_count when  no match  to ggstart or ggstop is found and count of merged_session_count is incresed if the time difference between ggstop and ggstart is less than 30 seconds. This is done to calculate the ratio of missing data which will satisfy the criteria of time difference of less than 30 seconds between ggstop and next ggstart.
 Two dictionaries are created:
 1) data- The code reads the raw data in 'lines'.  'data' is created which stores ai5, sdkv, ts,event and timestamp for each game_id.
Another dictionary called 'users' is created which stores session count, valid session count, valid session session length for each user(ai5) in every game_id before and after doing the missing value treatment, the latter being stored in adjusted_session_count and adjusted_valid_session_count)
In output:
'game_id' is the game_id in data, 'session_count' is the number of sessions for that game, 'valid_session_count' is the number of number of valid sessions, 'adjusted_session_count' is the number of sessions after taking the missing data into picture, 'adjusted_valid_session_count' is the number of valid sessions after taking missing data into consideration and  'avg_session_length' is the average duration of time spent on each game.
