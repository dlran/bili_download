import sys
import os
import argparse
from .__init__ import download
from .__version__ import __version__

def main():
    parser = argparse.ArgumentParser(description = 'oo', usage=".py [options...] [args] bvid")
    parser.add_argument('bvid', type=str, help="video bvid")
    parser.add_argument('-t', '--threads', type=int, help='max workers threads')
    parser.add_argument('-d', '--dest', type=str, help='output destination')
    parser.add_argument('-o', '--output', type=str, help='output filename')
    parser.add_argument('-v', '--version', action='version', version=__version__)
    parser.add_argument('-f', '--force', action='store_true', help="force override")
    argv = sys.argv
    args = parser.parse_args()
    if len(argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    download(bvid=args.bvid, threads=args.threads, output=args.output, dest=args.dest, force=args.force)

if __name__ == '__main__':
    main()
