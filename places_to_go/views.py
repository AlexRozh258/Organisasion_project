import random
from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import PlaceForm

def add_place(request):
    if request.method == "POST":
        form = PlaceForm(request.POST, request.FILES)
        if form.is_valid():
            place = form.save(commit=False)
            place.session_key = get_session_key(request)
            place.save()
            return redirect("places_list")
    else:
        form = PlaceForm()
    return render(request, "places_to_go/add_place.html", {"form": form})


def places_list(request):
    places = Place.objects.all().order_by('-rating')
    return render(request, "places_to_go/places_list.html", {"places": places})


def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    return render(request, "places_to_go/place_detail.html", {"place": place})

def add_default_places(session_key):
    # Перевіряємо, чи користувач уже має якісь місця
    if Place.objects.filter(session_key=session_key).exists():
        return

    default_places = [
        {
            "name": "Electroperedachi",
            "place_type": "вечірка",
            "location": "завжди різна",
            "description": "Техно-вечірка з унікальною атмосферою, музикою і світлом.",
            "site": "https://electroperedachi.com/en",
            "rating": 4,
            "image": "places/electroperedachi.jpg"
        },
        {
            "name": "Rumbabar",
            "place_type": "бар/ресторан",
            "location": "https://maps.app.goo.gl/v2MpxJDjsfdEoBat7",
            "description": "Гастропроєкт, що об'єднує локальні продукти та культуру української кухні.",
            "site": "https://www.rumbambar.com.ua/",
            "rating": 5,
            "image": "places/rumbabar.jpg"
        },
        {
            "name": "Smoky Bar",
            "place_type": "бар",
            "location": "https://maps.app.goo.gl/LwTNgreVTnFJBLkx5",
            "description": "Стильний бар із авторськими коктейлями у центрі Києва.",
            "menu": "https://smoky.choiceqr.com/menu/section:menyu/osin",
            "rating": 4,
            "image": "places/smoky-bar.jpg"
        },
        {
            "name": "ВДНГ",
            "place_type": "парк",
            "location": "https://maps.app.goo.gl/NA7REaAi5ADnozWv5",
            "description": "Найбільший виставковий і культурний центр України.",
            "site": "https://vdng.ua/",
            "rating": 5,
            "image": "places/vdng.jpg"
        },
        {
            "name": "Milk Bar",
            "place_type": "кав'ярня",
            "location": "https://maps.app.goo.gl/huGi4NJEoyeqSXGR6",
            "description": "Кав'ярня з атмосферою радості, смачними десертами та турботливим сервісом.",
            "site": "https://milkbar.ua/",
            "menu": "https://milkbarshotarustaveli.choiceqr.com/section:milk-bar-brunch/mousse-au-chocolat",
            "rating": 4,
            "image": "places/milk-bar.jpg"
        },
        {
            "name": "Оболонська набережна",
            "place_type": "парк",
            "location": "https://maps.app.goo.gl/xtkiAPTaprFiscVn9",
            "description": "Популярне місце відпочинку на березі Дніпра з прогулянковими зонами.",
            "rating": 4,
            "image": "places/obolon-naberezhna.jpg"
        },
        {
            "name": "Парк Феофанія",
            "place_type": "парк",
            "location": "https://maps.app.goo.gl/E6HZoH5b6CZ4uJ9E8",
            "description": "Мальовничий парк у Києві з духовною атмосферою та природною красою.",
            "rating": 5,
            "image": "places/feofaniya-park.jpg"
        },
        {
            "name": "Музей математики",
            "place_type": "музей",
            "location": "https://maps.app.goo.gl/xPHrNovAW9pipJz49",
            "description": "Інтерактивний простір для вивчення математики через експерименти.",
            "site": "https://mathmuseum.com.ua/",
            "rating": 4,
            "image": "places/math-museum.jpg"
        },
        {
            "name": "Музей медуз",
            "place_type": "музей",
            "location": "https://maps.app.goo.gl/E9sptirRpTkugzR67",
            "description": "Український музей, де можна спостерігати за медузами та дізнатися про їх життя.",
            "site": "https://jellyfishmuseum.kyiv.ua/",
            "rating": 4,
            "image": "places/jellyfish-museum.jpg"
        },
        {
            "name": "Реберня на Арсенальній",
            "place_type": "ресторан",
            "location": "https://maps.app.goo.gl/3E6vPzHJW4AfRuB28",
            "description": "Заклад з ребрами на відкритому вогні та атмосферою демократичного спілкування.",
            "menu": "https://expz.menu/bb7f5d9f-3be2-4e30-a771-7e8781b0f635",
            "rating": 4,
            "image": "places/rebernya.jpg"
        },
        {
            "name": "Capo di Monte",
            "place_type": "бар/ресторан",
            "location": "https://maps.app.goo.gl/8AM7buB2uHRFGMgL9",
            "description": "Італійський ресторан із вишуканою кухнею та затишною атмосферою.",
            "menu": "https://capodimonte.choiceqr.com/menu/section:sezonne-limonne-menyu/limonne-menyu",
            "rating": 5,
            "image": "places/capo-di-monte.jpg"
        },
        {
            "name": "Хомокерамікус",
            "place_type": "рукоділля",
            "location": "https://maps.app.goo.gl/VTZtjg6FE48dWoY27",
            "description": "Майстер-класи з кераміки для всіх бажаючих у центрі Києва.",
            "site": "https://homoceramicus.com/",
            "rating": 5,
            "image": "places/homoceramicus.jpg"
        },
        {
            "name": "Кафе Зустріч",
            "place_type": "кафе",
            "location": "https://maps.app.goo.gl/1kzYupwJxfkhPrqA8",
            "description": "Атмосферне кафе з зеленим інтер'єром та смачними коктейлями.",
            "site": "https://3ustrichcafe.choiceqr.com/",
            "rating": 5,
            "image": "places/kafe-zustrich.jpg"
        },
        {
            "name": "Воздвиженка",
            "place_type": "прогулянка",
            "location": "https://maps.app.goo.gl/D1Kn2zRrUAufyQ8o6",
            "description": "Барвистий район Києва з архітектурною красою та європейським шармом.",
            "rating": 4,
            "image": "places/vozdvyzhenka.jpg"
        },
        
        {
            "name": "Тісто та хміль",
            "description": "Смачна італійська кухня з європейським нахилом.",
            "place_type": "Ресторан",
            "location": "Метро Дарниця",
            "rating": 4.5,
            "image": "places/tisto-ta-hmil.jpg"
        },
        {
            "name": "Нац. бот. сад ім. Гришка",
            "description": "Просторі схили Печерську, затишні кущі для лежання.",
            "place_type": "Парк",
            "location": "Метро Звіриницька",
            "rating": 4.0,
            "image": "places/botanical-garden.jpg"
        },
        {
            "name": "Мама Манана",
            "description": "Прекрасна грузинська кухня, вааах смачно!",
            "place_type": "Ресторан",
            "location": "Велика кількість закладів по Києву",
            "rating": 5.0,
            "image": "places/mama-manana.jpg"
        },
        {
            "name": "Pan Chang",
            "description": "Азійська кухня, смачно, доволі гучна музика у залі.",
            "place_type": "Ресторан",
            "location": "Поділ",
            "rating": 4.0,
            "image": "places/pan-chang.jpg"
        },
        {
            "name": "Гамбургерна NUNU",
            "description": "Одні з найкращих бургерів у Києві! Дуже стильний інтер'єр.",
            "place_type": "Ресторан",
            "location": "Поділ",
            "rating": 4.0,
            "image": "places/nunu-burger.jpg"
        }
    ]
    # Додаємо кожне місце у базу
    for data in default_places:
        Place.objects.create(session_key=session_key, **data)

def get_session_key(request):
    """Гарантує, що кожен користувач (навіть без входу) має власний session_key."""
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key

def index(request):
    session_key = get_session_key(request)
    add_default_places(session_key)  # додаємо стандартні місця при першому вході

    places = Place.objects.filter(session_key=session_key)
    chosen_place = None
    if request.method == "POST" and places.exists():
        weights = [p.rating for p in places]
        chosen_place = random.choices(list(places), weights=weights, k=1)[0]
    return render(request, "places_to_go/index.html", {"chosen_place": chosen_place})
