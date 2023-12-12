from reactpy import component, html, run, use_state
from utils.logger import log, logging
from rectpy_apexcharts.example import ExampleCounter

@component
def AppMain():

    count, set_count = use_state(0)

    log.info('count = %d', count)

    return html.div(

        ExampleCounter(
            on_count_change = lambda event: set_count(count+1),
            button_text="this is a test",
            button_id="test-button",
            count = count
        )
    )

# python -m examples.example

if __name__ == "__main__":
    log.setLevel(logging.INFO)
    run(AppMain)
