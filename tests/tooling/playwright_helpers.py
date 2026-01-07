
from playwright.async_api import Page
from typing import Callable, Any, Coroutine

from .wait_stable import wait_page_stable

FuncType = Callable[..., Coroutine[Any, Any, Any]]

def wait_page(page: Page) -> Callable[[FuncType], FuncType]:

    def _decorator(decorated_func: FuncType) -> FuncType:

        async def _wrapper( *_args: Any, **_kwargs: Any) -> Any:
            await wait_page_stable(page)
            result = await decorated_func(*_args, **_kwargs)
            await wait_page_stable(page)
            return result

        return _wrapper

    return _decorator


def page_element(page: Page, name: str):

    @wait_page(page)
    async def get_text():
        element = await page.query_selector(name)
        if element:
            value = await element.text_content()
            return value
        else:
            return None
    return get_text

def input_field(page: Page, name: str):

    @wait_page(page)
    async def get_input():
        element = await page.query_selector(name)
        if element:
            value = await element.input_value()
            return value
        return None

    @wait_page(page)
    async def set_input(value:str):
        element = await page.query_selector(name)
        if element:
            await element.fill(value)

    return [get_input, set_input]


def select_element(page: Page, name: str):
    """Returns methods to allow control of html select element

    Args:
        page (Page): The page that contains the select element
        name (str): The html selector name

    Returns:
        callables: get_selection, select_option
    """

    # https://playwright.dev/python/docs/api/class-locator#locator-select-option

    @wait_page(page)
    async def get_select_option():
        element = await page.query_selector(name)
        if element:
            value = await element.get_property('value')
            return str(value)
        else:
            return None

    @wait_page(page)
    async def set_select_option(value:str):
        element = await page.query_selector(name)
        if element:
            await element.select_option(value)

    return get_select_option, set_select_option


def checkbox_element(page: Page, name: str):

    @wait_page(page)
    async def get_checked():
        element = await page.query_selector(f"input[name='{name}']")
        if element:
            value = await element.get_property('checked')
            # value = await element.get_property('value')
            return str(value) == 'true'
        else:
            return None

    @wait_page(page)
    async def set_checkbox(value:bool):
        element = await page.query_selector(f"input[name='{name}']")
        if element:

            # https://playwright.dev/python/docs/api/class-locator#locator-set-checked
            # https://playwright.dev/python/docs/api/class-locator#locator-click

            try:
                await element.click()
            except Exception:
                pass

    return get_checked, set_checkbox


def radio_btn_element(page: Page, value: str):

    @wait_page(page)
    async def get_radio_btn():
        element = await page.query_selector(f"input[value='{value}']")
        if element:
            val = await element.get_property('checked')
            return str(val) == 'true'
        else:
            return None

    @wait_page(page)
    async def set_radio_btn(value:str):
        element = await page.query_selector(f"input[value='{value}']")
        if element:

            # https://playwright.dev/python/docs/api/class-locator#locator-set-checked
            # https://playwright.dev/python/docs/api/class-locator#locator-click

            try:
                await element.click()
            except Exception:
                pass

    return get_radio_btn, set_radio_btn
