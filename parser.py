"""
Sample log file parser which will parse the log file, get the IP addressed with their count frequency and export the data to a csv file
"""

import re
import csv
import collections


def log_file_reader(filename):
    
    # Get all IP addresses from the log file
    with open(filename) as f:
        log = f.read()
        regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        ip_list = re.findall(regex, log)
        return ip_list
    
    """ To Read the log file line by line
        log_file = open(filename, "r+")
        for row in log_file:
            print(row)
            regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
            ip_list = re.findall(regex, row)
            print()
            return ip_list
        pass
    """

# Get total count of IPs
def count_ip(ip_list):
    return collections.Counter(ip_list)

def write_to_csv(counter):
    with open('output.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        header = ['IP', 'Count']
        writer.writerow(header)
        for item in counter:
            writer.writerow((item, counter[item]))



if __name__ == "__main__":
    write_to_csv(count_ip(log_file_reader('log')))