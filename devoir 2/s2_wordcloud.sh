#!/usr/bin/env bash

# Building a wordcloud based on one year of bulletins

YEAR=$1
#cat data/txt/*_${YEAR}_*.txt > module3/${YEAR}.txt
#python module3/filter.py $YEAR
wordcloud_cli --text tmp/${YEAR}_keywords.txt --imagefile tmp/${YEAR}.png --width 2000 --height 1000
display tmp/${YEAR}.png
