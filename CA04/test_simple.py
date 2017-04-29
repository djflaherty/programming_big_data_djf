
import unittest

from simple import read_file, get_commits, get_authors, get_author_totals, get_active_days, create_totals_list, get_change_totals

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
        
    def test_author_total_commits(self):
        author_totals = get_author_totals(self.data)
        self.assertEqual(10, len(author_totals))
        self.assertEqual(191, author_totals['Thomas'])
        
    def test_number_of_active_days(self):
        active_days = get_active_days(self.data)
        self.assertEqual(5, len(active_days))
        self.assertEqual(95, active_days['Fri'])

    def test_number_of_authors(self):
        authors = get_authors(self.data)
        self.assertEqual(10, len(authors))
        
    def test_author_total_list_init(self):
        init_total_list = create_totals_list(self.data)
        self.assertEqual(10, len(init_total_list))
        
    def test_author_change_totals(self):
        change_totals = get_change_totals(self.data)
        self.assertEqual(10, len(change_totals))
        self.assertEqual('Alan', change_totals[9]['author'])          
        self.assertEqual(9, change_totals[9]['additions'])
        self.assertEqual(6, change_totals[9]['deletions'])
        self.assertEqual(15, change_totals[9]['modifications'])
        self.assertEqual(0, change_totals[9]['replacements'])

if __name__ == '__main__':
    unittest.main()
