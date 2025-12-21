from typing import Callable
from reactpy.testing import DisplayFixture
from examples.simple_barchart import AppMain
from .tooling.wait_stable import wait_page_stable


async def test_all_simple_barchart(display: DisplayFixture, assert_snapshot: Callable[..., None]) -> None:
    await display.show(AppMain)
    await wait_page_stable(display.page)
    assert_snapshot(await display.page.screenshot())
