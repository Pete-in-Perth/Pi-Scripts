#!/bin/bash

# script for monitoring wireless connection and re-connecting if lost
# source: https://www.raspberrypi.org/forums/viewtopic.php?t=16054#p165196 and
# https://www.raspberrypi.org/forums/viewtopic.php?t=178175

while true ; do


	ping -c4 192.168.1.1 > /dev/null
	    if [ $? != 0 ]
	    then
		echo "No network connection, restarting wlan0"
		/sbin/ifdown 'wlan0'
		sleep 5
		/sbin/ifup --force 'wlan0'
		sleep 15
	    else
		echo "Connection seems fine"
		sleep 30
	    fi
    

done
