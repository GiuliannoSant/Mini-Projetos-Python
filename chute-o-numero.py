# CHUTE O NÚMERO
# Objetivo: Criar um algorítimo que gera um valor aleatório e eu tenho que ficar tentando o número até eu acertar

import random
import PySimpleGUI as sg

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 0
        self.valor_maximo = 100
        self.tentar_novamete = True

    def Iniciar(self):
        #Layout
        layout =[
            [sg.Text('Seu Chute', size=(39,0))],
            [sg.Input(size=(18,0), key='ValorChute')],
            [sg.Button('Chutar')],
            [sg.Output(size=(39,10))]
        ] 
        #making the Window
        self.window = sg.Window('Chute um numero!', layout=layout) 
        self.GerarNumeroAleatorio()
        try:
            while True:
                #receber valores
                self.eventos, self.valores = self.window.Read()
                #fazer algo com os valores
                if self.eventos == 'Chutar':
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamete == True:        
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print("Chute um valor mais baixo!")
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print("Chute um valor mais alto!")
                            break
                        elif int(self.valor_do_chute) == self.valor_aleatorio:
                            print("PAREBÉNS VOCÊ GANHOU!!!")
                            break
        except:
            print('Ocorreu um erro em receber o valor')
            self.Iniciar()

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)

chute = ChuteONumero()
chute.Iniciar()
