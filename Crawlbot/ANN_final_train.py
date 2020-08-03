
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Model,Sequential
from keras.layers import Activation, Dense
from keras.optimizers import Adam
from keras.preprocessing.text import Tokenizer


result2=pd.read_csv('fin_processed.csv')

x = result2.Contents
Y=result2.iloc[:, 2].values 
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(x).toarray()


X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.15)

#########################ANN#####################################################################
classifier = Sequential()
classifier.add(Dense(units = 1500, kernel_initializer = 'uniform', activation = 'relu',input_dim=1500))
classifier.add(Dense(units = 1000, kernel_initializer = 'uniform', activation = 'relu'))
classifier.add(Dense(units = 500, kernel_initializer = 'uniform', activation = 'relu'))
classifier.add(Dense(units = 200, kernel_initializer = 'uniform', activation = 'relu'))
classifier.add(Dense(units = 75, kernel_initializer = 'uniform', activation = 'relu'))
classifier.add(Dense(units = 50, kernel_initializer = 'uniform', activation = 'relu'))
classifier.add(Dense(units = 30, kernel_initializer = 'uniform', activation = 'relu'))
classifier.add(Dense(units = 20, kernel_initializer = 'uniform', activation = 'relu'))
classifier.add(Dense(units = 10, kernel_initializer = 'uniform', activation = 'relu'))
classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))
classifier.compile(optimizer = 'Adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
Ann_history=classifier.fit(X_train,Y_train, batch_size =15, epochs = 8,
                            validation_split=0.2)
classifier.save('Processed_ANN_weights.hdf5')

###################################TESTING########################################################

y_pred_ANN = classifier.predict(X_test)

final_pred=np.array([])
for i in y_pred_ANN:
    if(i<0.5):
        final_pred=np.append(final_pred,0)
    else:
        final_pred=np.append(final_pred,1)
from sklearn.metrics import confusion_matrix
cm_ANN = confusion_matrix(Y_test, final_pred)
from sklearn.metrics import accuracy_score
acc_ANN=accuracy_score(Y_test, final_pred)
