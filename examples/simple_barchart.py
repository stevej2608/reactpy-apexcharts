from reactpy import component, html
from utils.logger import log, logging
from reactpy_apexcharts.chart import ApexChart

from utils.fast_server import run

# https://apexcharts.com/docs/react-charts/

@component
def BatChart():
    return html.div(
        ApexChart(
            chart_type="bar",
            width=500,
            height=320,
            options = {
                'chart': {'id': 'apex-chart-example'},
                'xaxis': {
                'categories': [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]}
            },

            series = [{
                'name': 'series-1',
                'data': [30, 40, 35, 50, 49, 60, 70, 91, 125]
            }]
        )
    )


@component
def AppMain():
    return html.div({"class_name": "container grid"}, html.section(BatChart()))


# python -m examples.simple_barchart

if __name__ == "__main__":
    log.setLevel(logging.INFO)
    run(AppMain)
