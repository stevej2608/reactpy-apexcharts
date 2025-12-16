"""
ReactPy v1 compatible run() and pico_run() functions for ReactPy v2

This module provides run() and pico_run() functions that mimic the ReactPy v1 behavior,
making it easy to run simple examples without manual server setup.
"""

import sys
from typing import Any, List, Optional

import uvicorn
from reactpy import component, html
from reactpy.types import ComponentType, VdomDict
from reactpy.executors.asgi import ReactPy


def run(
    app_main: ComponentType,
    host: str = "127.0.0.1",
    port: int = 8000,
    title: str = "ReactPy App",
    head: Optional[VdomDict] = None,
    **kwargs: Any,
) -> None:
    """Run a ReactPy component with automatic server setup.

    This function reproduces the ReactPy v1 run() behavior by automatically
    creating and configuring an ASGI server to run your ReactPy component.

    Args:
        app_main: A ReactPy component function decorated with @component
        host: Server host address (default: "127.0.0.1")
        port: Server port (default: 8000)
        title: Page title (default: "ReactPy App")
        head: Optional HTML head VdomDict element with additional head content
        **kwargs: Additional arguments passed to uvicorn.run()

    Example:
        ```python
        from reactpy import component, html
        from examples.runner import run

        @component
        def AppMain():
            return html.h1("Hello ReactPy!")

        if __name__ == "__main__":
            run(AppMain)
        ```
    """

    # Build head element
    if head is None:
        head = html.head(html.title(title))
    elif "children" in head:
        # Add title to existing head if not present
        has_title = any(
            child.get("tagName") == "title"
            for child in head.get("children", [])
            if isinstance(child, dict)
        )
        if not has_title:
            head["children"].insert(0, html.title(title))
    else:
        head["children"] = [html.title(title)]

    # Create ReactPy ASGI app
    app = ReactPy(app_main, html_head=head)

    # Display startup message
    print(f"Starting ReactPy server at http://{host}:{port}")
    print("Press CTRL+C to quit")

    try:
        # Run the server
        uvicorn.run(app, host=host, port=port, **kwargs)
    except KeyboardInterrupt:
        print("\nShutting down server...")
    except Exception as ex:
        print(f"Server error: {ex}")
    finally:
        sys.exit(0)


def pico_run(
    app: ComponentType,
    host: str = "127.0.0.1",
    port: int = 8000,
    title: str = "ReactPy Table",
    additional_head: Optional[List[str]] = None,
    **kwargs: Any,
) -> None:
    """Run a ReactPy component wrapped in a Pico CSS container.

    This function wraps the provided component in a Pico CSS styled container
    and automatically includes the Pico CSS framework in the page head.

    Args:
        app: A ReactPy component function decorated with @component
        host: Server host address (default: "127.0.0.1")
        port: Server port (default: 8000)
        title: Page title (default: "ReactPy Table")
        additional_head: Optional list of CSS file paths to include
        **kwargs: Additional arguments passed to uvicorn.run()

    Example:
        ```python
        from reactpy import component, html
        from examples.runner import pico_run

        @component
        def AppMain():
            return html.h1("Hello with Pico CSS!")

        if __name__ == "__main__":
            pico_run(AppMain, additional_head=["assets/css/custom.css"])
        ```
    """

    # Build the head with Pico CSS
    pico_css = html.link({
        'rel': 'stylesheet',
        'href': 'https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css',
        'crossorigin': 'anonymous'
    })

    head_children = [html.title(title), pico_css]

    # Add any additional CSS files
    if additional_head:
        for css_path in additional_head:
            if css_path.endswith('.css'):
                head_children.append(html.link({'rel': 'stylesheet', 'href': css_path}))

    head = html.head(*head_children)

    # Wrap the app in a Pico CSS container
    @component
    def PicoContainer():
        return html.div(
            {'class': "container", 'style': {'max-width': '1900px'}},
            html.section(app())
        )

    # Create ReactPy ASGI app
    asgi_app = ReactPy(PicoContainer, html_head=head)

    # Display startup message
    print(f"Starting ReactPy server (with Pico CSS) at http://{host}:{port}")
    print("Press CTRL+C to quit")

    try:
        # Run the server
        uvicorn.run(asgi_app, host=host, port=port, **kwargs)
    except KeyboardInterrupt:
        print("\nShutting down server...")
    except Exception as ex:
        print(f"Server error: {ex}")
    finally:
        sys.exit(0)
