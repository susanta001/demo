class Subhajit:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    # self -> use to access variable in the class
    def total(self):
        print(f'{self.n1} + {self.n2} = {self.n1+self.n2}')


p1 = Subhajit(3,4)
p1.total()
    
