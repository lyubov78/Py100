INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    ...  # TODO перезаписать содержимое одного файла в другой


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILE) as file:
        for current_line in file:
            print(current_line, end="")
