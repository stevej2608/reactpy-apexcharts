from typing import List, Tuple
from datetime import datetime as dt
import random
from reactpy import component, html, run
from utils.logger import log, logging
from reactpy_apexcharts import ApexChart

DATE = dt(2017, 2, 11)

# https://apexcharts.com/javascript-chart-demos/line-charts/syncing-charts/

def time_series(date: dt, count: int, yrange: dict) -> List[Tuple[int, float]]:
    baseval: float = date.timestamp() * 1000
    series: List[Tuple[int, float]] = []
    i = 0
    while i < count:
        x = baseval
        y = random.randint(yrange["min"], yrange["max"])
        series.append((int(x), y))
        baseval += 86400000
        i += 1

    return series

options = {
    "series": [{"data": time_series(DATE, 20, {"min": 10, "max": 60})}],
    "chart": {"id": "fb", "group": "social", "type": "line", "height": 160},
    "xaxis": {'type': 'datetime'},
    "colors": ["#008FFB"],
}

optionsLine2 = {
    "series": [{"data": time_series(DATE, 20, {"min": 10, "max": 30})}],
    "chart": {"id": "tw", "group": "social", "type": "line", "height": 160},
    "xaxis": {'type': 'datetime'},
    "colors": ["#546E7A"],
}

optionsArea = {
    "series": [{"data": time_series(DATE, 20, {"min": 10, "max": 60})}],
    "chart": {"id": "yt","group": "social","type": "area","height": 160},
    "xaxis": {'type': 'datetime'},
    "colors": ["#00E396"]
}


@component
def CustomChart(options):
    return  html.div({'style': {'min-height': '175px'}},
        ApexChart(options=options),
    )

@component
def AppMain():
    return html.div(
        CustomChart(options=options),
        CustomChart(options=optionsLine2),
        CustomChart(options=optionsArea),
    )


# python -m examples.syncing_chart

if __name__ == "__main__":
    log.setLevel(logging.INFO)
    run(AppMain)
