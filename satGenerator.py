#!/usr/bin/env python3
import sys

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


class Vyrok:
    def __init__(self, n:int, formule:list = []) -> None:
        self.n = n
        self.formule = formule
        self.tabulka = Tabulka(n)
        self.pocetKlauzuli = 0

        # lepsi pro debug
        self.konec = 0 

    def jednoCisloNaJednePozici(self) -> list:
        """
        Vsechny vyroky odpovidajici ruznym cislum na stejne pozici vyORuju -> aspon jedno cislo musime zvolit.
        Pak projedu vsechny dvojice d
        """
        vyrok = 0                           # vyroky pak zacnu znacit od 1
        cisla = [0] * self.n                # ruzna cisla na stejne pozici
        for i in range(2 * self.n):
            for j in range(self.n):
                vyrok += 1
                cisla[j] = vyrok
                self.formule.append(vyrok)
            self.formule.append(self.konec)
            self.pocetKlauzuli += 1

            for k in range(len(cisla)):
                for l in range(k+1, len(cisla)):
                    self.formule.append(cisla[k] * (-1))
                    self.formule.append(cisla[l] * (-1))
                    self.formule.append(self.konec)
                    self.pocetKlauzuli += 1

    def dveCislaMax(self) -> list:
        # pres start se meni radek tabulky
        start = 1

        # maximalne 2 cisla v posloupnosti (ale i 0 nebo 1)
        while (start <= self.n):
            # iteruje pres vsechny dvojice v radku tabulky indexovane cislem a pozici - tedy projde vsechny
            # vyroky odpovidajici stejnemu cislu, ale na jinych polohach
            for i in range(start, ((2 * self.n) * self.n) + 1, self.n):  #HACK funuje pro n <= 10
                for j in range(i + self.n, ((2 * self.n) * self.n) + 1, self.n):
                    for k in range(start, ((2 * self.n) * self.n) + 1, self.n):  #HACK funuje pro n <= 10
                        if(k != i and k != j):
                            self.formule.append(i * (-1))
                            self.formule.append(j * (-1))
                            self.formule.append(k * (-1))
                            self.formule.append(self.konec)
                            self.pocetKlauzuli += 1

            # minimalne 2 cisla v posloupnosti (ale i 2 a vice)
            for i in range(start, ((2 * self.n) * self.n) + 1, self.n):  #HACK funuje pro n <= 10
                for j in range(start, ((2 * self.n) * self.n) + 1, self.n):  #HACK funuje pro n <= 10
                    if (i != j):
                        self.formule.append(j)
                
                self.formule.append(self.konec)
                self.pocetKlauzuli += 1
            
            start += 1
            # dohromady prave 2


    def vzdalenosti(self) -> list:
        for i in range(1, ((2 * self.n) * self.n) + 1):    #HACK funguje pro n <= 10
            pozice, cislo = self.tabulka.mapovani2D(i) 

            # zde menit metriku
            # ted je nastavena na 3xxx3 na misto 3xx3
            #doleva = pozice - cislo - 1
            #doprava = pozice + cislo + 1

            # ted je nastavena na 3xx3 na misto 3xxx3
            doleva = pozice - cislo
            doprava = pozice + cislo

            # pokud na obe strany
            if ((doleva) >= 0 and (doprava) < (2 * self.n)):
                self.formule.append(i * (-1))
                self.formule.append(self.tabulka.linearniMapovani(doleva, cislo))
                self.formule.append(self.tabulka.linearniMapovani(doprava, cislo))
                self.formule.append(self.konec)
                self.pocetKlauzuli += 1         #HACK pocet klauzuli si taklhe udrzovat je debilni

            # na levo
            elif ((doleva) >= 0):
                self.formule.append(i * (-1))
                self.formule.append(self.tabulka.linearniMapovani(doleva, cislo))
                self.formule.append(self.konec)
                self.pocetKlauzuli += 1

            # na pravo
            elif ((doprava) < (2 * self.n)):
                self.formule.append(i * (-1))
                self.formule.append(self.tabulka.linearniMapovani(doprava, cislo))
                self.formule.append(self.konec)
                self.pocetKlauzuli += 1
 
         
    def prelozProSat(self) -> list:
        print(f"p cnf {self.n * 2 * self.n} {self.pocetKlauzuli}")
        for i in range(len(self.formule)):
            print(self.formule[i], end=" ")
            if( (self.formule[i] == self.konec) and (i != len(self.formule) - 1) ): print()


def checkInput(argv):
    n = int(argv[0])

    if(len(argv) != 1):
        print("Wrong arguments count. Value must be one number between 1 and 10")
        return -1

    if (n <= 0 or n > 10):
        print("Wrong value. Value must be between 1 and 10")
        return -2

    return n

def main(argv):
    n = checkInput(argv)

    #n = 4
    vyrok = Vyrok(n)
    vyrok.jednoCisloNaJednePozici()            #funguje
    vyrok.dveCislaMax()
    vyrok.vzdalenosti()
    vyrok.prelozProSat()
    return 0


if __name__ == "__main__":
    main(sys.argv[1:])


