import pytest
from _pytest.config import Config
from _pytest.config.argparsing import Parser

from reactpy.testing import DisplayFixture, BackendFixture
from reactpy.testing.common import GITHUB_ACTIONS
from reactpy._option import Option

pytest_plugins = "tests.tooling.pytest_playwright_visual"

REACTPY_TESTS_DEFAULT_TIMEOUT = Option(
    "REACTPY_TESTS_DEFAULT_TIMEOUT",
    10.0,
    mutable=False,
    validator=float,
)
"""A default timeout for testing utilities in ReactPy"""


@pytest.fixture(scope="session")
def anyio_backend():
    return 'asyncio'

def pytest_addoption(parser: Parser) -> None:
    parser.addoption(
        "--headless",
        dest="headless",
        action="store_true",
        help="Don't open a browser window when running web-based tests",
    )

@pytest.fixture
async def display(server, page):
    async with DisplayFixture(server, page) as display:
        yield display

@pytest.fixture
async def server():
    async with BackendFixture() as server:
        yield server


@pytest.fixture
async def page(browser):
    pg = await browser.new_page()
    pg.set_default_timeout(REACTPY_TESTS_DEFAULT_TIMEOUT.current * 1000)
    try:
        yield pg
    finally:
        await pg.close()

# @pytest.fixture(scope="session")
# async def page(pytestconfig):
#     async with async_playwright() as pw:
#         yield await pw.chromium.launch(headless=not bool(pytestconfig.option.headed))


@pytest.fixture
async def browser(pytestconfig: Config):
    from playwright.async_api import async_playwright

    async with async_playwright() as pw:
        yield await pw.chromium.launch(
            headless=bool(pytestconfig.option.headless) or GITHUB_ACTIONS
        )
