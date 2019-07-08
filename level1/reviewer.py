from level1 import db


class Reviewer(object):
    DEFAULT_NUMBER = 30

    def __init__(self, number, commit):
        super().__init__()
        self.commit = commit or False
        self.number = number or self.DEFAULT_NUMBER

    def review(self):
        idioms = self._load_to_review()
        ids =[]
        count = 0
        for idiom in idioms:
            count += 1
            print("            %s: %s" % (count, idiom[1]))
            ids.append(idiom[0])
        if self.commit and ids:
            self._commit_review(ids)

    def _load_to_review(self):
        cur = db.get_cursor()
        cur.execute('SELECT id, idiom FROM level1_idioms ORDER BY learnt_count, learnt_date LIMIT %s', (self.number,))
        return cur.fetchall()

    def _commit_review(self, ids):
        cur = db.get_cursor()
        cur.execute('UPDATE level1_idioms SET learnt_count=learnt_count+1, last_updated=NOW() WHERE id IN (%s)' %
                    ','.join([str(id) for id in ids]))