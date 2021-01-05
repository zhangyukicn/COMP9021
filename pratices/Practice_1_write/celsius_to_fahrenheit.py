#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 11:04:01 2019

@author: yuki
"""

'''
Prints out a conversion table of temperatures from Celsius degrees to Fahrenheit,
with the former ranging from 0 to 100 in steps of 10.
'''
min_temperatures_celsius_degrees = 0
max_temperatures_celsius_degrees = 100
steps = 10
print('celsius_degrees\tfahrenheit')
for celsius_degrees in range(min_temperatures_celsius_degrees,max_temperatures_celsius_degrees + 1,steps):
    fahrenheit = (celsius_degrees * 9)/5 + 32
    print(f'{celsius_degrees:10}\t{fahrenheit:7.1f}')

celsius = 24
fahrenheit = (celsius_degrees * 9)/5 + 32
print(fahrenheit)
