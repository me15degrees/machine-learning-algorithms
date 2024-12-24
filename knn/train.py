import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import csv
import random
from knn import KNN


def dividir_csv(caminho_arquivo):
    dados = []

    with open(caminho_arquivo, 'r') as arquivo:
        leitor = csv.reader(arquivo)

        next(leitor, None) 

        for linha in leitor: # exclui o ID
            dados.append([float(linha[1]), float(linha[2]), float(linha[3]), float(linha[4]), linha[5]])

    random.shuffle(dados) # randomiza para criar datasets diferentes

    split_index = int(len(dados) * 0.6)
    
    dados_treinamento = dados[:split_index]
    dados_teste = dados[split_index:]

    x_train = [dado[:4] for dado in dados_treinamento]
    y_train = [dado[4] for dado in dados_treinamento]
    x_test = [dado[:4] for dado in dados_teste]
    y_test = [dado[4] for dado in dados_teste]

    return x_train, x_test, y_train, y_test

caminho_arquivo = 'KNN/Iris.csv'

x_train, x_test, y_train, y_test = dividir_csv(caminho_arquivo)

rotulos_unicos = list(set(y_train))
label_to_color = {rotulo: index for index, rotulo in enumerate(rotulos_unicos)}

y_train_numericos = [label_to_color[rotulo] for rotulo in y_train]
y_test_numericos = [label_to_color[rotulo] for rotulo in y_test]

classifier = KNN(k=4) # crio o objeto que usa a K-NN
classifier.fit(x_train, y_train)

predictions = classifier.predict(x_test) # uso o método de classe predict

accuracy = sum([pred == true for pred, true in zip(predictions, y_test)]) / len(y_test) # calcula acurácia

print("Acurácia:", accuracy)

# salvar uma figura com o gráfico plotado

color_map = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(
    [x[0] for x in x_train], 
    [x[1] for x in x_train], 
    [x[2] for x in x_train], 
    c=y_train_numericos,  
    cmap=color_map, 
    edgecolor='k', 
    s=20
)

plt.savefig('KNN/knn_3d.png')
plt.close()
