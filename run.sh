#!/bin/bash

cadvisor --port=6677 &

python3 /code/exporter.py 
