from app.Tariff import Tariff
from app.TariffManager import TariffManager

manager = None
my_online = None
total_black = None

my_online_name = 'Мой Онлайн'
my_online_price = 290
my_online_gb = 15
my_online_minutes = 400
my_online_sn = ['vk', 'fb', 'yt', 'inst']
my_online_hit = True
my_online_sms = 0
my_online_price_period = 'месяц'
my_online_min_unlim = True
my_online_archived = False

total_black_name = 'Беспредельно черный'
total_black_price = 310
total_black_gb = 30
total_black_minutes = 200
total_black_sn = None
total_black_hit = False
total_black_sms = 200
total_black_price_period = 'месяц'
total_black_min_unlim = False
total_black_archived = True


def test_tariff_init():
    global my_online, total_black
    my_online = Tariff(my_online_name, price=my_online_price, gb=my_online_gb, minutes=my_online_minutes,
                       social_networks_unlim=my_online_sn, hit=my_online_hit)
    total_black = Tariff(total_black_name, price=total_black_price, gb=total_black_gb, minutes=total_black_minutes, sms=total_black_sms, minutes_unlim_tele2=total_black_min_unlim,
                         archived=total_black_archived)

    assert my_online.name == my_online_name and \
           my_online.price == my_online_price and \
           my_online.price_period == my_online_price_period and \
           my_online.minutes == my_online_minutes and \
           my_online.gb == my_online_gb and \
           my_online.social_networks_unlim == my_online_sn and \
           my_online.hit == my_online_hit and \
           my_online.sms == my_online_sms and \
           my_online.minutes_unlim_tele2 == my_online_min_unlim and \
           my_online.archived == my_online_archived


def test_tariff_type():
    assert isinstance(my_online, Tariff)


def test_tariff_manager_init():
    global manager
    manager = TariffManager()

    assert manager.items == []


def test_tariff_manager_type():
    assert isinstance(manager, TariffManager)


def test_add():
    manager.add(my_online)
    manager.add(total_black)

    assert len(manager.items) == 2


def test_actual():
    actual = manager.actual()
    assert actual[0].name == my_online_name


def test_archived():
    archived = manager.archived()
    assert archived[0].name == total_black_name
