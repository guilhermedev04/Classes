class Quadrado:
    def __init__(self, lado): 
        self.lado = lado
        self.perimetro = int(self.lado) * 4
        self.area = int(self.lado) * int(self.lado)
    def MudarLado(self, novo_lado):
        print(f"Lado trocado de {self.lado} para {novo_lado} ✔")
        print("=-"*30)

        self.lado = novo_lado
        self.perimetro = int(self.lado) * 4
        self.area = int(self.lado) * int(self.lado)
    def MostrarInfo(self):
        print(f"Área do quadrado: {self.area}")
        print(f"Perimetro do quadrado: {self.perimetro}")
        print("=-"*30)
        
quadrado1 = Quadrado("2") #enviar dado em número
quadrado1.MostrarInfo() 
quadrado1.MudarLado(4)
quadrado1.MostrarInfo()
