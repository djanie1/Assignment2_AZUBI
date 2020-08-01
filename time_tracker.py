# Write a program that would help Nana track his money.


from datetime import datetime


def remove(string): 
	return string.replace(" ", "")     #removes spaces in project name to store output file as "projectname.xlsx" without spaces


Project_name = input ('Enter name of project:')


print("\n")
print ("START DATE DETAILS")
dt = datetime.now()
Start_year = dt.year
Start_month = dt.month
Start_day = dt.day
Start_hour = dt.hour
Start_minute = dt.minute

print ('The start date is today:', Start_year,'-', Start_month,'-', Start_day)
print ('The start time is now:', Start_hour,':', Start_minute)
print("\n")



print ("FINISH DATE DETAILS")
Finish_year= input ('Enter finish year of project (eg. 2019):')
Finish_year= int (Finish_year) # Assign as int because input automatically accepts strings as its data type
Finish_month= input('Enter finish month of the project (eg.December is represented as 12):')
Finish_month= int (Finish_month)
Finish_day= input ('Enter finish day of the month (eg.21):')
Finish_day= int (Finish_day)
Finish_time= input ('Enter finish time of the project (eg. 11:00 or 12:30):')
mylist1= Finish_time.split(':')
Finish_hour= int(mylist1[0])
Finish_minute= int(mylist1[1])



start_date = datetime(Start_year, Start_month, Start_day, Start_hour,Start_minute )
Finish_date = datetime(Finish_year, Finish_month, Finish_day, Finish_hour,Finish_minute)


difference_between_times=  Finish_date - start_date

hours_of_project=  difference_between_times.total_seconds()/ 60*60
pay_per_hour = 5
total_amount_received = hours_of_project * pay_per_hour

currency = "$"



print("\n")
print ("DETAILS ON PAYMENT")
print('Nana spent %f %s on project %s' % (hours_of_project,'hours', Project_name))
print('Nana will receive %s %f for project %s' % (currency,total_amount_received, Project_name))


# Install pip on laptop terminal
# With pip installed, install xlsxwriter on laptop terminal
# This helps save information in an Excel file.

import xlsxwriter 
workbook = xlsxwriter.Workbook(remove(Project_name)+".xlsx") 
worksheet = workbook.add_worksheet() 

#Setting Headers
worksheet.write('A1', 'ProjectName') 
worksheet.write('B1', 'StartDate') 
worksheet.write('C1', 'StartTime') 
worksheet.write('D1', 'FinishDate') 
worksheet.write('E1', 'FinishTime') 
worksheet.write('F1', 'HoursSpent') 
worksheet.write('G1', 'AmountReceived') 

worksheet.write('A2', Project_name)
g = str(Start_year)+"-"+str(Start_month)+"-"+str(Start_day)
worksheet.write('B2',g )  
h = str(Start_hour)+":"+str(Start_minute)
worksheet.write('C2', h) 
g1 = str(Finish_year)+"-"+str(Finish_month)+"-"+str(Finish_day)
worksheet.write('D2',g1 )  
h1 = str(Finish_hour)+":"+str(Finish_minute)
worksheet.write('E2', h1) 
worksheet.write('F2', str(hours_of_project)) 
worksheet.write('G2', str(total_amount_received)) 
workbook.close()
