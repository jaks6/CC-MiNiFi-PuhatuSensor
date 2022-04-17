

The below run command starts MiNiFi and a python script which publishes .json-formmatted sensor-data to `/opt/puhatu/output/sensor` .

It is advisable to use -v option to provide a minifi bootstrap.conf file. 

```
docker run -td --name puhatu-sensor -e DEVICE_ID="puhatu_c3" -e SENSOR_INTERVAL=5 jaks6/puhatu:latest
```



If you need to work with a NiFi instance that runs inside a docker container, you can adjust the hosts with --add-host


For example:
```
docker run -td --name puhatu-sensor -e DEVICE_ID="puhatu_c3" -e SENSOR_INTERVAL=5 --add-host=d3d1fc9d5279:123.45.67.69 jaks6/puhatu:latest

```