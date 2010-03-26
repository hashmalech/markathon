from functools import partial


class Markathon(dict):
    """To be done."""
    def __init__(self, tag, *body, **attr):
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
        body = ''.join(unicode(element) for element in self.body)
        attr = ''.join(' %s="%s"' % (key.strip('_'), value)
                        for key, value in self.iteritems())
        if not self.body and tag != 'script':
            return "%(bt)s<%(tag)s%(attr)s/>%(at)s" % locals()
        return "%(bt)s<%(tag)s%(attr)s>%(body)s</%(tag)s>%(at)s" % locals()

    __repr__ = __str__

    def before(self):
        """What this class method returns is added before any tag. Returns
        `None` by default. `before` can be overwritten when defining your own
        language inheriting from `Markathon`.

        Example from `markathon.xhtml`:

        >>> class XHTML(Markathon):
        ...     def before(self):
        ...     if self.tag == 'html':
        ...         return ('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 '
        ...         'Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/'
        ...         'xhtml1-strict.dtd">')

        Then, when defining and using the `html` tag, the doctype will be
        added just before it."""
        pass

    def after(self):
        """Class method, same as `Markathon.before`, but what it returns is
        added *after* a tag."""
        pass

    @classmethod
    def register_tags(cls, globals, tags):
        """Register multiple tags at once. `globals()` must be provided as
        first argument, followed by a list of strings to be registered.
        Registered tags can then be used as global variables.

        >>> tags = ['a', 'b', 'c']
        >>> Markathon.register_tags(globals(), tags)

        >>> a('hello') # => <a>hello</a>
        >>> b(c(attr='world')) # => <b><c attr="world"/></b>"""
        for tag in tags: cls.register_tag(globals, tag)

    @classmethod
    def register_tag(cls, globals, tag, **k):
        """Register a single tag. `globals()` must be provided as first
        argument, followed by a tag name (as a string). Optional kwargs can be
        provided as well to be user as tag attributes.

        >>> Markathon.register_tag(globals(), 'a', href="#")
        >>> a('link') # => <a href="#">link</a>"""
        globals[tag] = partial(cls, tag.strip('_'), **k)

