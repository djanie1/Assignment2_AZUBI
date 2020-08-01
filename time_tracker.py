# Write a program that would help Nana track his money.

from tkinter import *
from datetime import timedelta
import datetime


#import pandas as pd

#function to remove white spaces from project name to be used as the excel file name
def remove(string): 
	return string.replace(" ", "")     #removes spaces in project name to store output file as "projectname.xlsx" without spaces

window = Tk()
#window.title("TIME TRACKER")
window.geometry('285x480')
window.configure(bg='white')



greeting= Label(window, text="Welcome Nana, click Start to start timer", font=("Arial Bold", 10),background='white')
greeting.grid(column=0, row=1)

begun = Label(window, font=("Arial", 10),background='white')
begun.grid(column=0, row=3)

#stores start time of project
def start_time():
    global start_now
    start_now = datetime.datetime.now()
    started=start_now.strftime("Date:%Y-%m-%d  Start time:%H:%M")
    global started_time
    started_time=start_now.strftime("%H:%M")
    begun.configure (text=started)
    return started_time
   
    
#Start button
#btn = Button(window, text="START",command=calculate_date_time,background='white')
#btn.grid(column=0, row=2)

Project = Label(window, text="Enter project name", font=("Arial Bold", 10),background='white')
Project.grid(column=0, row=4)

#lbl5 = Label(window, text="Amount per hour:", font=("Arial", 10),background='white')
#lbl5.grid(column=0, row=5)

#variable that holds how much he earns
name = Entry(window,width=40)
name.grid(column=0, row=6)
name.focus()

total_time = Label(window, text="Hours spent:", font=("Arial", 20),background='white')
total_time.grid(column=0,row=7)

total_amount = Label(window, text="You have earned ($):", font=("Arial", 20),background='white')
total_amount.grid(column=0,row=9)

#total_time = Label(window, font=("Arial", 10),background='white')
#total_time.grid(column=0,row=10)

#function that stores your stop time and takes your start time and calculates your earnings
def end_work():
    
    global end_time
    global hours_worked
    global total_pay

    stop_time = datetime.datetime.now()
    
    end_time=stop_time.strftime("%H:%M")


    start_hour=started_time
    delta1 = timedelta(hours=int(start_hour.split(':')[0]), minutes=int(start_hour.split(':')[1]))
    hour_start = delta1.total_seconds()/3600
   

    end_hour=end_time
    delta2 = timedelta(hours=int(end_hour.split(':')[0]), minutes=int(end_hour.split(':')[1]))
    hour_end = delta2.total_seconds()/3600
   
    
    #amount he earns
    Project_name=str(name.get())
    
    
    hours_worked=round(hour_end-hour_start,1)
    total_pay= hours_worked*float(5)
    
    #displays the hours spent working
    total_time.configure(text=str(hours_worked)+("Hrs"))
    total_amount.configure(text=("$")+str(total_pay))
    

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
    g = str(start_now.year)+"-"+str(start_now.month)+"-"+str(start_now.day)
    worksheet.write('B2',g )  
    h = str(start_now.hour)+":"+str(start_now.minute)
    worksheet.write('C2', h) 
    g1 = str(stop_time.year)+"-"+str(stop_time.month)+"-"+str(stop_time.day)
    worksheet.write('D2',g1 )  
    h1 = str(stop_time.hour)+":"+str(stop_time.minute)
    worksheet.write('E2', h1) 
    worksheet.write('F2', str(hours_worked)) 
    worksheet.write('G2', str(total_pay)) 
    workbook.close()

    
    
    


    
start = Button(
    text="Start",
    width=25,
    height=5,
    bg="green",
    fg="white",
    font=("Arial",15),
    command=start_time
)
start.grid(column=0,row=8)  


   
 #stop button 
finish = Button(
    text="Finish",
    width=25,
    height=5,
    bg="red",
    fg="white",
    font=("Arial",15),
    command=end_work
)
finish.grid(column=0, row=11)


window.mainloop()
