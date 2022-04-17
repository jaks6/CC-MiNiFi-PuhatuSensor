#!/bin/python
import pandas as pd
import numpy as np
import argparse
import time

parser = argparse.ArgumentParser(description='Puhatu sensor simulator.')
parser.add_argument('device_id', metavar='device_id',
                    help='One of: puhatu_b1, puhatu_b2, puhatu_b3, puhatu_c1, puhatu_c2, puhatu_c3, puhatu_l1')
parser.add_argument('sleep_interval', type=int, help='How many seconds to sleep between producing values')
args = parser.parse_args()

print("Sensor with ID: %s is booting up...\n\n" % args.device_id)
types = {'air_Pressure_mH2o': np.float64, 'air_Temp_float': np.float64, 'airtime': 'str',
         'batt': float, 'dev_id': "str", 'dist': float, 'rssi': int,  'snr': float,
         'wat_Pressure_mH2o': float, 'wat_Temp_float': float, 'wat_level_mH2o': float}

df = pd.read_csv('/opt/puhatu/puhatu_data.csv', dtype=types)
df = df[(df.dev_id == args.device_id)]

while True:
    for i, row in df.iterrows():
        row['time'] = time.time()

        with open("/opt/puhatu/output/sensor", 'w') as file:
            file.write(row.to_json())

        time.sleep(args.sleep_interval)