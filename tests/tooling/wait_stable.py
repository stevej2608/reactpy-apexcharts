
async def wait_page_stable(page):
    await page.wait_for_load_state("networkidle")
    await page.wait_for_load_state("domcontentloaded")
    await page.wait_for_timeout(2000)
