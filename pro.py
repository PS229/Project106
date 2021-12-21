import plotly.express as px
import csv
import numpy as np

def getDataSource(dataPart):
    s = []
    t = []
    with open("pro.py") as f:
        df = csv.DictReader(f)
        for row in df:
            s.append(float(row["Days"]))
            t.append(float(row["Percentage"]))
    return{"x":s, "y":t}

def findCorr(dataSource):
    corr = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation of the percentage and no of days present is: ", corr[0,1])

def setup():
    dataPart = "pro.csv"
    dataSource = getDataSource(dataPart)
    findCorr(dataSource)

setup()