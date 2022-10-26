class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.maxSofFar = 0

        def recurse(s, i, arr):
            # print(">>", i, len(arr), maxSofFar)
            if i >= len(arr):
                # print(">>", self.maxSofFar)
                if len(set(s)) == len(s):
                    self.maxSofFar = max(self.maxSofFar, len(s))
                    # print("here", self.maxSofFar, s)
                return
            recurse(s, i+1, arr)
            if len(set(s+arr[i])) == len(s+arr[i]):
                recurse(s + arr[i], i+1, arr)

        recurse("", 0, arr)
        return self.maxSofFar