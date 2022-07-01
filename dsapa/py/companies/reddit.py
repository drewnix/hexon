'''
Implement a data structure that supports the following operations efficiently:

Insert : Insert an interval (x,y)
Find k : Given a point k, determine if k exists in any previously inserted interval


* Class
  * insert(start, end) ->
    * loop thru existing ranges
    * check for overlap, max(end points ranges

  * find(x)
    * iterate through our ranges, check if x in range
     * range(0, end) -> lazy evaluated,


      4, 5, 6, 7
2, 3, 4, 5
             7, 8, 9, 10


insert:        4, 5, 6, 7
existing 2, 3, 4, 5, 6

4, 7

insert: 1, 2  4, 5, 6, 7, 8
existing   2, 3, 4, 5, 6

start 1, end 8


2, 6


12, 13, 14


'''


class IntervalSet:
    def __init__(self):
        # self.num_range = set() # [(4,7) ,  (9, 10)]
        self.ranges = list()

    def insert(self, start: int, end: int) -> None:
        for r in ranges:
            # new range set of numbers
            #
            if end >= r[0] and end <
            for i in range(r[0], r[1]):

        # iterate thru our ranges
        # for i in range(start, end):   # O(N)
        #     self.num_range.add(i) # O(1)

    def find(self, num):

        # while l <= r:
        #.   mid = l + (r - l ) // 2
        #
        #.   if self.ranges[mid][0] <= num and num <= self.ranges[mid][1]

        if i in self.num_range:  # O(1)
            return True
        else:
            return False

# Example usage
interval_set = IntervalSet()
interval_set.insert(2,5)
interval_set.insert(7,10)

print(interval_set.find(3)) # should return True
print(interval_set.find(6)) # should return False


