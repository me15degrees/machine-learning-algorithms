from collections import Counter


class KNN:
    def __init__(self, k=4):
        self.k = k # quantidade de vizinhos que eu vou considerar

    def distance(self, point_1, point_2): # calcula a distância euclidiana considerando 4 coordenadas
        x, y, z, w = point_1
        x0, y0, z0, w0 = point_2
        return (((x - x0) ** 2) + ((y - y0) ** 2)+((z - z0) ** 2)+((w - w0) ** 2)) ** 0.5  
    
    def fit(self, x, y): # treinamento
        self.features = x # características dos dados de treinamento
        self.rotules = y # rótulos (nome das espécies)
        
    def predict(self, x): # cria um iterável aplicando o a fazendo a predição para cada ponto único
        predictions = [self.predict_single_point(xi) for xi in x]
        return predictions
    
    def predict_single_point(self, x):
        distances = [self.distance(x, features) for features in self.features] # armazena as distâncias em relação aos pontos
        # ordena de forma crescente as distâncias, mas guarda os k primeiros índices 
        k_indices = sorted(range(len(distances)), key=lambda i: distances[i])[:self.k] 
        k_nearest_labels = [self.rotules[i] for i in k_indices] # busca o label equivalente
        
        most_common = Counter(k_nearest_labels).most_common() # o label que mais se repete se torna o label daquele ponto
        # retorna o rótulo do mais comum entre os k mais próximos -> tupla ordenada pela frequência e ordem alfabética
        return most_common[0][0] 
