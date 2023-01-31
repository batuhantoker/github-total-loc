# Total lines of code in public repositories of a Github user

This script helps you in analyzing the repository details of the specified Github user. The tool fetches details of user's repositories (default number of repositories is all available repositories) such as: 
* the total number of files
* lines
* blank lines
* comments 
* lines of code 

in various languages using the [CodeTabs API](https://codetabs.com/). 

![case1](https://user-images.githubusercontent.com/55883119/215811615-944ec762-c016-4c5d-9660-d72e699fc862.png)
![final](https://user-images.githubusercontent.com/55883119/215811629-7e092b12-7114-49fd-bf67-654578561ac9.png)
![output](https://user-images.githubusercontent.com/55883119/215811642-ad89588f-6036-4be1-9ed9-da68d03bec4d.png)


After fetching the details, it returns the total statistics of the user for the first specified number of repositories in alphabetical order and plots the details using the specified plotting method (default kind='bar' and to_plot='total_lines_of_code').

## Getting started

To use this tool, you need to have python installed in your system. You can download [python](https://www.python.org/downloads/) from the official website: 

## Installation

Get the code by

```sh
git clone https://github.com/batuhantoker/github-total-loc.git
```
    

## Prerequisites

To run this script, you need to install the following packages:

* requests
* pandas
* matplotlib
* scienceplots

or simply:
```sh
pip install -r requirements.txt
```
## Usage

You can run the script by providing the Github username as the first argument:

```sh
python total_LOC.py <username> [number_of_repos]
```

where, username is the Github username and number_of_repos is the optional argument to specify the number of repositories to be analyzed (default value is all available repositories up to 1000).


## License

[MIT](https://choosealicense.com/licenses/mit/)
