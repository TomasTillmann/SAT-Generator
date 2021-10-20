#!/usr/bin/env python3

class Tabulka:
    def __init__(self, n:int) -> None:
        self.n = n

    def mapovani2D(self, linearniPozice:int):
        a = linearniPozice - 1       # odecteme jedna aby fungavala matika a indexovani od nuly
        pozice, cislo = 0, 0

        pozice = a // self.n          # pozice v tabulce indexujeme od nuly
        cislo = (a % self.n) + 1      # samotna cisla (vyroky) na pozici indexujeme od 1
        
        return (pozice, cislo)
    
    def linearniMapovani(self, pozice:int, cislo:int):
        return (pozice * self.n) + cislo

class Reader:
    def getSequence(filename:str):
        pass


def main():
    # could be potentially changed by user by command line
    upperBound = 10
    fileName = "satOutput"
    for n in range(1, upperBound + 1):
        file = open(f"{fileName}{n}.txt")

    pass


if (__name__ == '__main__'):
    main()
