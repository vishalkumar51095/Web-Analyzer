def trainingset2():
    s1=t.training2()
    #return m 
    s2=getset(data)
    m=s1.intersection(s2)
    l=list(m)
    text=dict1(data)
    l2=[]
    l3=[]
    for word in l:
        l2.append(word)
        l3.append(text[word])
    res={l2[i]:l3[i] for i in range(len(l2))}
    return res
def interplot2(data):
    words=trainingset2()
    text=nltk.FreqDist(words)
   # print(text.values())
   # print(text.keys())
    n=len(text)
    pltt=text.plot(n,cumulative=False)
    return pltt
def interfreGraph2(data):
    fig=plt.figure()
    interplot2(data)
    plt.show()
    fig.savefig("static/images/intersetplot.png")
    return fig