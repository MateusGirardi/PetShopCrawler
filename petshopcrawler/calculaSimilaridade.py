# coding=utf8
# Importando as bibliotecas
import pandas as pd
import heapq
import json
from cdifflib import CSequenceMatcher # 2X mais rápido
#from difflib import SequenceMatcher

# Extraindo o arquivo json
df = pd.read_json('petzResults.json')
df2 = pd.read_json('cobasiResults.json')

# Removendo linhas duplicadas
df = df.drop_duplicates(subset='id', keep='first')
print(len(df))
df2 = df2.drop_duplicates(subset='id', keep='first')
print(len(df2))

#Similaridade de produtos de duas listas de fornecedores diferentes
def similary_product(lista1, lista2):
    produtos = {"produtos": []}
    for i, j in lista1.iterrows():
        p = []
        f = []
        #Calcula a similaridade
        for c, n in lista2.iterrows():
            sim_name_brand = CSequenceMatcher(None, f"Produto: {lista1['name'][i]} - Marca: {lista1['brand'][i]}", f"Produto: {lista2['name'][c]} - Marca: {lista2['brand'][c]}").ratio()
            cal_sim_price = float(lista1['price'][i]) / float(lista2['price'][c])
            sim_price = 1 if cal_sim_price >= 0.85 and cal_sim_price <= 1.25 else 0
            sim = sim_name_brand + sim_price

            #Adiciona a lista
            p.append([sim, i, c])
        f = heapq.nlargest(1, p)
        d = {
                'nome_petz': lista1['name'][f[0][1]], 'nome_cobasi': lista2['name'][f[0][2]],
                'marca_petz': lista1['brand'][f[0][1]], 'marca_cobasi': lista2['brand'][f[0][2]],
                'preco_petz': lista1['price'][f[0][1]], 'preco_cobasi': lista2['price'][f[0][2]],
                'similaridade': f[0][0]
             }
        produtos['produtos'].append(d)

        print(heapq.nlargest(1, p))
        print(f"Produto Petz: {lista1['name'][f[0][1]]}")
        print(f"Produto Cobasi: {lista2['name'][f[0][2]]}")
        print(f"Marca Petz: {lista1['brand'][f[0][1]]}")
        print(f"Marca Cabasi: {lista2['brand'][f[0][2]]}")
        print(f"Preço Petz: {lista1['price'][f[0][1]]}")
        print(f"Preço Cabasi: {lista2['price'][f[0][2]]}")
        print(f"Similaridade: {f[0][0]}\n")
        if i == 999:
            break
    js = json.dumps(produtos, ensure_ascii=False).encode("utf-8")
    file = open('produtos.json', 'w+', encoding="utf-8")
    file.write(js.decode())
    file.close()

# Executando a função
similary_product(df, df2)