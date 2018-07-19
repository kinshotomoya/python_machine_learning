import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
# data = [setosa['SepalLength'], versicolor['SepalLength'], virginica['SepalLength']]
# plt.figure()
# plt.boxplot(data, sym="k.")
# plt.xlabel('Name')
# plt.ylabel('SepalLength')
# ax = plt.gca()
# plt.setp(ax, xticklabels=['setosa', 'versicolor', 'virginica'])
# plt.show()

# 散布図
# plt.scatter(setosa['SepalLength'], setosa['SepalWidth'])
# plt.xlabel('SepalLength')
# plt.ylabel('SepalWidth')
# plt.show()

# 相関係数
# corr = np.corrcoef(setosa['SepalLength'], setosa['SepalWidth'])
# print(corr[0, 1])

# 単回帰分析
# from sklearn import linear_model
# LinerRegr = linear_model.LinearRegression()
# X = setosa[['SepalLength']]
# Y = setosa[['SepalWidth']]
# LinerRegr.fit(X, Y)
# plt.scatter(X, Y, color='black')
# px = np.arange(X.min(), X.max(), .01)[:,np.newaxis]
# py = LinerRegr.predict(px)
# plt.plot(px, py, color='blue', linewidth=3)
# plt.xlabel('SepalLength')
# plt.ylabel('SepalWidth')
# plt.show()
# print(LinerRegr.coef_)
# print(LinerRegr.intercept_)
# # 決定係数
# print(LinerRegr.score(X, Y))

# 重回帰分析
# from sklearn import linear_model
# LinerRegr = linear_model.LinearRegression()
# X = setosa[['SepalLength', 'PetalLength', 'PetalWidth']]
# Y = setosa[['SepalWidth']]
# LinerRegr.fit(X,Y)
# # 偏回帰係数 β0,β1,β2,β3 の推定値を表示
# # 順番に表示している
# print(LinerRegr.coef_)
# # 決定係数を表示
# print(LinerRegr.score(X, Y))

# ダミー変数
from sklearn import linear_model
dummies = pd.get_dummies(iris['Name'])
iris = pd.concat([iris, dummies], axis=1)
LinerRegr = linear_model.LinearRegression()
X = iris[['Iris-virginica', 'Iris-versicolor']]
Y = iris[['SepalLength']]
LinerRegr.fit(X, Y)
# print(LinerRegr.coef_)

# ロジスティック回帰モデル
usedata = np.logical_or(iris['Name'] == 'Iris-setosa', iris['Name'] == 'Iris-virginica')
setosa_virginica = iris[usedata]
X = setosa_virginica[['SepalLength', 'SepalWidth']]
Y = setosa_virginica['Iris-setosa']
LogRegr = linear_model.LogisticRegression(C=1.0)
LogRegr.fit(X, Y)
# 偏回帰係数を表示
print(LogRegr.coef_)
print(LogRegr.intercept_)
print(pd.crosstab(Y, LogRegr.predict(X)))