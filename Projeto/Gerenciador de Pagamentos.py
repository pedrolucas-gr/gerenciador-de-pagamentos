from time import sleep

print('=============== \033[1;31mLOJA DAS ANDORINHAS\033[m ===============')
produto = float(input('Valor das compras [$]:  '))
print('FORMAS DE PAGAMENTO')
print('Digite 1 para pagar à vista no dinheiro, com 10% de desconto')
print('Digite 2 para pagar à vista no cartão, com 5% de desconto')
print('Digite 3 para pagar em 2x no cartão, preço normal')
print('Digite 4 para pagar em 3x ou mais, com 20% de juros')
opcao = ' '
pagamento1 = produto-((10/100)*produto)
pagamento2 = produto-((5/100)*produto)
pagamento3 = produto/2
pagamento4 = (produto+((20/100)*produto))
while opcao not in '1234':
    opcao = input('Opção: ')
    if opcao == '1':
        print('O produto ficou R${:.2f} , com 10% de desconto'.format(pagamento1))
    elif opcao == '2':
        print('O produto ficou R${:.2f} , com 5% de desconto'.format(pagamento2))
    elif opcao == '3':
        print('O produto ficou em 2 parcelas de R${:.2f} , no preço normal'.format(pagamento3))
    elif opcao == '4':
        parcelas = int(input('Quantas vezes? '))
        print('O produto ficou em {} parcelas de R${:.2f} , com 20% de juros'.format(parcelas, pagamento4/parcelas))
        print('Que ficará em R${:.2f} no total'.format(pagamento4))
    elif opcao != '1234':
        print('Opção inválida')
        sleep(1)
