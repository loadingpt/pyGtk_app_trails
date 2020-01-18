
class Recommend:
    def __init__(self, dic_trilhos, lista_compara):
        inter_lista = []
        reun_lista = []
        self.jaccard = {}

        #percorre as keys do dicionario
        for i in dic_trilhos:
            inter_lista = []
            reun_lista = []
            #print(i)
            #percorre o conteudo da key (lista de listas)
            for j in dic_trilhos[i]:
                contador = 0
                #print(j)
                #percorre cada lista individualmente, e compara à lista_compara. a variavel contador serve para auxiliar a percorrer a lista_compara
                for z in j:
                    #print(z)
                    #adiciona à lista inter_lista sempre que tiver valores iguais
                    if z == lista_compara[contador]:
                        if z not in inter_lista:
                            inter_lista += [lista_compara[contador]]

                    #se o valor ja existir no reun_lista, não faz nada, se nao existir, adiciona o valor à lista reun_lista, isto para ambas as listas.
                    if lista_compara[contador] in reun_lista:
                        pass
                    else:
                        reun_lista += [lista_compara[contador]]

                    if z in reun_lista:
                        pass
                    else:
                        reun_lista += [z]

                    contador += 1

            #jacard é um dicionario, em que a key é o nome do trilho, e o valor da key é o calculo resultado
            self.jaccard[i] = len(inter_lista) / len(reun_lista)


        temp_min = 0
        self.recommend = ""

        #percorre o dicionario jaccard, e sempre que encontrar um valor superior, guarda esse valor no self.recommend
        for i in self.jaccard:
            if self.jaccard[i] > temp_min:
                self.recommend = i
                temp_min = self.jaccard[i]

        #print(self.jaccard)

        
    def get_rec(self):
        return self.recommend
                
        


def main():
    dic = {"trilho1":[["portugal", "17-21", "M"],["portugal", "17-21", "M"],["portugal", "17-21", "M"]], "trilho2":[["portugal", "17-21", "M"],["portugal", "17-21", "M"],["portugal", "17-21", "M"]]}
    lista = ["portugal", "17-21", "M"]
    teste = Recommend(dic, lista)
    print(teste.get_rec())
    
    #recomend({trilho1:[[pais, faixa_etaria, genero], [pais, faixa_etaria, genero], ...], trilho2:[[...]...]}, [pais, faixa_etaria, genero])

main()
