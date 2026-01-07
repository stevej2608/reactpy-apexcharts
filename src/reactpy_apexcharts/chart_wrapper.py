from typing import Literal, Union, List, Dict, Any, Optional
from pathlib import Path

from reactpy.web.module import export, module_from_file

ChartType = Literal['line', 'area', 'bar', 'pie', 'donut', 'scatter', 'bubble', 'heatmap', 'radialBar']


_js_module = module_from_file(
    "reactpy-apexcharts",
    file=Path(__file__).parent / "static" / "bundle.js",
    fallback="⏳",
)

_ReactpyApexCharts = export(_js_module, "RactpyApexCharts")


Series = List[Dict[str, Any]]


def ApexChart(
        chart_type: Optional[ChartType] = None,
        series: Optional[Series] = None,
        width: Optional[Union[str,int]] = None,
        height: Optional[Union[str,int]] = None,
        options: Optional[Dict[str, Any]] = None
        ) -> Any:
    """ Wrapper for react-apexcharts library. For API and examples see:

        https://github.com/apexcharts/react-apexcharts

    Args:
        chart_type (ChartType): The chart type
        width (Union[str,int]): The chart width
        height (Union[str,int]): the chart height
        series (List[float]): Series to be displayed, see https://apexcharts.com/docs/options/series/
        options (Dict[str, Any]): Options

    Returns:
        A ReactPy component instance for rendering an ApexCharts chart
    """

    def unpack_option(option_name: str, value: Any, options: Optional[Dict[str, Any]]) -> Any:
        if not value:
            if options and option_name in options:
                value = options[option_name]  # type: ignore[reportUnknownVariableType]
            elif options:
                chart = options.get('chart', {})
                if isinstance(chart, dict) and option_name in chart:
                    value = chart[option_name]  # type: ignore[reportUnknownVariableType]
                else:
                    value = None
        return value  # type: ignore[reportUnknownVariableType]

    _args: Dict[str, Any] = {}

    # Args can be passed in directly or embedded in the options

    _args['type'] = unpack_option('type', chart_type, options)
    _args['width'] = unpack_option('width', width, options)
    _args['height'] = unpack_option('height', height, options)
    _args['series'] = unpack_option('series', series, options)

    if options:
        _args['options'] = options

    # Must have a chart type

    if _args['type'] is None:
        raise ValueError('Chart "type" is not defined')

    # Must have height or width or both

    if _args['width'] is None and _args['height'] is None:
        raise ValueError('Chart "width" or "height" or both must be defined')
    elif _args['width'] is None:
        _args.pop('width')
    else:
        _args.pop('height')

    return _ReactpyApexCharts(_args)
