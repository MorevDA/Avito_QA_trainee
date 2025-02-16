"""
Модуль для тестирования функционала по созданию объявления
"""
import pytest
import pages

from config.test_data import CreateAdvertisement


class TestCreateAdvertisement:
    # fields = {'name', 'price', 'description', 'imageUrl'}
    # values = {'name': 'Название1000', 'price': '100',
    #           'description': 'Описание', 'imageUrl': 'URL изображения'}

    @pytest.mark.run(order=1)
    def test_create_advertisement(self, page):
        """Тест создание документа"""
        pages.index_page.open_index_page(page)
        pages.index_page.click_button_by_role("button", "Создать", page)
        for field in CreateAdvertisement.FIELDS:
            text_field = pages.index_page.find_element_by_locator(f"[name={field}]", page)
            text_field.type(CreateAdvertisement.VALUES.get(field), delay=10)
        pages.index_page.click_button_by_role("button", "Сохранить", page)
