class CreateAdvertisement:
    FIELDS = {'name', 'price', 'description', 'imageUrl'}
    VALUES = {'name': 'Стол Ikea', 'price': '1000', 'description': 'Стол Ikea в отличном состоянии',
              'imageUrl': 'https://cdn1.ozone.ru/s3/multimedia-1-8/7072025804.jpg'}


class ChangeAdvertisement:
    FIELDS = {'name', 'price', 'description', 'imageUrl'}
    CHANGES_VALUES = {'name': 'Стул Ikea', 'price': '800', 'description': 'Стул Ikea в отличном состоянии',
                      'imageUrl': 'https://cdn1.ozone.ru/s3/multimedia-u/6836858562.jpg'}
