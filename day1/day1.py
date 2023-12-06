import argparse
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, required=True, dest="infile")
    args = parser.parse_args()

    if not os.path.exists(args.infile):
        print("Input file does not exist.")

    word_to_num = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    total_sum = 0

    with open(args.infile, 'r') as f:
        for line in f:
            first_num = None
            last_num = None
            for i, char in enumerate(line):
                char_num_exists = False
                if char.isnumeric():
                    if first_num is None:
                        first_num = char
                    last_num = char
                else:
                    for entry in word_to_num.keys():
                        line_slice = line[i:i+len(entry)]
                        if entry == line_slice:
                            char_num_exists = word_to_num[entry]
                            break
                    if char_num_exists:
                        if first_num is None:
                            first_num = char_num_exists
                        last_num = char_num_exists

            conjoined_num = int(f"{first_num}{last_num}")
            total_sum += conjoined_num
            # print(line.strip())
            # print(conjoined_num)

    print(total_sum)

if __name__ == "__main__":
    main()
