import pandas as pd

def readfromexcel():
    df=pd.read_excel("h:\\sbi\\sbi.xlsx",index_col=0)
    return df
def getBalance(accno,df):
    x = df[['balance']]

    return x.loc[accno][0]


df=readfromexcel()
print(df)
x=getBalance(2,df)
print("balance",x)