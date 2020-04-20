#!/bin/bash
sudo systemctl stop NeoGW.service      
sudo systemctl disable NeoGW.service
sudo cp NeoGW.service /lib/systemd/system/NeoGW.service
sudo cp NeoCortecGateway /lib/systemd/
sudo chmod 777 /lib/systemd/NeoCortecGateway 
sudo systemctl enable NeoGW.service
sudo systemctl start NeoGW.service      
