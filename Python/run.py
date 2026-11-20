import modules

modules.Hello()
print(modules.name)
print(modules.age)
modules.second()

from modules import Hello, age
Hello()
print(age)

#Import with Alias

import modules as cd
cd.Hello

from modules import Hello as he
he()

