class TariffManager:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def actual(self):
        return list(filter(lambda tariff: not tariff.archived, self.items))

    def archived(self):
        return list(filter(lambda tariff: tariff.archived, self.items))
