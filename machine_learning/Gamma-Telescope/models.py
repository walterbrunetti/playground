# -*- coding: utf-8 -*-
"""MachineLearningIntroductionCourse.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Zlp
"""

import pandas
import numpy
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler
import seaborn as sns

column_names = ["fLength", "fWidth", "fSize", "fConc", "fConc1", "fAsym", "fM3Long", "fM3Trans", "fAlpha", "fDist", "class"]
df = pandas.read_csv("magic04.data", names=column_names)
df.head()

df["class"] = (df["class"] == "g").astype(int)  # convert "g" to 1 and "h" to 0
df.head()

"""**Next step we do is exploratory data analysis(EDA). EDA is necessary for any problem as it helps us visualise the data and infer some conclusions initially just by looking at the data and not performing any algorithms.**"""

# Histogram: divide the entire range of values into a series of intervals—and then count how many values fall into each interval. 

for label in column_names[:-1]:
  #print(df[df["class"] == 1][label])  # select `label` from rows_in_csv where class == 1
  #density=True: the first element of the return tuple will be the counts normalized to form a probability density
  plt.hist(df[df["class"] == 1][label], color="blue", label="gamma", alpha=0.7, density=True)
  plt.hist(df[df["class"] == 0][label], color="red", label="hadron", alpha=0.7, density=True)
  plt.title(label)
  plt.ylabel("Probability")
  plt.xlabel(label)
  plt.legend()
  plt.show()

plt.close();
sns.set_style("whitegrid");
sns.pairplot(df, hue="class", height=3);
plt.show()

plt.close();
sns.set_style("whitegrid");
sns.FacetGrid(df, hue="class", size=10).map(plt.scatter, "fDist", "fWidth").add_legend();
plt.show()

"""#create training, validation and testing datasets

len(df) = 19020

0.6 * len(df) = 11412  (60% of the rows)

0.8 * len(df) = 15216  (80% of the rows)

**Numpy**

1-D array = [11412, 15216] = [:11412] [11412:15216] [15216:]

numpy.split(arr, [1-D array])

"""

# df.sample(frac=1)  # get 100% of the rows in a rondom order
train, valid, test = numpy.split(df.sample(frac=1), [int(0.6*len(df)), int(0.8*len(df))])

"""After the EDA and before training our model on the dataset, the one last thing left to do is normalisation. Normalisation is basically bringing all the values of different features on a same scale. As different features has different scale, normalising helps us and the model to optimise it’s parameters more efficiently. We normalise all our input from scale: 0 to 1. """

# in the table above, we got numbers like 45.9877 and 0.1245
# so we want to scale these so that it's relative to the mean and the standard deviation of that specific column

def scale_dataset(dataframe, oversample=False):
  X = dataframe[dataframe.columns[:-1]].values  # we are assuming the last column is the output - this is a matrix
  y = dataframe[dataframe.columns[-1]].values   # last column values - this is a vector

  scaler = StandardScaler()

  #print(X)
  X = scaler.fit_transform(X)   # TODO: transform to standard deviation ?
  #print("----------------")
  #print(X)

  if oversample:
    # give we got around of 7410 gamma and 4002 hadron, we want to make these to be more balanced
    ros = RandomOverSampler()
    X, y = ros.fit_resample(X, y)   # duplicate examples from the minority class


  # stack 2 arrays together side by side, X and y
  #data = numpy.hstack((X, y))   # now X is a 2-D array, while y is a vector, so numpy will complain when joining them, so reshape it..
  reshape_y = numpy.reshape(y, (-1, 1))   # new dimensions of the array
  data = numpy.hstack((X, reshape_y))

  #print(y)   #[1 1 1 ... 1 1 1]
  #print(reshape_y)   #[[1][1][1]...[1][1][1]]


  return data, X, y

train, X_train, y_train = scale_dataset(train, oversample=True)
valid, X_valid, y_valid = scale_dataset(valid, oversample=False)   # I don't want to oversample this, I want it as is for validation
test, X_test, y_test = scale_dataset(test, oversample=False)   # same

"""#KNN"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

knn_model = KNeighborsClassifier(n_neighbors=1)
knn_model.fit(X_train, y_train)

y_pred = knn_model.predict(X_test)

print(classification_report(y_test, y_pred))

"""#Naive Bayes"""

from sklearn.naive_bayes import GaussianNB

nb_model = GaussianNB()
nb_model = nb_model.fit(X_train, y_train)

y_pred = nb_model.predict(X_test)
print(classification_report(y_test, y_pred))

"""#Logistic Regression"""

from sklearn.linear_model import LogisticRegression
lg_model = LogisticRegression()
lg_model = lg_model.fit(X_train, y_train)

y_pred = lg_model.predict(X_test)
print(classification_report(y_test, y_pred))

"""#Support Vector Machines SVM"""

from sklearn.svm import SVC 
svm_model = SVC()
svm_model = svm_model.fit(X_train, y_train)
y_pred = svm_model.predict(X_test)
print(classification_report(y_test, y_pred))

"""# Neural Net"""

import tensorflow as tf

nn_model = tf.keras.Sequential([
    # layers
    tf.keras.layers.Dense(32, activation="relu", input_shape=(10,)),
    tf.keras.layers.Dense(32, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid"),  # output layer - using Sgmoid we are projecting our predictions to be 0 or 1                                
])

learning_rate = 0.001
nn_model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate), loss="binary_crossentropy", metrics=["accuracy"])

history = nn_model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2)

"""Training is playing with different parameter here, number of nodes, learning_rate, epochs, batch_size, etc...in order to get the pest accuarcy"""

def train_model(X_train, y_train, num_nodes, dropout_prob, learning_rate, batch_size, epochs):
    nn_model = tf.keras.Sequential([
        tf.keras.layers.Dense(num_nodes, activation="relu", input_shape=(10,)),
        tf.keras.layers.Dropout(dropout_prob),  # turning off a node during training
        tf.keras.layers.Dense(num_nodes, activation="relu"),
        tf.keras.layers.Dropout(dropout_prob),  # turning off a node during training
        tf.keras.layers.Dense(1, activation="sigmoid"),  # output layer - using Sgmoid we are projecting our predictions to be 0 or 1                                
    ])
    nn_model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate), loss="binary_crossentropy", metrics=["accuracy"])
    history = nn_model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, validation_split=0.2, verbose=0)   # TODO: use validation data instead of spliting the training data (it's a different parameter)

    return nn_model, history

def plot_history(history):
    fig, (axis1, axis2) = plt.subplots(1, 2, figsize=(10,4))
    
    axis1.plot(history.history["loss"], label="loss")
    axis1.plot(history.history["val_loss"], label="val_loss")
    axis1.set_xlabel("Epoch")
    axis1.set_ylabel("Binary crossentropy")
    axis1.grid(True)

    axis2.plot(history.history["accuracy"], label="accuracy")
    axis2.plot(history.history["val_accuracy"], label="val_accuracy")
    axis2.set_xlabel("Epoch")
    axis2.set_ylabel("Accuracy")
    axis2.grid(True)

    plt.show()

least_val_loss = float("inf")
least_loss_model = None
epochs = 100
for nodes in [16, 32, 64]:
  for dropout_prob in [0, 0.2]:
    for batch_size in [32, 64, 128]:
      for learning_rate in [0.01, 0.005, 0.001]:

        print(f"nodes: {nodes} - dropout: {dropout_prob} - LR: {learning_rate} - batch size: {batch_size}")
        model, hostory = train_model(X_train, y_train, nodes, dropout_prob, learning_rate, batch_size, epochs)

        plot_history(history)

        val_loss = model.evaluate(X_valid, y_valid)

        if val_loss[0] < least_val_loss:
          least_val_loss = val_loss[0]
          least_loss_model = model

# now we got our model, lets test and predict

y_pred = least_loss_model.predict(X_test)

# give output is using a Sigmoud function, some values are closer 1 an other to 0. So let's convert them into 1s and 0s
print(y_pred)
y_pred = (y_pred > 0.5).astype(int).reshape(-1, )   # and reshape to one dimension list
print(y_pred)

print(classification_report(y_test, y_pred))
