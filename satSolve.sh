#!/bin/bash
satGenerator="satGenerator.py"
upperBound="10"
satSolver="minisat"

for ((n=1; n <= $upperBound; n++)) do
    ./${satGenerator} $n >satInput${n}.txt
done

for ((n=1; n <= $upperBound; n++)); do 
    ${satSolver} satInput${n}.txt satOutput${n}.txt
done


