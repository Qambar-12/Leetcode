class TimeMap:

    def __init__(self):
        self.keyStore = {}  # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, [])

        #BINARY SEARCH b/c : All the timestamps timestamp of set are strictly increasing.
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] == timestamp:
                return values[m][0]
            elif values[m][1] < timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res