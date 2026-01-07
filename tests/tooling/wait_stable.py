import asyncio
import os

from playwright.async_api._generated import Page

GITHUB_ACTIONS = os.getenv("GITHUB_ACTIONS", "").lower() == "true"
CLICK_DELAY = 250 if GITHUB_ACTIONS else 25  # Delay in milliseconds.


async def wait_page_stable(page: Page, minimum_delay: int = CLICK_DELAY) -> None:
    """Wait for page to be stable before taking screenshots.

    Args:
        page: Playwright page object
        minimum_delay: Minimum delay in milliseconds to wait for animations.
                      Use this for pages with JS-based animations (e.g., charts).
    """
    await page.wait_for_load_state("networkidle")
    await page.wait_for_load_state("domcontentloaded")
    await asyncio.sleep(minimum_delay / 1000)
