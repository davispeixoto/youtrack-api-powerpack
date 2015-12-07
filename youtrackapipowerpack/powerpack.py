# coding=utf-8

import argparse
from youtrackapipowerpack import __version__
from youtrackapipowerpack.powerpackapi import PowerPackApi

__author__ = 'davis.peixoto'


def main():
    parser = get_powerpack_arg_parser()
    args = parser.parse_args()
    power_pack_api = PowerPackApi(args)


def get_powerpack_arg_parser():
    parser = argparse.ArgumentParser(description='powerpack')
    parser.add_argument('action', nargs='+', help='The action to take (e.g. deploy')
    parser.add_argument('--version', action='version', version='%(prog)s ' + __version__)
    return parser


if __name__ == "__main__":
    main()
