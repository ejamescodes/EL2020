#!/bin/bash

clear

function usage {

if [ "$1" = "clock" ] ; then
	let start_time=$(date +%s)
	let current_time=$(date +%s)+5
	echo $start_time
	echo $current_time
elif [ "$1"  = "timer" ] ; then
	read -p 'How long would you like to set the timer?(hh:mm:ss) : ' time
	let h=${time:0:2}*3600
	let m=${time: -5:-3}*60
	let s=${time:6}
	read -p $'What is your musical preference?\n(1. Default | 2. Gaming | 3. Religious | 4. Italian | 5. Nietzsche): ' tone
	let start_time=$(date +%s)
	let current_time=$(date +%s)
	let end_time=h+m+s+start_time
	echo $start_time
	echo $end_time
	while [ $current_time -lt $end_time ]
	do
		let current_time=$(date +%s)
		let count=$end_time-$current_time
		let h=count/3600
		let m=count%3600/60
		let s=count%3600%60
		echo "$h:$m:$s"
	done
	sound $tone
else 
	echo Options: clock, timer
fi
}

function sound {
if [ $tone = '1' ] ; then
        echo 1
elif [ $tone = '2' ] ; then
        echo 2
elif [ $tone = '3' ] ; then
        echo 3
elif [ $tone = '4' ] ; then
	echo 4
elif [ $tone = '5' ] ; then
	omxplayer -o local audio/god_is_dead_OwO.mp3
else
	echo default
fi
}

usage $1
echo --END--


