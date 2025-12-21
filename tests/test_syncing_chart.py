from typing import Callable
from reactpy.testing import DisplayFixture
from examples.syncing_chart import AppMain
from .tooling.wait_stable import wait_page_stable


async def test_syncing_chart(display: DisplayFixture, assert_snapshot: Callable[..., None]) -> None:
    await display.show(AppMain)
    await wait_page_stable(display.page)
    assert_snapshot(await display.page.screenshot(), threshold=0.8)
