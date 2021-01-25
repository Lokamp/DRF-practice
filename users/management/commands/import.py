from pathlib import Path

import requests
from django.contrib.auth.hashers import make_password
from django.core.management import BaseCommand

from config.settings import BASE_DIR
from items.models import Item
from reviews.models import Review
from users.models import User

URL_USERS = 'https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/recipients.json'
URL_REVIEW = 'https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/reviews.json'
URL_ITEM = 'https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/foodboxes.json'

start_color = '\033[34m'  # Blue colour, starting point.
end_color = '\033[0m'  # Blue colour, end point.


class Command(BaseCommand):
    help = 'import models - items, users, reviews'

    def handle(self, *args, **options):
        Path(BASE_DIR, 'media', 'image').mkdir(parents=True, exist_ok=True)
        model_user_data = requests.get(url=URL_USERS).json()
        if model_user_data:
            print(f'{start_color}Начинается импорт для модели User...{end_color}')
            for user in model_user_data:
                User.objects.update_or_create(
                    id=user['id'],
                    defaults={
                        'username': user['email'].split('@')[0],
                        'email': user['email'],
                        'password': make_password(user['password']),
                        'first_name': user['info']['name'],
                        'last_name': user['info']['surname'],
                        'middle_name': user['info']['patronymic'],
                        'phone_number': user['contacts']['phoneNumber'].replace('-', ''),
                        'address': user['city_kladr'],
                        'premium': user['premium']
                    }
                )
            print('Импорт для модели User прошел успешно!')
        else:
            print(f'Не смогли подключиться к {URL_USERS}!')

        model_review_data = requests.get(url=URL_REVIEW).json()
        if model_review_data:
            print(f'{start_color}Начинается импорт для модели Review...{end_color}')
            for review in model_review_data:
                Review.objects.update_or_create(
                    id=review['id'],
                    defaults={
                        'author_id': review['author'],
                        'text': review['content'],
                        'created_at': review['created_at '],
                        'published_at':
                            review['created_at '] if review['published_at'] == '' else review['published_at'],
                        'status': review['status']
                    }
                )
            print('Импорт для модели Review прошел успешно!')
        else:
            print(f'Не смогли подключиться к {URL_REVIEW}!')

        model_item_data = requests.get(url=URL_ITEM).json()
        if model_item_data:
            print(f'{start_color}Начинается импорт картинок для модели Item...{end_color}')
            counter_one = 0
            for item in model_item_data:
                counter_one += 1
                path = Path(BASE_DIR, 'media', 'image', f'{counter_one}.jpg')
                img_data = requests.get(item['image'])
                with open(path, 'wb') as img:
                    img.write(img_data.content)
            print('Картинки для модели Item успешно импортированы!')
            print(f'{start_color}Начинается импорт для модели Item...{end_color}')
            counter_two = 0
            for item in model_item_data:
                counter_two += 1
                Item.objects.update_or_create(
                    id=item['id'],
                    defaults={
                        'title': item['title'],
                        'description': item['description'],
                        'image': f'image/{counter_two}.jpg',
                        'weight': item['weight_grams'],
                        'price': item['price']
                    }
                )
            print('Импорт для модели Item прошел успешно!')
        else:
            print(f'Не смогли подключиться к {URL_ITEM}!')
