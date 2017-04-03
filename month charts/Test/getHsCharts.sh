#!/bin/sh

#Input {COORD}inates for existing charts (must be in this format eg. 22.00_68.50)

LAT=$1
LON=$2
#Grab Charts
wget http://qa.surfline.com/lola/climateCharts/climateChart_waveheight_1_${LAT}_${LON}_0_0_0_360_.png -O JAN.png
wget http://qa.surfline.com/lola/climateCharts/climateChart_waveheight_2_${LAT}_${LON}_0_0_0_360_.png -O FEB.png
wget http://qa.surfline.com/lola/climateCharts/climateChart_waveheight_3_${LAT}_${LON}_0_0_0_360_.png -O MAR.png
wget http://qa.surfline.com/lola/climateCharts/climateChart_waveheight_4_${LAT}_${LON}_0_0_0_360_.png -O APR.png
wget http://qa.surfline.com/lola/climateCharts/climateChart_waveheight_5_${LAT}_${LON}_0_0_0_360_.png -O MAY.png
wget http://qa.surfline.com/lola/climateCharts/climateChart_waveheight_6_${LAT}_${LON}_0_0_0_360_.png -O JUN.png
wget http://qa.surfline.com/lola/climateCharts/climateChart_waveheight_7_${LAT}_${LON}_0_0_0_360_.png -O JUL.png
wget http://qa.surfline.com/lola/climateCharts/climateChart_waveheight_8_${LAT}_${LON}_0_0_0_360_.png -O AUG.png
wget http://qa.surfline.com/lola/climateCharts/climateChart_waveheight_9_${LAT}_${LON}_0_0_0_360_.png -O SEP.png
wget http://qa.surfline.com/lola/climateCharts/climateChart_waveheight_10_${LAT}_${LON}_0_0_0_360_.png -O OCT.png
wget http://qa.surfline.com/lola/climateCharts/climateChart_waveheight_11_${LAT}_${LON}_0_0_0_360_.png -O NOV.png
wget http://qa.surfline.com/lola/climateCharts/climateChart_waveheight_12_${LAT}_${LON}_0_0_0_360_.png -O DEC.png

