.PHONY: run clean

VENV = .venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
FLASK = $(VENV)/bin/flask

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	. $(VENV)/bin/activate
	$(PIP) install -r requirements.txt

venv: clean
	@echo "Creating a new virtual environment..."
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt
	touch $(VENV)/bin/activate
	@echo "Virtual environment rejuvenated."

run: $(VENV)/bin/activate
	$(FLASK) --app app run --host 0.0.0.0 --port 5001

clean:
	rm -rf __pycache__
	rm -rf $(VENV)