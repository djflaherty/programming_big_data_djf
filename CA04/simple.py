
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
    # dictionary with authors name and how many commits they've done
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
                # otherwise, increase the number of commits for this author by 1
                authors[author] = authors[author] + 1
            index = data.index(sep, index + 1)
        except IndexError:
            break
    return authors
    
def get_active_days(data):
    # dictionary with days of the week and number of commits
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
    # dictionary with authors name and how many commits they've done
    # eg. authors = {'Thomas': 191, 'Vincent': 26}
    sep = 72*'-'
    authors = []
    index = 0
    while index < len(data):
        try:
            # parse each of the authors and put them into a dictionary with the number of commits they've done
            # get the author name with spaces at end removed
            author = data[index + 1].split('|')[1].strip()
            # check if author is already in the dictionary
            if author not in authors:
                authors.append(author)
            index = data.index(sep, index + 1)
        except IndexError:
            break
    return authors
    
def create_totals_list(data):
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
  
def get_change_totals(data):
    # list of dictionaries with author, additions, deletions and modifications
    sep = 72*'-'
    change_totals = create_totals_list(data)
    index = 0
    while index < len(data):
        try:
            # get the author name with spaces at end removed
            author = data[index + 1].split('|')[1].strip()
            additions = 0
            deletions = 0
            modifications = 0
            replacements = 0
            #print 'Current author: ', author
            
            # get the changed paths 
            # changed paths start at +3 from where the separator is 
            # and run up to where the next empty line is (empty line = '')
            changed_paths = data[index+3:data.index('',index+1)]
            
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
            
            # get dict for this author and update the totals
            for dict in change_totals:
                if dict['author'] == author:
                    dict['additions'] = dict['additions'] + additions
                    dict['deletions'] = dict['deletions'] + deletions
                    dict['modifications'] = dict['modifications'] + modifications
                    dict['replacements'] = dict['replacements'] + replacements
                else:
                    # no match found, move to next dict
                    pass
                       
            # increment the index and move on
            index = data.index(sep, index + 1)
        except IndexError:
            break
    return change_totals



if __name__ == '__main__':
    # open the file - and read all of the lines.
    changes_file = 'changes_python.log'
    data = read_file(changes_file)
    commits = get_commits(data)
    authors = get_authors(data)
    author_totals = get_author_totals(data)
    active_days = get_active_days(data)
   
    totals_list = create_totals_list(data)
    change_totals = get_change_totals(data)

    # print the number of lines read
    # print(len(data))
    # print(commits[0])
    # print(commits[1]['author'])
    # print(len(commits))
    
    print(authors)
    print(author_totals)
    print(active_days)
    print change_totals
  
    