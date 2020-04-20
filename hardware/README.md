This directory contains js files and scripts for sending sensor data from Pi to cloud directly or via neocortec mesh network

Component group 1 :
Laptop, Neocortec, Raspberry Pi

Component group 2 :
Laptop2, Neocortec2


Steps :

1. Connect Component group 1 
	Pi to Laptop via ethernet
	Neocortec to Pi via USB
2. Connect Component group 2
	Neocortec2 to Laptop2 via USB
3. Login to Pi via Laptop1 and run ./neo_start.sh in ~/neocortec/Raspberry.Pi 
4. In Pi, tail -f /var/log/syslog | grep -A 10 -B 10 "NeoCortec" for debugging
5. In Laptop2, run 
	ls -lathr /dev/ttyUSB*
   This could show /dev/ttyUSB0 and /dev/ttyUSB1 
   				or /dev/ttyUSB1 and /dev/ttyUSB2
6. In Laptop2,
	sudo chmod a+rw /dev/ttyUSBx
		for both
7. In Laptop2, in neo.gateway.405/src/NeoCortecGateway/Release, run     
	./NeoCortecGateway -C uart=/dev/ttyUSB0
		if usb devices are USB0 and USB1  |    
	./NeoCortecGateway -C uart=/dev/ttyUSB2
		if usb devices are USB1 and USB2
8. In Laptop1, 
		sudo node send_sensor_data.js
9. In Laptop2,
		sudo node send_sensor_data_from_nc.js
10. Data will be sent from Laptop1 to cloud via internet
	This simulates data sent over cellular network
11. Disable Wifi in Laptop1 to see data sent via NeoCortecs to Laptop2
	This simulates data sent via satellite
