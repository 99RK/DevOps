# Variables
PYTHON = python
PIP = pip
SRC_DIR = src
TEST_DIR = tests
VENV_DIR = venv
REQ_FILE = requirements.txt
ENTRY_POINT = code.py  # Change this to the main file of your project

# Default target
all: install test build

# Install dependencies
install:
	@echo "Creating virtual environment and installing dependencies..."
	$(PIP) install virtualenv
	virtualenv $(VENV_DIR)
	$(VENV_DIR)/Scripts/$(PIP) install -r $(REQ_FILE)

# Run the application
run:
	@echo "Running the application..."
	$(PYTHON) $(ENTRY_POINT)

# Run tests
test:
	@echo "Running unit tests..."
	$(PYTHON) -m unittest discover -s $(TEST_DIR) -p '*_test.py'

# Build step (optional)
build:
	@echo "Creating a deployable package..."
	# Zip the project files or create a dist folder for packaging
	zip -r build.zip $(SRC_DIR) $(TEST_DIR) $(ENTRY_POINT) $(REQ_FILE)

# Clean up (optional)
clean:
	@echo "Cleaning up..."
	rm -rf $(VENV_DIR)
	rm -f build.zip

# Run linter (optional)
lint:
	@echo "Checking code with linter..."
	$(PYTHON) -m flake8 $(SRC_DIR)

# Help
help:
	@echo "Makefile commands:"
	@echo "  make all       - Install dependencies, run tests, and build"
	@echo "  make install   - Install dependencies"
	@echo "  make run       - Run the application"
	@echo "  make test      - Run unit tests"
	@echo "  make build     - Create a deployable package"
	@echo "  make clean     - Clean up"
	@echo "  make lint      - Lint the code"
