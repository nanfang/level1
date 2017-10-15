import argparse
from dateutil import parser as date_parser
from level1.importer import IdiomImporter
from level1.reviewer import Reviewer


def _import(**kwargs):
    importer = IdiomImporter(
        open(kwargs['file']),
        date_parser.parse(kwargs['date']).date(),
        kwargs['name'])
    importer.process()


def _review(**kwargs):
    Reviewer(number=kwargs['number'], commit=kwargs['commit']).review()


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
    parser_show.add_argument('-n', '--number', dest='number', default=30, type=int, help='Number of idioms to review')
    parser_show.add_argument('-c', '--commit', dest='commit', default=False, action='store_true',
                             help='Commit reviewed idioms')

    kwargs = vars(parser.parse_args())
    globals()['_' + kwargs.pop('subparser')](**kwargs)
