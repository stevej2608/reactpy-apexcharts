import pytest
from reactpy.testing import DisplayFixture
from examples.simple_barchart import AppMain
from .tooling.wait_stable import wait_page_stable


@pytest.mark.anyio
async def test_all_simple_barchart(display: DisplayFixture, assert_snapshot):
    await display.show(AppMain)
    await wait_page_stable(display.page)
    assert_snapshot(await display.page.screenshot())
