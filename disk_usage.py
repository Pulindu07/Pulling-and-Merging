#!/usr/bin/env python3
import shutil
import sys
import psutil

def check_disk_usage(disk,min_absolute,min_percent):
    """"Returns True if there's enough disk space, false otherwise"""
    du = shutil.disk_usage(disk)
    # calculates the percentage of free disk space
    percent_free = du.free/du.total*100
    print(str(int(percent_free))+"% Free")
    # calculates how many free GBs
    gigabyte_free = du.free / 2**30
    print("{:.2f}GB Free.".format(gigabyte_free))
    if percent_free < min_percent or gigabyte_free < min_absolute:
        return False
    return True
def check_cpu_usage():
    cpu_use = psutil.cpu_percent(2)
    return cpu_use > 80

def disk_usage():
    if check_disk_usage("/",2,10):
        return False
        
    return True

if not check_disk_usage("/",2,10):
    print("ERROR: Not enough disk space")
    sys.exit(1)

print("Everything okay")

print("Line 1")
sys.exit(0)
