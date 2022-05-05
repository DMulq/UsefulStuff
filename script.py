#!/usr/bin/env python

import requests as req

resp = req.post("https://gwapi.fcdo.missionlabs.co.uk/stats/query")

print(resp.text)