# You are given two string arrays positive_feedback and negative_feedback, containing the words denoting positive and 
# negative feedback, respectively. Note that no word is both positive and negative.

# Initially every student has 0 points. Each positive word in a feedback report increases the points of a student by 3, 
# whereas each negative word decreases the points by 1.

# You are given n feedback reports, represented by a 0-indexed string array report and a 0-indexed integer array student_id,
# where student_id[i] represents the ID of the student who has received the feedback report report[i]. The ID of each student 
# is unique.

# Given an integer k, return the top k students after ranking them in non-increasing order by their points. In case more than
# one student has the same points, the one with the lower ID ranks higher.

from heapq import heappop, heappush

class Pair:
    def __init__(self, id, points):
        self.id = id
        self.points = points

    def __lt__(self, other):
        return self.points < other.points or (self.points == other.points and self.id > other.id)

def countPoints(feedback):
    points = 0  
    for word in feedback.split(" "):
        if word in positive:
            points += 3
        elif word in negative:
            points -= 1
    return points

# positive_feedback = ["smart","brilliant","studious"]
# negative_feedback = ["not"]
# report = ["this student is studious","the student is smart"]
# student_id = [1,2]
# k = 2

# positive_feedback = ["smart","brilliant","studious"]
# negative_feedback = ["not"]
# report = ["this student is not studious","the student is smart"]
# student_id = [1,2]
# k = 2

positive_feedback = ["fkeofjpc","qq","iio"]
negative_feedback = ["jdh","khj","eget","rjstbhe","yzyoatfyx","wlinrrgcm"]
report = ["rjstbhe eget kctxcoub urrmkhlmi yniqafy fkeofjpc iio yzyoatfyx khj iio","gpnhgabl qq qq fkeofjpc dflidshdb qq iio khj qq yzyoatfyx","tizpzhlbyb eget z rjstbhe iio jdh jdh iptxh qq rjstbhe","jtlghe wlinrrgcm jnkdbd k iio et rjstbhe iio qq jdh","yp fkeofjpc lkhypcebox rjstbhe ewwykishv egzhne jdh y qq qq","fu ql iio fkeofjpc jdh luspuy yzyoatfyx li qq v","wlinrrgcm iio qq omnc sgkt tzgev iio iio qq qq","d vhg qlj khj wlinrrgcm qq f jp zsmhkjokmb rjstbhe"]
student_id = [96537918,589204657,765963609,613766496,43871615,189209587,239084671,908938263]
k = 3

positive = set(positive_feedback)
negative = set(negative_feedback)

heap = []

for i in range(len(student_id)):
    student_points = countPoints(report[i])
    heappush(heap, Pair(student_id[i], student_points))
    if len(heap) > k:
        heappop(heap)

print([top.id for top in sorted(heap, reverse=True)])