from pathlib import Path
import json


def read_data(file_name, field):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    # get current working directory path
    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name

#2
import json

def read_data(filename, field):
    with open("sequential.json", "r") as f:
        data = json.load(f)
        if field not in data:
            return None

        return data[field]

def linear_search(data, target):

    #path = "sequential.json"
    # with open(path, "r") as f:
    #     data = json.load(f)
    position = []
    for i in range(len(data)):      #n
        if data[i] == target:       #n
            position.append(i)      #od 0 - n
    result = {"positions": position, "count": len(position)}
    return result


def binary_search(sequence, target):
    left = 0
    right = len(sequence) - 1

    while left <= (len(sequence) - 1):
        stred = (left + right) // 2

        if sequence[stred] == target:
            return stred
        elif sequence[stred] < target:
            left = stred + 1
        else:
            right = stred - 1

    return None

def main():
    unordered = read_data(filename = "sequential.json", field = "unordered_numbers")
    print(unordered)
    target = 5
    linear_result = linear_search(unordered, target)
    print(linear_result)

    ordered_data = read_data("sequential.json", "ordered_numbers")

    binary_result = binary_search(ordered_data, target)
    print(binary_result)

if __name__ == "__main__":
    main()


#3

def pattern_search(sequence, pattern):

    position = set()

    n = len(sequence)
    m = len(pattern)

    for i in range(n - m + 1):
        match = True

        for j in range(m):
            if sequence[i + j] != pattern[j]:
                match = False
                break

        if match:
            position.add(i)
    return position




