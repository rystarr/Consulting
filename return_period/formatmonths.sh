#!/bin/sh

#format 34 yr data for return period plot

#input file
filename=$1

#replace month names with mm

cat $filename| sed  "s/JAN/01/g" | sed  "s/FEB/02/g" | sed  "s/MAR/03/g" | sed  "s/APR/04/g" | sed  "s/MAY/05/g" | sed  "s/JUN/06/g" | sed  "s/JUL/07/g" | sed  "s/AUG/08/g" | sed  "s/SEP/09/g" | sed  "s/OCT/10/g" | sed  "s/NOV/11/g" | sed  "s/DEC/12/g"  > temp.$filename

cat temp.$filename | sed '1d' | sed 's/,/	/g' > new.$filename

rm temp.$filename

