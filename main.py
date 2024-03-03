from googleSheet import get_data
import yaml


def main():
    actualData = get_data()
    yamlData = yaml.dump(actualData['values'], explicit_start=True, default_flow_style=False)

    breakpoint()


if __name__ == '__main__':
    main()
