class PossitiveNumberError(Exception):
  def __init__(self):
    super().__init__("양수는 입력 불가")

try:
  num = int(input("음수를 입력해 주세요>>>"))
  if num >= 0:
    raise PossitiveNumberError
except PossitiveNumberError as e: 
  print("에러 발생!", e)
