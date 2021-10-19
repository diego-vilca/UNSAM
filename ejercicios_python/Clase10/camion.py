from lote import Lote

class Camion:
    def __init__(self, lotes):
        self.lotes = lotes

    def __iter__(self):
        return self.lotes.__iter__()

    def __contains__(self, nombre):
        return any(lote.nombre == nombre for lote in self.lotes) #expresion generadora

    def __len__(self):
        return self.lotes.__len__()

    def __getitem__(self, indice):
        return eval(self.lotes[indice].__repr__())

    def __repr__(self):
         return f'Camion({self.lotes})'

    def __str__(self):
        t = ['Camion con ' + str(self.__len__()) + ' lotes:' ]
        for lotes in self.lotes:
            s = lotes.__str__()
            t.append(s)
        return '\n'.join(t)

    def precio_total(self):
        return sum(l.costo() for l in self.lotes) #expresion generadora

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total
