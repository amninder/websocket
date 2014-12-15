#Websocket
python based websocket server

1.  url for websocket to listen is defined in line 23 of ws.py
2.  run
```bash
  python ws.py
```
or
```bash
  twistd -y ws.py
```
this option will generate two files
  1. "twistd.log". This file will keep the track of the log for the twisted websocket.
  2. "twistd.pid". This file will store the PID of the twistd process which can be used to kill the process by "kill -INT <PID number>".
