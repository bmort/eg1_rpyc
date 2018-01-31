# Example Master Controller with RPyC API

Example Master Controller with a **very simple** RPyC API.

## References

- <https://rpyc.readthedocs.io>

## Quickstart

Set up virtualenv:

```bash
pip install virtualenv
virtualenv -p python3 venv
. venv/bin/activate
pip install -r master_controller/requirements.txt
```

There are not yet any unit test to run as this is a little tricky with
RPyC! (need a test server running inside the test).

Run the Master Controller natively on localhost using the RPyC built-in
ThreadedServer class (note other servers including one based on gevent are
reportedly available, see: <https://rpyc.readthedocs.io/en/latest/api/utils_server.html#rpyc.utils.server.Server>):

```bash
python3 master_controller/app.py
```

In order to Test the RPyC Server a test CLI client is provided which can be
run using


```bash
python3 master_controller/cli_client.py
```

Now lets build the Docker image.

```bash
docker-compose build
```

And run a Docker container on the local Docker engine

```bash
docker-compose up -d
```

And to stop and clean up

```bash
docker-compose rm -s -f
```

Run as a Docker Swarm service stack

```bash
docker stack deploy -c docker-compose.yml sip
```

Clean up

```bash
docker stack rm sip
```
