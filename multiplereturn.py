def minimax(a,b):
    if(a>=b):
        max=a
        min=b
    else:
        max=b
        min=a
    return min,max

x,y=minimax(23,43)
print(x,y)