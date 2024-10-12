#!/usr/bin/python3
import argparse
import string
import time

from loguru import logger
from matplotlib import pyplot as plt

STARTING_TIME = time.thread_time()


def how_much_time():
    logger.debug(
        f"It\'s passed {round(time.thread_time() - STARTING_TIME,7)} seconds since the execution of the script")


def print_dict(_dict):
    return "".join([f"{iter[0]}: {iter[1]}\n" for iter in list(zip(_dict.keys(), _dict.values()))])


def open_file(file_path):
    with open(file_path, encoding="utf-8") as file:
        data = file.read()
    return data


def skip_file(data, skip):
    skip = (int(skip[0]), int(skip[1]))
    if (len(data.splitlines()) - skip[0]) <= 0:
        logger.error(
            "skip_top can\'t be more then the total number of lines in the text")
    if (len(data.splitlines()) - skip[1]) <= 0:
        logger.error(
            "skip_bot can\'t be more then the total number of lines in the text")
    if (skip[0] + skip[1]) >= len(data.splitlines()):
        logger.error("The total number of lines skipped can\'t be " /
                     "more the total number of line in the text")
    logger.debug(
        f"Starting from line {skip[0]} and ending at line {len(data.splitlines()) -int(skip[1])}")
    logger.info(
        f"Skipping {skip[0]} line(s) from the top and {skip[1]} line(s) from the bottom")
    return "\n".join(data.splitlines()[int(skip[0]):len(data.splitlines()) - int(skip[1])])


def gutenberg(file_path):
    data = open_file(file_path)
    data = data.splitlines()
    skip = [None, None]
    for i, line in enumerate(data):
        if "*** START OF THE PROJECT GUTENBERG EBOOK" in line:
            skip[0] = i
        if "*** END OF THE PROJECT GUTENBERG EBOOK" in line:
            skip[1] = len(data) - i
    if skip[0] is None:
        logger.warning(
            "Project Gutenberg starting Line not found, setting skip_top to 0")
        skip[0] = 0
    if skip[1] is None:
        logger.warning(
            "Project Gutenberg ending Line not found, setting skip_bot to 0")
        skip[1] = 0
    return skip


def plot_freq(data_dict, output):
    plt.title("Character Frequency")
    plt.bar(data_dict.keys(), data_dict.values(), color="orange")
    if output:
        plt.savefig(output)
        logger.debug(f"File Saved in {output}")
    else:
        logger.debug("Plotting on screen...")
        plt.show()


def text_stats(data):
    logger.info(
        f"This text has {len([a for a in data if a in string.ascii_letters])} characters")
    logger.info(f"This text has {len(data.splitlines())} lines")
    logger.info(f"This text has {len(data.split())} words")


def save_text(text_output, file_to_write):
    with open(text_output, "+w", encoding="utf-8") as save:
        save.write(print_dict(file_to_write))


def formatting_output_name(freq_type, path, skipline):
    if skipline != (0, 0):
        return f"{freq_type}_{path[:-4]}_skip{skipline}.txt"
    else:
        return f"{freq_type}_{path[:-4]}.txt"


def charcount(file_path, l_skip, char_numb, hist, output, file_info):
    char_dict = {a: 0 for a in string.ascii_lowercase}
    data = open_file(file_path)
    if l_skip != (0, 0):
        data = skip_file(data, l_skip)
    book_lines = [line.lower() for line in data.splitlines()]
    for line in book_lines:
        for chara in line:
            if chara in string.ascii_lowercase:
                char_dict[chara] += 1
    char_tot = sum(char_dict.values())
    char_dict_norm = {a: char_dict[a] /
                      char_tot for i, a in enumerate(char_dict)}
    if char_numb:
        output_text_path = formatting_output_name("Number", file_path, l_skip)
        logger.info(f"Printing frequencies...\n{print_dict(char_dict)}")
        logger.info(f"Saving frequencies in to {output_text_path} ...")
        save_text(output_text_path, char_dict)
    else:
        output_text_path = formatting_output_name("Freq", file_path, l_skip)
        logger.info(f"Printing frequencies...\n{print_dict(char_dict_norm)}")
        logger.info(f"Saving frequencies in to {output_text_path} ...")
        save_text(output_text_path, char_dict_norm)
        logger.debug(
            f"The sum of all the individual frequencies is {sum(char_dict_norm.values())}")
    if file_info:
        text_stats(data)
    if hist:
        plot_freq(char_dict_norm, output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Python Script that displays the characters frequencies in a text file submitted via CLI")
    parser.add_argument("file_path",    help="path of the selected file")
    parser.add_argument("--file-info", "-i",  action='store_true',
                        help="shows total # of characters, lines and words in the text")
    parser.add_argument("--char-numb", "-n",  action='store_true',
                        help="show characters total count instead of frequencies")
    parser.add_argument('--gutenberg', "-g",  action='store_true',
                        help="detect starting and ending line of gutenberg project ebooks and automaticly skips preamble and license of the book")
    parser.add_argument('--histogram', "-H",  action='store_true',
                        help="plot a histogram of the character frequencies on screen")
    parser.add_argument("--output", "-o", nargs='?',    const="Histogram.pdf",  metavar="OUTPUT_PATH",  default=False,
                        help="Save the histogram in OUTPUT_PATH, default path is 'Histogram.pdf'. --histogram is required to save the output file")
    parser.add_argument("--skip-lines", "-sl", nargs=2,   metavar=('SKIP_TOP', 'SKIP_BOT'),    default=(
        0, 0), help="skip SKIP_TOP line(s) from the top of the text and SKIP_BOT from the bottom of the text")
    args = parser.parse_args()
    logger.debug(args)
    skip_lines = args.skip_lines
    if args.gutenberg:
        if skip_lines != (0, 0):
            logger.warning(
                "--gutenberg option is active, --skip-lines parameter will be overwritten")
        skip_lines = gutenberg(args.file_path)
    if (not args.histogram and args.output):
        logger.warning(
            f"The --histogram argument is required for the --output argument, '{args.output}' file will not be created nor displayed")
    charcount(args.file_path, skip_lines, args.char_numb,
              args.histogram, args.output, args.file_info)
    how_much_time()
