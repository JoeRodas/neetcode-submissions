# Algorithm:
# 1. Use a dictionary
    # key -> list of [value, timestamp]
    # Timestamps for each key are stored in sorted order(because they arrive in increasing order).
# 2. set(key, value, timestamp)
# Append [value, timestamp] to the key's list.
# 3. get(key, timestamp):
# If the key does not exist, return ""
# Let arr be the list of [value, timestamp] pairs.
# Perform binary search on timestamps to find the rightmost timestamp t <= timestamp
# If found, return the corresponding value.
# If not found, return ""

class TimeMap:

    def __init__(self):
        self.keyStore = {} # key : list of [val, timestamp]
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])
    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res

        # time O(1) for set() and O(log n) for get().
        # space: O(m * n)