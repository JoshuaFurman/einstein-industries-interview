# einstein-industries-interview
Program reads in a config file and stores the information into a Python dictionary.
I've included an example config file in the directory.

# To run program:
```bash
pipenv shell

python main.py
```
You are then prompted to input the config_filename:
```
Please type which file to parse: <config_filename>
```
## Sample input:
```
# This is what a comment looks like, ignore it

# All these config lines are valid

host = test.com

server_id=55331

server_load_alarm=2.5

user= user

# comment can appear here as well

verbose =true

test_mode = on

debug_mode = off

log_file_path = /tmp/logfile.log

send_notifications = yes
```
## Sample output:
```
host is set to: test.com
server_id is set to: 55331
server_load_alarm is set to: 2.5
user is set to: user
verbose is set to: True
test_mode is set to: True
debug_mode is set to: False
log_file_path is set to: /tmp/logfile.log
send_notifications is set to: True
```
