"""
ReactPy v2 compatible runner classes with base class and subclasses

This module provides a base AppRunner class and specialized subclasses for running
ReactPy components with different CSS frameworks.
"""

import sys
from typing import Any, List, Optional

import uvicorn
from reactpy import html, component
from reactpy.types import RootComponentConstructor, VdomDict
from reactpy.executors.asgi import ReactPy


class AppRunner:
    """Base class for running ReactPy applications.

    Subclasses should implement build_header() and AppContainer() to customize
    the HTML head and app wrapper.
    """

    @classmethod
    def run(
        cls,
        app_main: RootComponentConstructor,
        host: str = "127.0.0.1",
        port: int = 8000,
        title: str = "ReactPy Forms",
        additional_head: Optional[List[str]] = None,
        **kwargs: Any,
    ) -> None:
        """Run a ReactPy component with automatic server setup.

        Args:
            app_main: A ReactPy component function decorated with @component
            host: Server host address (default: "127.0.0.1")
            port: Server port (default: 8000)
            title: Page title (default: "ReactPy Forms")
            additional_head: Optional list of CSS file paths to include
            **kwargs: Additional arguments passed to uvicorn.run()
        """

        # Build head element using subclass implementation
        head = cls.build_header(title, additional_head)

        # Wrap app using subclass implementation
        app = ReactPy(
            cls.AppContainer(app_main),
            html_head=head
        )

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

    @staticmethod
    def build_header(title: str, additional_head: Optional[List[str]] = None) -> VdomDict:
        """Build the HTML head element. Override in subclasses."""
        head_children = [html.title(title)]

        # Add any additional CSS files
        if additional_head:
            for css_path in additional_head:
                if css_path.endswith('.css'):
                    head_children.append(html.link({'rel': 'stylesheet', 'href': css_path}))

        return html.head(*head_children)

    @staticmethod
    def AppContainer(app: RootComponentConstructor) -> RootComponentConstructor:
        """Wrap the app component. Override in subclasses."""
        return app


class PicoRunner(AppRunner):
    """Runner that includes Pico CSS framework."""

    @staticmethod
    def build_header(title: str, additional_head: Optional[List[str]] = None) -> VdomDict:
        """Build the HTML head element with Pico CSS."""
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

        return html.head(*head_children)

    @staticmethod
    def AppContainer(app: RootComponentConstructor) -> RootComponentConstructor:
        """Wrap the app in a Pico CSS container."""
        @component
        def PicoContainer():
            return html.div(
                {'class': "container"},
                html.section(app())
            )
        return PicoContainer


class BootstrapRunner(AppRunner):
    """Runner that includes Bootstrap CSS framework."""

    @staticmethod
    def build_header(title: str, additional_head: Optional[List[str]] = None) -> VdomDict:
        """Build the HTML head element with Bootstrap CSS."""
        meta_viewport = html.meta({
            'name': 'viewport',
            'content': 'width=device-width',
            'initial-scale': 1
        })

        meta_color = html.meta({
            'name': 'theme-color',
            'content': '#000000'
        })

        bootstrap_css = html.link({
            'rel': 'stylesheet',
            'href': 'https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css'
        })

        github_buttons_css = html.link({
            'rel': 'stylesheet',
            'href': 'https://buttons.github.io/css/app.48c6bc16.css'
        })

        head_children = [html.title(title), meta_viewport, meta_color, bootstrap_css, github_buttons_css]

        # Add any additional CSS files
        if additional_head:
            for css_path in additional_head:
                if css_path.endswith('.css'):
                    head_children.append(html.link({'rel': 'stylesheet', 'href': css_path}))

        return html.head(*head_children)

    @staticmethod
    def AppContainer(app: RootComponentConstructor) -> RootComponentConstructor:
        """Wrap the app in a Bootstrap container."""
        @component
        def BootStrapContainer():
            return html.div(
                {'class': "container"},
                html.section(app())
            )
        return BootStrapContainer