# -*- coding: utf-8 -*-
"""Docker health check client script.

See: https://docs.docker.com/engine/reference/builder/#healthcheck

- exit state of 0 == healthy
- exit state of 1 == un-healthy
"""
import sys
import rpyc

if __name__ == '__main__':
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    try:
        CONNECTION = rpyc.connect(HOST, PORT)
        STATE = CONNECTION.root.get_state()
    except ConnectionRefusedError as error:
        sys.exit(1)
