from .models import Place

def load_initial_places():
    data = [
        {
            "name": "Electroperedachi",
            "type": "вечірка",
            "location": "завжди різна",
            "description": "Техно-вечірка з унікальною атмосферою, музикою і світлом.",
            "site": "https://electroperedachi.com/en",
            "rating": 4
        },
        {
            "name": "Rumbabar",
            "type": "бар/ресторан",
            "location": "https://maps.app.goo.gl/v2MpxJDjsfdEoBat7",
            "description": "Гастропроєкт, що об’єднує локальні продукти та культуру української кухні.",
            "site": "https://www.rumbambar.com.ua/",
            "rating": 5
        },
        {
            "name": "Smoky Bar",
            "type": "бар",
            "location": "https://maps.app.goo.gl/LwTNgreVTnFJBLkx5",
            "description": "Стильний бар із авторськими коктейлями у центрі Києва.",
            "menu": "https://smoky.choiceqr.com/menu/section:menyu/osin",
            "rating": 4
        },
        {
            "name": "ВДНГ",
            "type": "парк",
            "location": "https://maps.app.goo.gl/NA7REaAi5ADnozWv5",
            "description": "Найбільший виставковий і культурний центр України.",
            "site": "https://vdng.ua/",
            "rating": 5
        },
        {
            "name": "Milk Bar",
            "type": "кав’ярня",
            "location": "https://maps.app.goo.gl/huGi4NJEoyeqSXGR6",
            "description": "Кав’ярня з атмосферою радості, смачними десертами та турботливим сервісом.",
            "site": "https://milkbar.ua/",
            "menu": "https://milkbarshotarustaveli.choiceqr.com/section:milk-bar-brunch/mousse-au-chocolat",
            "rating": 4
        },
        {
            "name": "Оболонська набережна",
            "type": "парк",
            "location": "https://maps.app.goo.gl/xtkiAPTaprFiscVn9",
            "description": "Популярне місце відпочинку на березі Дніпра з прогулянковими зонами.",
            "rating": 4
        },
        {
            "name": "Парк Феофанія",
            "type": "парк",
            "location": "https://maps.app.goo.gl/E6HZoH5b6CZ4uJ9E8",
            "description": "Мальовничий парк у Києві з духовною атмосферою та природною красою.",
            "rating": 5
        },
        {
            "name": "Музей математики",
            "type": "музей",
            "location": "https://maps.app.goo.gl/xPHrNovAW9pipJz49",
            "description": "Інтерактивний простір для вивчення математики через експерименти.",
            "site": "https://mathmuseum.com.ua/",
            "rating": 4
        },
        {
            "name": "Музей медуз",
            "type": "музей",
            "location": "https://maps.app.goo.gl/E9sptirRpTkugzR67",
            "description": "Український музей, де можна спостерігати за медузами та дізнатися про їх життя.",
            "site": "https://jellyfishmuseum.kyiv.ua/",
            "rating": 4
        },
        {
            "name": "Реберня на Арсенальній",
            "type": "ресторан",
            "location": "https://maps.app.goo.gl/3E6vPzHJW4AfRuB28",
            "description": "Заклад з ребрами на відкритому вогні та атмосферою демократичного спілкування.",
            "menu": "https://expz.menu/bb7f5d9f-3be2-4e30-a771-7e8781b0f635",
            "rating": 4
        },
        {
            "name": "Capo di Monte",
            "type": "бар/ресторан",
            "location": "https://maps.app.goo.gl/8AM7buB2uHRFGMgL9",
            "description": "Італійський ресторан із вишуканою кухнею та затишною атмосферою.",
            "menu": "https://capodimonte.choiceqr.com/menu/section:sezonne-limonne-menyu/limonne-menyu",
            "rating": 5
        },
        {
            "name": "Хомокерамікус",
            "type": "рукоділля",
            "location": "https://maps.app.goo.gl/VTZtjg6FE48dWoY27",
            "description": "Майстер-класи з кераміки для всіх бажаючих у центрі Києва.",
            "site": "https://homoceramicus.com/",
            "rating": 5
        },
        {
            "name": "Кафе Зустріч",
            "type": "кафе",
            "location": "https://maps.app.goo.gl/1kzYupwJxfkhPrqA8",
            "description": "Атмосферне кафе з зеленим інтер’єром та смачними коктейлями.",
            "site": "https://3ustrichcafe.choiceqr.com/",
            "rating": 5
        },
        {
            "name": "Воздвиженка",
            "type": "прогулянка",
            "location": "https://maps.app.goo.gl/D1Kn2zRrUAufyQ8o6",
            "description": "Барвистий район Києва з архітектурною красою та європейським шармом.",
            "rating": 4
        }
    ]

    for item in data:
        Place.objects.get_or_create(**item)
