from imp_conv import ImportConverter
from without_imp_conv import Converter, prepare_data_for_json
import unittest
import json


class TestCsvJsonConverter(unittest.TestCase):

    csv = "./input.csv"
    json = "./output.json"
    selfmade_converter = Converter(csv, json)
    import_converter = ImportConverter(csv, json)

    def read(self):
        self.assertTrue(self.selfmade_converter.read_data())
        self.assertTrue(self.import_converter.read_data())

    def write(self):
        data = self.selfmade_converter.read_data()
        written_data = self.import_converter.write_data(data)

        title, values = self.selfmade_converter.read_data()

        data = prepare_data_for_json(title, values)
        check_data = self.selfmade_converter.write_data(data)
        self.assertEqual(written_data, check_data)

    def row(self):
        data = self.import_converter.read_data()
        data_lib = json.dumps(data)

        title, values = self.selfmade_converter.read_data()
        data_self = prepare_data_for_json(title, values)
        self.assertEqual(data_lib, data_self)



if __name__ == '__main__':
    unittest.main()
