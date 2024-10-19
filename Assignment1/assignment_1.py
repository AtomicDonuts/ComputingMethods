#!/usr/bin/python3
"""test module for displayin the character frequency in a text
"""

import argparse
import string
import time

from loguru import logger
from matplotlib import pyplot as plt

STARTING_TIME = time.thread_time()


def time_passed():
    """display time passed from the start of the script
    """
    logger.debug(
        f"It\'s passed {round(time.thread_time() - STARTING_TIME,7)}"/
        " seconds since the execution of the script")


def print_dict(_dict):
    """prints the dictonary
    """
    return "".join([f"{iter[0]}: {iter[1]}\n" for iter in list(zip(_dict.keys(), _dict.values()))])


def store_file(file_path):
    """store the data from the file given by file_path
    """
    with open(file_path, encoding="utf-8") as file:
        data = file.read()
    return data


def skip_file_lines(data, skip):
    """skips a # of lines from the data given

        Arguments:
                data: str
                skip: (int,int) first int is for skipping line
                                from the top of the file
                                second int is for skipping line
                                from the bottom of the fil

    """
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
    """if the given file is a guteberg ebook text file it return the
       the number of line to skip to get the ebook without License and
       other the gutenberg preamble
    """
    data = store_file(file_path)
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
    """plot the dict in an histogram
       if output path is given, the plot
       will be saved in the given path
    """
    plt.title("Character Frequency")
    plt.bar(data_dict.keys(), data_dict.values(), color="orange")
    if output:
        plt.savefig(output)
        logger.debug(f"File Saved in {output}")
    else:
        logger.debug("Plotting on screen...")
        plt.show()


def text_stats(data):
    """prints the text stats
    """
    logger.info(
        f"This text has {len([a for a in data if a in string.ascii_letters])} characters")
    logger.info(f"This text has {len(data.splitlines())} lines")
    logger.info(f"This text has {len(data.split())} words")


def save_dict(text_output, file_to_write):
    """save the dict to text_output
    """
    with open(text_output, "+w", encoding="utf-8") as save:
        save.write(print_dict(file_to_write))


def _formatting_output_name(freq_type, path, skipline):
    """format the string for a compact way
    """
    if skipline != (0, 0):
        return f"{freq_type}_{path[:-4]}_skip{skipline}.txt"
    return f"{freq_type}_{path[:-4]}.txt"


def charcount(file_path, l_skip, char_numb, hist, output, file_info):
    """it count all the character in the text given by file_path
       it skips l_skip[0] line from top and l_skip[1] line from
       the bottom.
    """
    char_dict = {a: 0 for a in string.ascii_lowercase}
    data = store_file(file_path)
    if l_skip != (0, 0):
        data = skip_file_lines(data, l_skip)
    book_lines = [line.lower() for line in data.splitlines()]
    for line in book_lines:
        for chara in line:
            if chara in string.ascii_lowercase:
                char_dict[chara] += 1
    char_tot = sum(char_dict.values())
    char_dict_norm = {a: char_dict[a] /
                      char_tot for i, a in enumerate(char_dict)}
    if char_numb:
        output_text_path = _formatting_output_name("Number", file_path, l_skip)
        logger.info(f"Printing frequencies...\n{print_dict(char_dict)}")
        logger.info(f"Saving frequencies in to {output_text_path} ...")
        save_dict(output_text_path, char_dict)
    else:
        output_text_path = _formatting_output_name("Freq", file_path, l_skip)
        logger.info(f"Printing frequencies...\n{print_dict(char_dict_norm)}")
        logger.info(f"Saving frequencies in to {output_text_path} ...")
        save_dict(output_text_path, char_dict_norm)
        logger.debug(
            f"The sum of all the individual frequencies is {sum(char_dict_norm.values())}")
    if file_info:
        text_stats(data)
    if hist:
        plot_freq(char_dict_norm, output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Python Script that displays the characters"/
        "frequencies in a text file submitted via CLI")
    parser.add_argument("file_path",    help="path of the selected file")
    parser.add_argument("--file-info", "-i",  action='store_true',
                        help="shows total # of characters, lines and words in the text")
    parser.add_argument("--char-numb", "-n",  action='store_true',
                        help="show characters total count instead of frequencies")
    parser.add_argument('--gutenberg', "-g",  action='store_true',
                        help="detect starting and ending line of gutenberg project "/
                        "ebooks and automaticly skips preamble and license of the book")
    parser.add_argument('--histogram', "-H",  action='store_true',
                        help="plot a histogram of the character frequencies on screen")
    parser.add_argument("--output", "-o", nargs='?',    const="Histogram.pdf",
                        metavar="OUTPUT_PATH",  default=False,
                        help="Save the histogram in OUTPUT_PATH, default path is "\
                            "'Histogram.pdf'. --histogram is required to save the output file")
    parser.add_argument("--skip-lines", "-sl", nargs=2,   metavar=('SKIP_TOP', 'SKIP_BOT'),
                         default=(0, 0),
                         help="skip SKIP_TOP line(s) from the top of the "\
                            "text and SKIP_BOT from the bottom of the text")
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
            "The --histogram argument is required for the --output argument"/
            f" '{args.output}' file will not be created nor displayed")
    charcount(args.file_path, skip_lines, args.char_numb,
              args.histogram, args.output, args.file_info)
    time_passed()
