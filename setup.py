#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# :Author: snxx
# :Copyright: (c) 2021 snxx
# For license and copyright information please follow this like:
# https://github.com/snxx-lppxx/toit-sublime/blob/master/LICENSE
''' GitHub:                          snxx-lppxx/toit-sublime '''

from threading import Lock

from .script import *

import os, sys, json
import sublime
import sublime_plugin


if sys.version_info < (3, 3):
	raise RuntimeError("Toit syntax works with (only) Sublime Text 3")

class Build(sublime_plugin.WindowCommand):

	encoding = 'utf-8'
	killed = False
	proc = None
	panel = None
	panel_lock = Lock()

	def is_enabled(self, lint=False, integration=False, kill=False):
		if kill:
			return self.proc is not None and self.proc.poll() is None
		return True

	def run(self, lint=False, integration=False, kill=False):
		if kill:
			if self.proc:
				self.killed = True
				self.proc.terminate()
			return

		var = self.window.extract_variables()
		working_dir = var['file_path']

		with self.panel_lock:
			self.panel = self.window.create_output_panel('exec')

			settings = self.panel.settings()
			settings.set(
				'result_line_regex',
				r'^\sline (\d+) col (\d+)'
			)
