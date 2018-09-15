# encoding: utf-8

###########################################################################################################
#
#
#	Filter without dialog Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Filter%20without%20Dialog
#
#
###########################################################################################################

import objc
from GlyphsApp import *
from GlyphsApp.plugins import *

class MakeBoxes(FilterWithoutDialog):
	
	def settings(self):
		self.menuName = Glyphs.localize({
			'en': u'Make Boxes',
			'de': u'Kastln machen',
		})
		self.keyboardShortcut = None # With Cmd+Shift

	def filter(self, layer, inEditView, customParameters):
		pathPoints = (
			NSPoint( 0.0,         layer.master.descender ),
			NSPoint( layer.width, layer.master.descender ),
			NSPoint( layer.width, layer.master.ascender ),
			NSPoint( 0.0,         layer.master.ascender ),
		)

		box = GSPath()
		for pointPosition in pathPoints:
			newNode = GSNode()
			newNode.position = pointPosition
			box.nodes.append( newNode )
		box.closed = True
		
		layer.clear()
		layer.paths.append(box)
	
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
	