from hashtable import HashTable



class Set(object):

    def __init__(self, elements=None):
        """Initialize this Set with the given elements"""

        self.data = HashTable()  #Store data in hashtable

        if elements is not None:
            for element in elements:
                self.add(element)


    def size(self):
        return self.data.size # O1 operation

    def contains(self, element):
        """
        Given an element will return true or false if element in Set
        O(1)
        """
        return self.data.contains(element)

    def add(self, element):
        """Add element to this set, if not present already"""
        # HashTable requires key,value. Sets are essentially just keys,
        # so setting the value to element ensures no confusion in terms of whats in the set
        if self.contains(element):
            return

        self.data.set(element,element)

    def remove(self, element):
        """Remove element from this set, if present, or else raise KeyError"""

        if self.contains(element):
            self.data.delete(element)
        else:
            raise KeyError('Element not found in set.')

    def elements(self):
        """ Iterable list of elements in Set"""

        return self.data.keys() # Keys from hashtable


    def union(self, other_set):
        """Return a new set that is the union of this set and other_set: O(M*N) for iterating over both sets"""

        union = Set(self.elements())

        # Go through other_set and add the keys that are not in the current set
        for key in other_set.elements():
            if union.contains(key):
                continue
            # Key not found in current set
            else:
                union.add(key)

        return union


    def intersection(self, other_set):
        """Return a new set that is the intersection of this set and other_set. Values contained in BOTH sets: O(n)"""

        # Empty set without any values from current or other set because we only want SIMILAR keys
        intersection = Set()

        for key in other_set.elements():

            # Keys matched in current set and other_set
            if self.contains(key):
                intersection.add(key)

            # There was no matching key
            else:
                continue

        return intersection


    def difference(self, other_set):
        """Return a new set that has elments of current set but not other_set"""


        difference = Set()

        for key in other_set.elements():
            if self.contains(key) == False:
                difference.add(key)
        return difference

    def symetric_difference(self, other_set):
            '''Return values unique in current set and other_set'''
        symetric_difference = et()

        for key in other_set.elements():
            if not self.contains(key):
                symetric_difference.add(key)

        for key in self.elements():
            if not other_set.contains(key):
                symetric_difference.add(item)

        return symetric_difference


    def is_subset(self, other_set):
        """
        Return Bool that represents if this set is a subset of the other_set: Best case: O1
        O(n) since we need to iterate over all data in self
        """

        # To be a subset, the current set needs to have smaller length
        if self.size() > other_set.size():
            return False

        # If smaller, check each element to ensure its in the larger set
        for element in self.elements():
            if not other_set.contains(element):
                return False

        # All elements in current set are in the larger set, therefore a subset
        return True
