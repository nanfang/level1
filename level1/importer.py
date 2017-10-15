
class IdiomImporter(object):

    def __init__(self, fp, date, name) -> None:
        super().__init__()
        self.name = name
        self.date = date
        self.fp = fp

    def process(self):
        print(self.date)
        for line in self.fp:
            print(line)