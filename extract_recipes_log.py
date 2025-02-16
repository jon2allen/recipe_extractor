#!/usr/bin/python3
import os
import sys
import subprocess
import time
import re
import logging
from logging.handlers import RotatingFileHandler

def split_filename(string):
    parts = string.split(' - ')
    if parts:
        return parts[0]
    else:
        return string

# Set up logging
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_file = 'script.log'
log_handler = RotatingFileHandler(log_file, maxBytes=1000000, backupCount=5)
log_handler.setFormatter(log_formatter)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)
logger.propagate = False  # Prevent logging to standard output

# Check for correct number of arguments
if len(sys.argv) < 3:
    logger.error("Usage: {} <file_with_youtube_links> <output_directory> [limit]".format(sys.argv[0]))
    print("Args problem - see log")
    sys.exit(1)

file_with_links = sys.argv[1]
output_directory = sys.argv[2]
limit = int(sys.argv[3]) if len(sys.argv) > 3 else 10  # Default limit to 10 if not provided

# Ensure the output directory exists
if not os.path.isdir(output_directory):
    logger.error("Output directory '{}' does not exist.".format(output_directory))
    sys.exit(1)

logger.info("Starting the program")
logger.info("input file: {} ".format(file_with_links))
logger.info("ouptput dir: {} ".format(output_directory))


# Open the file with YouTube links
with open(file_with_links, 'r') as fh:
    count = 0

    for link in fh:
        link = link.strip()
        if count >= limit:
            logger.info("limit: {} reached".format(limit)) 
            break

        logger.info(f"Processing entry {count + 1}: {link}")

        # Run the command and capture the output
        command = "yt {} | fabric -sp extract_recipe".format(link)
        output = subprocess.getoutput(command)
        lines_to_add = [" ", "### Youtube link ", " ", link, " "]
        output += "\n".join(lines_to_add)

        # Extract the recipe title from the 2nd or 3rd line after the ### Title
        match = re.search(r"### Title(.*?)### Objective", output, re.DOTALL)
        if match:
            filename = match.group(1).strip()  # Remove leading and trailing whitespace
            filename = split_filename(filename)
        else:
            filename = "recipe_{}.txt".format(count)

        # Construct the full path for the output file
        output_file = os.path.join(output_directory, filename)

        # Write the output to the file
        with open(output_file, 'w') as out_fh:
            out_fh.write(output)


        logger.info(f"wrote to file:  {output_file}")
        logger.info(f"Finished processing entry {count + 1}: {link}")

        count += 1
        time.sleep(20)

logger.info("Ending the program")

