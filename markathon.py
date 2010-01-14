from functools import partial


class Markathon(dict):
    def __init__(self, tag='', *content, **attr):
        self.tag = tag
        self.content = content
        self.update(attr)

    def __call__(self, *content, **attr):
        self.content += content
        self.update(attr)
        return self

    def __str__(self):
        content_string = str().join(str(element) for element in self.content)
        attr_string = str().join(' %s="%s"' % (key.strip('_'), value)
                                           for key, value in self.iteritems())
        if not self.content:
            return "<%s%s />" % (self.tag, attr_string)
        else:
            return "<%s%s>%s</%s>" % (
                              self.tag, attr_string, content_string, self.tag)

    __repr__ = __str__


DOCTYPE = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"'
                      '"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n'

TAGS = """a abbr acronym address area b base bdo big blockquote body br button
caption cite code col colgroup dd del dfn div dl dt em fieldset form h1 h2 h3
h4 h5 h6 head hr html i img input ins kbd label legend li link map meta
noscript object ol optgroup option p param pre q rb rbc rp rt rtc ruby samp
script select small span strong style sub sup table tbody td textarea tfoot th
thead title tr tt ul var""".split()

def register_tags(globals, tags):
    for tag in tags:
        globals[tag] = partial(Markathon, tag.strip('_'))

register_tags(globals(), TAGS)
