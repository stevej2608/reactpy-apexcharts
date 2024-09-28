import React from "react";
import ReactDOM from "react-dom";
import htm from "htm";

import Chart from 'react-apexcharts'

const html = htm.bind(React.createElement);


function format_wrapper(fmtString) {

  const fmtFunc = new Function('value', fmtString );

  const _wrapper = (value) => {
    try {
      return fmtFunc(value)
    } catch (e) {
      console.log('Failed to format "%s"', value)
      return value
    }
  }

  return _wrapper;
}

export function bind(node, config) {
  return {
    create: (type, props, children) => React.createElement(type, props, ...children),
    render: (element) => ReactDOM.render(element, node),
    unmount: () => ReactDOM.unmountComponentAtNode(node),
  }
}

export function RactpyApexCharts(props) {

    // console.log(JSON.stringify(props, null,2));

    // Any X and Y axis formatters are simple strings of the form:
    //
    //    "{value} m/s"

  try {
    const xFormatter  = props?.options?.xaxis?.labels?.formatter
    if (xFormatter ) {
      const formatter = format_wrapper(xFormatter )
      props.options.xaxis.labels.formatter = formatter
    }
  } catch (e) {
    console.log("XAxis formatter error %s", e)
  }

  try {
    const yFormatter = props?.options?.yaxis?.labels?.formatter
    if (yFormatter) {
      const formatter = format_wrapper(yFormatter)
      props.options.yaxis.labels.formatter = formatter
    }
  } catch (e) {
    console.log("YAxis formatter error %s", e)
  }

  return (
    <Chart {...props} />
    );
  }
