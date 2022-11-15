import json
import csv


class ImpConverter:

    def __init__(self, csv_path, json_path):
        self.input_path = csv_path
        self.output_path = json_path

    def read(self):
        with open(self.input_path, 'r', newline='') as f:
            return list(csv.DictReader(f, delimiter=','))

    def write(self, content):
        content = json.dumps(content)
        with open(self.output_path, 'w') as f:
            f.write(content)


def main():
    csv_path = './input.csv'
    json_path = './output.json'
    conv = ImpConverter(csv_path=csv_path, json_path=json_path)

    data = conv.read()
    conv.write(data)



def load_json():
    file_path = './output.json'
    with open(file_path, 'r') as f:
        data = f.read()
        data = json.loads(data)


if __name__ == "__main__":
    main()
