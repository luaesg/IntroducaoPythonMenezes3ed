""" Sequências e Tempo
Uma variável pode mudar pode ter seu valor modificado com o tempo devido a alterações futuras """
divida = 0
compra = 100 # substitui 0 por 100
divida = divida + compra # atualizando o valor da dívida para 100
compra = 200 # substitui 100 por 200
divida = divida + compra # valor da dívida é 300
compra = 300 # substitui 200 por 300
divida = divida + compra # agora o valor da dívida subiu para 600
compra = 0 # identifica que o cliente já encerrou as compras
print(divida) # exibe o valor


