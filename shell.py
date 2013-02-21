#!/usr/bin/env python
import os
import readline
from pprint import pprint

from flask import *
from app import *
from app.users.models import *
from app.facebook.models import *
from app.twitter import constants as CONSTANTS 

import tweepy

os.environ['PYTHONINSPECT'] = 'True'
