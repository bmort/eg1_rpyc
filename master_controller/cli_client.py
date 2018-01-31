# -*- coding: utf-8 -*-
"""CLI client for the RPyC Master Controller."""
import argparse

import rpyc


class MasterControllerClient:
    """RPyC client for the SDP Master Controller."""

    def __init__(self, host, port):
        """Create client.

        Args:
            host (str): Master Controllre RPyC Server host
            port (int): Master Controllre RPyC Server port
        """
        try:
            self._connection = rpyc.connect(host, port)
        except ConnectionRefusedError as error:
            self._connection = None
            print('ERROR: RPyC Connection error (%s)' % error)

    def command(self, command, *args):
        """Issue a command to the Master Controller"""
        commands = {
            'get_state': self.get_state,
            'set_state': self.set_state
        }
        if self._connection is None:
            return
        if command not in commands:
            print('ERROR: Unknown command: "%s".')
            return
        commands[command](*args)

    def get_state(self):
        """Print the Master Controller state."""
        print(self._connection.root.get_state())

    def set_state(self, state):
        """Sets the Master Controller state."""
        print(self._connection.root.set_state(state))

def main():
    """Main function."""
    parser = argparse.ArgumentParser(description='Master Controller CLI')
    parser.add_argument('--host', nargs='?', default='localhost', type=str,
                        help='Master Controller RPyC server host '
                             '(default=localhost).')
    parser.add_argument('--port', nargs='?', default=5000, type=int,
                        help='Master Controller RPyC server port '
                             '(default=5000).')
    parser.add_argument('COMMAND', choices=['get_state',
                                            'set_state'],
                        help='Command to run.')
    parser.add_argument('ARGS', help='Command args.', nargs='*')

    args = parser.parse_args()

    client = MasterControllerClient(host=args.host, port=args.port)
    client.command(args.COMMAND, *args.ARGS)

if __name__ == '__main__':
    main()
