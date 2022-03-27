# DECIDA POR MIM
# Objetivo: Faça uma pergunta para o programa e ele terá que te dar uma resposta
import random
import PySimpleGUI as sg

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            "Com certeza, você deve fazer isso!",
            "Não sei, você que sabe",
            "Não faz isso não!",
            "Acho que está na hora certa!"
        ]

    def Iniciar(self):
        #Layout
        layout = [
            [sg.Text('Pergunta')],
            [sg.Input()],
            [sg.Output(size=(50,10))],
            [sg.Button('Decida por mim'), sg.Cancel()]
        ]
        
        #Making the window
        self.window = sg.Window('Decida por mim', layout=layout)
        while True:
            #receber os dados
            self.eventos, self.valores = self.window.Read()
            #fazer algo com esse dados
            if self.eventos == sg.WIN_CLOSED or self.eventos == 'Cancel':
                break
            if self.eventos == 'Decida por mim':
                print(random.choice(self.respostas))

decida = DecidaPorMim()
decida.Iniciar()
