#!/bin/bash
python3 /opt/puhatu/sensor.py $DEVICE_ID $SENSOR_INTERVAL > /dev/null &
sh /app/minifi-1.16.0/bin/minifi.sh start &&
tail -f /app/minifi-1.16.0/logs/minifi-app.log
