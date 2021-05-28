from os import PathLike, sched_get_priority_max

dict = {
    'Hello World':'Olá Mundo',
    'Hello my Friend': 'Olá meu amigo',
    'Big Friend': 'Grande amigo'
}

var_name = 'BEM VINDO AO DICIONARIO'
print(var_name)
var_distanc = len(var_name)*"="
var_distancline = len(var_name)*"-"
print(var_distanc)
print(
    'Palavras disponiveis:'
)
for k in dict.keys():
    print("{}".format(k))

while True: 
    print(
        var_distancline
    )
    try:
        var_inputvalue = input('Palavra?: ')
        print(dict[var_inputvalue])
    except:
        if var_inputvalue == 'exit':
            break
        else: 
            print('A palavra digitada não existe.')