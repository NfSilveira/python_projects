from gettext import translation


colors = {'verde' : 'green', 'vermelho' : 'red', 'preto' : 'black', 'branco' : 'white'}
color = input('Escolha a cor que deseja traduzir: ').lower()
translation = colors.get(color, 'esta cor não consta no dicionário.')
print(translation)