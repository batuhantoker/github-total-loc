import requests
import pandas as pd
import matplotlib.pyplot as plt
import scienceplots
import sys
plt.rcParams.update(plt.rcParamsDefault)
plt.style.use(['science','nature','no-latex'])


def repos(username):
    # Use requests library to get the list of repos of the given Github username
    repo_list = requests.get(f'https://api.github.com/users/{username}/repos?page=1&per_page=1000').json()

    # Initialize an empty list to store the names of non-forked repos
    repo_names = []

    # Loop through the list of repos
    for i in repo_list:
        # Check if the repo is not forked
        if i['fork'] == False:
            # If it's not forked, append the repo name to the list of non-forked repos
            repo_names.append(i['name'])

    # Return the list of non-forked repo names
    return repo_names


def get_details(username, repo_list, number_of_repos):
    # Initialize an empty list to store the names of programming languages used in the repos
    list_of_languages = []

    # Initialize an empty dictionary to store the details of programming languages used in the repos
    details = {}

    # Print the information about the script execution
    print(f'The script will evaluate {number_of_repos} repos of user: {username}, in alphabetical order.')

    # Loop through the specified number of repos
    for i in repo_list[:number_of_repos]:
        # Print the name of the repo being accessed
        print(f'Accessing details of repository named : {i}')

        # Get the details of the repo using the codetabs API
        repo_details = requests.get(f'https://api.codetabs.com/v1/loc/?github={username}/{i}').json()

        # Loop through the details of the repo
        for k in repo_details:
            # Check if the language is already present in the list of languages
            if k['language'] in list_of_languages:
                # If the language is already present, update the details of the language in the dictionary
                details[k['language']] = {
                    'total_files': details[k['language']]['total_files'] + k['files'],
                    'total_lines': details[k['language']]['total_lines'] + k['lines'],
                    'total_blanks': details[k['language']]['total_blanks'] + k['blanks'],
                    'total_comments': details[k['language']]['total_comments'] + k['comments'],
                    'total_lines_of_code': details[k['language']]['total_lines_of_code'] + k['linesOfCode']
                }
            else:
                # If the language is not present in the list, add the language to the list and the details to the dictionary
                if k['language'] != 'Total':
                    list_of_languages.append(k['language'])
                    details[k['language']] = {
                        'total_files': k['files'],
                        'total_lines': k['lines'],
                        'total_blanks': k['blanks'],
                        'total_comments': k['comments'],
                        'total_lines_of_code': k['linesOfCode']
                    }

    # Convert the dictionary to a pandas dataframe
    details = pd.DataFrame.from_dict(details)

    # Add a new column in the dataframe to store the sum of all languages
    details['All languages'] = details[list(details.columns)].sum(axis=1)

    # Return the dataframe and the list of programming languages
    return details, list_of_languages


def plot_info(detailed_info, to_plot='total_lines_of_code', plot_kind='bar'):
    """
    This function plots information for given user activity on different programming languages.

    Parameters:
    detailed_info (DataFrame): Contains the user activity information on different programming languages
    to_plot (str, optional): Column name to be plotted. Defaults to 'total_lines_of_code'
    plot_kind (str, optional): Plot type. Defaults to 'bar'

    Returns:
    None
    """
    # Transpose the dataframe to plot columns as languages and index as user activity
    df = detailed_info.drop(['All languages'], axis=1).T
    df = df[to_plot]

    # Set the colors for plotting
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'g']
    fig, ax = plt.subplots()

    # Plot the information
    ax = df.plot(kind=plot_kind, ax=ax, rot=0, stacked=True, color=colors[:len(to_plot)], figsize=(10, 6))
    ax.set_title('Details of user activity', fontsize=20)
    ax.set_xlabel('Languages', fontsize=15)

    ax.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left', fontsize=15)
    fig.tight_layout()



# The main function to run the code
if __name__ == '__main__':
    # Get the username from the first argument of the command line
    username = str(sys.argv[1])
    # Call the repos function to get the list of repository names for the given username
    repo_names = repos(username)

    # Check if the number of repositories to be evaluated is provided in the command line
    if len(sys.argv) > 2:
        number_of_repos = int(sys.argv[2])
    else:
        number_of_repos = len(repo_names)
    # If the number of repositories is more than the available repositories for the given username
    # set the number of repositories to be evaluated as the number of available repositories
    if number_of_repos > len(repo_names):
        print(f'User {username} dont have {number_of_repos} repositories.')
        number_of_repos = len(repo_names)
    # Call the get_details function to get the detailed information about the code statistics
    detailed_info , list_of_languages = get_details(username, repo_names,number_of_repos)

    # Print the total statistics of the user for the first number_of_repos repositories, in alphabetical order
    print(f'\n Total statistics of the user {username} for the first {number_of_repos} repositories, in alphabetical order:')
    print(detailed_info['All languages'].to_string())

    # Plot the detailed information about the code statistics
    plot_info(detailed_info, to_plot=['total_lines_of_code','total_comments','total_blanks'])
    # Print the used programming languages
    print('\n Used languages:')
    print(*list_of_languages, sep=", ")
    #plot_info(detailed_info, to_plot=['total_files'],plot_kind='hbar')
    # Show the plot
    plt.show()




