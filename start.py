#!/usr/bin/python
import requests
from subprocess import Popen, PIPE
import os
script_base = os.path.dirname(os.path.abspath(__file__))

p = Popen([script_base + "/collect.sh"], stdout=PIPE)
raw_output = p.communicate()[0].split('\n')
trimmed = map(lambda entry: entry.split(), raw_output)
filtered = filter(lambda entry: len(entry) > 0, trimmed)
separated = map(lambda entry: dict(label=" ".join(entry[:-1]), value=entry[-1]), filtered)
data = {}
for entry in separated:
    label = entry["label"].lower().replace(" ", "_")
    data[label] = entry["value"]
print data

data.update(dict(device_id='rpi2'))

response = requests.post('https://thermonoto.herokuapp.com/ambient_noise_updates', data=data)
print('Posting with', data)
print(response)
