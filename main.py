# This is a sample Python script.
import PySimpleGUI as sg


class TelaPython:
    def __init__(self):
        """
        Temas para a Tela:
        :LightBlue[1...9]
        :DarkBlue[1...9]
        :Kayak
        :LightBrown[1...9]
        :DarkBrown[1...9]
        """
        sg.change_look_and_feel('BlueMono')
        # Layout
        layout = [
            [sg.Text('Nome', size=(5, 0)), sg.Input(size=(30, 0), key='Nome')],
            [sg.Text('Idade', size=(5, 0)), sg.Input(size=(10, 0), key='Idade')],
            [sg.Text('Genero')],
            [sg.Radio('Masculino', 'sexo', key='Masculino'),
             sg.Radio('Feminino', 'sexo', key='Feminino')],
            [sg.Text('Email de Inscrição')],
            [sg.Checkbox('Gmail', key='gmail'),
             sg.Checkbox('Outlook', key='outlook'), sg.Checkbox('Yahoo', key='yahoo')],
            [sg.Slider(range=(0,255), default_value=0,
                       orientation='h', size=(15, 20), key='SpeedSlider')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(40, 20))]
        ]
        # Janela
        self.janela = sg.Window("Dados do Usuário").layout(layout)

    def Iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.janela.Read()
            nome = self.values['Nome']
            idade = self.values['Idade']
            gmail = self.values['gmail']
            outlook = self.values['outlook']
            yahoo = self.values['yahoo']
            sexo_masc = self.values['Masculino']
            sexo_fem = self.values['Feminino']
            speed = self.values['SpeedSlider']
            print(f'Nome: {nome}')
            print(f'Idade: {idade}')
            print(f'Gmail: {gmail}')
            print(f'Outlook: {outlook}')
            print(f'Yahoo: {yahoo}')
            print(f'Masculino: {sexo_masc}')
            print(f'Feminino: {sexo_fem}')
            print(f'Speed: {speed}')



tela = TelaPython()
tela.Iniciar()
