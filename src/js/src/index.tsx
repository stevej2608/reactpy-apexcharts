import React from "react";
import ReactDOM from "react-dom";
import htm from "htm";

import * as ChartModule from "react-apexcharts";

const html = htm.bind(React.createElement);

// Handle CommonJS/ESM interop - react-apexcharts is a CommonJS module
// When bundled, ChartModule.default is the exports object, which has a default property
const Chart = ((ChartModule as any).default?.default || (ChartModule as any).default || ChartModule) as any;

console.log("ChartModule:", ChartModule);
console.log("ChartModule.default:", (ChartModule as any).default);
console.log("ChartModule.default.default:", (ChartModule as any).default?.default);
console.log("Chart (resolved):", Chart);
console.log("Chart type:", typeof Chart);

function format_wrapper(fmtString: string): (value: any) => any {
  const fmtFunc = new Function("value", fmtString);

  const _wrapper = (value: any): any => {
    try {
      return fmtFunc(value);
    } catch (e) {
      console.log('Failed to format "%s"', value);
      return value;
    }
  };

  return _wrapper;
}

interface BindConfig {
  [key: string]: any;
}

interface BindResult {
  create: (type: any, props: any, children: any[]) => React.ReactElement;
  render: (element: React.ReactElement) => void;
  unmount: () => void;
}

export function bind(node: HTMLElement, config: BindConfig): BindResult {
  return {
    create: (type, props, children) =>
      React.createElement(type, props, ...children),
    render: (element) => ReactDOM.render(element, node),
    unmount: () => ReactDOM.unmountComponentAtNode(node),
  };
}

interface ApexChartProps {
  type?: string;
  width?: string | number;
  height?: string | number;
  series?: any[];
  options?: {
    xaxis?: {
      labels?: {
        formatter?: string | ((value: any) => any);
      };
    };
    yaxis?: {
      labels?: {
        formatter?: string | ((value: any) => any);
      };
    };
    [key: string]: any;
  };
  [key: string]: any;
}

export function RactpyApexCharts(props: ApexChartProps) {
  // Any X and Y axis formatters are simple strings of the form:
  //
  //    "{value} m/s"

  try {
    const xFormatter = props?.options?.xaxis?.labels?.formatter;
    if (xFormatter) {
      const formatter = format_wrapper(xFormatter);
      props.options.xaxis.labels.formatter = formatter;
    }
  } catch (e) {
    console.log("XAxis formatter error %s", e);
  }

  try {
    const yFormatter = props?.options?.yaxis?.labels?.formatter;
    if (yFormatter) {
      const formatter = format_wrapper(yFormatter);
      props.options.yaxis.labels.formatter = formatter;
    }
  } catch (e) {
    console.log("YAxis formatter error %s", e);
  }

  console.log('props %s', props)

  return <Chart {...props} />;
}
