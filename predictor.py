import pandas as pd
from scipy import stats


def getSeries(seriesname, excelpath):
    #define function for geting excel data in dataframe and series name is column name which user want to get and excelpath is localtion of excel file and return dataframe in a list format
    df = pd.read_excel(excelpath)
    return list(df[seriesname])

def getX(n):
    # define function for create a list count for X axis
    l = []
    for i in range(1,n+1,1):
        l.append(i)
    return l

def linearRegression(x,y):
    slope, intercept, r, p, std_err = stats.linregress(x,y)
    return slope, intercept

class LF:
    def __init__(self,slope,intercept):
        self.slope=slope
        self.intercept=intercept
    def linefunc(self,x):

        return self.slope * x + self.intercept






seriesname = "min"
excelpath = "h:\\predictor\\weather.xlsx"
y = getSeries(seriesname,excelpath)
#print(y)
n = len(y)
x = getX(n)
#print(x)


slope, intercept = linearRegression(x,y)
newx = [14,15,16]
lf=LF(slope,intercept)
model = list(map(lf.linefunc,newx))


print(model)
