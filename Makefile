.PHONY: venv
venv:
	python3 -m venv venv	

.PHONY: test
test: venv
	. venv/bin/activate && pip3 install tox && tox

.PHONY: clean
clean:
	rm -rf venv .tox
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

