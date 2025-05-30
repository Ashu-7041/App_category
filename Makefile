# Variables
BLACK = black
BLACK_OPTIONS = 
CHECK = flake8
# Define variables
# SONAR_SCANNER=sonar-scanner
# SONAR_PROJECT=sonar-project.properties
# SONAR_DEBUG=-X  # Add -X for debug logs (optional)

# Run SonarScanner
# .PHONY: sonar
# sonar:
# 	$(SONAR_SCANNER) -Dproject.settings=$(SONAR_PROJECT) $(SONAR_DEBUG)

# Clean previous reports (optional target)
# .PHONY: clean
# clean:
# 	rm -rf .scannerwork

# Format the code using Black
format:
	$(BLACK) $(BLACK_OPTIONS) .

# Check if the code is formatted correctly
check:
	$(BLACK) --check $(BLACK_OPTIONS) .
 
# Automatically fix any code style issues using Black
reformat: 
	$(BLACK) --line-length 120 $(BLACK_OPTIONS)

# Run checks with flake8 (or you can change this to another linter)
lint:
	$(CHECK)
# Help message
help:
	@echo "Makefile commands:"
	@echo "  format     - Format the code using Black"
	@echo "  check      - Check if the code is formatted (without modifying files)"
	@echo "  reformat   - Reformat the code (can be used for fixing code style)"
	@echo "  lint       - Run linting with flake8"
	@echo "  help       - Show this message"

# Default target (can be executed with `make` without arguments)
# .DEFAULT_GOAL := lint