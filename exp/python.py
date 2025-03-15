import pandas as pd
import numpy
import csv
import math
'''cast=int(input("Enter your cast 1)for OC Open 2)for BC_A 3)for BC_B 4)FOR BC_C 5)for BC_D 6)for BC_E 7)for SC 8)for ST 9)for EWS : "))
gender=int(input("Enter 1)for male 2)for female :"))
rank=int(input("Enter your rank: "))'''
if(cast==1):
    if(gender==1):
        d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
        f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
        f.truncate(0)
        for i in range(0,951):
            a=math.floor(d.iloc[i]["OC Boys"])
            if(rank<a):
                l=d.iloc[i]
                w=csv.writer(f)
                w.writerow(l)
        f.close()
    if(gender==2):
        d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.CSV")
        f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
        f.truncate(0)
        for i in range(0,951):
            a=math.floor(d.iloc[i]["OC Girls"])
            if(rank<a):
                #l=d.iloc[i]
                w=csv.writer(f)
                w.writerow(d.iloc[i])
        f.close()
if(cast==2):
    if(gender==1):
        d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
        f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
        f.truncate(0)
        for i in range(0,951):
            a=math.floor(d.iloc[i]["BC_A Boys"])
            if(rank<a):
                l=d.iloc[i]
                w=csv.writer(f)
                w.writerow(l)
        f.close()
    if(gender==2):
        d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
        f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
        f.truncate(0)
        for i in range(0,951):
            a=math.floor(d.iloc[i]["BC_A Girls"])
            if(rank<a):
                #l=d.iloc[i]
                w=csv.writer(f)
                w.writerow(d.iloc[i])
        f.close()
if(cast==3):
    if(gender==1):
        d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
        f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
        f.truncate(0)
        for i in range(0,951):
            a=math.floor(d.iloc[i]["BC_B Boys"])
            if(rank<a):
                l=d.iloc[i]
                w=csv.writer(f)
                w.writerow(l)
        f.close()
    if(gender==2):
        d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
        f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
        f.truncate(0)
        for i in range(0,951):
            a=math.floor(d.iloc[i]["BC_B Girls"])
            if(rank<a):
                #l=d.iloc[i]
                w=csv.writer(f)
                w.writerow(d.iloc[i])
        f.close()
if(cast==4):
    if(gender==1):
        d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
        f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
        f.truncate(0)
        for i in range(0,951):
            a=math.floor(d.iloc[i]["BC_C Boys"])
            if(rank<a):
                l=d.iloc[i]
                w=csv.writer(f)
                w.writerow(l)
        f.close()
    if(gender==2):
        d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
        f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
        f.truncate(0)
        for i in range(0,951):
            a=math.floor(d.iloc[i]["BC_C Girls"])
            if(rank<a):
                #l=d.iloc[i]
                w=csv.writer(f)
                w.writerow(d.iloc[i])
        f.close()
if(cast==5):
    if(gender==1):
        d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
        f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
        f.truncate(0)
        for i in range(0,951):
            a=math.floor(d.iloc[i]["BC_D Boys"])
            if(rank<a):
                l=d.iloc[i]
                w=csv.writer(f)
                w.writerow(l)
        f.close()
    if(gender==2):
        d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
        f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
        f.truncate(0)
        for i in range(0,951):
            a=math.floor(d.iloc[i]["BC_D Girls"])
            if(rank<a):
                #l=d.iloc[i]
                w=csv.writer(f)
                w.writerow(d.iloc[i])
        f.close()
if(cast==6):
    if(gender==1):
        d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
        f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
        f.truncate(0)
        for i in range(0,951):
            a=math.floor(d.iloc[i]["BC_E Boys"])
            if(rank<a):
                l=d.iloc[i]
                w=csv.writer(f)
                w.writerow(l)
        f.close()
    if(gender==2):
        d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
        f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
        f.truncate(0)
        for i in range(0,951):
            a=math.floor(d.iloc[i]["BC_E Girls"])
            if(rank<a):
                #l=d.iloc[i]
                w=csv.writer(f)
                w.writerow(d.iloc[i])
        f.close()
if(cast==7):
    if(gender==1):
        d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
        f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
        f.truncate(0)
        for i in range(0,951):
            a=math.floor(d.iloc[i]["SC Boys"])
            if(rank<a):
                l=d.iloc[i]
                w=csv.writer(f)
                w.writerow(l)
        f.close()
    if(gender==2):
        d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
        f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
        f.truncate(0)
        for i in range(0,951):
            a=math.floor(d.iloc[i]["SC Girls"])
            if(rank<a):
                #l=d.iloc[i]
                w=csv.writer(f)
                w.writerow(d.iloc[i])
        f.close()
if(cast==8):
    if(gender==1):
        d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
        f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
        f.truncate(0)
        for i in range(0,951):
            a=math.floor(d.iloc[i]["ST Boys"])
            if(rank<a):
                l=d.iloc[i]
                w=csv.writer(f)
                w.writerow(l)
        f.close()
    if(gender==2):
        d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
        f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
        f.truncate(0)
        for i in range(0,951):
            a=math.floor(d.iloc[i]["ST Girls"])
            if(rank<a):
                #l=d.iloc[i]
                w=csv.writer(f)
                w.writerow(d.iloc[i])
        f.close()
if(cast==9):
    if(gender==1):
        d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
        f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
        f.truncate(0)
        for i in range(0,951):
            a=math.floor(d.iloc[i]["EWS Boys"])
            if(rank<a):
                l=d.iloc[i]
                w=csv.writer(f)
                w.writerow(l)
        f.close()
    if(gender==2):
        d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
        f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
        f.truncate(0)
        for i in range(0,951):
            a=math.floor(d.iloc[i]["EWS Girls"])
            if(rank<a):
                #l=d.iloc[i]
                w=csv.writer(f)
                w.writerow(d.iloc[i])
        f.close()