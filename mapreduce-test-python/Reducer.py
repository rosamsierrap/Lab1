#!/usr/bin/python
from operator import itemgetter
import sys

dict_ip_count = {}

for line in sys.stdin:
    line = line.strip()
    ip, num = line.split('\t')
    hour = ip[1:6]
    ip = ip[7:]
    try:
        num = int(num)
        if dict_hour_ip_count.get(hour):
          dict_ip_count[hour][ip] = dict_ip_count[hour].get(ip, 0) + num
        else:
            dict_hour_ip_count[hour] = {ip : 0}

    except ValueError:
        pass

sorted_dict_ip_count = sorted(dict_ip_count.items(), key=itemgetter(0))

for hour, ip_count in sorted_dict_ip_count:
    sorted_ip_count = sorted(ip_count.items(), key=itemgetter(1), reverse=True)
    print('\n')
    for ip, count in sorted_ip_count[:3]:
        print('[{}]{}\t{}'.format(hour,ip, count))