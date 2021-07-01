# 실습문제 5.3.4
# learning Korean

# 한국어 리스트
word_list = ["사랑해", "귀엽다", "고마워", "행복해"]

# 점수
score = 0

print("Let's Learning Korean")

for word in word_list:
  print(word)
  data = input()
  if data == word:
    score += 1

print("전체 문제 개수:", len(word_list), "개")
print("맞힌 문제 개수:", score, "개")
print("틀린 문제 개수:", len(word_list) - score, "개")