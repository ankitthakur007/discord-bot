# -*- coding: utf-8 -*-
"""
Created on Sat May 29 13:04:27 2021

@author: Akhil
"""

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am alive!"

def run():
  app.run(host= '0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()