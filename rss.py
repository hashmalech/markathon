from markathon import Markathon


TAGS = """author category channel cloud comments copyright description docs
enclosure generator guid height image item language lastBuildDate link
managingEditor name pubDate rating rss skipDays skipHours source textInput
title ttl url webMaster width""".split()

DTD = ('<?xml version="1.0" encoding="iso-8859-1"?>\n')


class RSS(Markathon):
    def before(self):
        if self.tag == 'rss': return DTD


RSS.register_tags(globals(), TAGS)
rss = rss(version="2.0")


if __name__ == '__main__':
    print rss(
        channel(
            title("My Cerulean Blog"),
            description("How to live well, long and rich in the color."),
            lastBuildDate("Sat, 07 Sep 2002 00:00:01 GMT"),
            link("http://www.example.com"),
            item(
                title("First Entry"),
                description("This is an entry!"),
                pubDate("Sat, 07 Sep 2002 00:00:01 GMT"),
                link("http://www.example.com/firstentry")
            )
        )
    )
