from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import statistics
import math
import pandas as pd

head = ['Country', 'Injuries', 'Deaths', 'Recovered']
country = []
sick = []
died = []
helth = []

with open('country.txt') as f1: country=f1.readlines()
with open('injuries.txt') as f2: sick=f2.readlines()
with open('deaths.txt') as f3: died=f3.readlines()
with open('Recovered.txt') as f4: helth=f4.readlines()

for i in range(0, len(sick)-1):
    country[i] = country[i].rstrip()
for i in range(0, len(sick)):
    sick[i] = int(sick[i])
for i in range(0, len(died)):
    died[i] = int(died[i])
for i in range(0, len(helth)):
    helth[i] = int(helth[i])

data = {'Country': country, 'Injuries': sick, 'Deaths': died, 'Recovered': helth}
table = pd.DataFrame(data, columns=head, index=country)


def plot(items1, items2, s1, s2):
    fig = plt.subplots(figsize=(14, 8))
    plt.plot(items1, items2, marker='o')
    plt.title("COVID-19")
    plt.ylabel(s1)
    plt.xlabel(s2)
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
    plot(country, sick, "Injuries", "Country")
def bar_Injuries():
    bar(sick, "Injuries")
def pie_Injuries():
    pie(sick, "Injuries")
def box_Injuries():
    boxplot(sick)

def plot_deaths():
    plot(country, died, "Deaths", "Country")
def bar_deaths():
    bar(died, "Deaths")
def pie_deaths():
    pie(died, "Deaths")
def box_deaths():
    boxplot(died)

def plot_Recovered():
    plot(country, helth, "Recovered", "Country")
def bar_Recovered():
    bar(helth, "Recovered")
def pie_Recovered():
    pie(helth, "Recovered")
def box_Recovered():
    boxplot(helth)

def relation1():
    fig = plt.subplots(figsize=(14, 8))
    plt.scatter(country, sick)
    plt.scatter(country, died)
    plt.title("COVID-19")
    plt.ylabel("Injuries & Deaths")
    plt.xlabel("Country")
    plt.grid()
    plt.show()

def relation2():
    fig = plt.subplots(figsize=(14, 8))
    plt.scatter(country, sick)
    plt.scatter(country, helth)
    plt.title("COVID-19")
    plt.ylabel("Injuries & Recovered")
    plt.xlabel("Country")
    plt.grid()
    plt.show()

def relation3():
    fig = plt.subplots(figsize=(14, 8))
    plt.scatter(country, helth)
    plt.scatter(country, died)
    plt.title("COVID-19")
    plt.ylabel("Recovered & Deaths")
    plt.xlabel("Country")
    plt.grid()
    plt.show()

x_dimensional = 1450
y_dimensional = 800
frm = Tk()
frm.title("COVID-19--Statistical")
frm.geometry(str(x_dimensional)+"x"+str(y_dimensional))
# frm['bg']='green'
Label(frm, text="COVID-19", font=("Kartika", 45, "underline"), fg='#0000cc').place(x=600, y=10)
title_color="#314f81"
fg_button="#002db3"

Label(frm, text="Injuries in all Countries :- ", font=("Arial", 15), fg=title_color).place(x=10, y=110)
Label(frm, text="Mean = "+str(round(statistics.mean(sick),3))).place(x=20, y=150)
Label(frm, text="Median = "+str(statistics.median(sick))).place(x=250, y=150)
Label(frm, text="Mode = "+str(statistics.mode(sick))).place(x=480, y=150)
Label(frm, text="Rang = "+str(rang(sick))).place(x=710, y=150)
Label(frm, text="IQR = "+str(IQR(sick))).place(x=20, y=175)
Label(frm, text="Variance = "+str(round(statistics.variance(sick), 3))).place(x=250, y=175)
Label(frm, text="Standard Deviation = "+str(round(math.sqrt(statistics.variance(sick)),3))).place(x=480, y=175)
Button(frm, text="Plot-graph", command=plot_Injuries, width=10, fg=fg_button).place(x=20, y=210)
Button(frm, text="Bar-Graph", command=bar_Injuries, width=10, fg=fg_button).place(x=140, y=210)
Button(frm, text="Pie-Chart", command=pie_Injuries, width=10, fg=fg_button).place(x=260, y=210)
Button(frm, text="Boxplot", command=box_Injuries, width=10, fg=fg_button).place(x=380, y=210)
Label(frm, text="------------------------------------------------------------------------------------------------------"
                "-----------------------------------------------------------------").place(x=10, y=245)

Label(frm, text="Deaths in all Countries :- ", font=("Arial", 15), fg=title_color).place(x=10, y=10+265)
Label(frm, text="Mean = "+str(round(statistics.mean(died), 3))).place(x=20, y=50+265)
Label(frm, text="Median = "+str(statistics.median(died))).place(x=250, y=50+265)
Label(frm, text="Mode = "+str(statistics.mode(died))).place(x=480, y=50+265)
Label(frm, text="Rang = "+str(rang(died))).place(x=710, y=50+265)
Label(frm, text="IQR = "+str(IQR(died))).place(x=20, y=340)
Label(frm, text="Variance = "+str(round(statistics.variance(died), 3))).place(x=250, y=340)
Label(frm, text="Standard Deviation = "+str(round(math.sqrt(statistics.variance(died)), 3))).place(x=480, y=340)
Button(frm, text="Plot-graph", command=plot_deaths, width=10, fg=fg_button).place(x=20, y=375)
Button(frm, text="Bar-Graph", command=bar_deaths, width=10, fg=fg_button).place(x=140, y=375)
Button(frm, text="Pie-Chart", command=pie_deaths, width=10, fg=fg_button).place(x=260, y=375)
Button(frm, text="Boxplot", command=box_deaths, width=10, fg=fg_button).place(x=380, y=375)
Label(frm, text="------------------------------------------------------------------------------------------------------"
                "-----------------------------------------------------------------").place(x=10, y=410)

Label(frm, text="Recovered in all Countries :- ", font=("Arial", 15), fg=title_color).place(x=10, y=440)
Label(frm, text="Mean = "+str(round(statistics.mean(helth), 3))).place(x=20, y=480)
Label(frm, text="Median = "+str(statistics.median(helth))).place(x=250, y=480)
Label(frm, text="Mode = "+str(statistics.mode(helth))).place(x=480, y=480)
Label(frm, text="Rang = "+str(rang(helth))).place(x=710, y=480)
Label(frm, text="IQR = "+str(IQR(helth))).place(x=20, y=505)
Label(frm, text="Variance = "+str(round(statistics.variance(helth), 3))).place(x=250, y=505)
Label(frm, text="Standard Deviation = "+str(round(math.sqrt(statistics.variance(helth)), 3))).place(x=480, y=505)
Button(frm, text="Plot-graph", command=plot_Recovered, width=10, fg=fg_button).place(x=20, y=540)
Button(frm, text="Bar-Graph", command=bar_Recovered, width=10, fg=fg_button).place(x=140, y=540)
Button(frm, text="Pie-Chart", command=pie_Recovered, width=10, fg=fg_button).place(x=260, y=540)
Button(frm, text="Boxplot", command=box_Recovered, width=10, fg=fg_button).place(x=380, y=540)
Label(frm, text="------------------------------------------------------------------------------------------------------"
                "-----------------------------------------------------------------").place(x=10, y=575)



Label(frm, text="Relations :- ", font=("Arial", 15), fg=title_color).place(x=10, y=605)

small_tit="#003366"
Label(frm, text="Injuries & Deaths :- ", font=("Arial", 12), fg=small_tit).place(x=30, y=640)
r = correlation(sick, died)
Label(frm, text="r = "+str(r)+correlation_rate(r)).place(x=200, y=642)
Label(frm, text="Y = "+str(b0(sick, died, r))+" + "+str(b1(sick, died, r))+" X").place(x=450, y=642)
Button(frm, text="Graph", command=relation1, fg=fg_button, width=10).place(x=620, y=640)

Label(frm, text="Injuries & Recovered :- ", font=("Arial", 12), fg=small_tit).place(x=30, y=675)
r = correlation(sick, helth)
Label(frm, text="r = "+str(r)+correlation_rate(r)).place(x=200, y=677)
Label(frm, text="Y = "+str(b0(sick, helth, r))+" + "+str(b1(sick, helth, r))+" X").place(x=450, y=677)
Button(frm, text="Graph", command=relation2, fg=fg_button, width=10).place(x=620, y=675)

Label(frm, text="Recovered & Deaths :- ", font=("Arial", 12), fg=small_tit).place(x=30, y=710)
r = correlation(helth, died)
Label(frm, text="r = "+str(r)+correlation_rate(r)).place(x=200, y=712)
Label(frm, text="Y = "+str(b0(helth, died, r))+" + "+str(b1(helth, died, r))+" X").place(x=450, y=712)
Button(frm, text="Graph", command=relation3, fg=fg_button, width=10).place(x=620, y=710)


font_siz_1 = 15
font_siz_2 = 10
Label(frm, text='Sample Data', font=("Arial", 18), fg="#660000").place(x=1100, y=140)

Label(frm, text='Country', font=("Arial", font_siz_1), fg="#990000").place(x=950, y=175)
Label(frm, text='Injuries', font=("Arial", font_siz_1), fg="#990000").place(x=1080, y=175)
Label(frm, text='Deaths', font=("Arial", font_siz_1), fg="#990000").place(x=1190, y=175)
Label(frm, text='Recovered', font=("Arial", font_siz_1), fg="#990000").place(x=1290, y=175)
for i in range(len(country)):
    Label(frm, text=country[i], font=("Arial", 13), fg="#990000").place(x=950, y=205+(i*25))
    Label(frm, text=str(sick[i]), font=("Arial", font_siz_2)).place(x=1080, y=205+(i*25))
    Label(frm, text=str(died[i]), font=("Arial", font_siz_2)).place(x=1190, y=205+(i*25))
    Label(frm, text=str(helth[i]), font=("Arial", font_siz_2)).place(x=1290, y=205+(i*25))


Button(frm, text="Exit", command=frm.destroy, font=("Arial", 13), width=8, height=1, fg="#b30000").place(x=x_dimensional-120, y=y_dimensional-65)
frm.mainloop()