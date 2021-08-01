# 1. import 패키지.모듈
import unit.charactor
unit.charactor.test()

# 2. form 패키지 import 모듈
from unit import item
item.test()

# 3. import 패키지 import *
from unit import *
charactor.test()
item.test()
monster.test()

# 4. import 패키지
import unit
unit.charactor.test()
unit.item.test()
unit.monster.test()