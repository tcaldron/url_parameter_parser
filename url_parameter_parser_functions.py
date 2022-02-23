import argparse
import csv
import xlsxwriter

def parse_arguments():
    """Parsing the arguments and/or displaying help information"""
    
    parser = argparse.ArgumentParser(description="""
    This script takes a list of URLs as input and outputs a spreadsheet
    with URL paramters parsed into separate columns. This makes it easier to 
    sort URLs by parameter values, identify likely duplicates, etc. Input
    can be either a .txt file list or a single-column .csv file.""",
    epilog="Feel free to email taylor@climbmarketing.com for further help.")
    
    parser.add_argument("inputFileName")

    parser.add_argument("--o", metavar="outputFileName", default="output.csv", 
    type=str, help="""file name for output (can be in either csv or xlsx
        format). Defaults to output.csv if left unspecified.""")
    
    namespace = parser.parse_args()
    
    return namespace


def process_input(inputFileName):
    """Simply takes the input and puts it in a list"""
    
    urls_to_process = [] # Empty list for URLs
    with open(inputFileName, "r", newline="\n") as f:
        f_reader = csv.reader(f)
        for row in f_reader:
            urls_to_process.append("".join(row))
    return urls_to_process
            

def url_parse(url_set):
    """The heart of the script, does the actual parsing of URLs"""
    
    # Setting up an empty set for deduplicated parameter names
    parameter_set = set()

    # Master data set
    parsed_data = []

    for count, url in enumerate(url_set):

        # Setting up dictionary for each URL and keeping track of which number it is
        url_dictionary = {}
        
        # First we split by ? to separate the "slug" from the string of parameters
        parameters_only = url.split("?")
        url_dictionary["slug"] = parameters_only[0]
        
        # Then we create an array consisting of the slug and each of the defined parameters
        parsed_array = [parameters_only[0]] + parameters_only[1].split("&")
        for parameter in parsed_array:
            
            # We then split the defined parameters into parameter variable and value
            parameter_pair = parameter.split("=")
            if len(parameter_pair) > 1:
                parameter_set.add(parameter_pair[0])
                url_dictionary[parameter_pair[0]] = parameter_pair[1]
        
        parsed_data.append(url_dictionary)
        
    # Creating an alphabetically sorted list from our total set of parameters
    parameter_set_alpha = sorted(parameter_set)
    parameter_set_alpha.insert(0, "slug")

    return parameter_set_alpha, parsed_data


def output_parsed_data(filename, parameter_set_alpha, parsed_data):
    """Writing the output to a file"""
    
    # First for an Excel file
    if filename.endswith(".xlsx"):
        
        # Creating a spreadsheet with a default name, change as necessary
        # I prefer no URLs in my spreadsheet so I turned off that conversion
        workbook = xlsxwriter.Workbook(filename, {'strings_to_urls': False})
        worksheet = workbook.add_worksheet()

        # Creating column headers for each unique parameter
        for count, parameter_name in enumerate(parameter_set_alpha):
            worksheet.write(0, count, parameter_name)

        for count, url in enumerate(parsed_data):
            for param,value in url.items():
                worksheet.write(count+1, parameter_set_alpha.index(param), value)
            
        # Saving and exiting workbook
        workbook.close()

    # Slightly simpler for a CSV file
    if filename.endswith(".csv"):
        with open(filename, "w", newline="") as csvfile:
            dict_writer = csv.DictWriter(csvfile, fieldnames=parameter_set_alpha)
            dict_writer.writeheader()
            for url in parsed_data:
                dict_writer.writerow(url)

    return