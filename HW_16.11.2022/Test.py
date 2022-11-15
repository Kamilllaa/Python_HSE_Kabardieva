from converter_by_class import ImpConverter
from selfmadeConv import Converter, prepare_row
import unittest
import json


class TestCsvJsonConverter(unittest.TestCase):

    csv = "./input.csv"
    json = "./output.json"
    selfmade_converter = Converter(csv, json)
    import_converter = ImpConverter(csv, json)

    def test_read(self):
        self.assertTrue(self.self_converter.read_data())
        self.assertTrue(self.lib_converter.read())

    def test_write(self):
        data = self.lib_converter.read()
        written_data = self.lib_converter.write(data)

        title, values = self.self_converter.read_data()

        data = prepare_row(title, values)
        check_data = self.self_converter.write_data(data)
        self.assertEqual(written_data, check_data)

    def test_row_to_pretty(self):
        data = self.lib_converter.read()
        data_lib = json.dumps(data)

        title, values = self.self_converter.read_data()
        data_self = prepare_row(title, values)
        self.assertEqual(data_lib, data_self)



if __name__ == '__main__':
    unittest.main()
