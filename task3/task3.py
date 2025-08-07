import json
import argparse

parser = argparse.ArgumentParser(description="Соединение файлов")
parser.add_argument("tests", help="Путь до файла с тестами")
parser.add_argument("values", help="Путь до файла с значениями")
args = parser.parse_args()
t, v = args.tests, args.values

tests = []
with open(t) as f:
    tests = json.load(f)

values = []
with open(v) as f:
    values = json.load(f)

values = values['values']
def fill_values(test_data):
    if isinstance(test_data, dict):
      for key, value in test_data.items():
        if isinstance(value, dict):
          fill_values(value)
        elif isinstance(value, list):
          for i in range(len(value)):
            fill_values(value[i])
        elif isinstance(value, str) and key == 'value':
          for i in range(len(values)):
            if values[i]['id'] == test_data['id']:
              test_data[key] = values[i]['value']

fill_values(tests)

with open("report.json", 'w') as f:
    json.dump(tests, f, indent=4)