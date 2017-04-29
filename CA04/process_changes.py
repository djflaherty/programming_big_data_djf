
# open the file - and read all of the lines.
changes_file = 'C:/Users/deird/OneDrive/Documents/College Work/02 Programming for Big Data/CA04/changes_python.log'

#my_file = open(changes_file, 'r')
#data = my_file.readlines()

# use strip to strip out spaces and trim the line.
data = [line.strip() for line in open(changes_file, 'r')]

# print the number of lines read
print(len(data))

sep = 72*'-'

# create the commit class to hold each of the elements - I am hoping there will be 422
# otherwise I have messed up.
class Commit(object):
    'class for commits'
   
    def __init__(self, revision = None, author = None, date = None, comment_line_count = None, changes = None, comment = None):
        #these are public class variables
        self.revision = revision
        self.author = author
        self.date = date
        self.comment_line_count = comment_line_count
        self.comment = comment

	
    def get_commit_comment(self):
        return 'svn merge -r' + str(self.revision-1) + ':' + str(self.revision) + ' by ' \
                + self.author + ' with the comment ' + ','.join(self.comment) \
                + ' and the changes ' + ','.join(self.changes)

commits = []
current_commit = None
index = 0 #first position

# Algorithm:
# Search for separator
# Read line for revision, author, date, comment, line count (this is line 2 but will be index 1 from the position of the separator)
# Read file changes
# Read comment
# Get next commit

author = {}
while True:
    try:
        # parse each of the commits and put them into a list of commits
        current_commit = Commit() #DF: current commit is equal to a blank object
        details = data[index + 1].split('|') #DF: the details are on line 2 but this is index 1 from the position of the separator, pipe is the delimiter for the pieces of info on this line
        current_commit.revision = int(details[0].strip().strip('r'))
        current_commit.author = details[1].strip()
        current_commit.date = details[2].strip()
        current_commit.comment_line_count = int(details[3].strip().split(' ')[0]) #want first entry back to get the number - comes after a space (eg. x lines)
        current_commit.changes = data[index+2:data.index('',index+1)] # the changed paths start at +2 from where my separator is and runs up to where the next empty line is (data is a list of lines, we're looking for an empty string '')
        #print(current_commit.changes)
        index = data.index(sep, index + 1) #search for the separator from index + 1 : runs the search from the next line
        current_commit.comment = data[index-current_commit.comment_line_count:index]
        commits.append(current_commit)
    except IndexError:
        break

print(len(commits))

commits.reverse()      #the list of commits is backwards (oldest commits are at the top), so reverse will put it in chronological order

for index, commit in enumerate(commits):
    print(commit.get_commit_comment())
