
import unittest

from simple import get_commits, read_file

class TestCommits(unittest.TestCase):

    def setUp(self):
        #runs at the very start, reads in the file so all other tests can use it
        self.data = read_file('changes_python.log')

    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))

    def test_number_of_commits(self):
        commits = get_commits(self.data)
        self.assertEqual(422, len(commits))

    def test_first_commit(self):
        commits = get_commits(self.data)
        self.assertEqual('Thomas', commits[0]['author'])
        self.assertEqual('r1551925', commits[0]['revision'])
        
    def test_number_of_authors(self):
        authors = get_authors.(self.data)
        self.assertEqual(10, len(authors))
        self.assertEqual(191, authors['Thomas'])

if __name__ == '__main__':
    unittest.main()
