#!/usr/bin/evn python

# Note: trailing slash right after ''' prevents
# a blank like from appearing as the first line
form1 = '''\
Dear %(name)s,

Please send back my %(item)s or pay me $ %(amount)0.2f.
                                       Sincerely yours,
                                       Joe Python User
'''

print form1 % {
    'name': 'Mr. Bush',
    'item': 'blender',
    'amount': 50.00
}
print "-----------------"

form2 = '''\
Dear {name},

Please send back my {item} or pay me $ {amount:0.2f}.
                                       Sincerely yours,
                                       Joe Python User
'''

print form2.format(name='Mr. Bush', item='blender', amount=50.0)
