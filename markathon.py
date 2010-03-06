from functools import partial


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
        bt = self.before() or '' # before tag
        at = self.after() or '' # after tag
        body = ''.join(str(element) for element in self.body)
        attr = ''.join(' %s="%s"' % (key.strip('_'), value)
                        for key, value in self.iteritems())
        if not self.body and tag != 'script':
            return "<%(tag)s%(attr)s />" % locals()
        return "%(bt)s<%(tag)s%(attr)s>%(body)s</%(tag)s>%(at)s" % locals()

    __repr__ = __str__

    def before(self): pass
    def after(self): pass

    @classmethod
    def register_tags(self, globals, tags):
        for tag in tags:
            globals[tag] = partial(self, tag.strip('_'))
