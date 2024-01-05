# Import pandas package
import pandas as pd

# Define a dictionary containing employee data
data = {'AccNo':[1,2],
		'Name':['Pappu','Pippi'],
		'Balance':[420,840]
		}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data,index=data["Name"])

# select two columns
x=df[['Balance', 'AccNo']]
print("x",x)
#Select AccNo=2
y=x.loc["Pappu"]
print("y",y)
balance=y[0]
print('balance',balance)
y[0]=9000
print(y)
print(df[["Balance"]].loc[1])
newdata = {'AccNo':[1],

		'Balance':[900]
		}

newdata=pd.DataFrame(newdata,index=newdata["AccNo"])
print(newdata)
df.update(newdata)
print("Updated data",df)

