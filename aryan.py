import pandas as pd
rupees={
    "Deepak":5000,
    "Champak":100000
    }
data=[rupees]
index=["rupees"]
df=pd.DataFrame(data,index)
print(df)
df.to_excel("C:\\Users\\Champak Roy\\Desktop\\champak baba\\ct.xlsx")
a=pd.read_excel("C:\\Users\\Champak Roy\\Desktop\\champak baba\\ct.xlsx")
print(a)

