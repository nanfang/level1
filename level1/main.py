import argparse
from dateutil import parser as date_parser
from level1.importer import IdiomImporter


def _import(**kwargs):
    importer = IdiomImporter(
        open(kwargs['file']),
        date_parser.parse(kwargs['date']).date(),
        kwargs['name'])
    importer.process()


def _review(**kwargs):
    print('review')
    print(kwargs)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='subparser')
    # parse import
    parser_import = subparser.add_parser('import')
    parser_import.add_argument('-f', '--file', dest='file', required=True, help='File to import')
    parser_import.add_argument('-d', '--date', dest='date', required=True, help='Date to import')
    parser_import.add_argument('-n', '--name', dest='name', required=True, help='Name to import')

    # parse show
    parser_show = subparser.add_parser('review')

    kwargs = vars(parser.parse_args())
    globals()['_' + kwargs.pop('subparser')](**kwargs)
