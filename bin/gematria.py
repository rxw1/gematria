#!/usr/bin/python3.8

import sys
import math
import unicodedata

table = [
    ["A", "ALEF", "ALPHA"],            # 001 Α α א
    ["B", "BET", "BETA"],              # 002 Β β ב
    ["C", "GIMEL", "GAMMA"],           # 003 Γ γ ג
    ["D", "DALET", "DELTA"],           # 004 Δ δ ד
    ["E", "HE", "EPSILON"],            # 005 Ε ε ה
    ["F", "VAV", "DIGAMMA", "STIGMA"], # 006 Ϝ ϝ ו *
    ["G", "ZAYIN", "ZETA"],            # 007 Ζ ζ ז
    ["H", "HET", "ETA"],               # 008 Η η ח
    ["I", "TET", "THETA"],             # 009 Θ θ ט
    ["J", "YOD", "IOTA"],              # 010 Ι ι י
    ["K", "KAF", "KAPPA"],             # 020 Κ κ כ
    ["L", "LAMED", "LAMDA"],           # 030 Λ λ ל
    ["M", "MEM", "MU"],                # 040 Μ μ מ
    ["N", "NUN", "NU"],                # 050 Ν ν נ
    ["O", "SAMEKH", "XI"],             # 060 Ξ ξ ס
    ["P", "AYIN", "OMICRON"],          # 070 Ο ο ע
    ["Q", "PE", "PI"],                 # 080 Π π פ
    ["R", "TSADI", "KOPPA"],           # 090 Ϟ ϟ צ *
    ["S", "QOF", "RHO"],               # 100 Ρ ρ ק
    ["T", "RESH", "SIGMA"],            # 200 Σ σ ר
    ["U", "SHIN", "TAU"],              # 300 Τ τ ש
    ["V", "TAV", "UPSILON"],           # 400 Υ υ ת
    ["W", "KAF", "PHI"],               # 500 Φ φ ך
    ["X", "MEM", "CHI"],               # 600 Χ χ ם
    ["Y", "NUN", "PSI"],               # 700 Ψ ψ ן
    ["Z", "PE", "OMEGA"],              # 800 Ω ω ף
    ["TSADI", "SAMPI"],                # 900 Ϡ ϡ ץ *
]

def f(x):
    return int(math.pow(10, math.floor((x - 1) / 9)) * (((x - 1) % 9) + 1))

sum = 0
for char in unicodedata.normalize("NFD", sys.argv[1]):
    name = unicodedata.name(char.lower())
    if not name.startswith("COMBINING"):
        name = name.split(" ")[-1]
        for sublist in table:
            if name in sublist:
                index = table.index(sublist) + 1
                val = f(index)
                print (char, name, index, val)
                sum += val

print(sum)
