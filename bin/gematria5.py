#!/usr/bin/python3.8

import re
import sys
import math
import argparse
import unicodedata
from pprint import pprint
from unidecode import unidecode

parser = argparse.ArgumentParser()

parser.add_argument('-l', '--lang', dest="lang",
                    help='Alphabet to use: [latin, greek, hebrew]', default="latin")

parser.add_argument('string')

args = parser.parse_args()

greek = {
    ["ALPHA"],    #          α  1
    ["BETA"],     #          β  2
    ["GAMMA"],    #          γ  3
    ["DELTA"],    #          δ  4
    ["EPSILON"],  #          ε  5    
    ["DIGAMMA,    STIGMA"],  #  ϝ    6
    ["ZETA"],     #          ζ  7    
    ["ETA"],      #          η  8    
    ["THETA"],    #          θ  9    
    ["IOTA"],     #          ι  10   
    ["KAPPA"],    #          κ  20   
    ["LAMDA"],    #          λ  30   
    ["MU"],       #          μ  40   
    ["NU"],       #          ν  50   
    ["XI"],       #          ξ  60   
    ["OMICRON"],  #          ο  70   
    ["PI"],       #          π  80   
    ["KOPPA"],    #          ϟ  90   
    ["RHO"],      #          ρ  100  
    ["SIGMA"],    #          σ  200  
    ["TAU"],      #          τ  300  
    ["UPSILON"],  #          υ  400  
    ["PHI"],      #          φ  500  
    ["CHI"],      #          χ  600  
    ["PSI"],      #          ψ  700  
    ["OMEGA"],    #          ω  800  
    ["SAMPI"],    #          ϡ  900  
}

lang = {
    "greek": [
        'α', # 001 Alpha
        'β', # 002 Beta
        'γ', # 003 Gamma
        'δ', # 004 Delta
        'ε', # 005 Epsilon
        '',  # 006 -------
        'ζ', # 007 Zeta
        'η', # 008 Eta
        'θ', # 009 Theta
        'ι', # 010 Iota
        'κ', # 020 Kappa
        'λ', # 030 Lambda
        'μ', # 040 Mu
        'ν', # 050 Nu
        'ξ', # 060 Xi
        'ο', # 070 Omicron
        'π', # 080 Pi
        '',  # 090 -------
        'ρ', # 100 Rho
        'σ', # 200 Sigma
        'τ', # 300 Tau
        'υ', # 400 Upsilon
        'φ', # 500 Phi
        'χ', # 600 Chi
        'ψ', # 700 Psi
        'ω', # 800 Omega
        'ϡ'  # 900 Sampi *
    ],
    "hebrew": [
        u'א', # Aleph
        u'ב', # Bet
        u'ג', # Gimel
        u'ד', # Daleth
        u'ה', # Heh
        u'ו', # Vav
        u'ז', # Zayin
        u'ח', # Het
        u'ט', # Tet
        u'י', # Yud
        u'כ', # Kaf
        u'ל', # Lamed
        u'מ', # Mem
        u'נ', # Nun
        u'ס', # Samech
        u'ע', # Ayin
        u'פ', # Peh
        u'צ', # Tzady
        u'ק', # Koof
        u'ר', # Reish
        u'ש', # Shin
        u'ת', # Taf
        u'ך', # Kaf
        u'ם', # Mem
        u'ן', # Nun
        u'ף', # Peh
        u'ץ'  # Tzady
    ],
    #"latin": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
    #        "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    "latin": ["a", "b", "g", "d", "e", "w", "z", "e", "th", "i", "k", "l", "m", "n",
            "x", "o", "p", "q", "r", "s", "t", "y", "ph", "ch", "ps", "o", "ts"]
}

def f(x):
    return int(math.pow(10, math.floor((x - 1) / 9)) * (((x - 1) % 9) + 1))

s = unicodedata.normalize("NFD", args.string)
s = s.replace('ς', 'σ')
for name in [unicodedata.name(c.lower()) for c in s]:
    if re.match("COMBINING", name):
        continue
    c = unicodedata.lookup(name)
    print(name, c)
    #print(c, name, f(lang[args.lang].index(c) + 1))



#print(args.string, s)

#for i in list(s):
#    x = lang[args.lang].index(i.lower()) + 1
#    print(i, x, f(x))
#
#print(sum([f(lang[args.lang].index(x.lower()) + 1) for x in
#           list(s)]))
#

