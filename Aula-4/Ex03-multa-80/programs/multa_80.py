velocidade = float(input("Digite a velocidade do seu carro (km/h): "))
if velocidade > 80:
    excesso = velocidade - 80
    print(f"Você foi multado! Valor da multa: R$ {excesso * 5:.2f}")
else:
    print("Velocidade dentro do limite. Boa viagem!")
