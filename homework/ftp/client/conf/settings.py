#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: vita
import os
import logging
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_LEVEL = logging.INFO
LOG_TYPES = {
    "client_log": "%s/log/server_log" % BASE_DIR
     }