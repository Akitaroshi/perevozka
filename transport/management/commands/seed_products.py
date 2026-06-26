from django.core.management.base import BaseCommand
from transport.models import Product

class Command(BaseCommand):
    help = 'Наполняет базу данных 20 спортивными товарами'

    def handle(self, *args, **options):
        # Удаляем старые товары, чтобы не дублировать их при повторном запуске
        Product.objects.all().delete()

        products_data = [
            {
                "name": "Футбольный мяч Adidas",
                "description": "Профессиональный игровой мяч. Официальный размер 5. Износостойкий материал.",
                "price": 3490.00,
                "image_url": "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Баскетбольный мяч Wilson",
                "description": "Классический мяч для игры в зале и на улице. Композитная кожа.",
                "price": 2890.00,
                "image_url": "https://images.unsplash.com/photo-1546519638-68e109498ffc?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Беговые кроссовки Nike",
                "description": "Легкие кроссовки с амортизацией для ежедневных тренировок и пробежек.",
                "price": 8990.00,
                "image_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Теннисная ракетка Wilson Pro",
                "description": "Профессиональная ракетка для точных ударов и максимального контроля.",
                "price": 12500.00,
                "image_url": "https://images.unsplash.com/photo-1626224583764-f87db24ac4ea?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Коврик для йоги Reebok",
                "description": "Нескользящая поверхность. Толщина 4 мм обеспечивает комфорт для суставов.",
                "price": 1990.00,
                "image_url": "https://images.unsplash.com/photo-1601925260368-ae2f83cf8b7f?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Гантели разборные (пара по 10 кг)",
                "description": "Удобные стальные гантели с обрезиненными дисками. Надежные замки-гайки.",
                "price": 4500.00,
                "image_url": "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Бутылка для воды спортивная",
                "description": "Объем 750 мл. Пищевой пластик без вредных примесей BPA. Удобный клапан.",
                "price": 890.00,
                "image_url": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Фитнес-браслет Xiaomi",
                "description": "Мониторинг пульса, сна и физической активности. Экран AMOLED, влагозащита.",
                "price": 3990.00,
                "image_url": "https://images.unsplash.com/photo-1575311373937-040b8e1fd5b6?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Спортивный рюкзак",
                "description": "Вместительный рюкзак с отделением для обуви и ноутбука. Водоотталкивающая ткань.",
                "price": 3200.00,
                "image_url": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Очки для плавания Arena",
                "description": "Гидродинамическая форма, защита от запотевания (Anti-fog) и УФ-лучей.",
                "price": 1490.00,
                "image_url": "https://images.unsplash.com/photo-1582971805810-b24306e4afe5?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Шлем велосипедный Rockbros",
                "description": "Легкий шлем с отличной вентиляцией. Регулировка размера, съемный козырек.",
                "price": 2490.00,
                "image_url": "https://images.unsplash.com/photo-1598550476439-6847785fce6e?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Скоростная скакалка",
                "description": "Встроенные подшипники для быстрого вращения. Стальной трос в защитной оплетке.",
                "price": 750.00,
                "image_url": "https://images.unsplash.com/photo-1434596955112-0f2fe641c12b?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Спортивные перчатки",
                "description": "Защищают ладони от мозолей и скольжения во время тренировок на турниках и с железом.",
                "price": 990.00,
                "image_url": "https://images.unsplash.com/photo-1583454110551-21f2fa2afe61?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Массажный фоам-роллер",
                "description": "Для самомассажа (МФР) и расслабления мышц после интенсивных нагрузок.",
                "price": 1200.00,
                "image_url": "https://images.unsplash.com/photo-1600881333168-2ef49b341f30?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Шейкер для спортивного питания",
                "description": "Объем 600 мл. Металлическая пружина внутри для идеального смешивания протеина.",
                "price": 650.00,
                "image_url": "https://images.unsplash.com/photo-1593079831268-3381b0db4a77?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Спортивная сумка",
                "description": "Удобная сумка для спортзала с отдельным вентилируемым карманом для кроссовок.",
                "price": 2790.00,
                "image_url": "https://images.unsplash.com/photo-1590556409324-aa1d726e5c3c?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Футболка беговая дышащая",
                "description": "Влагоотводящая синтетическая ткань. Плоские швы предотвращают натирание кожи.",
                "price": 1190.00,
                "image_url": "https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Набор фитнес-резинок (5 шт)",
                "description": "Разный уровень сопротивления — от легкого до супер-тяжелого. Тканевый мешочек в комплекте.",
                "price": 850.00,
                "image_url": "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Эспандер кистевой",
                "description": "Регулируемая нагрузка от 10 до 60 кг. Прорезиненные эргономичные ручки.",
                "price": 550.00,
                "image_url": "https://images.unsplash.com/photo-1584735935682-2f2b69dff9d2?auto=format&fit=crop&w=600&q=80"
            },
            {
                "name": "Спортивный секундомер",
                "description": "Точность измерения 1/100 секунды. Календарь, часы, будильник, защита от брызг.",
                "price": 790.00,
                "image_url": "https://images.unsplash.com/photo-1508962914676-134849a727f0?auto=format&fit=crop&w=600&q=80"
            }
        ]

        for item in products_data:
            Product.objects.create(**item)

        self.stdout.write(self.style.SUCCESS('База данных успешно наполнена 20 товарами!'))