from typing import Callable
from reactpy.testing import DisplayFixture
from examples.sales_example import AppMain
from .tooling.wait_stable import wait_page_stable

# https://github.com/kumaraditya303/pytest-playwright-snapshot


async def test_all_sales_example(display: DisplayFixture, assert_snapshot: Callable[..., None]) -> None:
    await display.show(AppMain)
    await wait_page_stable(display.page, minimum_delay=1500)
    assert_snapshot(await display.page.screenshot())
