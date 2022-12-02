env:
	python -m venv ~/.venv

active:
	source ~/.venv/bin/activate

install:
	pip install --upgrade pip\
		pip install -r requirements.txt

