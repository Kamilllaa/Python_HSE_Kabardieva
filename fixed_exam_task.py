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
               f"Percent: {self.get_target_percents()[i]}%\n" \
               f"Bank: {self.get_target_banks()[i]}"

    def __str__(self):
        targets = '\n\n'.join([self.get_target_data(i) for i in range(len(self.targets))])
        return f"BANK: {self.bank}\nSTART_PRICE: {self.entry}\nSTOP_PRICE: {self.close}\n\n{targets}"


def read_data(filename):
    f = open(filename, "r")
    data = f.read()
    f.close()
    return data


def parse_data(data):
    separated_data = data.split('-----')
    result_list = []
    for ind, current_deal in enumerate(separated_data):
        if len(''.join(current_deal.split())) == 0:
            continue
        current_deal_filtered = list(filter(lambda x: len(x) != 0, current_deal.split('\n')))
        bank = float("".join(filter(lambda x: x.startswith("B"), current_deal_filtered)).split(": ")[1][:-3])
        entry = float("".join(filter(lambda x: x.startswith("E"), current_deal_filtered)).split(": ")[1][:-3])
        close = float("".join(filter(lambda x: x.startswith("C"), current_deal_filtered)).split(": ")[1][:-3])
        targets_filtered = "".join(filter(lambda x: x.startswith("T"), current_deal_filtered)).split(": ")[1].split("; ")
        target = [float(i[:-3]) for i in targets_filtered]

        result_list.append(StrategyDeal(bank, entry, target, close))

    result_string = '\n\n-----\n\n'.join([str(current_list) for current_list in result_list])
    return result_string


def write_data(file_name, data):
    f = open(file_name, 'w')
    result = f.write(data)
    f.close()
    return result


def main():
    content = read_data('deals.txt')
    result = parse_data(content)
    write_data('out.txt', result)


if __name__ == '__main__':
    main()