from level1 import db
from datetime import timedelta
import re


class IdiomImporter(object):

    def __init__(self, fp, date, name) -> None:
        super().__init__()
        self.name = name
        self.date = date or date.today()
        self.fp = fp
        # example: S9E10, S3
        self.title_patten_re = re.compile(r'S\d+(E\d+)?')

    def process(self):
        cur = db.get_cursor()
        title = ''
        count = 0
        date = self.date
        for line in self.fp:
            # print(line)
            line = line.strip()
            if not line:
                continue

            if self._is_title(line):
                if count:
                    print('Added %s idioms for %s learnt from %s on %s' % (count, title, self.name, date))
                    date -= timedelta(days=1)
                    count = 0
                title = line
                continue

            try:
                self._add_idiom(cur, date, line, title)
                count += 1
            except db.IntegrityError:
                print('Duplicate: %s' % line)

        if count:
            print('Added %s idioms for %s learnt from %s on %s' % (count, title, self.name, date))

    def _add_idiom(self, cur, date, line, title):
        cur.execute(
            """
            INSERT INTO level1_idioms(idiom, title, name, learnt_date, last_updated)
            VALUES (%s, %s, %s, %s, NOW())
            """, (line, title, self.name, date)
        )

    def _is_title(self, line):
        return self.title_patten_re.match(line)