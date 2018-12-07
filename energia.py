import sklearn
from sklearn import datasets
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.neural_network import MLPClassifier
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

energia_treino = sklearn.datasets.load_files('energia', categories=None, random_state=42)

vectorizer = TfidfVectorizer()
X_train_tfidf_vectorize = vectorizer.fit_transform(energia_treino.data)

clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(70, ), random_state=1, verbose=True)
clf.fit(X_train_tfidf_vectorize, energia_treino.target) 

energia_teste = sklearn.datasets.load_files('energia', categories=None, random_state=42)
docs_test = energia_teste.data

vect_transform = vectorizer.transform(docs_test)
predicted = clf.predict(vect_transform)

confusion_matrix = confusion_matrix(energia_teste.target, predicted)
print(confusion_matrix)

plt.matshow(confusion_matrix)
plt.title("Matriz de confusão")
plt.colorbar()
plt.ylabel("Classificações corretas")
plt.xlabel("Classificações obtidas")
plt.show()

docs_new = [
    'Eu, Gutemberg Rocha, venho respeitosamente, a presença de V. Exa. propor a presente AÇÃO DE INDENIZAÇÃO(Direito à restituição de valor de ICMS pago a maior em contas de luz/energia)1 viso demonstrar que é cobrado valores equivocados nas contas de energia/luz, mesmo com a interpretação pacífica de nossos tribunais a respeito da conduta das concessionárias que repassam valores de ICMS ao consumidor.'
]

X_new_tfidf_vectorize = vectorizer.transform(docs_new)

predicted = clf.predict(X_new_tfidf_vectorize)
energia_treino
for doc, category in zip(docs_new, predicted):
    print('%r => %s' % (doc, energia_treino.target_names[category]))