
import unittest

from simple import read_file, get_commits, get_authors, get_author_totals, get_active_days, create_totals_list, get_change_totals, get_active_hours, get_changes, update_dict

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
        
    def test_author_totals(self):
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
        self.assertEqual('Thomas', authors[0])
        
    def test_totals_list_create(self):
        init_total_list = create_totals_list(self.data)
        self.assertEqual(10, len(init_total_list))
        self.assertEqual('Alan', init_total_list[9]['author'])          
        self.assertEqual(0, init_total_list[9]['additions'])
        self.assertEqual(0, init_total_list[9]['deletions'])
        self.assertEqual(0, init_total_list[9]['modifications'])
        self.assertEqual(0, init_total_list[9]['replacements'])
    
    def test_number_of_changes(self):
        changed_paths = self.data[3:data.index('',1)]
        additions, deletions, modifications, replacements = get_changes(changed_paths)
        self.assertEqual(2, additions)
        self.assertEqual(2, deletions)
        self.assertEqual(0, modifications)
        self.assertEqual(0, replacements)
        
    def test_update_dict(self):
        change_totals = create_totals_list(self.data)
        changed_paths = self.data[3:self.data.index('',1)]
        author = 'Thomas'
        update_dict(author, changed_paths, change_totals)
        self.assertEqual('Thomas', change_totals[0]['author'])          
        self.assertEqual(2, change_totals[0]['additions'])
        self.assertEqual(2, change_totals[0]['deletions'])
        self.assertEqual(0, change_totals[0]['modifications'])
        self.assertEqual(0, change_totals[0]['replacements'])
        
    def test_author_change_totals(self):
        change_totals = get_change_totals(self.data)
        self.assertEqual(10, len(change_totals))
        self.assertEqual('Alan', change_totals[9]['author'])          
        self.assertEqual(9, change_totals[9]['additions'])
        self.assertEqual(6, change_totals[9]['deletions'])
        self.assertEqual(15, change_totals[9]['modifications'])
        self.assertEqual(0, change_totals[9]['replacements'])

    def test_number_of_active_hours(self):
        active_hours = get_active_hours(self.data)
        self.assertEqual(24, len(active_hours))
        self.assertEqual(4, active_hours[17])
        
if __name__ == '__main__':
    unittest.main()
