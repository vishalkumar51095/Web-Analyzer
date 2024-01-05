import nltk
import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize as st
from nltk.tokenize import word_tokenize as wt
from nltk.corpus import stopwords as sw
import downloader as dd
import analyzer as an

url="http://varanasikshetra.com"

def divsText(data):
    divs=an.GetDivs(data)
    output=""
    for i in divs.values():
     output =output + i.text
    return output
def HeadingsText(data):
    headings=an.GetHeadings(data)
    output=""
    for i in headings.values():
        output=output+i.text
    return output
def ParagraphsText(data):
    paragraphs=an.GetParagraphs(data)
    output=""
    for i in paragraphs.values():
        output=output+i.text
    return output
def AltText(data):
    alt=an.GetImagesAlt(data)
    output=""
    for i in alt.values():
      output=output + "," +  str(i)
    return output 
def CompleteText(data):
    text=divsText(data)+HeadingsText(data)+ParagraphsText(data)+AltText(data)
    return text
def Sentence(data):
    text=CompleteText(data)
    sentences =st(text)
    return sentences
def words(data):
    text=CompleteText(data)
    words=wt(text)
    return words
def wordswithfrequencies(data):
    text=words(data)
    wordswithfrequencies=nltk.FreqDist(text)
    keyvaluepairs=wordswithfrequencies.items()
    return keyvaluepairs
def Gplot(data):
    word=words(data)
    text=nltk.FreqDist(word)
   # print(text.values())
   # print(text.keys())
    n=len(text)
    pllt=text.plot(n,cumulative=False)
    return pllt
def plot(data):
    fig = plt.figure()
    Gplot(data)
    plt.show()
    fig.savefig("static/images/display.png")
    return fig
def stopwords(data):
    stops = sw.words('english')
    return stops
def Removestopword(data):
    text=CompleteText(data)
    stops = sw.words('english')
    tokens=wt(text)
    for token in tokens:
        if token in stops:
            tokens.remove(token)
    return tokens
def frerstopword(data):
#    text=Removestopword(data)
    wf=nltk.FreqDist(data)
    kvp=wf.items()
    return kvp
def Rplot(data):
    words=Removestopword(data)
    text=nltk.FreqDist(words)
  #  print(text.values())
  #  print(text.keys())
    n=len(text)
    pltt=text.plot(n,cumulative=False)
    return pltt
def RSWplot(data):
    fig=plt.figure()
    Rplot(data)
    plt.show()
    fig.savefig("static/images/RSWplot.png")
    return fig
data=dd.downloadUrl(url)
y=Rplot(data)
print(y)
#text=stopwords(data)
#data='''My My name . name is vishal'''
#m=wordswithfrequencies(data)
#print(text)
#Gplot(data)
#data=dd.downloadUrl(url)
#plot(data)
#print("\nAfter removal\n")
#p=Removestopword(data)
#print(p)
#data="apple mango apple"
#plot(data)
#plt.savefig('graph.png')
#plt.show()