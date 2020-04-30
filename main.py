"""Polish character replacer

This script allows user to replace weird special characters into normal polish ones in a text file.
This will mostly happen when we are dealing with incorrect encoding of a file.

Before running this script, make sure that your file is converted to UTF-8.
You can do that by editing file in Notepad++ and choosing Encoding->Convert to UTF-8.

If you don't specify path using -o option, script will save it in the same location as
your source file is in with _converted added to the filename.

Examples of use:
python main.py subtitles.txt
python main.py subtitles.txt -o C:\bla\fixed_subtitles.txt
"""

import sys
import codecs
from argparse import ArgumentParser
import logging

CHAR_LIST = [["¹", "ą"],
             ["Æ", "Ć"],
             ["æ", "ć"],
             ["ê", "ę"],
             ["£", "Ł"],
             ["³", "ł"],
             ["ñ", "ń"],
             ["Œ", "Ś"],
             ["œ", "ś"],
             ["", "Ź"],
             ["Ÿ", "ź"],
             ["¯", "Ż"],
             ["¿", "ż"]]


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument("input", type=str, help="path to input text file")
    parser.add_argument("-o", "--output", type=str, help="path where to save converted input file")
    parser.add_argument("-d", "--debug", '--DEBUG', action='store_true', help="set logging to be debug")
    return parser.parse_args()


def convert(input, output):
    #TODO if file is not utf-8 give error and fail the script. Or try to convert it...
    input_f = open(input, "r+", encoding="utf-8", errors='ignore')
    text = input_f.read()
    input_f.close()

    output_text = ""
    for char in CHAR_LIST:
        logging.debug("Replacing {} with {}".format(char[0], char[1]))
        output_text = text.replace(char[0], char[1])
        text = output_text
        #TODO better counting - if in file we had both characters this will give wrong count
        logging.debug("Replaced {} times".format(text.count(char[1])))

    #TODO what if there is already file with that name - you shouldn't overwrite it
    output_f = open(output, "w", encoding="utf-8")
    output_f.write(output_text)
    output_f.close()


def get_new_filename(input):
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
        args.output = get_new_filename(args.input)

    convert(args.input, args.output)
    logging.info('Finished replacing characters. File is in {}'.format(args.output))


if __name__ == "__main__":
    main()
