"""
Модуль для тестирования функционала по изменению объявления
"""
import pytest
from playwright.sync_api import expect, Page

import pages


class TestChangeAdvertisement:
    locator_button = '#root > div > div.chakra-container.css-1lle71m > div > div.css-nb383z > svg'
    placeholder = "Поиск по объявлениям"
    name = "Название1000"
    text = 'Picture of Название1000'
    fields = {'name', 'price', 'description', 'imageUrl'}
    values = {'name': 'Проба', 'price': '10',
              'description': 'Проба', 'imageUrl': 'Проба'}

    @pytest.mark.run(order=3)
    def test_change_advertisement(self, page: Page):
        """Метод для тестирования функционала изменения существующего объявления"""
        pages.index_page.open_index_page(page)
        find = pages.index_page.find_element_by_placeholder(self.placeholder, page)
        find.fill(self.name)
        pages.index_page.click_button_by_role("button", "Найти", page)
        advertisement = pages.index_page.find_element_by_alt_text(self.text, page)
        advertisement.click()
        cursor = pages.index_page.find_element_by_locator(self.locator_button, page)
        cursor.click()
        for field in self.fields:
            text_field = pages.index_page.find_element_by_locator(f"[name={field}]", page)
            text_field.clear()
            text_field.type(self.values.get(field), delay=10)
            expect(text_field).to_have_value(self.values.get(field))  # проверяем, что в поле внесены корректные данные
        cursor.click()
