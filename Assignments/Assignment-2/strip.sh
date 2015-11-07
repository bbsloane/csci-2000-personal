#!/bin/bash
#Brittany Sloane
#100568757
touch "bottom_removal"
touch "top_removal"
top="top_removal"
topnum=$1
bot="bottom_removal"
botnum=$2
infile=$3
tail -n +$topnum $infile > $top
head -n -$botnum  $top > $bot 
rm $top
cat $bot
rm $bot
   



