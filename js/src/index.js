import React from "react";
import ReactDOM from "react-dom";

import Chart from 'react-apexcharts'

export function bind(node, config) {
  return {
    create: (type, props, children) => React.createElement(type, props, ...children),
    render: (element) => ReactDOM.render(element, node),
    unmount: () => ReactDOM.unmountComponentAtNode(node),
  }
}

function isString(x) {
  return Object.prototype.toString.call(x) === "[object String]"
}

// https://stackoverflow.com/a/57565813

const interpolate = (str, obj) => str.replace(
  /{([^}]+)}/g,
  (_, prop) => obj[prop]
);

/**
 * Wrapper for react-apexcharts library. For API and
 * examples see:
 *
 * https://github.com/apexcharts/react-apexcharts
 *

 */

export function RactpyApexCharts(props) {

    // const { id, setProps, loading_state, children, ...chartProps } = props;

    console.log(JSON.stringify(props, null,2));

    // Any X and Y axis formatters are simple strings of the form:
    //
    //    "{value} m/s"

    try {
      const xfmt = props.options.xaxis.labels.formatter
      if (xfmt){
        props.options.xaxis.labels.formatter = function(value){
          return interpolate(xfmt, { value })
        }
      }
    } catch (e) {
    }

    try {
      const xfmt = props.options.yaxis.labels.formatter
      if (xfmt){
        props.options.yaxis.labels.formatter = function(value){
          return interpolate(xfmt, { value })
        }
      }
    } catch (e) {
    }

  return (
    <Chart {...props} />
    );
  }
