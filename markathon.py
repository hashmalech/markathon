from functools import partial

# XHTML tags. Should go to a more appropriate location.
TAGS = """a abbr acronym address area b base bdo big blockquote body br button
caption cite code col colgroup dd del dfn div dl dt em fieldset form h1 h2 h3
h4 h5 h6 head hr html i img input ins kbd label legend li link map meta
noscript object ol optgroup option p param pre q rb rbc rp rt rtc ruby samp
script select small span strong style sub sup table tbody td textarea tfoot th
thead title tr tt ul var""".split()


class Markathon(dict, basestring):
    def __init__(self, tag='', *body, **attr):
        self.tag = tag
        self.body = body
        self.update(attr)

    def __call__(self, *body, **attr):
        self.update(attr)
        self.body += body
        return self

    def __add__(self, other):
        return str(self) + str(other)

    def __str__(self):
        tag = self.tag
        bt = self.get_dtd() or '' # before tag
        at = '' # after tag
        body = ''.join(str(element) for element in self.body)
        attr = ''.join(' %s="%s"' % (key.strip('_'), value)
                        for key, value in self.iteritems())
        if not self.body and tag != 'script':
            return "<%(tag)s%(attr)s />" % locals()
        return "%(bt)s<%(tag)s%(attr)s>%(body)s</%(tag)s>%(at)s" % locals()

    __repr__ = __str__

    def get_dtd(self):
        if self.tag == 'html':
            return ('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"'
                    ' "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n')


def register_tags(globals, tags):
    for tag in tags:
        globals[tag] = partial(Markathon, tag.strip('_'))

register_tags(globals(), TAGS)


if __name__ == '__main__':
    print Markathon('html', xmlns="http://www.w3.org/1999/xhtml")(
        head(
            meta(content='application/xhtml+xml;charset=utf-8'),
            title("Holy smokes!")
        ),
        body(
            img(src="test.img", alt="just a test"),
            h1(_class="Chunk")("Grail"),
            p("lorem")
        )
    )
