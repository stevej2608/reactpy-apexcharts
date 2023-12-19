## Building

    poetry install --no-root

    cd js
    npm install
    npm run build

### Debugging

Python VSCODE launch configurations are provided for each of the 
examples and for the pytest tests.

Javascript VSCODE launch configuration is provided for debugging the
browser code. For this to work the test application needs to be 
started with the env variable **REACTPY_DEBUG_MODE** set prior to 
running the application:

    export REACTPY_DEBUG_MODE=1 
    python -m examples.single

Select the launch configuration **3. Launch Chrome**. You will
now be able to set breakpoints from withing VSCODE. The javascript
source code is in **./js/src/*.js**

## Testing

    playwright install

*Then:*

    pytest [--headed]

## Publish 

    rm -rf dist && poetry build
    poetry publish

Or publish to local repo

    poetry publish -r pypicloud
