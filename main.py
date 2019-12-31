import sys
import codecs
from argparse import ArgumentParser
import logging

CHAR_LIST = [["¹", "ą"],
             ["æ", "ć"],
             ["ê", "ę"],
             ["³", "ł"],
             ["ñ", "ń"],
             ["œ", "ś"],
             ["Ÿ", "ź"],
             ["¿", "ż"]]


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument("input", type=str, help="path to input text file")
    parser.add_argument("-o", "--output", type=str, help="path where to save converted input file")
    parser.add_argument("-d", "--debug", '--DEBUG', action='store_true', help="set logging to be debug")
    return parser.parse_args()


def convert(input, output):
    input_f = open(input, "r+", encoding="utf-8")
    text = input_f.read()
    input_f.close()

    output_text = ""
    for char in CHAR_LIST:
        logging.debug("Replacing {} with {}".format(char[0], char[1]))
        output_text = text.replace(char[0], char[1])
        text = output_text

    output_f = open(output, "w", encoding="utf-8")
    output_f.write(output_text)
    output_f.close()


def rename_file(input):
    pos = input.rfind('.')
    output = input[:pos] + "_converted" + input[pos:]
    return output


def main():
    args = parse_arguments()
    if args.debug:
        loglevel = logging.DEBUG
    else:
        loglevel = logging.INFO
    logging.basicConfig(format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s', datefmt='%H:%M:%S', level=loglevel)
    logging.info('Starting replacing script')

    if args.output is None:
        args.output = rename_file(args.input)

    convert(args.input, args.output)


if __name__ == "__main__":
    main()
