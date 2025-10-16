import pandas as pd




df = pd.read_csv(r"C:\Users\VAIBHAVI\Downloads\College - College.csv", encoding="utf-8")
#print(df.head())
#print(df)

data={
    "Name":['Vaibhavi','Savani','Tanisha'],
    "Age":[20,19,19],
    "City":['Napur','Nagpur','Pune']
}

df=pd.DataFrame(data)
#print(df)

#df.to_csv('output1.csv',index=False)
#df.to_excel('output1.xlsx',index=False)

"""print("Display first 10 rows")
print(df.head())

print("Display last 10 rows")
print(df.tail())"""

#print(df.info())
#print(df.describe())
print(f"shape{df.shape}")
print(f"columns{df.columns}")