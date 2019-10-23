#!/usr/bin/python3
#_*_ coding: utf8 _*_

#Noselllama
#By @JoshuaProvoste

from faker import Faker
import os
import random
import time
from datetime import date

fake = Faker()
hostname = fake.name().replace(' ', '-')

a = os.system('hostnamectl set-hostname ' + hostname + '-PC')

os.system('ifconfig wlan0 down')
os.system('ifconfig eth0 down')
os.system('ifconfig lo down')
os.system('macchanger -A eth0')
os.system('macchanger -A wlan0')
os.system('macchanger -A lo')
os.system('ifconfig eth0 up')
os.system('ifconfig wlan0 up')
os.system('ifconfig lo up')
os.system('service network-manager restart')
os.system('service networking restart')