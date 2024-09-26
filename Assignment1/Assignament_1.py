#!/usr/bin/python3
import argparse
import math
import string
import time

from loguru import logger
from matplotlib import pyplot as plt

STARTING_TIME = time.thread_time_ns()

def open_file(file_path):
    with open(file_path) as file:
        data = file.read()
    return data

def plot_freq(data_dict):
    plt.bar(data_dict.keys(),data_dict.values(), color = "orange")
    plt.savefig("CharactersFrequencies.pdf")
    logger.debug("File Saved in \'CharactersFrequencies.pdf\'")

def how_much_time():
    logger.debug(f"Its passed {time.thread_time_ns() - STARTING_TIME} nanoseconds since the execution of the script")

def text_stats(file_path):
    data = open_file(file_path)
    logger.info(f"This text has {len([a for a in data if a in string.ascii_letters])} characters")
    logger.info(f"This text has {len(data.splitlines())} lines")
    logger.info(f"This text has {len(data.split())} words")
    

def charcount(file_path,l_skip,char_numb,hist):
    char_dict = {a: 0 for a in string.ascii_lowercase}
    data = open_file(file_path)
    book_lines = [line.lower() for line in data.splitlines()]
    for line in book_lines[int(l_skip):]:
        for chara in line:
            if chara in string.ascii_lowercase:
                char_dict[chara] += 1
    char_tot = sum(char_dict.values())
    char_dict_norm = {a: char_dict[a]/char_tot for i,a in enumerate(char_dict)}
    if char_numb:
        logger.info(char_dict)
    else:
        logger.info(char_dict_norm)
        logger.debug(sum(char_dict_norm.values()))
    if hist:
        plot_freq(char_dict_norm)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description= "Python Script that counts the character frequencies in a text file submitted via CLI")
    parser.add_argument("file_path",    help= "path of the selecter file")
    parser.add_argument("--file-info",  action='store_true',    help= "shows total # of characters, lines and words of the text")
    parser.add_argument("--char-numb",  action='store_true',    help= "show characters total count instead of frequencies")
    parser.add_argument('--histogram',  action='store_true',    help= "plot a histogram of the character frequencies, it get stored in a pdf file named \'CharactersFrequencies.pdf\'")
    parser.add_argument("--skip-lines", default= 0, help= "skip # of lines from the text")
    args = parser.parse_args()
    #logger.debug(args)
    charcount(args.file_path,args.skip_lines,args.char_numb,args.histogram)
    if args.file_info:
        text_stats(args.file_path)
    how_much_time()
