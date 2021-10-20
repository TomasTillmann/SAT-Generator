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

class Reader:
    def __init__(self, upperBound:int, fileName:str):
        self.upperBound = upperBound
        self.fileName = fileName

    def printSequences(self):
        for n in range(1, self.upperBound + 1):
            table = Tabulka(n)
            sequence = []
            file = open(f"{self.fileName}{n}.txt")
            # first line is useless
            line = file.readline()
            line = file.readline().split(" ")
            try:
                line = [int(x) for x in line]
            except ValueError:
                continue


            for i in range(len(line)):
                # non negative, hence true in sat langugage
                if (line[i] > 0):
                    pozice, cislo = table.mapovani2D(line[i])
                    sequence.append(cislo)
            print(f"Pro n = {n}:", end=" ")
            print(*sequence, end=" ")
            print()


def main():
    # could be potentially changed by user by command line
    reader = Reader(10, "satOutput")
    reader.printSequences()



if (__name__ == '__main__'):
    main()
