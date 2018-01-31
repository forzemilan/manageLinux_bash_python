#!/usr/bin/python
#-*- coding: UTF-8 -*-
#*************************************************************************
#    > File Name: anylyse_ApacheLog.py
#    > Mail: spookw@foxmail.com
#    > Created Time: Wed 31 Jan 2018 05:07:23 PM CST
# ************************************************************************/

from __future__ import print_function
from collections import Counter


#function 1:  to calculate PV&UV and access parameter log_path
def calculate_PV_UV(log_path):
	ips = []	
	with open(log_path) as f:
		for line in f:
			ips.append(line.split()[0])

	print("PV is {0}".format(len(ips)))
	print("UV is {0}\n".format(len(set(ips))))

#function 2: show the website Top10 resource
def Top10_resource(log_path):
	c = Counter()
	with open(log_path) as f:
		for line in f:
			c[line.split()[6]] += 1
	print("Popular resources: {0}\n".format(c.most_common(10)))

#function 3: calculate  percent error_requests/sum_requests
def error_requests(log_path):
	d = {}
	with open(log_path) as f:
		for line in f:
			key = line.split()[8]		
			d.setdefault(key,0)
			d[key] += 1
	sum_requests = 0
	error_requests = 0
	
	for key,value in d.iteritems():
		if int(key) >= 400:
			error_requests += value
		sum_requests += value
	print("error rate: {0:.2f}%\n".format(error_requests * 100.0 / sum_requests))


if __name__ == '__main__':
	log_path = 'access_log-20180131'
	calculate_PV_UV(log_path)
	Top10_resource(log_path)
	error_requests(log_path)



