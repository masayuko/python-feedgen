# -*- coding: utf-8 -*-
'''
	feedgen.util
	~~~~~~~~~~~~

	This file contains helper functions for the feed generator module.

	:copyright: 2013, Lars Kiesow <lkiesow@uos.de>
	:license: FreeBSD and LGPL, see license.* for more details.
'''
import sys
from lxml import etree


def ensure_format(val, allowed, required, allowed_values=None, defaults=None):
	'''Takes a dictionary or a list of dictionaries and check if all keys are in
	the set of allowed keys, if all required keys are present and if the values
	of a specific key are ok.

	:param val:            Dictionaries to check.
	:param allowed:        Set of allowed keys.
	:param required:       Set of required keys.
	:param allowed_values: Dictionary with keys and sets of their allowed values.
	:param defaults:       Dictionary with default values.
	:returns:              List of checked dictionaries.
	'''
	if not val:
		return None
	if allowed_values is None:
		allowed_values = {}
	if defaults is None:
		defaults = {}
	# Make shure that we have a list of dicts. Even if there is only one.
	if not isinstance(val, list):
		val = [val]
	for elem in val:
		if not isinstance(elem, dict):
			raise ValueError('Invalid data (value is no dictionary)')
		# Set default values

		version = sys.version_info[0]

		if version == 2:
			items = defaults.iteritems()
		else:
			items = defaults.items()

		for k,v in items:
			elem[k] = elem.get(k, v)
		if not set(elem.keys()) <= allowed:
			raise ValueError('Data contains invalid keys')
		if not set(elem.keys()) >= required:
			raise ValueError('Data contains not all required keys')

		if version == 2:
			values = allowed_values.iteritems()
		else:
			values = allowed_values.items()

		for k,v in values:
			if elem.get(k) and not elem[k] in v:
				raise ValueError('Invalid value for %s' % k )
	return val


def atom_content(element, text, typ=None, cdata=False):
	if cdata:
		element.text = etree.CDATA(text)
	else:
		# Surround xhtml with a div tag, parse it and embed it
		if typ == 'xhtml':
			content.append(etree.fromstring(
				'<div xmlns="http://www.w3.org/1999/xhtml">%s</div>' % text))
		# Embed the text in escaped form
		elif not typ or typ.startswith('text') or typ == 'html':
			element.text = text
		# Parse XML and embed it
		elif typ.endswith('/xml') or typ.endswith('+xml'):
			element.append(etree.fromstring(text))
		# Everything else should be included base64 encoded
		else:
			raise ValueError(
				'base64 encoded content is not supported at the moment.'
				+ 'If you are interested , please file a bug report.')

	# Add type description of the content
	if typ:
		element.attrib['type'] = typ

	return element
