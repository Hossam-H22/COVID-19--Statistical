from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import statistics
import math

country = []
sick = []
died = []
helth = []

with open('country.txt') as f1: country=f1.readlines()
with open('injuries.txt') as f2: sick=f2.readlines()
with open('deaths.txt') as f3: died=f3.readlines()
with open('healthful.txt') as f4: helth=f4.readlines()

for i in range(0, len(sick)):
    sick[i] = int(sick[i])
for i in range(0, len(died)):
    died[i] = int(died[i])
for i in range(0, len(helth)):
    helth[i] = int(helth[i])

def plot(items, s):
    fig = plt.subplots(figsize=(14, 8))
    plt.plot(country, items, marker='o')
    plt.title("COVID-19")
    plt.ylabel(s)
    plt.xlabel("Country")
    plt.grid()
    plt.show()

def bar(items, s):
    fig = plt.subplots(figsize=(14, 7))
    plt.bar(country, items)
    plt.xlabel('Country', fontweight='bold', fontsize=15)
    plt.ylabel(s, fontweight='bold', fontsize=15)
    plt.show()

def pie(items, s):
    fig = plt.subplots(figsize=(8, 7))
    plt.pie(items, labels=country)
    plt.title(s)
    plt.show()

def boxplot(items):
    fig = plt.subplots(figsize=(5, 6))
    plt.boxplot(items)
    plt.show()

def rang(items):
    sortList = sorted(items)
    length = len(items)
    return (sortList[length-1]-sortList[0])

def IQR(items):
    sortList = sorted(items)
    q3, q1 = np.percentile(sortList, [75, 25])
    return (q3-q1)

def z_score(x, x_bar, s):
    return ((x-x_bar)/s)

def correlation(items1, items2):
    r=0
    mean1=statistics.mean(items1)
    mean2 = statistics.mean(items2)
    s1= math.sqrt(statistics.variance(items1))
    s2= math.sqrt(statistics.variance(items2))
    for i in range(0, len(items1)):
        r += (z_score(items1[i], mean1, s1) * z_score(items2[i], mean2, s2))
    return round((r/len(items1)),1)

def correlation_rate(x):
    if x>=0.1 and x<=0.3 : return "  +ve Weak correlation coefficient"
    elif x>=-0.3 and x<=-0.1 : return "  -ve Weak correlation coefficient"
    elif x>=0.4 and x<=0.6 : return "  +ve Moderate correlation coefficient"
    elif x>=-0.6 and x<=-0.4 : return "  -ve Moderate correlation coefficient"
    elif x>=0.7 and x<=0.9 : return "  +ve Strong correlation coefficient"
    elif x>=-0.9 and x<=-0.7 : return "  -ve Strong correlation coefficient"
    elif x==1 : return "  There are same"
    elif x==0 : return "  No Correlation"

def b1(items1, items2, r):
    sy = math.sqrt(statistics.variance(items2))
    sx = math.sqrt(statistics.variance(items1))
    return round((r*(sy/sx)), 3)

def b0(items1, items2, r):
    x_bar = statistics.mean(items1)
    y_bar = statistics.mean(items2)
    b = b1(items1, items2, r)
    return round((y_bar-(b*x_bar)), 3)

def plot_Injuries():
    plot(sick, "Injuries")
def bar_Injuries():
    bar(sick, "Injuries")
def pie_Injuries():
    pie(sick, "Injuries")
def box_Injuries():
    boxplot(sick)

def plot_deaths():
    plot(died, "deaths")
def bar_deaths():
    bar(died, "deaths")
def pie_deaths():
    pie(died, "deaths")
def box_deaths():
    boxplot(died)

def plot_healthful():
    plot(helth, "healthful")
def bar_healthful():
    bar(helth, "healthful")
def pie_healthful():
    pie(helth, "healthful")
def box_healthful():
    boxplot(helth)


x_dimensional = 1000
y_dimensional = 950
frm = Tk()
frm.geometry(str(x_dimensional)+"x"+str(y_dimensional))
Label(frm, text="COVID-19", font=("Kartika", 40, "underline"), fg='red').place(x=360, y=10)
t=100
title_color="#0099ff"
# bg_button="black"
fg_button="#002db3"

Label(frm, text="Injuries in all Countries :- ", font=("Arial", 15), fg=title_color).place(x=10, y=10+t)
Label(frm, text="Mean = "+str(round(statistics.mean(sick),3))).place(x=20, y=50+t)
Label(frm, text="Median = "+str(statistics.median(sick))).place(x=250, y=50+t)
Label(frm, text="Mode = "+str(statistics.mode(sick))).place(x=480, y=50+t)
Label(frm, text="Rang = "+str(rang(sick))).place(x=710, y=50+t)
Label(frm, text="IQR = "+str(IQR(sick))).place(x=20, y=75+t)
Label(frm, text="Variance = "+str(round(statistics.variance(sick),3))).place(x=250, y=75+t)
Label(frm, text="Standard Deviation = "+str(round(math.sqrt(statistics.variance(sick)),3))).place(x=480, y=75+t)
Button(frm, text="Plot-graph", command=plot_Injuries, fg=fg_button).place(x=20, y=110+t)
Button(frm, text="Bar-Graph", command=bar_Injuries, fg=fg_button).place(x=140, y=110+t)
Button(frm, text="Pie-Chart", command=pie_Injuries, fg=fg_button).place(x=260, y=110+t)
Button(frm, text="Boxplot", command=box_Injuries, fg=fg_button).place(x=380, y=110+t)
Label(frm, text="------------------------------------------------------------------------------------------------------"
                "---------------------------------------------------------------------------------------------").place(x=10, y=145+t)

h1=165
Label(frm, text="deaths in all Countries :- ", font=("Arial", 15), fg=title_color).place(x=10, y=10+h1+t)
Label(frm, text="Mean = "+str(round(statistics.mean(died),3))).place(x=20, y=50+h1+t)
Label(frm, text="Median = "+str(statistics.median(died))).place(x=250, y=50+h1+t)
Label(frm, text="Mode = "+str(statistics.mode(died))).place(x=480, y=50+h1+t)
Label(frm, text="Rang = "+str(rang(died))).place(x=710, y=50+h1+t)
Label(frm, text="IQR = "+str(IQR(died))).place(x=20, y=75+h1+t)
Label(frm, text="Variance = "+str(round(statistics.variance(died),3))).place(x=250, y=75+h1+t)
Label(frm, text="Standard Deviation = "+str(round(math.sqrt(statistics.variance(died)),3))).place(x=480, y=75+h1+t)
Button(frm, text="Plot-graph", command=plot_deaths, fg=fg_button).place(x=20, y=110+h1+t)
Button(frm, text="Bar-Graph", command=bar_deaths, fg=fg_button).place(x=140, y=110+h1+t)
Button(frm, text="Pie-Chart", command=pie_deaths, fg=fg_button).place(x=260, y=110+h1+t)
Button(frm, text="Boxplot", command=box_deaths, fg=fg_button).place(x=380, y=110+h1+t)
Label(frm, text="------------------------------------------------------------------------------------------------------"
                "---------------------------------------------------------------------------------------------").place(x=10, y=145+h1+t)

h2=165
Label(frm, text="healthful in all Countries :- ", font=("Arial", 15), fg=title_color).place(x=10, y=10+h1+h2+t)
Label(frm, text="Mean = "+str(round(statistics.mean(helth),3))).place(x=20, y=50+h1+h2+t)
Label(frm, text="Median = "+str(statistics.median(helth))).place(x=250, y=50+h1+h2+t)
Label(frm, text="Mode = "+str(statistics.mode(helth))).place(x=480, y=50+h1+h2+t)
Label(frm, text="Rang = "+str(rang(helth))).place(x=710, y=50+h1+h2+t)
Label(frm, text="IQR = "+str(IQR(helth))).place(x=20, y=75+h1+h2+t)
Label(frm, text="Variance = "+str(round(statistics.variance(helth),3))).place(x=250, y=75+h1+h2+t)
Label(frm, text="Standard Deviation = "+str(round(math.sqrt(statistics.variance(helth)),3))).place(x=480, y=75+h1+h2+t)
Button(frm, text="Plot-graph", command=plot_healthful, fg=fg_button).place(x=20, y=110+h1+h2+t)
Button(frm, text="Bar-Graph", command=bar_healthful, fg=fg_button).place(x=140, y=110+h1+h2+t)
Button(frm, text="Pie-Chart", command=pie_healthful, fg=fg_button).place(x=260, y=110+h1+h2+t)
Button(frm, text="Boxplot", command=box_healthful, fg=fg_button).place(x=380, y=110+h1+h2+t)
Label(frm, text="------------------------------------------------------------------------------------------------------"
                "---------------------------------------------------------------------------------------------").place(x=10, y=145+h1+h2+t)


r = correlation(sick, helth)
Label(frm, text="r = "+str(r)+correlation_rate(r)).place(x=20, y=75+h1+h2+t+100)
Label(frm, text="Y = "+str(b0(sick, helth, r))+" + "+str(b1(sick, sick, r))+" X").place(x=20, y=75+h1+h2+t+125)

table = 170
row = 180
for i in range(len(country)):
    Label(frm, text=country[i]).place(x=20+(row*0), y=75+h1+h2+t+table+(i*20))
    Label(frm, text=str(sick[i])).place(x=20+(row*1), y=75+h1+h2+t+table+(i*20))
    Label(frm, text=str(died[i])).place(x=20+(row*2), y=75+h1+h2+t+table+(i*20))
    Label(frm, text=str(helth[i])).place(x=20+(row*3), y=75+h1+h2+t+table+(i*20))



Button(frm, text="Quit", command=frm.destroy, fg="#b30000").place(x=x_dimensional-50, y=y_dimensional-40)
frm.mainloop()