# -*- coding: utf-8 -*-
__version__ = '0.1'
from flask import Flask

app = Flask('app')
app.config.from_pyfile('../config.cfg')

from app.controllers import *
