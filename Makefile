# Makefile

.PHONY: clean

default: dev

dev: venv/bin/activate
	. venv/bin/activate && ./cba_server.py

prod: venv/bin/activate
	. venv/bin/activate && CBA_PRODUCTION=1 nohup ./cba_server.py script args >stdout.log 2>stderr.log&

venv venv/bin/activate: requirements.txt clean
	test -d venv || virtualenv venv --no-site-packages
	. venv/bin/activate && pip install -r requirements.txt

clean:
	find . -type f -name "*.pyc" -delete
