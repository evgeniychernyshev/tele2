class Tariff:
    def __init__(self,
                 name,
                 *,
                 price=0,
                 price_period='месяц',
                 gb=0,
                 minutes=0,
                 sms=0,
                 social_networks_unlim=None,
                 hit=False,
                 minutes_unlim_tele2=True,
                 archived=False):
        self.name = name
        self.price = price
        self.price_period = price_period
        self.gb = gb
        self.minutes = minutes
        self.sms = sms
        self.social_networks_unlim = social_networks_unlim
        self.hit = hit
        self.minutes_unlim_tele2 = minutes_unlim_tele2
        self.archived = archived

