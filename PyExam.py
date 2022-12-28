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

    def get_target_data(self, i):
        return f"{i + 1} target: {self.get_targets()[i]}\n" \
               f"percent = Percent: {round(self.get_target_percents()[i], 3)}%\n" \
               f"bank = Bank: {round(self.get_target_banks()[i], 3)}"

    def __str__(self):
        targets = '\n\n'.join([self.get_target_data(i) for i in range(len(self.targets))])
        return f"BANK: {self.bank}\nSTART_PRICE: {self.entry}\nSTOP_PRICE: {self.close}\n\n{targets}"


def read_data(filename):
    f = open(filename, "r")
    data = f.read()
    f.close()
    return data


def parse_data(data):
    seperated_data = data.split('-----')
    result_list = []
    for ind, current_deal in enumerate(seperated_data):
        if len(''.join(current_deal.split())) == 0:
            continue

        bank_ind = current_deal.find('Bank')
        entry_ind = current_deal.find('Entry')
        target_ind = current_deal.find('Target')
        close_ind = current_deal.find('Close')

        bank = float(current_deal[bank_ind:current_deal.find('\n', bank_ind) - 3].split(": ")[1])
        entry = float(current_deal[entry_ind:current_deal.find('\n', entry_ind) - 3].split(": ")[1])
        target = [float(tar[:-3]) for tar in current_deal[target_ind:current_deal.find('\n',
                                                                                           target_ind)].split(": ")[1].split(';')]
        close = float(current_deal[close_ind:current_deal.find('\n', close_ind) - 3].split(": ")[1])

        result_list.append(StrategyDeal(bank, entry, target, close))

    result_string = '\n\n-----\n\n'.join([str(current_list) for current_list in result_list])

    return result_string


def write_data(file_name, data):
    with open(file_name, 'w') as f:
        f.write(data)


def main():
    content = read_data('deals.txt')
    result = parse_data(content)
    write_data('out.txt', result)


if __name__ == '__main__':
    main()