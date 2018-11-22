s = 'dsvewgxhdtqsrwrpwbwciolv'
lowerCase = s.lower()
longest = 1
longestStr = ''
testLen = 1
while testLen <= len(s):
    for i in range(len(s)-testLen+1):
        if s[i:i+testLen] ==''.join(sorted(s[i:i+testLen])):
            longestStr = s[i:i+testLen]
            longest = testLen
            break
    testLen += 1
print 'Longest substring in alphabetical order is: ' + longestStr