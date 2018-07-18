import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv('iris.csv')
setosa = iris[iris['Name'] == "Iris-setosa"]
versicolor = iris[iris['Name'] == "Iris-versicolor"]
virginica = iris[iris['Name'] == "Iris-virginica"]

# setosaのヒストグラムを描写
# plt.figure()
# plt.hist(setosa["SepalLength"])
# plt.xlabel("SepalLength")
# plt.ylabel('Freq')
# plt.show()

# 箱ひげ図
data = [setosa['SepalLength'], versicolor['SepalLength'], virginica['SepalLength']]
plt.figure()
plt.boxplot(data, sym="k.")
plt.xlabel('Name')
plt.ylabel('SepalLength')
ax = plt.gca()
plt.setp(ax, xticklabels=['setosa', 'versicolor', 'virginica'])
plt.show()