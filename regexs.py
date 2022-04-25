import re

maybe_email = "name@something.com"
email_rx = r"^[^@ ]+@[^@ ]+\.[^@ ]+$"

# verbose
email_rx = r"""(?x)         # verbose flag
    ^                       # beggining of string
    [^@ ]+                  # stuff without @ or space (name)
    @                       # an @ signb
    [^@ ]+                  # more stuff
    \.                      # a dot
    [^@ ]+                  # final studd ( comm, org ... )
    $                       # end of string 
"""

if m := re.match(email_rx, maybe_email):
    # its an email address, do something
    pass

# .* is greedy, it finds the longest match it can
# .? finds the shortest match

text = "hello, Vannia. Welcome"

m = re.search(r"Hello, (?P<name>.*)\.", text)
print(m["name"])  # 'Vannia. Welcome'

m = re.search(r"Hello, (?P<name>.?)\.", text)
print(m["name"])  # 'Vannia'
