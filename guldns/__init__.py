#! /usr/bin/env python3
__version__ = '0.0.1'
import argparse
from .device import get, get_hosts, get_external_addr, generate, generate_device

def main():
    parser = argparse.ArgumentParser('gns')
    parser.add_argument("command", type=str, default="get", choices=["get", "get_hosts", "gen_device", "gen"])
    parser.add_argument("-n", '--name', type=str, help="The full or top level name to use.")
    parser.add_argument('-x', '--include-external', dest='incex', action='store_true', help="Include external IP address as reported by ipify.")
    parser.add_argument('-X', '--exclude-external', dest='incex', action='store_false', help="Exclude external IP address.")
    parser.set_defaults(incex=True)
    args = parser.parse_args()
    if args.command == 'get':
        print('\n'.join(get(args.name)))
    elif args.command == 'get_hosts':
        print('\n'.join(get_hosts(args.name)))
    elif args.command == 'gen':
        print(generate())
    elif args.command == 'gen_device':
        print(generate_device(args.incex))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
