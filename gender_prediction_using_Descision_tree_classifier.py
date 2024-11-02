from sklearn.tree import DecisionTreeClassifier
#[height,weight,shoe size] of 11 people as the number of people increases the prediction becomes more and more accurate
x=[[181,80,44],[177,70,43],[160,60,38],[154,54,37],[166,65,40],[190,90,47],[175,64,39],[177,70,40],[159,55,37],
  [171,75,42],[181,85,43]]
#corresponding gender of each of the metric lists
y=['male','female','female','female','male','male','male','female','male','female','male']
classifier=DecisionTreeClassifier()
classifier=classifier.fit(x,y)
prediction=classifier.predict([[190,70,43]])
print(prediction)
