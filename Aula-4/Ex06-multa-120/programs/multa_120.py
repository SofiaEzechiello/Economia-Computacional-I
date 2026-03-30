velocidade = float(input("Digite a velocidade do seu carro (km/h): "))
if velocidade > 120:
    excesso = velocidade - 120
    print(f"Você foi multado! Valor da multa: R$ {excesso * 5:.2f}")
else:
    print("Velocidade dentro do limite. Boa viagem!")
