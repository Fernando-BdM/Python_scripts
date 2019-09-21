import pandas as pd

print('#####  SIMULADOR DE FINANCIAMENTO  #####')
valor_financ = int(input('Informe o valor a ser financiado: '))
prazo = int(input('Informe o prazo do financiamento: '))
taxa = (float(input('Informe a taxa de juros: ')))/100
tipo = input('Escolha o sistema de amortização?\n\n1) SAC\n2) PRICE ')
saldo_devedor = valor_financ
colunas = ['Prestação','Juros','Amortização','Saldo Devedor']
simulacao = pd.DataFrame(data =[[0,0,0,saldo_devedor]],columns = colunas).rename_axis('Mês')

if tipo == '2':
    print('\nSistema PRICE escolhido!\n')
    while saldo_devedor > 0 :
        prestacao = valor_financ * ((((1 + taxa) ** prazo) * taxa) / ((1 + taxa) ** prazo - 1))
        juros_mes = saldo_devedor * taxa
        amortizacao = prestacao - juros_mes
        saldo_devedor -= amortizacao

        simulacao = simulacao.append(pd.DataFrame(data = [[prestacao.__round__(2),juros_mes.__round__(2)
                        ,amortizacao.__round__(2),saldo_devedor.__round__(2)]],columns = colunas),
                                      ignore_index=True)
else:
    print('\nSistema SAC escolhido!\n')
    while saldo_devedor > 0:

        juros_mes = saldo_devedor * taxa
        amortizacao = valor_financ / prazo
        prestacao = amortizacao + juros_mes
        saldo_devedor -= amortizacao

        simulacao = simulacao.append(pd.DataFrame(data=[[prestacao.__round__(2), juros_mes.__round__(2)
                                                            , amortizacao.__round__(2), saldo_devedor.__round__(2)]],
                                                  columns=colunas),
                                     ignore_index=True)
simulacao = simulacao.rename_axis('Mês')
print(simulacao)
escolha = input('\nGostaria de salvar a simulação? (s/n)')
if escolha == 's':
    simulacao.to_csv('simulacao.csv')
    print('Simulador salvo!')
else:
    print('A simulação não foi salva')


