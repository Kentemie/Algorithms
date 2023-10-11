# You are given an array of words where each word consists of lowercase English letters.

# wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order 
# of the other characters to make it equal to wordB.

    # For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".

# A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is 
# a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

# Return the length of the longest possible word chain with words chosen from the given list of words.



# Work backwards to find the longest chain: abcd -> abd -> ab -> b , abcd -> abc -> ab -> b , abcd -> bcd and so on.

def longestStrChain(words):
    words_set = set(words)
    memo = {}

    def DFS(word):
        if word not in words_set:
            return 0
        if word in memo:
            return memo[word]
        
        memo[word] = 1

        for i in range(len(word)):
            next_word = word[:i] + word[i + 1:]
            memo[word] = max(memo[word], 1 + DFS(next_word))

        return memo[word]
    
    return max(DFS(word) for word in words)


words = ["a","b","ba","bca","bda","bdca"]
words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
words = ["a","ac","acy","aucy","abucy","abaucy","abacucy","abacfucy","abacyfucy","abacyfucey","vabacyfucey","vabacyfbucey","vaubacyfbucey","vaubacyfdbucey","dvaubacyfdbucey","dvaubaccyfdbucey","a","ae","aey","ayey","ayeyd","adyeyd","avdyeyd","yavdyeyd","yadvdyeyd","yadvydyeyd","yadxvydyeyd","yadxvydbyeyd","yaydxvydbyeyd","yaydxvydbyceyd","yaydxvvydbyceyd","yaydxfvvydbyceyd","a","va","ava","eava","euava","euxava","euaxava","euavxava","euavvxava","eufavvxava","eufavvxazva","eufavvxcazva","eufavvvxcazva","eufdavvvxcazva","eubfdavvvxcazva","eubfdavvvxxcazva","a","ae","eae","eaze","beaze","ubeaze","ubeavze","ubeauvze","ubeauuvze","xubeauuvze","xubeabuuvze","xubeabuuvzze","xubeabuuvzzze","bxubeabuuvzzze","bxubeabuuvzzzey","bxubeabubuvzzzey","a","ba","cba","cbca","cbcay","cybcay","cybcday","cxybcday","cvxybcday","cvzxybcday","cvzxybecday","cvzxybecdayz","cvzxybecddayz","cvzxybeecddayz","cbvzxybeecddayz","cbvzxyubeecddayz","a","ab","azb","adzb","adzbf","adzbff","adzdbff","dadzdbff","dadfzdbff","dazdfzdbff","dazdfzdzbff","dazdfzdzbffb","dazddfzdzbffb","edazddfzdzbffb","edazddfczdzbffb","edazddfczdzebffb","a","af","ayf","dayf","dayfz","dayfzz","dauyfzz","ddauyfzz","ddauyfzzf","ddauyefzzf","ddauzyefzzf","ddauzyezfzzf","ddauzcyezfzzf","ddaduzcyezfzzf","ddaduzcyezefzzf","ddaduzccyezefzzf","a","ea","eda","eyda","euyda","euydza","eudydza","ueudydza","ueuddydza","ueuddydzaf","ueuyddydzaf","uveuyddydzaf","uveuydbdydzaf","uveuydbdydzabf","uveuydbddydzabf","uveuydbddydzvabf","a","ba","baa","ybaa","ydbaa","ydabaa","ydeabaa","uydeabaa","fuydeabaa","fuydeabaaz","fuydeaabaaz","fuydeaabaeaz","fuydeaabaeayz","fuydeaabaeayaz","fuydeaabaeaayaz","fuydeaabaeafayaz","a","ca","xca","xcxa","xcyxa","xucyxa","xucyxfa","xucyxxfa","xucyxxfaa","xucyxxfaca","xucyxxfuaca","xucyxxfuayca","xucxyxxfuayca","xucxdyxxfuayca","zxucxdyxxfuayca","zxucxdyxxfuaayca","a","au","uau","vuau","yvuau","yvuacu","yvuaucu","yvvuaucu","yvvuauzcu","yvvuazuzcu","yavvuazuzcu","yavvuafzuzcu","yavvuafzuzcuu","yavvuafzfuzcuu","yadvvuafzfuzcuu","yadvvuafzfuxzcuu","a","aa","aaz","eaaz","eaxaz","eaxavz","eadxavz","xeadxavz","xeaduxavz","xdeaduxavz","xdeaduxbavz","xdeaduxbavuz","xdeaduxbavuyz","xdeaduxbcavuyz","xdeaduxbcaxvuyz","xdeaduxbcaaxvuyz","a","ac","ace","avce","avcea","afvcea","afuvcea","afuvcead","afuvceadd","afyuvceadd","afyuvceaedd","afyuvceaexdd","afyuvceaexddx","avfyuvceaexddx","avfyufvceaexddx","avfyufvceaexvddx","a","za","zya","zyau","zyauu","zyauuv","zfyauuv","xzfyauuv","exzfyauuv","exzfyabuuv","eaxzfyabuuv","exaxzfyabuuv","fexaxzfyabuuv","fexaxzfxyabuuv","fexaxzfxyabuuvy","fexaxvzfxyabuuvy","a","ad","aud","aued","auecd","auedcd","ayuedcd","ayuedccd","ayuedccda","ayuedccdae","ayuedccddae","ayuedccddaex","aybuedccddaex","aybuedccfddaex","ayvbuedccfddaex","ayuvbuedccfddaex","a","da","eda","edad","edazd","ebdazd","ebdazfd","evbdazfd","evfbdazfd","evbfbdazfd","evbfbdazfdf","evbfbdazfduf","zevbfbdazfduf","zevbfbdazzfduf","zevxbfbdazzfduf","zevxbfbdazzfdufz","a","aa","aua","auau","auxau","auxauc","auxaubc","auxfaubc","auzxfaubc","azuzxfaubc","azuezxfaubc","yazuezxfaubc","yazueczxfaubc","yaazueczxfaubc","yadazueczxfaubc","yadazueczxfaubbc","a","xa","xax","xdax","xdbax","xdbaux","xdbbaux","xdabbaux","xxdabbaux","xxxdabbaux","xxxdeabbaux","xxxdeabbauxx","xxxdeaxbbauxx","xxxdceaxbbauxx","xaxxdceaxbbauxx","xaxxfdceaxbbauxx","a","ua","uax","uuax","uuavx","uuavxx","uubavxx","uubaxvxx","uubaxdvxx","uubaxdvyxx","uucbaxdvyxx","vuucbaxdvyxx","vuucbuaxdvyxx","vuucabuaxdvyxx","vuucdabuaxdvyxx","vuucdabuaxdvyxxb","a","ab","fab","fabu","fabzu","vfabzu","vfabzau","vfabzaub","vfabvzaub","yvfabvzaub","yvfabvzauyb","yvbfabvzauyb","yvbfabvezauyb","yvbfabveezauyb","yvbfabveezauyyb","yvbfabveezauyyab","a","ae","aee","aeue","aeuce","aeucee","aeudcee","aeudcaee","aeudcaeee","aeudcaeeee","aeudcafeeee","aeudcafeeeec","xaeudcafeeeec","xaeudcafeeeeyc","xaeudcafeeeveyc","xaeudcafeeeaveyc","a","ba","fba","fbda","fbdva","fbedva","fbedbva","fbcedbva","fbcedbvaa","fbcaedbvaa","fbcaedbvaaa","afbcaedbvaaa","zafbcaedbvaaa","zafbcavedbvaaa","zafbacavedbvaaa","zazfbacavedbvaaa","a","va","yva","yvya","yvyda","yvybda","yvybdab","yvybdaby","yvcybdaby","dyvcybdaby","dyvfcybdaby","dyvyfcybdaby","dyvyfacybdaby","adyvyfacybdaby","adfyvyfacybdaby","adfyvyfacybdabfy","a","az","vaz","vfaz","fvfaz","fvfavz","fvfavza","fxvfavza","fxavfavza","fxavvfavza","fxavfvfavza","xfxavfvfavza","xfxcavfvfavza","xfxcavfvfauvza","vxfxcavfvfauvza","vxfxcavfvfxauvza","a","za","zba","zaba","zabda","zaebda","zaebday","zaeabday","zaeabdauy","zaeabdaauy","zaeabdaauyc","zaeabdaauyyc","zaeabdavauyyc","zaezabdavauyyc","zaezabdavauyycy","yzaezabdavauyycy","a","fa","fca","fcav","fcdav","fcdaav","fcdaaxv","fcdaaxyv","ufcdaaxyv","ufcdaaxyvv","ufcdaxaxyvv","ufcdaxaxyvuv","ufcdaxaxdyvuv","ufcdaxaxdyyvuv","ufcdaxaxdyyvduv","ufcvdaxaxdyyvduv","a","ca","caa","caca","fcaca","yfcaca","yfacaca","yfacyaca","ycfacyaca","ycfacyazca","ycbfacyazca","ycbfacyazcca","ycbfacyazecca","ycbfacyazeccav","ycbcfacyazeccav","ycbcfacyauzeccav"]
words = ["x"]
words = ["u","v","u","z","v","v","x","x","x","x"]
words = ["uvvyzyuvuuxxyyz"]
words = ["a","b","ba","abc","abd","bdca"]

print(longestStrChain(words))