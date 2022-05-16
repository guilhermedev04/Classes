class Bola:
    def __init__(self, cor, circunferencia, material): 
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    def TrocarCor(self, nova_cor):
        print(f"Cor trocada de {self.cor} para {nova_cor} ✔")
        self.cor = nova_cor
    def MostrarCor(self):
        print(f"Sua cor é {self.cor} ✔")
bola1 = Bola("Branca", "4 metros", "Metal")
bola2 = Bola("azul", "6 metros", "Plástico")
print(bola1.cor)
print(bola2.cor)

bola1.TrocarCor(input('Nova cor para a Bola1 '))
bola2.TrocarCor(input('Nova cor para a Bola2 '))

print(bola1.cor)
print(bola2.cor)
