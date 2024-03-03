import json
from prettytable import PrettyTable
from googleSheet import get_data
import yaml


def getFormatData(array):
    prettyTable = PrettyTable()
    prettyTable.field_names = array[0]
    array.pop(0)
    prettyTable.add_rows(array)

    htmlData = prettyTable.get_html_string(header=True, indent=2,
                                           attributes=
                                           {
                                               "id": "my_table",
                                               "class": "styled-table"
                                           }
                                           )
    htmlData = htmlData + '<link type="text/css" rel="stylesheet" href="styles.css" media="all" />'
    with open('pages/rss-feed-data.html', 'w', encoding="utf-8") as file:
        file.write(htmlData)
    textData = prettyTable.get_string(header=True, indent=2)
    with open('rss-feed-data.txt', 'w', encoding="utf-8") as file:
        file.write(textData)
    jsonData = prettyTable.get_json_string(sort_keys=False, header=False, indent=2)
    with open('rss-feed-data.json', 'w', encoding="utf-8") as file:
        file.write(jsonData)
    yamlData = yaml.dump(json.loads(jsonData), sort_keys=False, explicit_start=True, default_flow_style=False)
    with open('rss-feed-data.yaml', 'w', encoding="utf-8") as file:
        file.write(yamlData)


def main():
    actualData = get_data()
    array = actualData['values']
    getFormatData(array)


if __name__ == '__main__':
    main()
