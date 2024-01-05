import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

x = [1,2,3,4]
y = [1,4,9,14]
print(numpy.linspace(1,101,11))
model = numpy.poly1d(numpy.polyfit(x, y, 2))
print(model)
print(numpy.polyfit(x, y, 1))
plotx =x#[1,2,3,4,5,6,7]# numpy.linspace(1, 22, 100)
correlation=r2_score(y, model(x))
print("Correlation",correlation)
plt.scatter(x,y,color="yellow")
plt.plot(x,y,"b-",label="Original")
plt.plot(plotx, model(plotx),"r-",label="Predicted")
plt.ylabel('Y')
plt.xlabel('X')
plt.legend()
plt.show()
xvalue=4
predict=model(xvalue)
print(predict)