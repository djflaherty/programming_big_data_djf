"""
B8IT105 Programming for Big Data
Assignment 4 - Analysis on a 5000 line dataset

Submitted by:
Deirdre Flaherty (10349680)
"""
import pandas as pd

def read_file(changes_file):
    # use strip to strip out spaces and trim the line.
    data = [line.strip() for line in open(changes_file, 'r')]
    return data

def get_commits(data):
    # list of dictionaries with commit details
    sep = 72*'-'
    commits = []    #empty list
    index = 0
    while index < len(data):
        try:
            # parse each of the commits and put them into a list of commits
            details = data[index + 1].split('|')
            # add the commit details to the dictionary
            commit = {'revision': details[0].strip(),
                'author': details[1].strip(),
                'date': details[2].strip(),
                'number_of_lines': details[3].strip().split(' ')[0]
            }
            # add the dicionary to the list
            commits.append(commit)
            index = data.index(sep, index + 1)
        except IndexError:
            break
    return commits
    
def get_author_totals(data):
    # dictionary with authors name as key and the total number of commits they've done as value
    # eg. authors = {'Thomas': 191, 'Vincent': 26}
    sep = 72*'-'
    authors = {}
    index = 0
    while index < len(data):
        try:
            # parse each of the authors and put them into a dictionary with the number of commits they've done
            # get the author name with spaces at end removed
            author = data[index + 1].split('|')[1].strip()
            # check if author is already in the dictionary
            if author not in authors:
                # if not, add the author and set the number of commits to 1
                authors[author] = 1
            else:
                # otherwise, increment the number of commits for this author
                authors[author] = authors[author] + 1
            index = data.index(sep, index + 1)
        except IndexError:
            break
    return authors
    
def get_active_days(data):
    # dictionary with days of the week as key and the total number of commits as value
    # eg. active_days = {'Mon': 53, 'Tue': 80}
    sep = 72*'-'
    active_days = {}
    index = 0
    while index < len(data):
        try:
            # parse each of the weekdays and put them into a dictionary along with the number of commits on this day
            # get the full date & time of the commit eg. '2015-11-27 16:57:44 +0000 (Fri, 27 Nov 2015)'
            full_datetime = data[index + 1].split('|')[2]
            # then pull out the weekday (eg. 'Mon') by first splitting on '(' and then splitting on ','
            weekday = full_datetime.split('(')[1].split(',')[0]
            # check if weekday is already in the dictionary
            if weekday not in active_days:
                # if not, add the weekday and set the number of commits to 1
                active_days[weekday] = 1
            else:
                # otherwise, increase the number of commits for this weekday by 1
                active_days[weekday] = active_days[weekday] + 1
            index = data.index(sep, index + 1)
        except IndexError:
            break
    return active_days

def get_authors(data):
    # list of unique authors
    sep = 72*'-'
    authors = []
    index = 0
    while index < len(data):
        try:
            # parse each of the authors and put them into a list
            # get the author name with spaces at end removed
            author = data[index + 1].split('|')[1].strip()
            # check if author is already in the list
            if author not in authors:
                authors.append(author)
            index = data.index(sep, index + 1)
        except IndexError:
            break
    return authors
    
def create_totals_list(data):
    # list of dictionaries with author, additions, deletions, modifications and replacements
    # initially, each dictionary in the list will have the author's name and zeros for all other key/value pairs
    change_totals = []
    change_dict = {}
    authors = get_authors(data)
    for author in authors:
        change_dict = {'author': author,
            'additions': 0,
            'deletions': 0,
            'modifications': 0,
            'replacements': 0
        }
        # add the dictionary to the list
        change_totals.append(change_dict)
    return change_totals  

def get_changes(changed_paths):
    # get the number of additions, deletions, modifications & replacements in the list of changed paths
    additions = 0
    deletions = 0
    modifications = 0
    replacements = 0
    for change in changed_paths:
        change_type = change.split(' ')[0]
        if change_type == 'A':
            additions = additions + 1
        elif change_type == 'D':
            deletions = deletions + 1
        elif change_type == 'M':
            modifications = modifications + 1
        elif change_type == 'R':
            replacements = replacements + 1
    return additions, deletions, modifications, replacements

def update_dict(author, changed_paths, change_totals):
    # function to update the list of dictionaries containing the the change totals per author
    # will get the changes contained in the list of changed_paths and calculate the number of additions, deletions etc to add
    # first, get the number of additions, deletions, modifications & replacements in the list of changed paths
    additions, deletions, modifications, replacements = get_changes(changed_paths)        
    # then get the dict for this author and update the totals
    for dict in change_totals:
        if dict['author'] == author:
            dict['additions'] = dict['additions'] + additions
            dict['deletions'] = dict['deletions'] + deletions
            dict['modifications'] = dict['modifications'] + modifications
            dict['replacements'] = dict['replacements'] + replacements
    return
  
def get_change_totals(data):
    # list of dictionaries with author, additions, deletions, modifications and replacements
    sep = 72*'-'
    # create the initial list of dictionaries with zeros for each author
    change_totals = create_totals_list(data)
    index = 0
    while index < len(data):
        try:
            # get the author name with spaces at end removed
            author = data[index + 1].split('|')[1].strip()
            #print 'Current author: ', author
            
            # get the changed paths 
            # changed paths start at +3 from where the separator is 
            # and run up to where the next empty line is (empty line = '')
            changed_paths = data[index+3:data.index('',index+1)]
            
            # update the dictionary for this author in the list of change totals
            update_dict(author, changed_paths, change_totals)
                       
            # increment the index and move on
            index = data.index(sep, index + 1)
        except IndexError:
            break
    return change_totals

def get_active_hours(data):
    # dictionary with hours as key and the total number of commits as value
    # eg. active_hours = {'17': 53, '18': 80}
    sep = 72*'-'
    hours_list = []
    active_hours = {}
    index = 0
    
    # create a list of hours in the day
    hours_list = range(1,25)
    # create a series with zeros for each hour of the day
    s2 = pd.Series(0,index = hours_list)
    # convert the series to a dictionary
    active_hours = s2.to_dict()
    
    while index < len(data):
        try:
            # parse each of the hours and put them into a dictionary along with the number of commits during this hour
            # get the full date & time of the commit eg. '2015-11-27 16:57:44 +0000 (Fri, 27 Nov 2015)'
            full_datetime = data[index + 1].split('|')[2]
            # then pull out the hour (eg. '16') by first splitting on a space ' ' and then splitting on ':' & convert to int
            commit_hour = int(full_datetime.split(' ')[2].split(':')[0])
            #print(commit_hour)
           
            # increase the number of commits for this hour by 1
            active_hours[commit_hour] = active_hours[commit_hour] + 1

            index = data.index(sep, index + 1)
        except IndexError:
            break
    return active_hours

def output_CSV(s, filename):
    # function to convert a series or list of dicts to a dataframe and output to CSV
    df = pd.DataFrame(s)
    df.to_csv(filename)

if __name__ == '__main__':
    # open the file - and read all of the lines.
    changes_file = 'changes_python.log'
    data = read_file(changes_file)
    commits = get_commits(data)
    author_totals = get_author_totals(data)
    
    # output active_days to a CSV file
    active_days = get_active_days(data)
    s = pd.Series(active_days)
    output_CSV(s, 'active_days.csv')
    
    # output active_hours to a CSV file
    active_hours = get_active_hours(data)
    s = pd.Series(active_hours)
    output_CSV(s, 'active_hours.csv')
    
    # output change_totals to a CSV file
    change_totals = get_change_totals(data)
    output_CSV(change_totals, 'change_totals.csv')
    
    print('3 files output')
    
    # print the number of lines read
    # print(len(data))
    # print(commits[0])
    # print(commits[1]['author'])
    # print(len(commits))
    
    #print(authors)
    #print(author_totals)
    #print(active_days)
    #print(active_hours)
    #print(change_totals)
    
  
    