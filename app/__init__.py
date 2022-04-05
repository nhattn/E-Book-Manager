# -*- coding: utf-8 -*-

import os
from flask import Flask

engine = Flask(__name__)

ABSPATH = os.path.dirname(__file__)

engine.config["JSON_AS_ASCII"] = False
engine.config["JSONIFY_PRETTYPRINT_REGULAR"] = False
engine.config["DEBUG"] = True
engine.config["ENV"] = "production"
engine.config["PORT"] = 8650

RANDOM_UID = 0

from .views import *
