
from tkinter import *
import sqlite3
from PIL import Image, ImageTk
from bs4 import BeautifulSoup
import csv
import requests
from numpy.random import randint
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


# Web scraping
html = requests.get('https://docs.google.com/spreadsheets/d/1juMkL3DrnYw4czji43DcIUoN5JIq1zYMfSbVMJEnliM/edit?usp=sharing').text
soup = BeautifulSoup(html, "lxml")
tables = soup.find_all("table")
index = 0

#Working with excel file
with open(r'C:\Users\Manas Kapoor\Desktop\project_stocks\imp.csv', 'w', newline='') as file_final:
    csvwriter = csv.writer(file_final)
count=0
for table in tables:
    with open(str(index) + ".csv", "w") as f:
        if count<1:
            wr = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
            a=[[td.text for td in row.find_all("td")] for row in table.find_all("tr")]
            wr.writerows([[td.text for td in row.find_all("td")] for row in table.find_all("tr")])
            count+=1
            
            # csvwriter.writerow([[td.text for td in row.find_all("td")] for row in table.find_all("tr")]
        index = index + 1
count=0
for i in a:
    if len(i)==27 and i[0]!='' and i[0]!='' and count<len(a)/2:
        if (i[0]=='Timestamp') and count>1:
            break
        count+=1
        with open(r'C:\Users\Manas Kapoor\Desktop\project_stocks\imp.csv', 'a') as f:
            csvwriter = csv.writer(f)

            csvwriter.writerow(i)

df = pd.read_csv (r'C:\Users\Manas Kapoor\Desktop\project_stocks\imp.csv')
key=df.key
global temp_1
global temp_2
global temp_3

#Depression Calculation
def depression_calculation(d1,d2,d3,d4,d5,d6):
    ans=0
    sum=0
    result_depression=[]
    for i in range(0,len(d1)):
        sum=d1[i]+d2[i]+d3[i]+d4[i]+d5[i]+d6[i]
        if(sum>18):
            result_depression.append(1)
        elif(sum>12):
            result_depression.append(0.75)
        elif(sum>6):
            result_depression.append(0.50)
        else:
            result_depression.append(0.25)

    result_2=np.array(result_depression)
    result=np.sum(result_2)
    temp_1=result/len(d1)

    dep=['Depressed','Not Depressed']
    data=[result/len(d1)*100,100-(result/len(d1)*100)]

    fig = plt.figure(figsize =(10, 7))
    plt.pie(data, labels = dep)
    fig.savefig('C:/Users/Manas Kapoor/Desktop/hackathon/3.png')
    return temp_1,fig

#Anxiety calculaion 
def anxiety_calculation(a1,a2,a3,a4,a5,a6):
    ans=0
    sum=0
    result_anxiety=[]
    for i in range(0,len(a1)):
        sum=a1[i]+a2[i]+a3[i]+a4[i]+a5[i]+a6[i]
        if(sum>18):
            result_anxiety.append(1)
        elif(sum>12):
            result_anxiety.append(0.75)
        elif(sum>6):
            result_anxiety.append(0.50)
        else:
            result_anxiety.append(0.25)

    result_2=np.array(result_anxiety)
    result=np.sum(result_2)
    temp_2=result/len(a1)

    dep=['Anxiety','No Anxiety']
    data=[result/len(a1)*100,100-(result/len(a1)*100)]

    fig = plt.figure(figsize =(10, 7))
    plt.pie(data, labels = dep)
    fig.savefig('C:/Users/Manas Kapoor/Desktop/hackathon/2.png')
    return temp_2,fig

#PTSD calculaion 
def ptsd_calculation(p1,p2,p3,p4,p5):
    ans=0
    sum=0
    result_ptsd=[]
    for i in range(0,len(p1)):
        sum=p1[i]+p2[i]+p3[i]+p4[i]+p5[i]
        if(sum>4):
            result_ptsd.append(1)
        elif(sum>3):
            result_ptsd.append(0.75)
        elif(sum>2):
            result_ptsd.append(0.50)
        else:
            result_ptsd.append(0.25)

    result_2=np.array(result_ptsd)
    result=np.sum(result_2)

    dep=['PTSD','Not PTSD']
    data=[result/len(p1)*100,100-(result/len(p1)*100)]
    temp_3=result/len(p1)

    fig = plt.figure(figsize =(10, 7))
    plt.pie(data, labels = dep)
    fig.savefig('C:/Users/Manas Kapoor/Desktop/hackathon/1.png')
    return temp_3,fig

#most prevalent disorder finder
def major(temp1,temp2,temp3):
    if(temp1>=temp2 and temp1>=temp3):
        print("According to our analysis, we have planned an activity which involves depression")
    elif(temp2>temp1 and temp2>temp3):
        print("According to our analysis, we have planned an activity which involves anxiety")
    else:
        print("According to our analysis, we have planned an activity which involves ptsd")
def analysis(df,username,key):

    d1=[]
    d2=[]
    d3=[]
    d4=[]
    d5=[]
    d6=[]
    a1=[]
    a2=[]
    a3=[]
    a4=[]
    a5=[]
    a6=[]
    p1=[]
    p2=[]
    p3=[]
    p4=[]
    p5=[]
    p6=[]
    dep1=df.d1
    dep2=df.d2
    dep3=df.d3
    dep4=df.d4
    dep5=df.d5
    dep6=df.d6
    an1=df.a1
    an2=df.a2
    an3=df.a3
    an4=df.a4
    an5=df.a5
    an6=df.a6
    pt1=df.p1
    pt2=df.p2
    pt3=df.p3
    pt4=df.p4
    pt5=df.p5
    

    for i in range (0,len(key)):
        if username==key[i]:
            d1.append(dep1[i])
            d2.append(dep2[i])
            d3.append(dep3[i])
            d4.append(dep4[i])
            d5.append(dep5[i])
            d6.append(dep6[i])
            a1.append(an1[i])
            a2.append(an2[i])
            a3.append(an3[i])
            a4.append(an4[i])
            a5.append(an5[i])
            a6.append(an6[i])
            p1.append(pt1[i])
            p2.append(pt2[i])
            p3.append(pt3[i])
            p4.append(pt4[i])
            p5.append(pt5[i])
    global fig_depression
    global fig_anxiety
    global fig_ptsd
    global temp_1
    global temp_2
    global temp_3

    temp_1,fig_depression=depression_calculation(d1,d2,d3,d4,d5,d6)
    temp_2,fig_anxiety=anxiety_calculation(a1,a2,a3,a4,a5,a6)
    temp_3,fig_ptsd=ptsd_calculation(p1,p2,p3,p4,p5)
    print(d1)
    major(temp_1,temp_2,temp_3)
def windows():

    #create an object to create a window
    global window
    window = Tk()
    window.geometry("1920x1080")
    image2 = Image.open("C:/Users/Manas Kapoor/Desktop/hackathon/background.png")
    image1=image2.resize((1920,1080))
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test

    # Position image
    label1.place(x=0, y=0)

    #add title to the window
    window.title("Login and Signup system")
    
    #adding two buttons - login and signup
    button1 = Button(window,text="Login",height=2,width=30,borderwidth=10,bg='pink',font='times 16 bold',command=login)
    #button1.grid(row=15,column=17)
    button1.place(x=1250, y=600)
    button2 = Button(window,text="Signup",height=2,width=30,borderwidth=10,bg='pink',font='times 16 bold',command=signup)
    #button2.grid(row=18,column=28)
    button2.place(x=1250, y=690)
    #calling mainloop method which is used when your application is ready to run and it tells the code to keep displaying




    window.mainloop()

def interface():
        
    
            login_window.destroy() #closes the previous window
            global inter
            analysis(df,user_name,key)
            inter = Tk() #creates a new window for signup process
            image2 = Image.open("C:/Users/Manas Kapoor/Desktop/hackathon/activate.png")
            image1=image2.resize((1920,1080))
            test = ImageTk.PhotoImage(image1)

            l1 = Label(image=test)
            l1.image = test

            # Position image
            l1.place(x=0, y=0)
            inter.geometry("1920x1080") #dimensions for new window
            inter.title("SAMWAD") #title for the window
            l1 = Label(inter,text=user_name,font="times 30",bg='white')
            l1.place(x=1360,y=570)
            
            l2 = Label(inter,text="https://forms.gle/zkYdVXRhssKGctVX8",font="times 20")
            l2.place(x=1100,y=320)            
            b3 = Button(inter,text="logout",width=20,height=3,font='times 20 bold',bg='sky blue',borderwidth=10,command=back)
            b3.place(x=1400,y=800)
            b4 = Button(inter,text="ANALYZE!",width=20,height=3,font='times 20 bold',bg='sky blue',borderwidth=10,command=final)
            b4.place(x=1000,y=800)
            
            inter.mainloop()
def back():
    inter.destroy()
    windows()
#Actions on Pressing Login Button
def back2():
    ana.destroy()
    windows()
def back3():
    planning.destroy()
    windows()
def login():
    def login_database():
        conn = sqlite3.connect("1.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM test WHERE email=? AND password=?",(e1.get(),e2.get()))
        row=cur.fetchall()
        conn.close()
        print(row)
        if row!=[]:
            global user_name
            user_name=row[0][1]
            l3.config(text="user name found with name: "+user_name)
            
            interface()
        else:
            l3.config(text="user not found")
    
            
           
    window.destroy()  #closes the previous window
    global login_window #creates a new window for loging in
    login_window=Tk()
    image2 = Image.open("C:/Users/Manas Kapoor/Desktop/hackathon/background.png")
    image1=image2.resize((1920,1080))
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test
    label1.place(x=0,y=0)
    login_window.title("LogIn")  #set title to the window
    login_window.geometry("1920x1080")  #set dimensions to the window
    #add 2 Labels to the window
    #bg=PhotoImage(file= "hi.jpg")
    l1 = Label(login_window,text="Email:    ",font="times 20 bold")
    l1.place(x=1250,y=600)

    l2 = Label(login_window,text="Password: ",font="times 20 bold")
    l2.place(x=1250,y=660)

    l3 = Label(login_window,font="times 20")
    l3.grid(row=5,column=1)

    #creating 2 adjacent text entries
    email_text = StringVar() #stores string
    e1 = Entry(login_window,textvariable=email_text,width=30)
    e1.place(x=1450,y=600)

    password_text = StringVar()
    e2 = Entry(login_window,textvariable=password_text,width=30,show='*')
    e2.place(x=1450,y=660)

    #create 1 button to login
    b = Button(login_window,text="login",width=30,command=login_database)
    b.place(x=1450,y=700)
    
    login_window.mainloop()
def plan():
    ana.destroy()
    global planning
    planning=Tk()
    image2 = Image.open("C:/Users/Manas Kapoor/Desktop/hackathon/activities.png")
    image1=image2.resize((1920,1080))
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test
    label1.place(x=0,y=0)
    planning.title("Activities")  #set title to the window
    planning.geometry("1920x1080")  #set dimensions to the window
    b4=Button(planning,text="Log Out",width=20,font='times 15 bold',command=back3)
    b4.place(x=860,y=925)
    planning.mainloop()
#Actions on Pressing Signup button
def final():
        
    
            inter.destroy() #closes the previous window
            global ana
            ana = Tk() #creates a new window for signup process
            image2 = Image.open("C:/Users/Manas Kapoor/Desktop/hackathon/pie.png")
            image1=image2.resize((1920,1080))
            test = ImageTk.PhotoImage(image1)

            l1 = Label(image=test)
            l1.image = test

            # Position image
            l1.place(x=0, y=0)
            image2 = Image.open("C:/Users/Manas Kapoor/Desktop/hackathon/3.png").resize((450,450))
            test = ImageTk.PhotoImage(image2)

            l2 = Label(image=test)
            l2.image = test

            # Position image
            l2.place(x=160, y=320)
            image3 = Image.open("C:/Users/Manas Kapoor/Desktop/hackathon/2.png").resize((450,450))
            test1 = ImageTk.PhotoImage(image3)

            l3 = Label(image=test1)
            l3.image = test1
            # Position image
            l3.place(x=780, y=320)
            image4 = Image.open("C:/Users/Manas Kapoor/Desktop/hackathon/1.png").resize((450,450))
            test2 = ImageTk.PhotoImage(image4)

            l4 = Label(image=test2)
            l4.image = test2

            # Position image
            l4.place(x=1350, y=320)
            
            ana.geometry("1920x1080") #dimensions for new window
            ana.title("OUTCOME") #title for the window
            l1 = Label(ana,text=str(round(temp_3*100,2))+"%",font="times 20")
            l1.place(x=1575,y=800)
            
            l2 = Label(ana,text=str(round(temp_1*100,2))+"%",font="times 20")
            l2.place(x=335,y=800)            
            l3 = Label(ana,text=str(round(temp_2*100,2))+"%",font="times 20")
            l3.place(x=945,y=800)
            l4 = Label(ana,text="HAPPINESS INDEX = "+str(round(1-(temp_1+temp_2+temp_3)/3,2)),font="times 20 bold")
            l4.place(x=200,y=900)
            b4=Button(ana,text="Logout",width=20,command=back2)
            b4.place(x=1500,y=900)
            b4=Button(ana,text="Personalized Recommendations",width=50,font='times 15 bold',command=plan)
            b4.place(x=650,y=900)

            ana.mainloop()
def signup():
    #Database action on pressing signup button
    def signup_database():
        conn = sqlite3.connect("1.db") #create an object to call sqlite3 module & connect to a database 1.db
        #once you have a connection, you can create a cursor object and call its execute() method to perform SQL commands
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY,name text,email text,password text)")
        cur.execute("INSERT INTO test Values(Null,?,?,?)",(e1.get(),e2.get(),e3.get()))
        
        #execute message after account successfully created
        l4 = Label(signup_window1,text="account created",font="times 15")
        l4.place(x=1450,y=820)
        
        conn.commit()  #save the changes 
        conn.close() #close the connection
        back1()
    window.destroy()  #closes the previous window
    global signup_window1 #creates a new window for signup process
    signup_window1 = Tk()
    signup_window1.geometry("1920x1080") #dimensions for new window
    signup_window1.title("Sign Up") #title for the window
    # Add image file
    bg = PhotoImage( file = "C:/Users/Manas Kapoor/Desktop/hackathon/background.png")
    
    # Show image using label
    l1 = Label(image = bg)
    l1.place(x = 0,y = 0)

    
    
    
    
    #create 3 Labels
    l1 = Label(signup_window1,text="User Name: ",font="times 20")
    l1.place(x=1250,y=600)

    l2 = Label(signup_window1,text="User email: ",font="times 20")
    l2.place(x=1250,y=660)

    l3 = Label(signup_window1,text="Password: ",font="times 20")
    l3.place(x=1250,y=720)

    #create 3 adjacent text entries
    name_text = StringVar() #declaring string variable for storing name and password
    e1 = Entry(signup_window1,textvariable=name_text,borderwidth=7)
    e1.place(x=1450,y=600)

    email_text = StringVar()
    e2 = Entry(signup_window1,textvariable=email_text,borderwidth=7)
    e2.place(x=1450,y=660)

    password_text = StringVar()
    e3 = Entry(signup_window1,textvariable=password_text,borderwidth=7,show='*')
    e3.place(x=1450,y=720)

    #create 1 button to signup
    b1 = Button(signup_window1,text="Signup",width=15,font='times 15 bold',borderwidth=10,command=signup_database)
    b1.place(x=1430,y=760)
    signup_window1.mainloop()
def back1():
    signup_window1.destroy()
    windows()

windows()
