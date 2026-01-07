## Development Setup

The cookiecutter creates a simple button component that can be used as a starting point 
for your component development.

```bash
cd reactpy-apexcharts
```
Then run the tests. This will confirm the initial cookiecutter example works and 
also setup the virtual environment for you to develop your code.

    hatch test --headless

## Building

    hatch build --clean


## VSCODE Support

Running 'hatch test' creates the venv '.venv/hatch-test.py3.11'. The VSCODE settings.json
is configured to use this env for development and debugging. You may need to run the
VSCODE command **Developer: Reload Window** for the settings to take effect.

### Debugging

Launch scripts are available to debug:

- /examples/button_example.py
- /tests/test_button.py 

Python VSCODE launch configurations are provided for each of the 
examples and for the pytest tests.

Javascript VSCODE launch configuration is provided 
for debugging the browser code. 

Build the development version of the browser code and run the 
ReactPy example:

    hatch run javascript:build-dev && python -m examples.button_example


Then, select the launch configuration **3a. Launch Chrome**. You will
now be able to set breakpoints from withing VSCODE.


## Publish 

    hatch build --clean

    hatch publish

Or publish to local repo

    hatch publish -r pypicloud
