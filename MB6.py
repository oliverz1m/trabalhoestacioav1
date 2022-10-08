#QUESTÃO 6 // LISTA 1

tamanho = float(input('Tamanho do arquivo (MB):'))            #EX:30
velocidade = float(input('Velocidade de Internet (MBps): '))   #EX:60
print('Tempo aproximado de download: %.0f Minutos ' %((tamanho / velocidade) * 60))