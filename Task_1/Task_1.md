## Поиск багов на скриншоте

**1. Сообщение об ошибке на странице.** На странице отображается плашка с ошибкой хотя станица отображается корректно.   
Приоритет: high   

![](https://github.com/MorevDA/Avito_QA_trainee/blob/20bb5099cf6b643df32d232d033b6b396d6e3be0/Task_1/screenshots/bag_1.png)


**2. Не соответствует режим отображения объявлений.** Выбран режим отображения "на карте", карточки объявлений отображаются в виде сетки.   
Приоритет: high   

![](https://github.com/MorevDA/Avito_QA_trainee/blob/20bb5099cf6b643df32d232d033b6b396d6e3be0/Task_1/screenshots/bag_2.png)


**3. Ошибка сортировки.** Выбрана сортровка по возрастанию цены, но карточки отсортированы неверно.   
Приоритет: medium   
![](https://github.com/MorevDA/Avito_QA_trainee/blob/20bb5099cf6b643df32d232d033b6b396d6e3be0/Task_1/screenshots/bag_3.png)


**4. Количество найденных объявлений.** В разных частях страницы отображается разное количество найденных объявлений.   
Приоритет: low   
![](https://github.com/MorevDA/Avito_QA_trainee/blob/20bb5099cf6b643df32d232d033b6b396d6e3be0/Task_1/screenshots/bag_4.png)


**5. Неверная выборка по региону.** Установлен фильтр по г. Москва, одно из объявлений из Липецкой области.   
Приоритет: low   
![](https://github.com/MorevDA/Avito_QA_trainee/blob/20bb5099cf6b643df32d232d033b6b396d6e3be0/Task_1/screenshots/bag_5.png)


**6. Хлебные крошки.** Отсутствует указание категории веллосипедов.   
Приоритет: low   
![](https://github.com/MorevDA/Avito_QA_trainee/blob/20bb5099cf6b643df32d232d033b6b396d6e3be0/Task_1/screenshots/bag_6.png)


**7. Не соответствие адреса.** В объявлении указан г. Липецк, но при этом указана станция метро.   
Приоритет: low   
![](https://github.com/MorevDA/Avito_QA_trainee/blob/20bb5099cf6b643df32d232d033b6b396d6e3be0/Task_1/screenshots/bag_6.png)
### Возможные баги(требуется дополнительное исследование)

**8. Не соответствие производителя.** Фильтрация осуществляется по производителю Author, в описании одного из объявлений указан производитель Atom.  
*Такое поведение возможно при некорректном выборе производителя при оформлении объявления. Без просмотра объявления невозможно однозначно сказать баг это ошибка при оформлении*
Приоритет: low   
![](https://github.com/MorevDA/Avito_QA_trainee/blob/20bb5099cf6b643df32d232d033b6b396d6e3be0/Task_1/screenshots/bag_8.png)

**9. Пагинация.** Количество найденных объявлений - 61, на странице отображается 12 объявлений, таким образм в блоке пагинации должно быть 5 страниц, а не 100.  
*Как правило, помимо найденных объявлений сервис Авито предлагает к просмотру объявления категории "Рекомендуем к просмотру" и объявления из других городов подходящие по условиям фильтрации. Таким образм невозможно однозначно заключить баг ли это, требуется дополнительное исследование.*
Приоритет: low   
![](https://github.com/MorevDA/Avito_QA_trainee/blob/20bb5099cf6b643df32d232d033b6b396d6e3be0/Task_1/screenshots/bag_9.png)



