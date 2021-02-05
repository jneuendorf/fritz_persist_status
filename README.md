# fritzbox_persistent_status_monitor
Persist your Fritz!Box connection status over time


## Run

`nohup pipenv run python ./main.py > output.log &`

## Kill

`ps ax | grep main.py`, then `kill PID`