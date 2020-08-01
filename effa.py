from datetime import datetime as dt
from datetime import timedelta as td
import csv

# Print a message out to the user
print('\nTime Tracker')
print('Please Enter Date and Time at start of work')
print('-------------------------------------------')

# prompt user to enter date and time in the specified format
entered_start_date = input('Enter start of work date (format - DD-MM-YYYY) : ')
entered_start_time = input('Enter start of work time (format - H:M AM/PM) : ')
print('\n')
print('--------------------------------------------------------------------')
entered_finish_date = input('Enter end of work date: (format - DD-MM-YYYY) :')
entered_finish_time = input('Enter end of work time: (format - H:M AM/PM) :')

# using the datetime module converted the string entered into datetime object
start_datetime_str = f'{entered_start_date} {entered_start_time}'
start_datetime_obj = dt.strptime(start_datetime_str, '%d-%m-%Y %H:%M %p')

finish_datetime_str = f'{entered_finish_date} {entered_finish_time}'
finish_datetime_obj = dt.strptime(finish_datetime_str, '%d-%m-%Y %H:%M %p')


# a function to check if the time is AM or PM in the 12 Hour format and return usable start date and time
def datetime_returner(datetime_object, datetime_string):
    if datetime_object.hour < 12:
        if datetime_string[-2:].upper() == 'PM':
            start_date = datetime_object + td(hours=12)
            return start_date
        elif datetime_string[-2:].upper() == 'AM':
            start_date = datetime_object
            return start_date
    else:
        if datetime_string[-2:].upper() == 'AM':
            start_date = datetime_object - td(hours=12)
            return start_date
        elif datetime_string[-2:].upper() == 'PM':
            start_date = datetime_object
            return start_date


# get the useful datetime for your calculations
start_datetime = datetime_returner(start_datetime_obj, start_datetime_str)
finish_datetime = datetime_returner(finish_datetime_obj, finish_datetime_str)

# subtract start time from finish time
time_difference = finish_datetime - start_datetime

# split the time_difference on the : and get the first index as hour and convert the string to integer
hours = int(str(time_difference).split(':')[0])

# split the time_difference on the : and get the second index as minute and covert the string to integer
minutes = int(str(time_difference).split(':')[1])

# convert the minutes to a decimal value
decimal_minute = (minutes * 0.5) / 30

# calculate the actual time worked by adding the hour to decimal_minute
time_worked = hours + decimal_minute

# calculate the money made by multiplying as below
money_made = round((time_worked * 5), 2)

# print the results to the user as below
print(f'Hello, you worked for {hours} hours, {minutes} minutes and made GHS {money_made}')

log = open('tracker_log.csv', "w", newline="")
writer = csv.writer(log)
# setting header for csv file
writer.writerow(['Start Date', 'Start Time', 'Finish Date', 'Finish Time', 'Hours Worked', 'Money Made'])

# writing first row of data
writer.writerow([entered_start_date, entered_start_time, entered_finish_date, entered_finish_time, time_worked, money_made])
log.close()
