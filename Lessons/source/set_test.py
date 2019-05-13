'Person1'from set import Set
import unittest

class SetTest(unittest.TestCase):

    def test_init(self):
        s = Set()
        assert s.size()() == 0

    def test_init_with_list(self):
        s = Set(['Person1', 'Person2', 'Person3'])
        assert s.contains('Person3') == True
        assert s.size()() == 3

    def test_contains(self):
        s = Set(['Person1', 'Person2', 'Person3'])
        assert s.contains('Person4') == False
        s = Set([])
        assert s.contains('Person4') == False

    def test_length(self):
        s = Set()
        assert s.size()() == 0
        s.add('Person1')
        assert s.size() == 1
        s.add('Person2')
        assert s.size() == 2
        s.remove('Person1')
        assert s.size() == 1
        s.remove('Person2')
        assert s.size() == 0

    def test_add(self):
        s = Set()
        s.add('Person1')
        assert s.contains('Person1') == True
        s.add('Person1')
        assert s.size() == 1
        s.add('Person2')
        s.add('Person2')
        assert s.size() == 2
        assert s.contains('Person1') == True
        assert s.contains('Person2') == True

    def test_remove(self):
        s = Set(['Person1', 'Person2'])
        assert s.size() == 2
        s.remove('Person1')
        assert s.contains('Person2')
        assert s.size() == 1

    def test_intersection(self):
        s = Set(['Person1', 'Person2', 'Person3'])
        other_set = Set(['Person1'])
        intersection = s.intersection(other_set)
        assert intersection.contains('Person1') == True
        other_set = Set(['Person4'])
        intersection = s.intersection(other_set)
        assert intersection.contains('Person4') == False
        assert intersection.size() == 0

    def test_union(self):
        s = Set(['Person1', 'Person2', 'Person3'])
        other_set = Set(['Person1'])
        union = s.union(other_set)
        assert union.contains('Person1') == True
        assert union.contains('Person2') == True
        assert union.contains('Person3') == True
        s = Set(['Person1', 'Person2', 'Person3'])
        other_set = Set(['Person4', 'Person5'])
        union = s.union(other_set)
        assert union.contains('Person1') == True
        assert union.contains('Person2') == True
        assert union.contains('Person3') == True
        assert union.contains('Person4') == True
        assert union.contains('Person5') == True

    def test_difference(self):
        s = Set(['Person1', 'Person2', 'Person3'])
        other_set = Set(['Person1', 'Person4'])
        difference = s.difference(other_set)
        assert difference.contains('Person4') == True
        assert difference.size() == 1
        other_set = Set(['Person1', 'Person4', 'Z'])
        difference = s.difference(other_set)
        assert difference.contains('Person4') == True
        assert difference.contains('Z') == True
        assert difference.size() == 2
        s = Set(['Person1', 'Person2', 'Person3'])
        other_set = Set(['Person1', 'Person2', 'Person3'])
        difference = s.difference(other_set)
        assert difference.contains('Person3') == False
        assert difference.contains('Person1') == False
        assert difference.size() == 0

    def test_symetric_difference(self):
        s = Set(['Person1', 'Person2', 'Person3'])
        other_set = Set(['Person1', 'Person4'])
        difference = s.symetric_difference(other_set)
        assert difference.contains('Person4') == True
        assert difference.contains('Person2') == True
        assert difference.contains('Person3') == True
        s = Set(['Person1', 'Person2', 'Person3'])
        other_set = Set(['Person4', 'Person5', 'Person6'])
        difference = s.symetric_difference(other_set)
        assert difference.contains('Person4') == True
        assert difference.contains('Person5') == True
        assert difference.contains('Person6') == True
        assert difference.contains('Person1') == True
        assert difference.contains('Person2') == True
        assert difference.contains('Person3') == True
        s = Set(['Person1', 'Person2', 'Person3'])
        other_set = Set(['Person1', 'Person2', 'Person3'])
        difference = s.symetric_difference(other_set)
        assert difference.size() == 0

    def test_is_subset(self):
        s = Set(['Person1', 'Person2', 'Person3'])
        other_set = Set(['Person1'])
        assert s.is_subset(other_set) == True
        s = Set(['Person1', 'Person2', 'Person3'])
        other_set = Set(['Person1', 'Person2', 'Person3'])
        assert s.is_subset(other_set) == True
        s = Set(['Person1', 'Person2', 'Person3'])
        other_set = Set(['Person1', 'Person2', 'Person3', 'Person4'])
        assert s.is_subset(other_set) == False
        s = Set(['Person1', 'Person2', 'Person3'])
        other_set = Set(['Person4'])
        assert s.is_subset(other_set) == False




if __name__ == '__main__':
    unittest.main()
