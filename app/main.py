import os
import waitress
from flask import Flask, render_template, request, url_for
from app.TariffManager import TariffManager
from app.Tariff import Tariff


def start():
    app = Flask(__name__)

    manager = TariffManager()
    my_online = Tariff('Мой Онлайн', price=290, gb=15, minutes=400, social_networks_unlim=['vk', 'fb', 'yt', 'inst'], hit=True)
    unlimited = Tariff('Безлимит', price=350, gb=-1, minutes=500, sms=50, social_networks_unlim=['vk', 'fb', 'yt', 'inst'])
    classic = Tariff('Классический', minutes_unlim_tele2=False)
    total_black = Tariff('Беспредельно черный', price=310, gb=30, minutes=200, sms=200, minutes_unlim_tele2=False,
                         archived=True)
    city = Tariff('Сити', minutes_unlim_tele2=False, archived=True)

    manager.add(my_online)
    manager.add(unlimited)
    manager.add(classic)
    manager.add(total_black)
    manager.add(city)

    actual = manager.actual()
    archived = manager.archived()

    @app.route('/')
    def index():
        return render_template('index.html', tariffs=actual)

    @app.route('/archived')
    def old():
        return render_template('archived.html', tariffs=archived)

    if os.getenv('APP_ENV') == 'PROD' and os.getenv('PORT'):
        waitress.serve(app, port=os.getenv('PORT'))
    else:
        app.run(port=9877, debug=True)


if __name__ == '__main__':
    start()
