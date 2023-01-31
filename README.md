# Total lines of code in public repositories of a Github user

This script helps you in analyzing the repository details of the specified Github user. The tool fetches details of user's repositories (default number of repositories is all available repositories) such as: 
* the total number of files
* lines
* blank lines
* comments 
* lines of code 

in various languages using the [CodeTabs API](https://codetabs.com/). 

After fetching the details, it returns the total statistics of the user for the first specified number of repositories in alphabetical order and plots the details using the specified plotting method (default kind='bar' and to_plot='total_lines_of_code').

## Getting started

To use this tool, you need to have python installed in your system. You can download [python](https://www.python.org/downloads/) from the official website: 

## Installation

Get the code by

```sh

```
    

## Prerequisites

To run this script, you need to install the following packages:

* requests
* pandas
* matplotlib

## Usage

You can run the script by providing the Github username as the first argument:

```sh
python total_LOC.py <username> [number_of_repos]
```

where, username is the Github username and number_of_repos is the optional argument to specify the number of repositories to be analyzed (default value is all available repositories up to 1000).


## License

[MIT](https://choosealicense.com/licenses/mit/)
