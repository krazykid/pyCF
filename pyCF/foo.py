#!/usr/local/bin/python

from networkACL import networkACL
from complexEncoder import complexEncoder
import json

def main():
    n = networkACL('netACL1', 'abce', {'a': 'b'})
    jsonStr = json.dumps(n, cls=complexEncoder, indent=4)
    print jsonStr


if __name__ == '__main__':
    main()
