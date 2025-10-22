import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

class nome_teste:
    def __init__(self,salario:float,outras_rendsa:float):
        self.salario = salario 
        self.outras_rendas = outras_rendsa
    
    def despesas(self):
        despesas = []
        print("Bem vindo: ")
        print("Se não tiver mais nenhuma aperte 999 ;)")
        while True:
            per = str(input("Digite a sua despesas: "))
            valor = float(input("Digite o valor da despesas: "))
            despesas.append(per,valor)
            if per == '999':
                break 
        return np.sum(despesas)
    