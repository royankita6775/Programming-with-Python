# 6.4

def judgement():
    judge1 = int(input("Give points from judge 1: "))
    judge2 = int(input("Give points from judge 2: "))
    judge3 = int(input("Give points from judge 3: "))
    judge4 = int(input("Give points from judge 4: "))
    judge5 = int(input("Give points from judge 5: "))
    
    score = [judge1, judge2, judge3, judge4, judge5]
    score.remove(max(score))
    score.remove(min(score))
    final_score = sum(score)
    print(final_score)

judgement()
