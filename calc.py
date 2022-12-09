#Criar variáveis
nome = str(input("Digite seu nome :")).strip().upper()
idade = int(input("Digite sua idade :"))
peso = float(input("Digite seu peso em KG :"))
altura = float(input("Digite sua altura em m :"))
imc = peso /(altura **2) 
#Criação da lógica 
print("Seu imc é de {: .2f}".format(imc))
if imc < 18.5:
    print("Seu peso está abaixo do normal !")
elif  imc >= 18.5 and imc <= 24.9:
     print("Seu peso está ideal")
elif  imc >= 25 and imc <= 29.9 :
     print("Peso em pré-obesidade ou acima do peso")
elif  imc >= 30 and imc <= 34.9:
     print("Este índice indica obesidade grau um")
else:
    print("Seu peso está em Obesidade grau dois, três ou mórbida")