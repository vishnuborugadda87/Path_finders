from flask import Flask,request,render_template
import pandas as pd
import numpy
import csv
import math
app=Flask(__name__)
@app.route('/')
def hello_world():
    C=0
    if(True):
        cast=1
        gender=1
        rank=13336
        if(cast==1):
            if(gender==1):
                d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
                f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
                f.truncate(0)
                l=["INST CODE","INSTITUTE NAME","PLACE","DISTRICT","CO-ED OR NOT","TYPE","YEAR OF ESTABLISHMENT","BRANCH","BRANCH NAME","BOYS CUT-OFF","GIRLS CUT-OFF","TUTION FEE","AFFILIATED","LINK"]
                for i in range(0,951):
                    a=math.floor(d.iloc[i]["OC Boys"])
                    if(rank<a):
                        C=C+1
                        l=d.iloc[i]
                        w=csv.writer(f)
                        w.writerow(l)
                f.close()
            if(gender==2):
                d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.CSV")
                f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
                f.truncate(0)
                l=["INST CODE","INSTITUTE NAME","PLACE","DISTRICT","CO-ED OR NOT","TYPE","YEAR OF ESTABLISHMENT","BRANCH","BRANCH NAME","BOYS CUT-OFF","GIRLS CUT-OFF","TUTION FEE","AFFILIATED","LINK"]
                for i in range(0,951):
                    a=math.floor(d.iloc[i]["OC Girls"])
                    if(rank<a):
                        C=C+1
                        #l=d.iloc[i]
                        w=csv.writer(f)
                        w.writerow(d.iloc[i])
                f.close()
        if(cast==2):
            if(gender==1):
                d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
                f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
                f.truncate(0)
                l=["INST CODE","INSTITUTE NAME","PLACE","DISTRICT","CO-ED OR NOT","TYPE","YEAR OF ESTABLISHMENT","BRANCH","BRANCH NAME","BOYS CUT-OFF","GIRLS CUT-OFF","TUTION FEE","AFFILIATED","LINK"]
                for i in range(0,951):
                    a=math.floor(d.iloc[i]["BC_A Boys"])
                    if(rank<a):
                        C=C+1
                        l=d.iloc[i]
                        w=csv.writer(f)
                        w.writerow(l)
                f.close()
            if(gender==2):
                d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
                f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
                f.truncate(0)
                l=["INST CODE","INSTITUTE NAME","PLACE","DISTRICT","CO-ED OR NOT","TYPE","YEAR OF ESTABLISHMENT","BRANCH","BRANCH NAME","BOYS CUT-OFF","GIRLS CUT-OFF","TUTION FEE","AFFILIATED","LINK"]
                for i in range(0,951):
                    a=math.floor(d.iloc[i]["BC_A Girls"])
                    if(rank<a):
                        C=C+1
                        #l=d.iloc[i]
                        w=csv.writer(f)
                        w.writerow(d.iloc[i])
                f.close()
        if(cast==3):
            if(gender==1):
                d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
                f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
                f.truncate(0)
                l=["INST CODE","INSTITUTE NAME","PLACE","DISTRICT","CO-ED OR NOT","TYPE","YEAR OF ESTABLISHMENT","BRANCH","BRANCH NAME","BOYS CUT-OFF","GIRLS CUT-OFF","TUTION FEE","AFFILIATED","LINK"]
                for i in range(0,951):
                    a=math.floor(d.iloc[i]["BC_B Boys"])
                    if(rank<a):
                        C=C+1
                        l=d.iloc[i]
                        w=csv.writer(f)
                        w.writerow(l)
                f.close()
            if(gender==2):
                d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
                f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
                f.truncate(0)
                l=["INST CODE","INSTITUTE NAME","PLACE","DISTRICT","CO-ED OR NOT","TYPE","YEAR OF ESTABLISHMENT","BRANCH","BRANCH NAME","BOYS CUT-OFF","GIRLS CUT-OFF","TUTION FEE","AFFILIATED","LINK"]
                for i in range(0,951):
                    a=math.floor(d.iloc[i]["BC_B Girls"])
                    if(rank<a):
                        C=C+1
                        #l=d.iloc[i]
                        w=csv.writer(f)
                        w.writerow(d.iloc[i])
                f.close()
        if(cast==4):
            if(gender==1):
                d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
                f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
                f.truncate(0)
                l=["INST CODE","INSTITUTE NAME","PLACE","DISTRICT","CO-ED OR NOT","TYPE","YEAR OF ESTABLISHMENT","BRANCH","BRANCH NAME","BOYS CUT-OFF","GIRLS CUT-OFF","TUTION FEE","AFFILIATED","LINK"]
                for i in range(0,951):
                    a=math.floor(d.iloc[i]["BC_C Boys"])
                    if(rank<a):
                        C=C+1
                        l=d.iloc[i]
                        w=csv.writer(f)
                        w.writerow(l)
                f.close()
            if(gender==2):
                d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
                f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
                f.truncate(0)
                l=["INST CODE","INSTITUTE NAME","PLACE","DISTRICT","CO-ED OR NOT","TYPE","YEAR OF ESTABLISHMENT","BRANCH","BRANCH NAME","BOYS CUT-OFF","GIRLS CUT-OFF","TUTION FEE","AFFILIATED","LINK"]
                for i in range(0,951):
                    a=math.floor(d.iloc[i]["BC_C Girls"])
                    if(rank<a):
                        C=C+1
                        #l=d.iloc[i]
                        w=csv.writer(f)
                        w.writerow(d.iloc[i])
                f.close()
        if(cast==5):
            if(gender==1):
                d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
                f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
                f.truncate(0)
                l=["INST CODE","INSTITUTE NAME","PLACE","DISTRICT","CO-ED OR NOT","TYPE","YEAR OF ESTABLISHMENT","BRANCH","BRANCH NAME","BOYS CUT-OFF","GIRLS CUT-OFF","TUTION FEE","AFFILIATED","LINK"]
                for i in range(0,951):
                    a=math.floor(d.iloc[i]["BC_D Boys"])
                    if(rank<a):
                        C=C+1
                        l=d.iloc[i]
                        w=csv.writer(f)
                        w.writerow(l)
                f.close()
            if(gender==2):
                d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
                f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
                f.truncate(0)
                l=["INST CODE","INSTITUTE NAME","PLACE","DISTRICT","CO-ED OR NOT","TYPE","YEAR OF ESTABLISHMENT","BRANCH","BRANCH NAME","BOYS CUT-OFF","GIRLS CUT-OFF","TUTION FEE","AFFILIATED","LINK"]
                for i in range(0,951):
                    a=math.floor(d.iloc[i]["BC_D Girls"])
                    if(rank<a):
                        C=C+1
                        #l=d.iloc[i]
                        w=csv.writer(f)
                        w.writerow(d.iloc[i])
                f.close()
        if(cast==6):
            if(gender==1):
                d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
                f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
                f.truncate(0)
                l=["INST CODE","INSTITUTE NAME","PLACE","DISTRICT","CO-ED OR NOT","TYPE","YEAR OF ESTABLISHMENT","BRANCH","BRANCH NAME","BOYS CUT-OFF","GIRLS CUT-OFF","TUTION FEE","AFFILIATED","LINK"]
                for i in range(0,951):
                    a=math.floor(d.iloc[i]["BC_E Boys"])
                    if(rank<a):
                        C=C+1
                        l=d.iloc[i]
                        w=csv.writer(f)
                        w.writerow(l)
                f.close()
            if(gender==2):
                d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
                f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
                f.truncate(0)
                l=["INST CODE","INSTITUTE NAME","PLACE","DISTRICT","CO-ED OR NOT","TYPE","YEAR OF ESTABLISHMENT","BRANCH","BRANCH NAME","BOYS CUT-OFF","GIRLS CUT-OFF","TUTION FEE","AFFILIATED","LINK"]
                for i in range(0,951):
                    a=math.floor(d.iloc[i]["BC_E Girls"])
                    if(rank<a):
                        C=C+1
                        #l=d.iloc[i]
                        w=csv.writer(f)
                        w.writerow(d.iloc[i])
                f.close()
        if(cast==7):
            if(gender==1):
                d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
                f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
                f.truncate(0)
                l=["INST CODE","INSTITUTE NAME","PLACE","DISTRICT","CO-ED OR NOT","TYPE","YEAR OF ESTABLISHMENT","BRANCH","BRANCH NAME","BOYS CUT-OFF","GIRLS CUT-OFF","TUTION FEE","AFFILIATED","LINK"]
                for i in range(0,951):
                    a=math.floor(d.iloc[i]["SC Boys"])
                    if(rank<a):
                        C=C+1
                        l=d.iloc[i]
                        w=csv.writer(f)
                        w.writerow(l)
                f.close()
            if(gender==2):
                d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
                f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
                f.truncate(0)
                l=["INST CODE","INSTITUTE NAME","PLACE","DISTRICT","CO-ED OR NOT","TYPE","YEAR OF ESTABLISHMENT","BRANCH","BRANCH NAME","BOYS CUT-OFF","GIRLS CUT-OFF","TUTION FEE","AFFILIATED","LINK"]
                for i in range(0,951):
                    a=math.floor(d.iloc[i]["SC Girls"])
                    if(rank<a):
                        C=C+1
                        #l=d.iloc[i]
                        w=csv.writer(f)
                        w.writerow(d.iloc[i])
                f.close()
        if(cast==8):
            if(gender==1):
                d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
                f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
                f.truncate(0)
                l=["INST CODE","INSTITUTE NAME","PLACE","DISTRICT","CO-ED OR NOT","TYPE","YEAR OF ESTABLISHMENT","BRANCH","BRANCH NAME","BOYS CUT-OFF","GIRLS CUT-OFF","TUTION FEE","AFFILIATED","LINK"]
                for i in range(0,951):
                    a=math.floor(d.iloc[i]["ST Boys"])
                    if(rank<a):
                        C=C+1
                        l=d.iloc[i]
                        w=csv.writer(f)
                        w.writerow(l)
                f.close()
            if(gender==2):
                d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
                f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
                f.truncate(0)
                l=["INST CODE","INSTITUTE NAME","PLACE","DISTRICT","CO-ED OR NOT","TYPE","YEAR OF ESTABLISHMENT","BRANCH","BRANCH NAME","BOYS CUT-OFF","GIRLS CUT-OFF","TUTION FEE","AFFILIATED","LINK"]
                for i in range(0,951):
                    a=math.floor(d.iloc[i]["ST Girls"])
                    if(rank<a):
                        C=C+1
                        #l=d.iloc[i]
                        w=csv.writer(f)
                        w.writerow(d.iloc[i])
                f.close()
        if(cast==9):
            if(gender==1):
                d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
                f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
                f.truncate(0)
                l=["INST CODE","INSTITUTE NAME","PLACE","DISTRICT","CO-ED OR NOT","TYPE","YEAR OF ESTABLISHMENT","BRANCH","BRANCH NAME","BOYS CUT-OFF","GIRLS CUT-OFF","TUTION FEE","AFFILIATED","LINK"]
                for i in range(0,951):
                    a=math.floor(d.iloc[i]["EWS Boys"])
                    if(rank<a):
                        C=C+1
                        l=d.iloc[i]
                        w=csv.writer(f)
                        w.writerow(l)
                f.close()
            if(gender==2):
                d=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\OC.csv")
                f=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv","w")
                f.truncate(0)
                l=["INST CODE","INSTITUTE NAME","PLACE","DISTRICT","CO-ED OR NOT","TYPE","YEAR OF ESTABLISHMENT","BRANCH","BRANCH NAME","BOYS CUT-OFF","GIRLS CUT-OFF","TUTION FEE","AFFILIATED","LINK"]
                w=csv.writer(f)
                w.writerow(l)
                for i in range(0,951):
                    a=math.floor(d.iloc[i]["EWS Girls"])
                    if(rank<a):
                        C=C+1
                        #l=d.iloc[i]
                        w=csv.writer(f)
                        w.writerow(d.iloc[i])
                f.close()
    f1=open("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.html","w")
    d1=pd.read_csv("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.csv")
    if(gender==1):
        for i in range(0,c):
            for j in range(0,c-i-1):
                if(d1.iloc[j]["BOYS CUT-OFF"]>d1.iloc[j+1]["BOYS CUT-OFF"]):
                    temp=d1.iloc[j]
                    d1.iloc[j]=d1.iloc[j+1]
                    d1.iloc[j+1]=temp
    if(gender==2):
        for i in range(0,c):
            for j in range(0,c-i-1):
                if(d1.iloc[j]["GIRLS CUT-OFF"]>d1.iloc[j+1]["GIRLS CUT-OFF"]):
                    temp=d1.iloc[j]
                    d1.iloc[j]=d1.iloc[j+1]
                    d1.iloc[j+1]=temp
    

    f1.write("<h1>You are eligible for the following list of colleges</h1>")

    f1.write("<table>\n")
    f1.write("<tr>\n")
    f1.write("<th>INST CODE</th>\n")
    f1.write("<th>INSTITUTE NAME</th>\n")
    f1.write("<th>PLACE</th>\n")
    f1.write("<th>DISTRICT</th>\n")
    f1.write("<th>CO-ED OR NOT</th>\n")
    f1.write("<th>TYPE</th>\n")
    f1.write("<th>YEAR OF ESTABLISHMENT</th>\n")
    f1.write("<th>BRANCH</th>\n")
    f1.write("<th>BRANCH NAME</th>\n")
    f1.write("<th>BOYS CUT-OFF</th>\n")
    f1.write("<th>GIRLS CUT-OFF</th>\n")
    f1.write("<th>TUTION FEE</th>\n")
    f1.write("<th>AFFILIATED</th>\n")
    f1.write("<th>LINKS</th>\n")
    f1.write("</tr>\n")
    for i in range(1,C):
    
        f1.write("<tr>\n")
        for j in d1.iloc[i]:
            s=str(j)
            f1.write("<td>"+s+"</td>\n")
        f1.write("</tr>")
    f1.write("<script>\n")
    f1.write("function filterTable() {\n")
    f1.write(" var branchFilter = document.getElementById(\"branchFilter\").value\n")
    f1.write("var tableRows = document.querySelectorAll(\"tbody tr\");\n\n")
    f1.write(" tableRows.forEach(function(row) {\n")
    f1.write(" var branchCell = row.getElementsByTagName(\"td\")[2].textContent;\n")
    f1.write(" if (branchFilter === \"all\" || branchCell === branchFilter || (branchFilter === \"Other\" && (branchCell === \"Other\" || branchCell === \"Other Non-Common\"))) {\n")
    f1.write(" row.style.display = "";\n")
    f1.write(" } else {\n")
    f1.write(" row.style.display = \"none\";\n")
    f1.write(" }\n")
    f1.write(" });\n")
    f1.write(" }\n")
    f1.write("</script>")

    f1.close()
    return  render_template("C:\\Users\\vishn\\OneDrive\\Desktop\\EAMCET - Copy\\out.html")