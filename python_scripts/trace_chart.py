#!/usr/bin/python
# -*- coding: UTF-8 -*- 
#***********************************************************************
#> File Name: trace_chart.py
#> Mail: spookw@foxmail.com
#> Created Time: Thu 01 Feb 2018 04:23:48 PM CST
#************************************************************************/
from __future__ import print_function

import os
import sys
import time
import subprocess

import warnings
import logging
warnings.filterwarnings("ignore", category=DeprecationWarning)
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import traceroute

target = "www.google.com"
dport = [80]
res,unans = traceroute(target, dport=dport, retry=-2)
res.graph()
res.graph(target="> google.svg")
time.sleep(1)
subprocess.Popen("/usr/bin/convert google.svg google.png", shell=True)
