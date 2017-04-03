#!/bin/sh

echo Latitude:
read varlat
echo Longitude:
read varlon
echo Define variable eg. waveheight,waveperiod,windspeed:
read varinp


LAT=$varlat
LON=$varlon
VAR=$varinp

#if [ $# -eq 0 ]
#  then
#    echo "No argument supplied"
#    exit
#fi

#Define months:
months={1..12}
months=$(seq 1 1 12)
#Grab Charts

for i in $months; do
	wget http://qa.surfline.com/lola/climateCharts/climateChart_${VAR}_${i}_${LAT}_${LON}_0_0_0_360_.png -O $i.png
done

./num2months.sh