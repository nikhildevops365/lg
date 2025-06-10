# -*- coding: utf-8 -*-
"""
Created on Sat Jun  7 14:18:13 2025

@author: nsain
"""
import time
def log_producer(log_size):
    g = 4*4
   # print(log_size)
    

import json
import random
import string
import sys
from datetime import datetime

def generate_random_log():
    return json.dumps({
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "level": random.choice(["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]),
        "service": random.choice(["auth", "payment", "inventory", "shipping"]),
        "message": ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(50, 150))),
        "trace_id": ''.join(random.choices(string.hexdigits, k=16)).lower()
    })

def generate_logs(log_size_mb, increment_mb=0.005, output=sys.stdout):
    target_bytes = int(log_size_mb * 1024 * 1024)
    increment_bytes = int(increment_mb * 1024 * 1024)
    written_bytes = 0

    while written_bytes < target_bytes:
        batch = []
        batch_size = 0

        while batch_size < increment_bytes:
            log = generate_random_log() + "\n"
            encoded_log = log.encode('utf-8')
            batch.append(log)
            batch_size += len(encoded_log)

        output.writelines(batch)
        written_bytes += batch_size

    print(f"Generated {written_bytes / (1024 * 1024):.3f} MB of logs.")



def run_for_one_second(log_size):
    """Run the given task repeatedly for ~1 second."""
    start_time = time.time()
    while time.time() - start_time <= 1:
        generate_logs(log_size)


start_log_volume_size = 1
desired_volume_size = 90
time_span_hours = 5
time_span_hours_to_seconds = time_span_hours * 60 * 60
print(time_span_hours_to_seconds)
log_size_increment = desired_volume_size/time_span_hours_to_seconds 
print(log_size_increment)
print(f"log size we started with {start_log_volume_size} MBs")
count = 1 
start_time_of_log_size_increase = time.time()
while start_log_volume_size < desired_volume_size:
    run_for_one_second(start_log_volume_size)
    
    #time.sleep(1)
    start_log_volume_size = start_log_volume_size + log_size_increment
    count = count + 1
end_time_of_log_size_increase = time.time()
    
time_to_increase_log_volume  =  end_time_of_log_size_increase -  start_time_of_log_size_increase
print(f"log size we ended with after gradually increasing volume in {time_to_increase_log_volume} seconds is {start_log_volume_size} MBs")
print(f"count {count}")    

print("=================================================================================================")

desired_volume_size = 1
start_time_of_log_size_decrease = time.time()
print(f"log size we started with {start_log_volume_size} MBs")
count = 1 

while start_log_volume_size > 1:
    run_for_one_second(start_log_volume_size)
   # time.sleep(1)
    start_log_volume_size = start_log_volume_size - log_size_increment
    count = count + 1
end_time_of_log_size_decrease = time.time()
time_to_decrease_log_volume  =  end_time_of_log_size_decrease -  start_time_of_log_size_decrease
print(f"log size we ended with after gradually decreasing volume in {time_to_decrease_log_volume} seconds is {start_log_volume_size} MBs")
print(f"count {count}")    

    
