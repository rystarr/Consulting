#!/bin/sh

END=2014

for i in $(seq 2010 $END);
do 
cat test_data.txt | grep $i;
done