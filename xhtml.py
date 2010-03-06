from markathon import Markathon

TAGS = """a abbr acronym address area b base bdo big blockquote body br button
caption cite code col colgroup dd del dfn div dl dt em fieldset form h1 h2 h3
h4 h5 h6 head hr html i img input ins kbd label legend li link map meta
noscript object ol optgroup option p param pre q rb rbc rp rt rtc ruby samp
script select small span strong style sub sup table tbody td textarea tfoot th
thead title tr tt ul var""".split()

DTD = ('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"'
       ' "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n')


class XHTML(Markathon):
    def before(self):
        if self.tag == 'html': return DTD


XHTML.register_tags(globals(), TAGS)
html = html(xmlns="http://www.w3.org/1999/xhtml")


if __name__ == '__main__':
    print html(
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
