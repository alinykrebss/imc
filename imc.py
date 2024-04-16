nome = (input("diga seu nome "))
altura = float(input("diga sua altura "))
peso = float(input("diga seu peso  "))

imc = peso / (altura ** 2)

if imc < 18.5:
    categoria = "abaixo do peso, busque suplementos cariani "

elif  18.6 <= imc <= 24.9:
       categoria = "parabens esta no peso ideal "

elif 25.0 <= imc <=  29.9:
      categoria = "sobrepeso "
           
elif 30.0<= imc <=  34.9:
      categoria = "obesidade grau 1"

elif 35.0 <= imc <=  39.9:
      categoria = "obesidade grau 2"

else:
      categoria = "obesidade grau 3, recorra a academia mais proxima urgentemente!!!!!!!"

print(f" o IMC de {nome} eh {imc} esta na categoria {categoria}")