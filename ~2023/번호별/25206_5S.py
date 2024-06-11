<<<<<<< HEAD
# 너의 평점은
import sys
input = sys.stdin.readline

score_dict = { 'A+' : 4.5, 'A0' : 4.0, 'B+' : 3.5,
            'B0' : 3.0, 'C+' : 2.5, 'C0' : 2.0,
            'D+' : 1.5, 'D0' : 1.0, 'F' : 0.0}

All_credit = 0
All_score = 0

for _ in range(20):
    name, credit, score = map(str, input().rstrip().split(" "))
    if score == "P":
        continue
    All_credit += float(credit)
    All_score += score_dict[score] * float(credit)
    
print(All_score / All_credit)

=======
# 너의 평점은
import sys
input = sys.stdin.readline

score_dict = { 'A+' : 4.5, 'A0' : 4.0, 'B+' : 3.5,
            'B0' : 3.0, 'C+' : 2.5, 'C0' : 2.0,
            'D+' : 1.5, 'D0' : 1.0, 'F' : 0.0}

All_credit = 0
All_score = 0

for _ in range(20):
    name, credit, score = map(str, input().rstrip().split(" "))
    if score == "P":
        continue
    All_credit += float(credit)
    All_score += score_dict[score] * float(credit)
    
print(All_score / All_credit)

>>>>>>> e238a4b4840a248e25507837388f6aee8e657899
