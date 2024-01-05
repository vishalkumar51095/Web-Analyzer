import pandas as pd
account={
    1:10001,
    2:1003,
    3:1004
}
name={
    1:"shashwat",
    2:"aryan,",
    3:"siresh"
}
balance={
1:100000,
2:20000,
3:200
}
data=[account,name,balance]
index=["acount","name","balance"]

df=pd.DataFrame(data,index)
# print(df)

df.to_excel("C:\\Users\\Champak Roy\\Desktop\\champak baba\\hahaha.xlsx")
a=pd.read_excel("C:\\Users\\Champak Roy\\Desktop\\champak baba\\hahaha.xlsx")
print(a)

x=df[[1]]
print(x)

while True:
    if


