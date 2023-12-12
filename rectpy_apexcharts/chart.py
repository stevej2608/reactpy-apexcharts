from typing import Literal, Union, List, Dict, Any
from pathlib import Path

from reactpy.web.module import export, module_from_file

ChartType = Literal['line', 'area', 'bar', 'pie', 'donut', 'scatter', 'bubble', 'heatmap', 'radialBar']


_js_module = module_from_file(
    "rectpy-apexcharts",
    file=Path(__file__).parent / "bundle.js",
    fallback="⏳",
)

_RactpyApexCharts = export(_js_module, "RactpyApexCharts")


def Chart(
        chart_type:ChartType,
        width: Union[str,int],
        height: Union[str,int],
        series: List[float],
        options: Dict[str, Any]
        ):

    return _RactpyApexCharts(
        {
            "type": chart_type,
            "width": width,
            "height": height,
            "series": series,
            "options": options,
        }
    )
