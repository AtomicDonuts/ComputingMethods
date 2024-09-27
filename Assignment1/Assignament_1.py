#!/usr/bin/python3
import argparse
import math
import string
import time

from loguru import logger
from matplotlib import pyplot as plt

STARTING_TIME = time.thread_time()

def how_much_time():
    logger.debug(f"Its passed {round(time.thread_time() - STARTING_TIME,7)} seconds since the execution of the script")

def print_dict(_dict):
    return "".join([f"{iter[0]}: {iter[1]}\n" for iter in list(zip(_dict.keys(),_dict.values()))])

def open_file(file_path,skip):
    with open(file_path) as file:
        data = file.read()
    if skip != 0:
        logger.info(f"Skipping {skip} line(s)")
    return "\n".join(data.splitlines()[int(skip):])

def plot_freq(data_dict,output):
    plt.title("Character Frequencies")
    plt.bar(data_dict.keys(),data_dict.values(), color = "orange")
    if output:    
        plt.savefig(output)
        logger.debug(f"File Saved in {output}")
    else:
        logger.debug("Plotting on screen...")
        plt.show()
    
def text_stats(file_path,skip):
    data = open_file(file_path,skip)
    logger.info(f"This text has {len([a for a in data if a in string.ascii_letters])} characters")
    logger.info(f"This text has {len(data.splitlines())} lines")
    logger.info(f"This text has {len(data.split())} words")
    
def save_text(text_output,file_to_write):
    with open(text_output,"+w") as save:
        #[save.write(f"{iter[0]}: {iter[1]}\n") for iter in list(zip(file_to_write.keys(),file_to_write.values()))]
        save.write(print_dict(file_to_write))

def formatting_output_name(freq_type,path,skipline):
    if skipline:
        return f"{freq_type}_{path[:-4]}_skip{skipline}.txt"
    else:
        return f"{freq_type}_{path[:-4]}.txt"

def charcount(file_path,l_skip,char_numb,hist,output):
    char_dict = {a: 0 for a in string.ascii_lowercase}
    data = open_file(file_path,l_skip)
    book_lines = [line.lower() for line in data.splitlines()]
    for line in book_lines:
        for chara in line:
            if chara in string.ascii_lowercase:
                char_dict[chara] += 1
    char_tot = sum(char_dict.values())
    char_dict_norm = {a: char_dict[a]/char_tot for i,a in enumerate(char_dict)}
    if char_numb:
        output_text_path = formatting_output_name("Number",file_path,l_skip)
        logger.info(f"Printing freq...\n{print_dict(char_dict)}")
        logger.info(f"Saving frequencies in to {output_text_path} ...")
        save_text(output_text_path,char_dict)
    else:
        output_text_path = formatting_output_name("Freq",file_path,l_skip)
        logger.info(f"Printing freq...\n{print_dict(char_dict_norm)}")
        logger.info(f"Saving frequencies in to {output_text_path} ...")
        save_text(output_text_path,char_dict_norm)
        logger.debug(f"The sum of all the individual freq. is {sum(char_dict_norm.values())}")
    if hist:
        plot_freq(char_dict_norm,output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description= "Python Script that counts the character frequencies in a text file submitted via CLI")
    parser.add_argument("file_path",    help= "path of the selected file")
    parser.add_argument("--file-info",  action='store_true',    help= "shows total # of characters, lines and words of the text")
    parser.add_argument("--char-numb",  action='store_true',    help= "show characters total count instead of frequencies")
    parser.add_argument('--histogram',  action='store_true',    help= "plot a histogram of the character frequencies on screen, if you want to save it use --output NAME_FILE")
    parser.add_argument("--output" ,default= False, help= "name of the output file, --histogram is required")
    parser.add_argument("--skip-lines", default= 0, help= "skip # of lines from the text")
    args = parser.parse_args()
    logger.debug(args)
    if ( not args.histogram and args.output):
        logger.warning("The --histogram argument is required for the --output argument, histogram file will not be created nor displayed") 
    charcount(args.file_path,args.skip_lines,args.char_numb,args.histogram,args.output)
    if args.file_info:
        text_stats(args.file_path,args.skip_lines)
    how_much_time()
