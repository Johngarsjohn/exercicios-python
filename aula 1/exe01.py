import calculadora

a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))

soma = calculadora.somar(a, b)
subtracao = calculadora.subtrair(a, b)
multiplicacao = calculadora.multiplicar(a, b)
divisao = calculadora.dividir(a, b)
print(f'A soma de {a} + {b} = {soma}')
print(f'A subtração {a} - {b} = {subtracao}')
print(f'A multiplicação de {a} * {b} = {multiplicacao}')
print(f'A divisao de {a} / {b} = {divisao}')