#!/bin/bash

clear

function usage {

if [ "$1" = "clock" ] ; then
	echo "$(date)"
elif [ "$1"  = "timer" ] ; then
	read -p 'How long would you like to set the timer?(hh:mm:ss) : ' time
	let H=${time:0:2}*3600
	let M=${time: -5:-3}*60
	let S=${time:6}
	read -p $'What is your musical preference?\n(1. Default | 2. Gaming | 3. Religious | 4. Italian | 5. Nietzsche): ' tone
	let start_time=$(date +%s)
	let current_time=$(date +%s)
	let end_time=H+M+S+start_time
	echo $start_time
	echo $end_time
	while [ $current_time -lt $end_time ]
	do
		let current_time=$(date +%s)
		let count=$end_time-$current_time
		let H=count/3600
		let M=count%3600/60
		let S=count%3600%60
		echo "$H h:$M m:$S s"
	done
	sound $tone
else 
	echo Options: clock, timer
fi
}

function sound {
if [ $tone = '1' ] ; then
        omxplayer -o local audio/wry.mp3
elif [ $tone = '2' ] ; then
        omxplayer -o local audio/mii.mp3
elif [ $tone = '3' ] ; then
        omxplayer -o local audio/waluigi.mp3
elif [ $tone = '4' ] ; then
	omxplayer -o local audio/giorno.mp3
elif [ $tone = '5' ] ; then
	omxplayer -o local audio/god_is_dead_OwO.mp3
else
	omxplayer -o local audio/wry.mp3
fi
}

usage $1
echo --END--


