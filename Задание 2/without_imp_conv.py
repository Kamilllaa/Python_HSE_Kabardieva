def prepare_title_value(data):
    title = data.pop(0).strip().split(',')
    return title, data


def prepare_data_for_json(title, values):
    result = []
    for value in values:
        to_dict = dict(zip(title, value.split(",")))
        json_dicts = []
        for key in to_dict:
            json_dicts.append('\n\t"{key}": "{value}"'.format(key=key, value=to_dict[key]))

        result.append("\n" + "{" + ",".join(json_dicts) + "\n}")

    result = "[" + ", ".join(result) + "\n]"
    return result


class Converter:
    def __init__(self, csv_path, json_path):
        self.csv_path = csv_path
        self.json_path = json_path

    def read_data(self):
        with open(self.csv_path, "r", newline="") as f:
            read_data = f.read().splitlines()
            f.close()
        return prepare_title_value(read_data)

    def write_data(self, write_data):
        with open(self.json_path, "w") as f:
            f.write(write_data)
        return write_data


csv_path = "./input.csv"
json_path = "./output.json"
converter = Converter(csv_path, json_path)
title, values = converter.read_data()
data = prepare_data_for_json(title, values)
converter.write_data(data)
