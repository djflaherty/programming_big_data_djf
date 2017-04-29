
def read_file(changes_file):
    # use strip to strip out spaces and trim the line.
    data = [line.strip() for line in open(changes_file, 'r')]
    return data

def get_commits(data):
    #list of dictionaires with commit details
    sep = 72*'-'
    commits = []
    current_commit = None
    index = 0
    while index < len(data):
        try:
            # parse each of the commits and put them into a list of commits
            details = data[index + 1].split('|')
            # the author with spaces at end removed.
            commit = {'revision': details[0].strip(),
                'author': details[1].strip(),
                'date': details[2].strip(),
                'number_of_lines': details[3].strip().split(' ')[0]
            }
            # add details to the list of commits.
            commits.append(commit)
            index = data.index(sep, index + 1)
        except IndexError:
            break
    return commits
    
def get_authors(data):
    #dictionary with authors name and how many commits they've done
    #eg. authors = {'Thomas': 191, 'Vincent': 26}
    sep = 72*'-'
    authors = {}
    index = 0
    while index < len(data):
        try:
            # parse each of the authors and put them into a dictionary with the number of commits they've done
            #get the author name with spaces at end removed
            author = data[index + 1].split('|')[1].strip()
            #check if author is already in the dictionary
            if author not in authors:
                authors[author] = 1
            else:
                authors[author] = authors[author] + 1
            index = data.index(sep, index + 1)
        except IndexError:
            break
    return authors
    
def get_active_days(data):
    #dictionary with days of the week and number of commits
    #eg. active_days = {'Mon': 53, 'Tue': 80}
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
            #check if weekday is already in the dictionary
            if weekday not in active_days:
                active_days[weekday] = 1
            else:
                active_days[weekday] = active_days[weekday] + 1
            index = data.index(sep, index + 1)
        except IndexError:
            break
    return active_days

if __name__ == '__main__':
    # open the file - and read all of the lines.
    changes_file = 'changes_python.log'
    data = read_file(changes_file)
    commits = get_commits(data)
    authors = get_authors(data)
    active_days = get_active_days(data)

    # print the number of lines read
    print(len(data))
    print(commits[0])
    print(commits[1]['author'])
    print(len(commits))
    print(authors)
    print(active_days)