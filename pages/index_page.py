from playwright.sync_api import Page, Locator, expect
import config


class IndexPage:
    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)

    def click_button_by_role(self, role, name_button, page: Page) -> None:
        page.get_by_role(role, name=name_button).click()

    def find_element_by_placeholder(self, placeholder: str, page: Page) -> Locator:
        field = page.get_by_placeholder(placeholder)
        return field

    def find_element_by_alt_text(self, text: str, page: Page) -> Locator:
        field = page.get_by_alt_text(text)
        return field

    def find_element_by_locator(self, locator, page: Page) -> list[Locator]:
        return page.locator(locator).all()




    def find_element_by_locator(self, locator: str, page: Page) -> Locator:
        advertisement = page.locator(locator)
        return advertisement


