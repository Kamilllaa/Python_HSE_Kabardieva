import json
import csv


class ImportConverter:

    def __init__(self, csv_path, json_path, delimiter=','):
        self.csv_input = csv_path
        self.json_output = json_path
        self.delimiter = delimiter

    def read_data(self):
        with open(self.csv_input, 'r', newline='') as f:
            return list(csv.DictReader(f, delimiter=self.delimiter))

    def write_data(self, content):
        content = json.dumps(content, indent=4)
        with open(self.json_output, 'w') as f:
            f.write(content)


csv_path = './input.csv'
json_path = './output.json'
import_converter = ImportConverter(csv_path=csv_path, json_path=json_path, delimiter=',')
csv_data = import_converter.read_data()
import_converter.write_data(csv_data)

