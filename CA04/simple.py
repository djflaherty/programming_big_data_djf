
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

if __name__ == '__main__':
    # open the file - and read all of the lines.
    changes_file = 'changes_python.log'
    data = read_file(changes_file)
    commits = get_commits(data)
    authors = get_authors(data)

    # print the number of lines read
    print(len(data))
    print(commits[0])
    print(commits[1]['author'])
    print(len(commits))
    print(authors)