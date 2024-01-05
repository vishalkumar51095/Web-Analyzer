l=["Mumbai","Delhi","Patna"]
d={1:"Mumbai",2:"Pure",3:"Patna"}
l2=[]
for word in l:
    if word in d.values():
        l2.append(word)
for key,value in d.items():
   for word in l2:
       if(value==word):
           print(key,word)