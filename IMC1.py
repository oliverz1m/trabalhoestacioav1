#QUESTÃO 1 // LISTA 1

altura = float(input('Entre com sua altura:'))  #EX: 1.90
peso = float(input('Entre com seu peso:'))  #EX:80
imc = peso/(altura * altura)  
print('Seu índice de massa corporal é {:.2f}'.format(imc))