import pytest
from reactpy.testing import DisplayFixture
from examples.sales_example import AppMain
from .tooling.wait_stable import wait_page_stable

# https://github.com/kumaraditya303/pytest-playwright-snapshot

@pytest.mark.anyio
async def test_all_sales_example(display: DisplayFixture, assert_snapshot):
    await display.show(AppMain)
    await wait_page_stable(display.page)
    assert_snapshot(await display.page.screenshot())
