# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 20:05:20 2024

@author: janra
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

import os

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)