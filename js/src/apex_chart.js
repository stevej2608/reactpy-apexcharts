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


/**
 * Wrapper for react-apexcharts library. For API and
 * examples see:
 *
 * https://github.com/apexcharts/react-apexcharts
 *
 */

export function RactpyApexCharts(props) {

  // console.log(JSON.stringify(props, null,2));

  return html`<Chart ${props} />`;

  }
