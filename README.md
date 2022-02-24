# xmlscrape

This incredibly simple Python 3 script helps you make sense of a set of URLs with numerous URL parameters. For example, let's say you've just been handed a list of 500,000 URLs for a large website - maybe from Google Search Console, a Screaming Frog crawl, a backlink database like ahrefs, etc. Most large sites use URL parameters extensively; they may be used in faceted navigation, internal site search, session tracking, geolocation, etc. 

It's tricky to sort 500,000 URLs with 100 unique parameters in something like Excel, especially if the parameters aren't present in every URL or can appear in different orders. This Python script solves the issue by simply breaking each of the parameters into a separate column in a spreadsheet. This way you can easily sort, filter, etc. based on parameter values. 

Many thanks to the team at [Climb](https://www.climbmarketing.com) for the support in developing this and our other tools.  

## Installation

Installation (and the instructions for it) have been kept as simple and plain English as possible in order to support those that are newer to Python and GitHub.

Start out by making sure you have Python 3 installed. If you want to check, open up a terminal window on your computer and type "python3 --version." If it says Python 3.6 or higher, you're good to go. If not, go here: <https://www.python.org/downloads/>

Click the green button on this page (on the upper right) and download the zip file. Then open a terminal in the same directory as the zip file's contents (on a Mac, you can right click the folder and look through the options for "New Terminal at Folder") and run:

```bash
pip install -r requirements.txt
```

## Usage

You can run the script with a simple "python3 url_parameter_parser.py [file containing list of URLs]" in the terminal. The list of URLs can be a .txt, .csv, or anything else so long as it's just a list of URLs separated by a new line without any additional formatting.

```bash
python3 url_parameter_parser.py input.txt # simplest usage, outputs to "output.csv" by default
python3 url_parameter_parser.py input.txt --o output.xlsx # outputs the extracted URLs to an Excel file (or a csv file, if that's the file extension you use)
```

Some notes:

* The output file extension needs to be either .xlsx (Excel) or .csv (comma-separated value)
* It outputs to the same directly you're running the script in, unless otherwise specified
* Feedback in the terminal will show the total URL count and total parameters found
* Parameters are presented in alphabetical order

## To Do

* [ ] Figure out how it handles other character sets (only tested with US English so far)
* [ ] Maybe create Excel input options (not sure if useful)

## License

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
