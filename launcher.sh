#!/bin/bash
sleep 10 
echo "startup"
#cd /
#cd /home/pi/RPi_Photobooth
sudo python /home/pi/RPi_Photobooth/photobooth.py | tee /home/pi/RPi_Photobooth/photobooth_log.txt &
#sudo python startuptest1.py | tee log.txt &
#sudo python startuptest2.py &
#cd /
exit 0