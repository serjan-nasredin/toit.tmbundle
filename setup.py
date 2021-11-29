#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# :Author: snxx
# :Copyright: (c) 2021 snxx
# For license and copyright information please follow this like:
# https://github.com/snxx-lppxx/toit-sublime/blob/master/LICENSE
''' GitHub:                          snxx-lppxx/toit-sublime '''

from .script import *

import os, sys, json
import sublime
import sublime_plugin


if sys.version_info < (3, 3):
	raise RuntimeError("Toit syntax works with (only) Sublime Text 3")

def plugin_loaded():
