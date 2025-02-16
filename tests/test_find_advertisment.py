"""
Модуль для тестирования функционала по поиску объявления
"""


import pytest

import pages
from config.test_data import CreateAdvertisement


class TestFindAdvertisement:
    placeholder = "Поиск по объявлениям"
    name_advertisement:str = CreateAdvertisement.VALUES.get('name')
    text: str = f'Picture of {name_advertisement}'

    @pytest.mark.run(order=2)
    def test_find_advertisement(self, page):
        """Метод для тестирования функционала поиска существующего объявления"""
        pages.index_page.open_index_page(page)
        field = pages.index_page.find_element_by_placeholder(self.placeholder, page)
        field.fill(self.name_advertisement)
        pages.index_page.click_button_by_role("button", "Найти", page)
        advertisement = pages.index_page.find_element_by_alt_text(self.text, page)

        assert advertisement is not None
