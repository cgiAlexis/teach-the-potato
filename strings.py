'''
Strings can't appear the same as variables, so they must be quoted
What to do about the double string?
'''

agate = 'agate'
jypsum = 'jypsum'
print('%s is a mineral found in the ground' % agate)
print('%s is a crystal found in mineral formations' % jypsum)
print('%s and %s are equally valuable' % agate % jypsum)
