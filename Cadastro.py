from PySimpleGUI import PySimpleGUI as sg

# layout
sg.theme('Reddit')
layout = [
    [ sg.Text('Usuário'), sg.Input(key='usuário', size=(20, 1))],
    [ sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [ sg.Checkbox('Salvar o login?')],
    [ sg.Button('Entrar')],
]
# janela
janela = sg.Window('Tela login', layout)

# ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuário'] == 'Tatiany' and valores['senha'] == '654321':
            print('Seja bem vindo')