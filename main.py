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
    fig = plt.subplots(figsize=(13, 7))
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

frm = Tk()
frm.geometry("1000x800")
Label(frm, text="COVID-19", font=("Kartika", 40, "underline"), fg="red").place(x=360, y=10)
t=100
title_color="#0099ff"

Label(frm, text="Injuries in all Countries :- ", font=("Arial", 15), fg=title_color).place(x=10, y=10+t)
Label(frm, text="Mean = "+str(round(statistics.mean(sick),3))).place(x=20, y=50+t)
Label(frm, text="Median = "+str(statistics.median(sick))).place(x=250, y=50+t)
Label(frm, text="Mode = "+str(statistics.mode(sick))).place(x=480, y=50+t)
Label(frm, text="Rang = "+str(rang(sick))).place(x=710, y=50+t)
Label(frm, text="IQR = "+str(IQR(sick))).place(x=20, y=75+t)
Label(frm, text="Variance = "+str(round(statistics.variance(sick),3))).place(x=250, y=75+t)
Label(frm, text="Standard Deviation = "+str(round(math.sqrt(statistics.variance(sick)),3))).place(x=480, y=75+t)
Button(frm, text="Plot-graph", command=plot_Injuries).place(x=20, y=110+t)
Button(frm, text="Bar-Graph", command=bar_Injuries).place(x=140, y=110+t)
Button(frm, text="Pie-Chart", command=pie_Injuries).place(x=260, y=110+t)
Button(frm, text="Boxplot", command=box_Injuries).place(x=380, y=110+t)
Label(frm, text="------------------------------------------------------------------------------------------------------"
                "---------------------------------------------------------------------------------------------").place(x=10, y=145+t)

h1=180
Label(frm, text="deaths in all Countries :- ", font=("Arial", 15), fg=title_color).place(x=10, y=10+h1+t)
Label(frm, text="Mean = "+str(round(statistics.mean(died),3))).place(x=20, y=50+h1+t)
Label(frm, text="Median = "+str(statistics.median(died))).place(x=250, y=50+h1+t)
Label(frm, text="Mode = "+str(statistics.mode(died))).place(x=480, y=50+h1+t)
Label(frm, text="Rang = "+str(rang(died))).place(x=710, y=50+h1+t)
Label(frm, text="IQR = "+str(IQR(died))).place(x=20, y=75+h1+t)
Label(frm, text="Variance = "+str(round(statistics.variance(died),3))).place(x=250, y=75+h1+t)
Label(frm, text="Standard Deviation = "+str(round(math.sqrt(statistics.variance(died)),3))).place(x=480, y=75+h1+t)
Button(frm, text="Plot-graph", command=plot_deaths).place(x=20, y=110+h1+t)
Button(frm, text="Bar-Graph", command=bar_deaths).place(x=140, y=110+h1+t)
Button(frm, text="Pie-Chart", command=pie_deaths).place(x=260, y=110+h1+t)
Button(frm, text="Boxplot", command=box_deaths).place(x=380, y=110+h1+t)
Label(frm, text="------------------------------------------------------------------------------------------------------"
                "---------------------------------------------------------------------------------------------").place(x=10, y=145+h1+t)

h2=180
Label(frm, text="healthful in all Countries :- ", font=("Arial", 15), fg=title_color).place(x=10, y=10+h1+h2+t)
Label(frm, text="Mean = "+str(round(statistics.mean(helth),3))).place(x=20, y=50+h1+h2+t)
Label(frm, text="Median = "+str(statistics.median(helth))).place(x=250, y=50+h1+h2+t)
Label(frm, text="Mode = "+str(statistics.mode(helth))).place(x=480, y=50+h1+h2+t)
Label(frm, text="Rang = "+str(rang(helth))).place(x=710, y=50+h1+h2+t)
Label(frm, text="IQR = "+str(IQR(helth))).place(x=20, y=75+h1+h2+t)
Label(frm, text="Variance = "+str(round(statistics.variance(helth),3))).place(x=250, y=75+h1+h2+t)
Label(frm, text="Standard Deviation = "+str(round(math.sqrt(statistics.variance(helth)),3))).place(x=480, y=75+h1+h2+t)
Button(frm, text="Plot-graph", command=plot_healthful).place(x=20, y=110+h1+h2+t)
Button(frm, text="Bar-Graph", command=bar_healthful).place(x=140, y=110+h1+h2+t)
Button(frm, text="Pie-Chart", command=pie_healthful).place(x=260, y=110+h1+h2+t)
Button(frm, text="Boxplot", command=box_healthful).place(x=380, y=110+h1+h2+t)
Label(frm, text="------------------------------------------------------------------------------------------------------"
                "---------------------------------------------------------------------------------------------").place(x=10, y=145+h1+h2+t)


# Button(frm, text="Quit", command=root.destroy)

frm.mainloop()
