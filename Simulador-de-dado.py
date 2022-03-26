# Simulador de dado
# Simular o uso de um dado, gerando um valor de 1 até 6
import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        # Layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'), sg.Button('Não')]
        ]

    def Iniciar(self):
        # making the Window
        self.window = sg.Window('Simulador de Dado', layout=self.layout)
        # Ler os eventos da tela
        self.eventos, self.valores = self.window.Read()
        #Fazer alguma coisa com esses valores
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.GerarValorDoDado()
            elif self.eventos == 'Não' or self.eventos == 'n':
                print('Agradecemos a sua participação!')
            else:
                print('Favor digitar sim ou não')
        except:
            print('Ocorreu um erro em receber sua resposta')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


simulador = SimuladorDeDado()
simulador.Iniciar()


