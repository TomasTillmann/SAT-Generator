#!/bin/bash

upperBound="10"
for ((n=1; n <= $upperBound; n++)) do
    pocetPromennych=$( cat satInput${n}.txt | head -1 | cut -d" " -f3 )
    pocetKlauzuli=$( cat satInput${n}.txt | head -1 | cut -d" " -f4 )
    echo "Pro n rovno ${n} je pocet promennych ${pocetPromennych} a pocet klauzuli ${pocetKlauzuli}."
done


