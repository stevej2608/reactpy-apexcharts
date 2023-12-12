import React from "react";
import ReactDOM from "react-dom";

export function bind(node, config) {
  return {
    create: (type, props, children) => React.createElement(type, props, ...children),
    render: (element) => ReactDOM.render(element, node),
    unmount: () => ReactDOM.unmountComponentAtNode(node),
  }
}

export function ExampleCounter(props) {
  const [count, setCount] = React.useState(props.count);

  const updateCount = () => {
    const newCount = count + 1;
    props.onCountChange(newCount);
    setCount(newCount);
  };

  return(
    <div>
      <button id={props.buttonId} onClick={updateCount}>
        {props.buttonText}
      </button>
      <p>current count is: {count}</p>
    </div>)
  
}
