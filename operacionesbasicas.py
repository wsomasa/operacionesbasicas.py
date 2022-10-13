mensaje_1 = "===================================="
mensaje = "Operaciones básicas matemáticas"
mensaje_2 = "===================================="
print('\033[92m'"\n\t", mensaje_1.center(50, "="),""'\033[0m')
print('\033[92m'"\t", mensaje.center(50, "="),""'\033[0m')
print('\033[92m'"\t", mensaje_2.center(50, "="),"\n"'\033[0m')

banner = """Operaciones básicas de matemáticas: 
        suma, resta, multiplicación, división"""
print('\033[92m'"\n\t", banner.ljust(100), '\033[0m')

num1 = int(input("\n\t""Ingrese el primer número: "'\033[0m'))
num2 = int(input("\n\t""Ingrese el segundo número: "'\033[0m'))
resultado = 0
 
resultado = num1 + num2
print('\033[91m'"\n\t""El resultado de la suma (+) es: ", resultado)

resultado = num1 - num2
print('\033[92m'"\n\t""El resultado de la resta (-) es: ", resultado)

resultado = num1 * num2
print('\033[93m'"\n\t""El resultado de la multiplicación (*) es: ", resultado)

resultado = num1 / num2
print('\033[94m'"\n\t""El resultado de la división (/) es: ", float(round(resultado,2)),'\n''\033[0m')
