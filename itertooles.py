from itertools import chain
my_list = ['foo','bar']
numbers = list(range(5))
cmds = ['ls','/some/dir']
my_list = list(chain(['foo','bar'], cmds, numbers))