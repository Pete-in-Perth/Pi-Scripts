#!/bin/bash

# script for monitoring wireless connection and re-connecting if lost
# source: https://www.raspberrypi.org/forums/viewtopic.php?t=16054#p165196

while true ; do
	if ifconfig wlan0 | grep -q "inet addr:" ; then
                echo "Connected."
		sleep 30
	else
		echo "Network connection down! Attempting reconnection."
		ifup --force wlan0
		sleep 15
	fi
done
