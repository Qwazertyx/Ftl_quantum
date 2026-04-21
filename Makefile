.PHONY: all setup install run clean

all: setup install

setup:
	python3 -m venv venv
	. venv/bin/activate

install: 
	. venv/bin/activate && \
	pip install qiskit && \
	pip install matplotlib && \
	pip install qiskit[visualization]

run:
	. venv/bin/activate && \
	python3 exercises/main.py

clean:
	rm -rf venv