# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.

from heapq import heappush, heappop

def reorganizeString(s):
    counter = {}
    for char in s:
        counter[char] = counter.get(char, 0) + 1

    heap = []
    for char, freq in counter.items():
        heappush(heap, (-freq, char))

    reorganized_string = []
    while len(heap) > 1:
        freq1, first_char = heappop(heap)
        freq2, second_char = heappop(heap)
        reorganized_string.append(first_char)
        reorganized_string.append(second_char)
        if freq1 + 1 != 0:
            heappush(heap, (freq1 + 1, first_char))
        if freq2 + 1 != 0:
            heappush(heap, (freq2 + 1, second_char))

    if heap:
        if heap[0][0] < -1:
            return ""
        reorganized_string.append(heappop(heap)[1])

    return "".join(reorganized_string)

s = "tndsewnllhrtwsvxenkscbivijfqnysamckzoyfnapuotmdexzkkrpmppttficzerdndssuveompqkemtbwbodrhwsfpbmkafpwyedpcowruntvymxtyyejqtajkcjakghtdwmuygecjncxzcxezgecrxonnszmqmecgvqqkdagvaaucewelchsmebikscciegzoiamovdojrmmwgbxeygibxxltemfgpogjkhobmhwquizuwvhfaiavsxhiknysdghcawcrphaykyashchyomklvghkyabxatmrkmrfsppfhgrwywtlxebgzmevefcqquvhvgounldxkdzndwybxhtycmlybhaaqvodntsvfhwcuhvuccwcsxelafyzushjhfyklvghpfvknprfouevsxmcuhiiiewcluehpmzrjzffnrptwbuhnyahrbzqvirvmffbxvrmynfcnupnukayjghpusewdwrbkhvjnveuiionefmnfxao"
# s = "baaba"
# s = "aaab"
s = "sfffp"

print(reorganizeString(s))