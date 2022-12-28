class StrategyDeal:

    def __init__(self, bank, entry, targets, close):
        self.bank = bank
        self.entry = entry
        self.targets = targets
        self.close = close

    def get_targets(self):
        # вернуть список таргетов в виде числовых значений float [21.5432423, 22.864732843, 23.556789]
        return self.targets

    def get_target_percents(self):
        # вернуть список процентов, как в примере, округленные до 3 знака [6.912, 13.376, 16.857]
        target_percents = []
        for target in self.get_targets():
            percent = round((target / self.entry - 1) * 100, 3)
            target_percents.append(percent)
        return target_percents

    def get_target_banks(self):
        # список значений банков, если продавать активы по таргетам, как в пример,
        # округленные до 3 знака [1069.12, 1133.764, 1168.573]
        banks_values = []
        for target_percent in self.get_target_percents():
            value = round(self.bank * (target_percent + 100) / 100, 3)
            banks_values.append(value)
        return banks_values

    def __str__(self):
        # текстовое представление сделки
        pass


def read_data(file_name):
    pass


def write_data(file_name, data):
    pass


def parse_data(data):
    pass


def main():
    pass


# content = read_data('deals.txt')
# result = parse_data(content)
# ...
# write_data('out.txt', result)


if __name__ == '__main__':
    main()