from typing import Protocol
from reactpy import component, html
from reactpy.types import RootComponentConstructor
from reactpy.testing import DisplayFixture
from playwright.async_api import Page

from utils.server_options.pico_options import PICO_CSS
from . import wait_page_stable


class IContainer(Protocol):
    """Interface for page container classes."""

    @property
    def page(self) -> Page:
        """Get the Playwright page instance."""
        ...

    async def show(self, app: RootComponentConstructor) -> None:
        """Show a ReactPy component in the container.

        Args:
            app: A component function (not called - pass the function itself)
        """
        ...

    async def page_stable(self) -> None:
        """Wait for the page to become stable."""
        ...

class PicoContainer(IContainer):
    
    """Simple wrapper for the reactpy component being tested"""

    @property
    def page(self) -> Page:
        return self.display.page


    def __init__(self, display:DisplayFixture):
        self.display = display

    async def show(self, app: RootComponentConstructor) -> None:
        """Show a ReactPy component in a Pico CSS styled container.

        Args:
            app: A component function (not called - pass the function itself)
        """

        @component
        def AppContainer():
            return html._(
                html.head(
                    html.link(PICO_CSS)
                ),
                app()  # Call the component here inside AppContainer
            )

        await self.display.show(AppContainer)


    async def page_stable(self):
        await wait_page_stable(self.display.page)
