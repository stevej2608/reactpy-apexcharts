from typing import Literal, Union, List, Dict, Any, Optional
from os import environ
from pathlib import Path

from reactpy.web.module import export, module_from_file

ChartType = Literal['line', 'area', 'bar', 'pie', 'donut', 'scatter', 'bubble', 'heatmap', 'radialBar']


_js_module = module_from_file(
    "rectpy-apexcharts",
    file=Path(__file__).parent/"bundle.dev.js" if environ.get("REACTPY_DEBUG_MODE") else Path(__file__).parent/"bundle.min.js" ,
    fallback="⏳",
)

_RactpyApexCharts = export(_js_module, "RactpyApexCharts")


def ApexChart(
        chart_type: Optional[ChartType] = None,
        series: Optional[List[float]] = None,
        width: Optional[Union[str,int]] = None,
        height: Optional[Union[str,int]] = None,
        options: Optional[Dict[str, Any]] = None
        ):
    """ Wrapper for react-apexcharts library. For API and examples see:

        https://github.com/apexcharts/react-apexcharts

    Args:
        chart_type (ChartType): _description_
        width (Union[str,int]): _description_
        height (Union[str,int]): _description_
        series (List[float]): _description_
        options (Dict[str, Any]): _description_

    Returns:
        _type_: _description_
    """

    def unpack_option(option_name:str, value, options = {}):
        if not value:
            if option_name in options:
                value = options[option_name]
            else:
                chart = options['chart'] if 'chart' in options else {}
                if option_name in chart:
                    value = chart[option_name]
                else:
                    value = None
        return value


    _args: Dict[str, Any] = {}

    _args['type'] = unpack_option('type', chart_type, options)
    _args['width'] = unpack_option('width', width, options)
    _args['height'] = unpack_option('height', height, options)
    _args['series'] = unpack_option('series', series, options)

    if options:
        _args['options'] = options

    if _args['type'] is None:
        raise ValueError('Chart "type" is not defined')

    if _args['width'] is None and _args['height'] is None:
        raise ValueError('Chart "width" or "height" or both must be defined')
    elif _args['width'] is None:
        _args.pop('width')
    else:
        _args.pop('height')

    return _RactpyApexCharts(_args)
