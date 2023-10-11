# You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one
# flight. Reconstruct the itinerary in order and return it.

# All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid 
# itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.


def findItinerary(tickets):
    flight_map = {}

    for src, dest in tickets:
        flight_map.setdefault(src, []).append(dest)

    for _, dest in flight_map.items():
        dest.sort(reverse = True)

    result = []

    def DFS(src):
        dest_list = flight_map.get(src, [])

        while dest_list:
            next_dest = dest_list.pop()
            DFS(next_dest)

        result.append(src)

    DFS("JFK")

    return result[::-1]



tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
# tickets = [["JFK","ATL"],["ATL","JFK"]]
# tickets = [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]

print(findItinerary(tickets))