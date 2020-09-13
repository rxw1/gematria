#!/bin/zsh -f

typeset -A a=(
  1   א # Aleph   
  2   ב # Bet     
  3   ג # Gimel   
  4   ד # Daleth  
  5   ה # Heh     
  6   ו # Vav     
  7   ז # Zayin   
  8   ח # Het     
  9   ט # Tet     
  10  י # Yud     
  20  כ # Kaf     
  30  ל # Lamed   
  40  מ # Mem     
  50  נ # Nun     
  60  ס # Samech  
  70  ע # Ayin    
  80  פ # Peh     
  90  צ # Tzady   
  100 ק # Koof    
  200 ר # Reish   
  300 ש # Shin    
  400 ת # Taf     
  500 ך # Kaf     
  600 ם # Mem     
  700 ן # Nun     
  800 ף # Peh     
  900 ץ # Tzady   
)

typeset -A b=(
  a 1
  b 2
  c 3
  d 4
  e 5
  f 6
  g 7
  h 8
  i 9
  j 10
  k 20
  l 30
  m 40
  n 50
  o 60
  p 70
  q 80
  r 90
  s 100
  t 200
  u 300
  v 400
  w 500
  x 600
  y 700
  z 800
)

d=();

#for ((i=1; i<=$#1; i++)); do
#  d+=$(expr index abcdefghijklmnopqrstuvwxyz ${1[$i]});
#done;

for ((i=1; i<=$#1; i++)); do
  d+=$b[${1[$i]}]
done

bc <<< ${(j:+:)d}
