from set import Set
import unittest


class SetTest(unittest.TestCase):

    def test_init(self):
        test_set = Set(['Person1','Person2','Person3','Person4','Person5'])
        assert test_set.data.length() == 5  # Length of set is 5

    def test_has_duplicates(self):
        test_set = Set(['Person1','Person2','Person2','Person4','Person5'])
        assert test_set.data.length() == 4  # Length of set is 4 since Person 2 can't be repeated

    def test_contains(self):
        test_set = Set(['Person1','Person2','Person3','Person4','Person5'])
        assert test_set.length() == 4  # should be 4
        assert test_set.contains('Person1') is True
        assert test_set.contains('NotPerson') is False  # NotPerson is not in  the set

    def test_add(self):
        test_set = Set()
        test_set.add('Person1')
        assert test_set.length() == 1
        assert test_set.contains('Person1') is True  # Person1 is in the set
        test_set.add('Person2')
        assert test_set.length() == 2  # set has 2
        test_set.add('Person2') # No duplicates
        assert test_set.length() == 2  # Unchanged


    def test_remove(self):
        test_set = Set(['Person1','Person2','Person3','Person4','Person5'])
        assert test_set.length() == 5
        test_set.remove('Person3')
        assert test_set.length() == 4  # Removed Person3 and set is smaller


    def test_union(self):
        test_set = Set(['Person1','Person2','Person3','Person4','Person5'])
        other_set = Set(['a', 'b', 'c'])
        assert test_set.union(other_set).length() == 8  # the union should have 7 elements

    def test_union_with_duplicates(self):
        test_set = Set(['Person1','Person2','Person3','Person4','Person5'])
        other_set = Set(['Person1'])
        assert test_set.union(other_set).length() == 5  # Person1 is a repeated element

    def test_intersect(self):
        test_set = Set(['Person1','Person2','Person3','Person4','Person5'])
        other_set = Set(['Person1'])
        assert test_set.intersection(other_set).length() == 1  # 1 intersecting value


    def test_difference(self):
        test_set = Set(['Person1','Person2','Person3','Person4','Person5'])
        other_set = Set(['a', 'b', 'c', 'd'])
        assert test_set.difference(other_set).length() == 5

    def test_is_subset_true(self):
        test_set = Set(['Person1','Person2','Person3','Person4','Person5'])
        other_set = Set(['Person2', 'Person3'])
        assert other_set.is_subset(set) is True  # is subset
        other_set = Set(['a', 'b', 'c'])
        assert test_set.is_subset(other_set) is False # not subset


if __name__ == '__main__':
    unittest.main()
