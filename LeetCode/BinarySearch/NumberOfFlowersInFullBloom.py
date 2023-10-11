# You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi] means the ith flower will be in
# full bloom from starti to endi (inclusive). You are also given a 0-indexed integer array people of size n, where people[i]
# is the time that the ith person will arrive to see the flowers.

# Return an integer array answer of size n, where answer[i] is the number of flowers that are in full bloom when the ith 
# person arrives.


# Algorithm: 
    # For any given time t, the number of flowers blooming at time t is equal to the number of flowers that have started
    # blooming minus the number of flowers that have already stopped blooming.
    # Use binary search to obtain these values efficiently


def fullBloomFlowers(flowers: list[list[int]], people: list[int]) -> list[int]:
    start_blooming: list[int] = sorted(start for start, _ in flowers)
    end_blooming: list[int] = sorted(end for _, end in flowers)
    cache: dict[int, int] = {}

    def bi_left(time: int) -> int:
        low: int = 0
        high: int = len(end_blooming)

        while low < high:
            mid = (low + high) // 2

            if end_blooming[mid] < time:
                low = mid + 1
            else:
                high = mid

        return low
    
    def bi_right(time: int) -> int:
        low: int = 0
        high: int = len(start_blooming)

        while low < high:
            mid = (low + high) // 2

            if time < start_blooming[mid]:
                high = mid
            else:
                low = mid + 1

        return low
    
    res: list[int] = []

    for time in people:
        if time in cache:
            res.append(cache[time])
        else:
            res.append(ans := bi_right(time) - bi_left(time))
            cache[time] = ans

    return res
    


flowers = [[1,6],[3,7],[9,12],[4,13]]
people = [2,3,7,11]

flowers = [[1,10],[3,3]]
people = [3,3,2]

print(fullBloomFlowers(flowers, people))