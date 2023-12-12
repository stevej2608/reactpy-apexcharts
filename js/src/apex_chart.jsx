import React, { Component } from 'react';
import ReactDOM from "react-dom";
import PropTypes from 'prop-types';

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

    // Any X and Y axis formatters a simple strings of the form:
    //
    //    "{value} m/s"


    // const xfmt = props.options.xaxis.labels.formatter
    // if (xfmt){
    //   props.options.xaxis.labels.formatter = function(value){
    //     return interpolate(xfmt, { value })
    //   }
    // }

    // const yfmt = props.options.yaxis.labels.formatter
    // if (yfmt){
    //   props.options.yaxis.labels.formatter = function(value){
    //     return interpolate(yfmt, { value })
    //   }
    // }


  return (
    <Chart {...props} />
    );
  }



// RactpyApexCharts.defaultProps = {
//   type: 'line',
//   width: '100%',
//   height: 'auto'
// };

// RactpyApexCharts.propTypes = {

//   /**
//    * line, area, bar, pie, donut, scatter, bubble, heatmap, radialBar
//    */

//   type: PropTypes.string.isRequired,

//   /**
//    * Possible values for width can be 100%, 400px or 400 (by default is 100%)
//    */

//   width: PropTypes.oneOfType([
//     PropTypes.string,
//     PropTypes.number,
//   ]),

//   /**
//    * Possible values for height can be 100%, 300px or 300 (by default is auto)
//    */

//   height: PropTypes.oneOfType([
//     PropTypes.string,
//     PropTypes.number,
//   ]),

//   /**
//    * The series is a set of data. To know more about the format of
//    * the data, checkout Series docs on the website.
//    */

//   series: PropTypes.array.isRequired,

//   /**
//    * The configuration object, see options on API (Reference)
//    */

//   options: PropTypes.object.isRequired,


//   /**
//    * Dash-assigned callback that should be called to report property changes
//    * to Dash, to make them available for callbacks.
//    */
//   setProps: PropTypes.func
// };
