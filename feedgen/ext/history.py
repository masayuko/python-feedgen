# -*- coding: utf-8 -*-

# Copyright © 2015  IGARASHI Masanao

# Permission is hereby granted, free of charge, to any
# person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the
# Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the
# Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from feedgen.ext.base import BaseExtension

HISTORY_NS = 'http://purl.org/syndication/history/1.0'

class HistoryExtension(BaseExtension):

    def __init__(self):
        self._history_complete = False
        self._history_archive = False

    def extend_ns(self):
        return {'fh': HISTORY_NS}

    def _extend_xml(self, xml_elem):
        if self._history_complete:
            complete = etree.SubElement(xml_elem,'{%s}complete' % (HISTORY_NS,))
        if self._history_archive:
            archive = etree.SubElement(xml_elem,'{%s}archive' % (HISTORY_NS,))
        return xml_elem

    def history_complete(self, value=True):
        self._history_complete = value
        return value

    def history_archive(self, value=True):
        self._history_archive = value
        return value

    def extend_atom(self, atom_feed):
        self._extend_xml(atom_feed)
        return atom_feed

    def extend_rss(self, rss_feed):
        channel = rss_feed[0]
        self._extend_xml(channel)
        return rss_feed

class HistoryEntryExtension(BaseExtension):
    pass
