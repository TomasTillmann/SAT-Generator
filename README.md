# About
Little script for generating SAT formulas, that are in valid format to be solved for SAT solvers. Generated SAT formulas are logically equivalent to the problem down below.

# Problem
Convert this problem to CNF and solve by using a SAT solver: Decide, whether two sets {1,...n} can be arranged in a sequence of length 2n, such as distance between numbers k is exactly k.
Solve for n≤10.

# Zadání
Převeďte na CNF a vyřešte pomocí (některého) SAT solveru:  Rozhodněte, zda dvě množiny {1,...,n} jdou uspořádat do posloupnosti délky 2n tak, že vzdálenost mezi čísly k je právě k.  
Vyřešte pro n≤10.

## Řešení
### RESENI - UKOL 2 VPL
### AUTOR: Tomas Tillmann

* Pro n = 1: 1 1 
* Pro n = 4: 4 2 3 2 4 3 1 1 
* Pro n = 5: 5 2 4 2 3 5 4 3 1 1 
* Pro n = 8: 6 8 3 7 4 3 6 5 4 8 7 2 5 2 1 1 
* Pro n = 9: 6 8 5 9 7 3 6 5 3 8 4 7 9 2 4 2 1 1 

### Pro jina n posloupnost neexistuje.

* Pro n rovno 1 je pocet promennych 2 a pocet klauzuli 6.
* Pro n rovno 2 je pocet promennych 8 a pocet klauzuli 48.
* Pro n rovno 3 je pocet promennych 18 a pocet klauzuli 240.
* Pro n rovno 4 je pocet promennych 32 a pocet klauzuli 792.
* Pro n rovno 5 je pocet promennych 50 a pocet klauzuli 2010.
* Pro n rovno 6 je pocet promennych 72 a pocet klauzuli 4296.
* Pro n rovno 7 je pocet promennych 98 a pocet klauzuli 8148.
* Pro n rovno 8 je pocet promennych 128 a pocet klauzuli 14160.
* Pro n rovno 9 je pocet promennych 162 a pocet klauzuli 23022.
* Pro n rovno 10 je pocet promennych 200 a pocet klauzuli 35520.

### Generujcici soubor: satGenerator.py
### Generovane vysledky SAT solverem: satOutputn.txt
### Generovany input pro SAT solver: satInputn.txt

* Preklad SAT vysledku: satOutputTranslator.py
* Prikaz pro automatizovane spusteni minisatu pro n od 1 do 10: ./satSolve.sh

### Prerekvizity:
* bash
* python3
* Pouzity SAT solver: minisat


# Example
* for n = 4
* 4 2 3 2 4 3 1 1
