# -*- coding: utf-8 -*-
"""Example Master Contoller with RPyC API."""
import random
import json

import rpyc
from rpyc.utils.server import ThreadedServer

class MasterControllerService(rpyc.Service):
    """RPyC service for the Master Controller."""

    states = ['OFF', 'INIT', 'STANDBY', 'ON', 'DISABLE', 'FAULT', 'ALARM',
              'UNKNOWN']

    def __init__(self, *args):
        """Constructor."""
        super().__init__(*args)

    def on_connect(self):
        """Called when connection is established."""
        print('Client connected!')

    def on_disconnect(self):
        """Called after service disconnects (for cleanup)"""
        print('Client disconnected!')

    def exposed_get_state(self):
        """Return the SDP state."""
        return json.dumps(dict(state=random.choice(self.states)), indent=2)

    def exposed_set_state(self, state):
        """Sets the SDP state."""
        return json.dumps(dict(message='Triggered state: {}'.format(state)),
                          indent=2)


def main():
    """Master Controller main function."""
    server = ThreadedServer(MasterControllerService, port=5000)
    server.start()


if __name__ == "__main__":
    main()
