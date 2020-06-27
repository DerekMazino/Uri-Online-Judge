salario=float(input())
salario1=salario
if salario<=400.00:
    salario=salario*1.15
    reaj=salario1*0.15
    por=15
elif salario>400.00 and salario<=800.00:
    salario=salario*1.12
    reaj=salario1*0.12
    por=12
elif salario>800.00 and salario<=1200.00:
    salario=salario*1.10
    reaj=salario1*0.10
    por=10
elif salario>1200.00 and salario<=2000.00:
    salario=salario*1.07
    reaj=salario1*0.07
    por=7
elif salario>2000.00:
    salario=salario*1.04
    reaj=salario1*0.04
    por=4
print('Novo salario: {:.2f}'.format(salario))
print('Reajuste ganho: {:.2f}'.format(reaj))
print('Em percentual: {} %'.format(por))