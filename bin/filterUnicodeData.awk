#!/usr/bin/awk

BEGIN {
  FS=";"
  printf("hex,name\n")
}

$2~/^(GREEK|HEBREW|LATIN) (CAPITAL|SMALL)? ?LETTER ?(FINAL)? ?[A-Z]*$/ {
  printf("\"%s\",\"%s\"\n", $1, $2)
}
