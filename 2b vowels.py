element = input("enter word")
vowels=['a','e','i','o','u']
list1=[]
for x in element:
    
  if(x in vowels and x not in list1):
    list1.append(x)
  print("vowels present", list1)






from sklearn.tree Import DecisionTreeClassifier

JupyterLab

Python 3

A

X_train, X_test, y_train, y_test train_test_split(X, y, random_state = 50, test_size = 0.25)

classifier DecisionTreeClassifier() classifier.fit(X_train, y_train)

y_pred classifier.predict(X_test)

from sklearn.metrics import accuracy_score

print('Accuracy on train data using Gini:', accuracy_score (y_true y_train, y_pred classifier.predict(X_train)))

print('Accuracy on test data using Gini:', accuracy_score (y_truey_test, y_pred=y_pred))

classifier_entropy. fit(X_train, y_train)

classifier_entropy DecisionTreeClassifier(criterion='entropy')

?

y_pred_entropy classifier_entropy.predict(X_test)

print('Accuracy on train data using entropy', accuracy_score (y_true=y_train, y_pred classifier_entropy.predict(X_train)))

print('Accuracy on test data using entropy', accuracy_score(y_true y_test, y_pred=y_pred_entropy)) classifier_entropyl DecisionTreeClassifier (criterion 'entropy', min_samples_split=50)

classifier_entropy1.fit(X_train, y_train)

y_pred_entropy1 classifier_entropy1.predict(X_test)

print('Accuracy on train data using entropy', accuracy_score (y_true y_train, y_pred classifier_entropy1.predict(X_train)))

print('Accuracy on test data using entropy', accuracy_score (y_true y_test, y_pred y_pred_entropy1))

from sklearn.tree import export_graphviz

from six import String10

from IPython.display import Image

import pydotplus

dot_data String10()

export_graphviz(classifier, out_file dot_data, filled True, rounded =

True, special_characters True, feature_names data.feature names, class_names data.target_names)

graph pydotplus.graph_from_dot_data(dot_data.getvalue())

Image(graph.create_png())