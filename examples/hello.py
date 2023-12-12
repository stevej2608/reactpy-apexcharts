from reactpy import component, html, run
from utils.logger import log, logging


GREETING = 'Hello, World!'

@component
def AppMain():
    element = html.h2(GREETING)
    return html.div(
        element
    )

# python -m examples.hello

if __name__ == "__main__":
    log.setLevel(logging.INFO)
    run(AppMain)
