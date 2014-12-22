
# Testing code for pysnot
# tested with snot database
# assumes ticket 11440 doesn't exist


import pysnot
import os

class ShitsFucked(Exception):
    pass

#test stat_ticket

assert(True == pysnot.stat_ticket(252))
assert(False == pysnot.stat_ticket(11440))


# test get assigned
assert('monkc' == pysnot.get_assigned(20))
assert(None == pysnot.get_assigned(117))
try:
    a = pysnot.get_assigned(11440)
except pysnot.TicketNotFoundException:
    pass
else:
    raise ShitsFucked('Expected exception not thrown')


# 255
# Should start assigned to nibz
# Then get assigned to cawil
# Then get assigned back to nibz
assert('nibz' == pysnot.get_assigned(255))
assert(True == pysnot.assign_ticket(255, 'cawil'))
assert('cawil' == pysnot.get_assigned(255))
assert(True == pysnot.assign_ticket(255, 'nibz'))
assert('nibz' == pysnot.get_assigned(255))

# 256
# Should start assigned to nobody
# Assign to nibz
# Reassign to nibz (should succeed)
# Assign back to nobody
assert(None == pysnot.get_assigned(256))
assert(True == pysnot.assign_ticket(256, 'nibz'))
assert('nibz' == pysnot.get_assigned(256))
assert(True == pysnot.assign_ticket(256, 'nibz'))
assert('nibz' == pysnot.get_assigned(256))
assert(True == pysnot.assign_ticket(256, 'nobody'))
assert(None == pysnot.get_assigned(256))


# 257 >> Assigned to nibz, test assign to nibz
# Maybe don't need this after all?



