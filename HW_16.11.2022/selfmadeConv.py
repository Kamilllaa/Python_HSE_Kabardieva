def prepare_data(data):
    title = data.pop(0).strip().split(',')
    return title, data


def prepare_row(title, rows):
    result = []
    for row in rows:
        pivot = "{"
        to_json_dict = dict(zip(title, row.split(",")))
        result_list = []
        for key in to_json_dict:
            result_list.append('\n\t"{key}": "{value}"'.format(key=key, value=to_json_dict[key]))

        pivot += ",".join(result_list) + "\n}"
        result.append("\n" + pivot)

    result = "[" + ", ".join(result) + "\n]"
    return result


class Converter:
    def __init__(self, csv_path, json_path):
        self.csv_path = csv_path
        self.json_path = json_path

    def read_data(self):
        with open(self.csv_path, "r", newline="") as f:
            r_data = f.read().splitlines()
            f.close()
        return prepare_data(r_data)

    def write_data(self, data):
        with open(self.json_path, "w") as f:
            f.write(data)
        return data


def main():
    csv_path = "./input.csv"
    json_path = "./output.json"
    converter = Converter(csv_path, json_path)
    title, rows = converter.read_data()

    data = prepare_row(title, rows)
    converter.write_data(data)


if __name__ == "__main__":
    main()

