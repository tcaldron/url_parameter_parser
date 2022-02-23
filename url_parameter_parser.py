## url_parameter_parser v1.0
## Written by Taylor Caldron at Climb Marketing
## Questions or suggestions: taylor@climbmarketing.com

import url_parameter_parser_functions

def main():

    # Start by parsing our arguments
    namespace = url_parameter_parser_functions.parse_arguments()

    # Checking for invalid file formats
    if not (namespace.o.endswith(".xlsx") or namespace.o.endswith(".csv")):
        print("Error: Specified output file must be .xlsx or .csv format")
        quit()

    # Get our list of URLs from the input file
    url_set = url_parameter_parser_functions.process_input(namespace.inputFileName)

    # Execute parsing function which returns a list of parameters
    # as well as the parsed URL data
    parameter_set_alpha, parsed_data = url_parameter_parser_functions.url_parse(url_set)

    # Giving some simple feedback before writing to file
    print(f"Identified {len(parameter_set_alpha)} unique URL parameters in " +
         f"{len(url_set)} URLs. Writing to output to {namespace.o}.")
    
    # Writing to file
    url_parameter_parser_functions.output_parsed_data(namespace.o, parameter_set_alpha, parsed_data)


if __name__ == '__main__':
    main()