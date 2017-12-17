# Getting the RPi ready

## Prepare the server
Video with instructions [here](https://www.youtube.com/watch?v=AsDHEDbyLfg&t=46s).
```
sudo apt-get install mosquitto
sudo apt-get install mosquitto-clients
```
Link to the mosquitto configuration options [here](http://mosquitto.org/man/mosquitto-conf-5.html).

 Create the user who will use mosquitto. In this case the user is username.
 ```
 sudo mosquitto_passwd -c /etc/mosquitto/pwfile username
 ```

 Then reboot the Pi...
 
 After the Pi reboots, test the mosquitto. Start two ssh connections (or use screen). 
 In the first one subscribe for a test topic:
 ```
 mosquito_sub -d -u username -P password -t dev/test
 ```
 And in the second one send a test message
 ```
 mosquitto_pub -d -u username -P password -t dev/test -m "hello world"
 ```

