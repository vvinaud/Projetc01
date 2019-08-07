import pandas as pd
import numpy as np

base = pd.read_csv('credit_data.csv')
base.loc[base.age < 0, 'age'] = 40.92
               
previsores = base.iloc[:, 1:4].values
classe = base.iloc[:, 4].values

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
imputer = imputer.fit(previsores[:, 1:4])
previsores[:, 1:4] = imputer.transform(previsores[:, 1:4])

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)

from sklearn.model_selection import train_test_split
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.25, random_state=0)

from sklearn.svm import SVC
classificador = SVC(C=18, kernel='rbf',random_state=1,gamma='auto')
classificador.fit(previsores_treinamento, classe_treinamento)
previsoes = classificador.predict(previsores_teste)

from sklearn.metrics import confusion_matrix, accuracy_score
precisao = accuracy_score(classe_teste, previsoes)
matriz = confusion_matrix(classe_teste, previsoes)
 
# Conta o Melhor
#ctgm = 1
#while ctgm <= 100:
# classificador = SVC(C=ctgm, kernel='rbf',random_state=1,gamma='auto')
# classificador.fit(previsores_treinamento, classe_treinamento)
# previsoes = classificador.predict(previsores_teste)
# from sklearn.metrics import confusion_matrix, accuracy_score
# precisao = accuracy_score(classe_teste, previsoes)
# matriz = confusion_matrix(classe_teste, previsoes)
# if precisao> 0.99:
# print(ctgm,precisao)
# ctgm += 1 

import collections
print(collections.Counter(classe_teste))


