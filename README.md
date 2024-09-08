
# cis6930fa24 -- Assignment0 -- 

**Name: Ronit Bali**

# Assignment Description

This is my assignment 0 submission. My python package extracts data from the FBI Wanted API "https://www.fbi.gov/wanted/api". I have used the Python "request" library to retrieve information about wanted people for FBI. I have used the REST GET request to retrieve first 20 records of information. I have incorporated a variable which denotes the page number, so that the user can enter custom page number for data retrieval. Each page record contains several details, however with this assignment the only fields to be retrieved were **title** which describes the wanted persons name or an event, **subjects** which states the reason for the wanted person and **field_offices** which describes the FBI office assigned to the case. The main purpose of the assignment is to build a python function which collects elements from a given page and represents them in **thorn character "þ"** separated format. For example, output from a page could look like this:

    BORIS YAKOVLEVICH LIVSHITSþCounterintelligenceþnewyork
    JESUS DE LA CRUZ - LYNN, MASSACHUSETTSþViCAP Missing Personsþ


# How to install
If the package is locally stored on the system, then it can be installed directly by specifying the path

    pipenv install /path

To install the package in editable mode to make changes which are immediately reflected without reinstalling, use -e before the file path

    pipenv install -e /path

## How to run

In the Python package, the user can run the file by creating a command line Python file that takes a page parameter which corresponds to the FBI API page, or can specify the file location. 

The **"--page** parameter will be used to specify the page number of the FBI API

    pipenv run python main.py --page <integer>

The **--file location** parameter should contain the location of the json file to be used for testing. Only one parameter can be specified

    pipenv run python main.py --file <file-location>

## Functions


#### main.py

*parse_func()* - This function is used to pass the command line arguments to functions. I have used *argparse*, which is the command-line parsing module in the Python standard library. The tester can either run the page number or specify the file location while running the program using command prompt.

*api_call()* - This function checks if the parse_func() function returns the page number or the file location specified. If page number is entered, then an API request to the website is recorded. If the file location is specified, then it is loaded locally and imported using json.load().

*main()* - This function runs a loop for 20 times and extracts the title, subjects and field_offices fields in the specified format and prints them.

    {title}{thorn}{subjects}{thorn}{field_offices}


#### test_page.py

*test_download()* - This function tests whether the data request was successful and asserts that the response status code is 200 (successful request code).

*test_title()* - This function tests whether the *title* field is successfully extracted and matches the mock output mentioned. 

*test_subjects()* - This function tests whether the *subjects* field is successfully extracted and matches the mock output mentioned. 

*test_field_offices()* - This function tests whether the *field offices* field is successfully extracted and matches the mock output mentioned. 

*test_thorn()* - This function tests whether all fields have been printed in the specified thorn separated format i.e. match the mock output mentioned.

  
## Bugs and Assumptions

There shouldn't be any bugs encountered if installed and run properly. However some assumptions can be kept in mind:

1) Entering a --page number value more than the maximum number of pages in the fbi API will simply not print anything as output. 
2) For testing, I am mocking the fbi api using "Mock" and "patch" from "unittest" so that we can test the code without needing to call the api. This can lead to Assertion error if expected call not found. 
3) The tests are made using custom mock data and custom page number.
4) All required libraries and packages should be installed with correct versions to avoid runtime errors. 
5) If using a custom file for testing, the file should have the fields mentioned above as in the fbi API, or else will give an error while running.