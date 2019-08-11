class NodoPi():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sig = None


class Pila():
    def __init__(self):
        self.cabeza = None

    def push(self,x,y):
        nuevo = NodoPi(x, y)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            nuevo.sig = self.cabeza
            self.cabeza = nuevo

    def impri(self):
        temp = self.cabeza
        if temp is None:
            print("La pila esta vacia")
        else:
            while temp is not None:
                
                temp = temp.sigprint(temp.x, ",", temp.y)

    def peek(self):
        if self.cabeza is None:
            print("Esta vacia")
        else:
            print("quitar: " + str(self.cabeza.x + "," + self.cabeza.y))

    def pop(self):
        temp = self.cabeza
        self.cabeza = self.cabeza.sig




P = Pila()
P.push(0,0)
P.push(1, 1)
P.push(2, 2)
P.impri()


