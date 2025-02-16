"""
Модуль для тестирования функционала по поиску объявления
"""

import pages
import pytest


class TestFindAdvertisement:
    placeholder = "Поиск по объявлениям"
    name = 'ghdydytdf'  # "Название100"
    text = 'ghdydytdf'  # 'Picture of Название100'

    @pytest.mark.run(order=2)
    def test_find_advertisement(self, page):
        """Метод для тестирования функционала поиска существующего объявления"""
        pages.index_page.open_index_page(page)
        field = pages.index_page.find_element_by_placeholder(self.placeholder, page)
        field.fill(self.name)
        pages.index_page.click_button_by_role("button", "Найти", page)
        advertisement = pages.index_page.find_element_by_alt_text(self.name, page)

        assert advertisement is not None
