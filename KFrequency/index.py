def topKFrequent(nums, k):
    freq = [[] for i in range(len(nums) + 1)]
    hashVal = {
        1: 3,
        2: 1,
        3: 2,
    }
    for n, c in hashVal.items():
        freq[c].append(n)
    print(freq)
    output = []
    inc = 0
    for i in reversed(range(len(nums))):
        if len(freq[i]) > 0:
            for j in freq[i]:
                output.append(j)
            inc += 1
        if inc == k:
            break

    print(output)


topKFrequent([1, 1, 1, 2, 2, 3], 2)
