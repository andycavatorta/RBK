#!/bin/bash


set -m
sudo pkill python
fg
cd /home/pi/RBK
sudo python main.py client


