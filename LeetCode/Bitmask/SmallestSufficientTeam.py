# In a project, you have a list of required skills req_skills, and a list of people. The ith person people[i] contains a list 
# of skills that the person has.

# Consider a sufficient team: a set of people such that for every required skill in req_skills, there is at least one person
# in the team who has that skill. We can represent these teams by the index of each person.

    # For example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].

# Return any sufficient team of the smallest possible size, represented by the index of each person. You may return the answer
# in any order.

# It is guaranteed an answer exists.


# Algorithm

    # Set n to the number of people.
    # Set m to the number of required skills.
    # Declare the hash map skillId.
    # Iterate i from 0 to m−1.
        # Set skillId[req_skills[i]]=i.
    # Declare and initialize the array skillsMaskOfPerson.
    # Iterate i from 0 to n−1.
        # Iterate skill over people[i].
            # Set the bit skillId[skill] in the bitmask skillsMaskOfPerson[i].
    # Declare the array dp of size 2^m and initialize it with the values of 2^n - 1 
    # Set dp[0]=0. (The base case of the DP.)
    # Iterate skillsMask from 1 to 2^m - 1.
        # Iterate i from 0 to n−1.
            # Set smallerSkillsMask=skillsMask∖skillsMaskOfPerson[i].
            # If smallerSkillsMask≠skillsMask.
                # Set peopleMask to dp[smallerSkillsMask] OR 2^i. This is the mask that represents the new team once you add 
                # the current person.
                # Update dp[skillsMask] with peopleMask, if it is better (has fewer bits set).
    # Return the array containing the elements from the bitmask dp[2^m−1].


def smallestSufficientTeam(req_skills, people):
    n = len(people)
    m = len(req_skills)
    skill_id = { skill: i for i, skill in enumerate(req_skills) }
    skills_mask_of_person = [0] * n

    for i in range(n):
        for skill in people[i]:
            skills_mask_of_person[i] |= 1 << skill_id[skill]

    dp = [(1 << n) - 1] * (1 << m)
    dp[0] = 0

    for skills_mask in range(1, 1 << m):
        for i in range(n):
            smaller_skills_mask = skills_mask & ~skills_mask_of_person[i]
            if smaller_skills_mask != skills_mask:
                people_mask = dp[smaller_skills_mask] | (1 << i)
                if people_mask.bit_count() < dp[skills_mask].bit_count():
                    dp[skills_mask] = people_mask

    answer_mask = dp[(1 << m) - 1]
    res = []

    for i in range(n):
        if (answer_mask >> i) & 1:
            res.append(i)

    return res



req_skills = ["java","nodejs","reactjs"]
people = [["java"],["nodejs"],["nodejs","reactjs"]]

req_skills = ["algorithms","math","java","reactjs","csharp","aws"]
people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]

print(smallestSufficientTeam(req_skills, people))