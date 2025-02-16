"""
Модуль для тестирования функционала по изменению объявления
"""
import pytest
from playwright.sync_api import expect, Page

import pages
from config.test_data import ChangeAdvertisement, CreateAdvertisement


class TestChangeAdvertisement:
    locator_button: str = '#root > div > div.chakra-container.css-1lle71m > div > div.css-nb383z > svg'
    placeholder: str = "Поиск по объявлениям"
    name_advertisement: str = CreateAdvertisement.VALUES.get('name')
    text: str = f'Picture of {name_advertisement}'

    @pytest.mark.run(order=3)
    def test_change_advertisement(self, page: Page):
        """Метод для тестирования функционала изменения существующего объявления"""
        pages.index_page.open_index_page(page)
        find = pages.index_page.find_element_by_placeholder(self.placeholder, page)
        find.fill(self.name_advertisement)
        pages.index_page.click_button_by_role("button", "Найти", page)
        advertisement = pages.index_page.find_element_by_alt_text(self.text, page)
        advertisement.click()
        cursor = pages.index_page.find_element_by_locator(self.locator_button, page)
        cursor.click()
        for field in ChangeAdvertisement.FIELDS:
            text_field = pages.index_page.find_element_by_locator(f"[name={field}]", page)
            text_field.clear()
            text_field.type(ChangeAdvertisement.CHANGES_VALUES.get(field), delay=10)
            expect(text_field).to_have_value(ChangeAdvertisement.CHANGES_VALUES.get(field))  # проверяем, что в поле
            # внесены корректные данные
        cursor.click()
