class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = ([], [])
            
        timestamps, values = self.map[key]
        timestamps.append(timestamp)
        values.append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key in self.map:
            timestamps = self.map[key][0]
            left = 0
            right = len(timestamps) - 1

            while left <= right:
                i = (left + right) // 2

                if timestamps[i] > timestamp:
                    right = i - 1
                elif timestamps[i] < timestamp:
                    left = i + 1
                else:
                    return self.map[key][1][i]

            if timestamps[left-1] < timestamp:
                return self.map[key][1][left-1]

        return ""
