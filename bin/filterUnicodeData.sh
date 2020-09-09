#!/bin/zsh -fe
awk -f bla.awk < UnicodeData.txt | csvjson |\
  jq '. | map({(.hex|tostring): (.name|tostring)}) | add'
