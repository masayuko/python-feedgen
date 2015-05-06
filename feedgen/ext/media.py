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

from lxml import etree
from feedgen.ext.base import BaseExtension
from feedgen.util import ensure_format
import sys

version = sys.version_info[0]

MEDIA_NS = 'http://search.yahoo.com/mrss/'

class MediaBaseExtension(BaseExtension):
    """Media RSS Specification"""

    def __init__(self):
        self._media_rating = None
        self._media_title = None
        self._media_description = None
        self._media_keywords = None
        self._media_thumbnail = None
        self._media_category = None
        self._media_hash = None
        self._media_credit = None
        self._media_copyright = None
        self._media_text = None
        self._media_restriction = None
        self._media_community = None
        self._media_comments = None
        #self._media_embed = None
        self._media_responses = None
        self._media_backLinks = None
        self._media_status = None
        self._media_price = None
        self._media_license = None
        self._media_subTitle = None
        self._media_peerLink = None
        #self._media_location = None
        self._media_rights = None
        self._media_scenes = None

    def _extend_xml(self, xml_elem):
        for r in self._media_rating or []:
            rating = etree.SubElement(xml_elem, '{%s}rating' % (MEDIA_NS,))
            rating.text = r['rating']
            if r.get('scheme') is not None:
                rating.attrib['scheme'] = r['scheme']
        if self._media_title is not None:
            title = etree.SubElement(xml_elem, '{%s}title' % (MEDIA_NS,))
            title.text = self._media_title['title']
            if self._media_title.get('type') is not None:
                title.attrib['type'] = self._media_title.get('type')
        if self._media_description is not None:
            description = etree.SubElement(xml_elem,
                                           '{%s}description' % (MEDIA_NS,))
            description.text = self._media_description['description']
            if self._media_description.get('type') is not None:
                description.attrib['type'] = self._media_description.get('type')
        if self._media_keywords is not None:
            keywords = etree.SubElement(xml_elem, '{%s}keywords' % (MEDIA_NS,))
            keywords.text = ','.join(self._media_keywords)
        for t in self._media_thumbnail or []:
            thumbnail = etree.SubElement(xml_elem,'{%s}thumbnail' % (MEDIA_NS,))
            if version == 2:
                items = t.iteritems()
            else:
                items = t.items()
            for k,v in items:
                thumbnail.attrib[k] = v
        for c in self._media_category or []:
            category = etree.SubElement(xml_elem, '{%s}category' % (MEDIA_NS,))
            category.text = c['category']
            if c.get('scheme') is not None:
                category.attrib['scheme'] = c['scheme']
            if c.get('label') is not None:
                category.attrib['label'] = c['label']
        if self._media_hash is not None:
            xhash = etree.SubElement(xml_elem, '{%s}hash' % (MEDIA_NS,))
            xhash.text = self._media_hash['hash']
            if self._media_hash.get('algo') is not None:
                xhash.attrib['algo'] = self._media_hash.get('algo')
        for c in self._media_credit or []:
            credit = etree.SubElement(xml_elem, '{%s}credit' % (MEDIA_NS,))
            credit.text = c['credit']
            if c.get('role') is not None:
                credit.attrib['role'] = c['role']
            if c.get('scheme') is not None:
                credit.attrib['scheme'] = c['scheme']
        if self._media_copyright is not None:
            xcopyright = etree.SubElement(
                xml_elem, '{%s}copyright' % (MEDIA_NS,))
            xcopyright.text = self._media_copyright['copyright']
            if self._media_copyright.get('url') is not None:
                xcopyright.attrib['url'] = self._media_copyright.get('url')
        for t in self._media_text or []:
            text = etree.SubElement(xml_elem, '{%s}text' % (MEDIA_NS,))
            text.text = t['text']
            if t.get('type') is not None and t.get('type') != 'plain':
                text.attrib['type'] = t['type']
            if t.get('lang') is not None:
                text.attrib['lang'] = t['lang']
            if t.get('start') is not None:
                text.attrib['start'] = t['start']
            if t.get('end') is not None:
                text.attrib['end'] = t['end']
        for r in self._media_restriction or []:
            restriction = etree.SubElement(xml_elem,
                                           '{%s}restriction' % (MEDIA_NS,))
            if r['restriction'] is not None:
                restriction.text = r['restriction']
            restriction.attrib['relationship'] = r['relationship']
            if r.get('type') is not None:
                restriction.attrib['type'] = r['type']
            else:
                if r['restriction'] != 'all' and r['restriction'] != 'none':
                    raise ValueError(
                        'type attribute is required for media:restiction')
        if self._media_community:
            community = etree.SubElement(xml_elem,'{%s}community' % (MEDIA_NS,))
            if self._media_community.get('starRating'):
                startrating = etree.SubElement(
                    community,'{%s}starRating' % (MEDIA_NS,))
                if self._media_community['starRating'].get('average'):
                    startrating.attrib['average'] = (
                        self._media_community['starRating']['average'])
                if self._media_community['starRating'].get('count'):
                    startrating.attrib['count'] = (
                        self._media_community['starRating']['count'])
                if self._media_community['starRating'].get('min'):
                    startrating.attrib['min'] = (
                        self._media_community['starRating']['min'])
                if self._media_community['starRating'].get('max'):
                    startrating.attrib['max'] = (
                        self._media_community['starRating']['max'])
            if self._media_community.get('statistics'):
                statistics = etree.SubElement(
                    community,'{%s}statistics' % (MEDIA_NS,))
                if self._media_community['statistics'].get('views'):
                    statistics.attrib['views'] = (
                        self._media_community['statistics']['views'])
                if self._media_community['statistics'].get('favorites'):
                    statistics.attrib['favorites'] = (
                        self._media_community['statistics']['favorites'])
            if self._media_community.get('tags'):
                tags = etree.SubElement(community,'{%s}tags' % (MEDIA_NS,))
                tags.text = self._media_community['tags']
        if self._media_comments:
            comments = etree.SubElement(xml_elem, '{%s}comments' % (MEDIA_NS,))
            for c in self._media_comments:
                comment = etree.SubElement(comments,'{%s}comment' % (MEDIA_NS,))
                comment.text = c
        if self._media_responses:
            responses = etree.SubElement(xml_elem,'{%s}responses' % (MEDIA_NS,))
            for r in self._media_responses:
                response = etree.SubElement(responses,
                                            '{%s}response' % (MEDIA_NS,))
                response.text = r
        if self._media_backLinks:
            backLinks = etree.SubElement(xml_elem,'{%s}backLinks' % (MEDIA_NS,))
            for b in self._media_backLinks:
                backLink = etree.SubElement(backLinks,
                                            '{%s}backLink' % (MEDIA_NS,))
                backLink.text = b
        if self._media_status:
            status = etree.SubElement(xml_elem,'{%s}status' % (MEDIA_NS,))
            status.attrib['state'] = self._media_status['state']
            if self._media_status['reason'] is not None:
                status.attrib['reason'] = self._media_status['reason']
        for p in self._media_price or []:
            price = etree.SubElement(xml_elem, '{%s}price' % (MEDIA_NS,))
            price.text = p['price']
            if p['type'] is not None:
                price.attrib['type'] = p['type']
                if p.get('price') is not None:
                    price.attrib['price'] = p['price']
                if p.get('currency') is not None:
                    price.attrib['currency'] = p['currency']
                if p['type'] == 'package' or p['type'] == 'subscription':
                    if p.get('info') is not None:
                        price.attrib['info'] = p['info']
        if self._media_license is not None:
            license = etree.SubElement(xml_elem, '{%s}license' % (MEDIA_NS,))
            license.text = self._media_license['license']
            if self._media_license.get('type') is not None:
                license.attrib['type'] = self._media_license.get('type')
            if self._media_license.get('href') is not None:
                license.attrib['href'] = self._media_license.get('href')
        for s in self._media_subTitle or []:
            subTitle = etree.SubElement(xml_elem, '{%s}subTitle' % (MEDIA_NS,))
            subTitle.text = s['subTitle']
            subTitle.attrib['href'] = s['href']
            if s.get('type') is not None:
                subTitle.attrib['type'] = s['type']
            if s.get('lang') is not None:
                subTitle.attrib['lang'] = s['lang']
        if self._media_peerLink is not None:
            peerLink = etree.SubElement(xml_elem, '{%s}peerLink' % (MEDIA_NS,))
            peerLink.text = self._media_peerLink['peerLink']
            if self._media_peerLink.get('type') is not None:
                peerLink.attrib['type'] = self._media_peerLink.get('type')
            if self._media_peerLink.get('href') is not None:
                peerLink.attrib['href'] = self._media_peerLink.get('href')
        if self._media_rights is not None:
            rights = etree.SubElement(xml_elem, '{%s}rights' % (MEDIA_NS,))
            rights.attrib['status'] = self._media_rights
        if self._media_scenes is not None and len(self._media_scenes):
            scenes = etree.SubElement(xml_elem, '{%s}scenes' % (MEDIA_NS,))
            for s in self._media_scenes or []:
                scene = etree.SubElement(scenes, '{%s}scene' % (MEDIA_NS,))
                sceneTitle = etree.SubElement(
                    scene, '{%s}sceneTitle' % (MEDIA_NS,))
                sceneTitle.text = s['Title']
                sceneDescription = etree.SubElement(
                    scene, '{%s}sceneDescription' % (MEDIA_NS,))
                sceneDescription.text = s['Description']
                sceneStartTime = etree.SubElement(
                    scene, '{%s}sceneStartTime' % (MEDIA_NS,))
                sceneStartTime.text = s['StartTime']
                sceneEndTime = etree.SubElement(
                    scene, '{%s}sceneEndTime' % (MEDIA_NS,))
                sceneEndTime.text = s['EndTime']

        return xml_elem

    def rating(self, rating=None, replace=False, **kwargs):
        if rating is None and kwargs:
            rating = kwargs
        if not rating is None:
            if replace or self._media_rating is None:
                self._media_rating = []
            self._media_rating += ensure_format(
                rating, set(['rating','scheme']), set(['rating']))
        return self._media_rating

    def title(self, title, type=None):
        if title is None:
            self._media_title = None
        else:
            self._media_title = {'title': title}
            if type is not None and type != 'plain' and type != 'html':
                raise ValueError('{0} is invalid for type of media:title'
                                 .format(type))
            if type == 'html':
                self._media_title['type'] = type
        return self._media_title

    def description(self, description, type=None):
        if description is None:
            self._media_description = None
        else:
            self._media_description = {'description': description}
            if type is not None and type != 'plain' and type != 'html':
                raise ValueError('{0} is invalid for type of media:description'
                                 .format(type))
            if type == 'html':
                self._media_description['type'] = type
        return self._media_description

    def keywords(self, keywords):
        if keywords is None:
            self._media_keywords = None
        else:
            if len(keywords) > 10:
                raise ValueError('a maximum of 10 words for media:keywords')
            self._media_keywords = keywords
        return self._media_keywords

    def thumbnail(self, thumbnail=None, replace=False, **kwargs):
        if thumbnail is None and kwargs:
            thumbnail = kwargs
        if not thumbnail is None:
            if replace or self._media_thumbnail is None:
                self._media_thumbnail = []
            self._media_thumbnail += ensure_format(
                thumbnail, set(['url','height','width','time']), set(['url']))
        return self._media_thumbnail

    def category(self, category=None, replace=False, **kwargs):
        if category is None and kwargs:
            category = kwargs
        if not category is None:
            if replace or self._media_category is None:
                self._media_category = []
            self._media_category += ensure_format(
                category, set(['category','scheme','label']), set(['category']))
        return self._media_category

    def xhash(self, xhash, algo=None):
        if xhash is None:
            self._media_hash = None
        else:
            self._media_hash = {'hash': xhash}
            if algo is not None and algo != 'md5' and algo != 'sha-1':
                raise ValueError('{0} is invalid for algo of media:hash'
                                 .format(algo))
            if algo == 'sha-1':
                self._media_hash['algo'] = algo
        return self._media_hash

    def credit(self, credit=None, replace=False, **kwargs):
        if credit is None and kwargs:
            credit = kwargs
        if not credit is None:
            if replace or self._media_credit is None:
                self._media_credit = []
            self._media_credit += ensure_format(
                credit, set(['credit','role','scheme']), set(['credit']))
        return self._media_credit

    def copyright(self, xcopyright, url=None):
        if xcopyright is None:
            self._media_copyright = None
        else:
            self._media_copyright = {'copyright': xcopyright}
            if url is not None:
                self._media_copyright['url'] = url
        return self._media_copyright

    def text(self, text=None, replace=False, **kwargs):
        if text is None and kwargs:
            text = kwargs
        if not text is None:
            if replace or self._media_text is None:
                self._media_text = []
            self._media_text += ensure_format(
                text, set(['text','type','lang','start','end']), set(['text']),
                {'type':['plain','html']})
        return self._media_text

    def restriction(self, restriction=None, replace=False, **kwargs):
        if restriction is None and kwargs:
            restriction = kwargs
        if not restriction is None:
            if replace or self._media_restriction is None:
                self._media_restriction = []
            self._media_restriction += ensure_format(
                restriction, set(['restriction','relationship','type']),
                set(['relationship']),
                {'relationship':['allow','deny'],
                 'type':['country','uri','sharing']})
        return self._media_restriction

    def community(self, average=None, count=None, xmin=None, xmax=None,
                  views=None, favorites=None, tags=None):
        self._media_community = []
        if (average is not None or count is not None or
            xmin is not None or xmax is not None):
            self._media_community.append({'starRating': {}})
            if average is not None:
                self._media_community['starRating']['average'] = average
            if count is not None:
                self._media_community['starRating']['count'] = count
            if xmin is not None:
                self._media_community['starRating']['min'] = xmin
            if xmax is not None:
                self._media_community['starRating']['max'] = xmax
        if views is not None or favorites is not None:
            self._media_communiti.append({'statistics': {}})
            if views is not None:
                self._media_community['statistics']['views'] = views
            if favorites is not None:
                self._media_community['statistics']['favorites'] = favorites
        if tags is not None:
            self._media_communiti.append({'tags': tags})
        return self._media_communiti

    def comments(self, comments):
        self._media_comments = comments
        return self._media_comments

    def responses(self, responses):
        self._media_responses = responses
        return self._media_responses

    def backLinks(self, backLinks):
        self._media_backLinks = backLinks
        return self._media_backLinks

    def status(self, state, reason=None):
        if state is not None:
            if not state in ('active','blocked','deleted'):
                raise ValueError('{0} is invalid for state of media:status'
                                 .format(state))
            self._media_status = {'state': status, 'reason': reason}
        return self._media_status

    def price(self, price=None, replace=False, **kwargs):
        if price is None and kwargs:
            price = kwargs
        if not price is None:
            if replace or self._media_price is None:
                self._media_price = []
            self._media_price += ensure_format(
                price, set(['price','type','info','currency']),
                set(['type']),
                {'type':['rent','purchase','package','subscription',None]})
        return self._media_price

    def license(self, license, type=None, href=None):
        if license is None:
            self._media_license = None
        else:
            self._media_license = {'license': license}
            if type is not None:
                self._media_license['type'] = type
            if href is not None:
                self._media_license['href'] = href
        return self._media_license

    def subTitle(self, subTitle=None, replace=False, **kwargs):
        if subTitle is None and kwargs:
            subTitle = kwargs
        if not subTitle is None:
            if replace or self._media_subTitle is None:
                self._media_subTitle = []
            self._media_subTitle += ensure_format(
                subTitle, set(['subTitle','type','lang','href']),
                set(['subTitle','href']))
        return self._media_subTitle

    def peerLink(self, peerLink, type=None, href=None):
        if peerLink is None:
            self._media_peerLink = None
        else:
            self._media_peerLink = {'peerLink': peerLink}
            if type is not None:
                self._media_peerLink['type'] = type
            if href is not None:
                self._media_peerLink['href'] = href
        return self._media_peerLink

    def rights(self, rights):
        if (rights is not None and
            rights != 'userCreated' and rights != 'official'):
                raise ValueError(
                    '{0} is invalid for status of media:rights'.format(rights))
        self._media_rights = rights
        return self._media_rights

    def scenes(self, scenes=None, replace=False, **kwargs):
        if scenes is None and kwargs:
            scenes = kwargs
        if not scenes is None:
            if replace or self._media_scenes is None:
                self._media_scenes = []
            self._media_scenes += ensure_format(
                scenes, set(['Title','Description','StartTime','EndTime']),
                set(['Title','Description','Starttime','Endtime']))
        return self._media_scenes


class MediaContent(MediaBaseExtension):

    def __init__(self, **attributes):
        super(MediaContent, self).__init__()
        if version == 2:
            items = attributes.iteritems()
        else:
            items = attributes.items()
        for k,v in items:
            if not k in ('url','player','fileSize','type','medium','isDefault',
                         'expression','bitrate','framerate','samplingrate',
                         'channels','duration','height','width','lang'):
                raise ValueError(
                    '{0} is invalid attribute for media:content'.format(k))
        if attributes.get('url') is None and attributes.get('player') is None:
            raise ValueError(
                'url or player is required for a media:content element')
        if attributes.get('url') is None:
            if not isinstance(attributes['player'], dict):
                raise ValueError('player must be dictionary')
            if version == 2:
                items = attributes['player'].iteritems()
            else:
                items = attributes['player'].items()
            for k,v in items:
                if not k in ['url','height','width']:
                    raise ValueError('{0} is invalid attribute for media:player'
                                     .format(k))
            if attributes['player'].get('url') is None:
                raise ValueError(
                    'url attribute is required for a media:player element')
        if (attributes.get('medium') is not None and
            not attributes.get('medium') in
            ('image','audio','video','document','executable')):
            raise ValueError(
                '{0} is invalid for medium attribute of media:content'
                .format(medium))
        if (attributes.get('isDefault') is not None and
            not attributes.get('isDefault') in ('true','false')):
            raise ValueError(
                '{0} is invalid for isDefault attribute of media:content'
                .format(isDefault))
        if (attributes.get('expression') is not None and
            not expression in ('sample','full','nonstop')):
            raise ValueError(
                '{0} is invalid for expression attribute of media:content'
                .format(expression))
        self.attributes = attributes

    def _extend_xml(self, xml_elem):
        node = etree.SubElement(xml_elem, '{%s}content' % (MEDIA_NS,))
        if version == 2:
            items = self.attributes.iteritems()
        else:
            items = self.attributes.items()
        for k,v in items:
            if k == 'player':
                player = etree.SubElement(node, '{%s}player' % (MEDIA_NS,))
                if version == 2:
                    vitems = v.iteritems()
                else:
                    vitems = v.items()
                for pk,pv in vitems:
                    player.attrib[pk] = pv
            else:
                node.attrib[k] = v
        super(MediaContent, self)._extend_xml(node)
        return xml_elem


class MediaGroup(MediaBaseExtension):

    def __init__(self):
        super(MediaGroup, self).__init__()
        self._media_content = []

    def _extend_xml(self, xml_elem):
        node = etree.SubElement(xml_elem, '{%s}group' % (MEDIA_NS,))
        for c in self._media_content:
            c._extend_xml(node)
        super(MediaGroup, self)._extend_xml(node)
        return xml_elem

    def add_content(self, **attributes):
        c = MediaContent(attributes)
        self._media_content.append(c)
        return c


class MediaExtension(MediaBaseExtension):
    """Media RSS Specification"""

    def extend_ns(self):
        return {'media': MEDIA_NS}

    def extend_atom(self, atom_feed):
        self._extend_xml(atom_feed)
        return atom_feed

    def extend_rss(self, rss_feed):
        channel = rss_feed[0]
        self._extend_xml(channel)
        return rss_feed


class MediaEntryExtension(MediaGroup):
    """Media RSS Specification"""

    def __init__(self):
        super(MediaEntryExtension, self).__init__()
        self._media_group = []

    def _extend_xml(self, xml_elem):
        super(MediaGroup, self)._extend_xml(xml_elem)
        for g in self._media_group:
            g._extend_xml(xml_elem)
        return xml_elem

    def extend_atom(self, entry):
        self._extend_xml(entry)
        return entry

    def extend_rss(self, item):
        self._extend_xml(item)
        return item

    def add_group(self):
        g = MediaGroup()
        self._media_group.append(g)
        return g
