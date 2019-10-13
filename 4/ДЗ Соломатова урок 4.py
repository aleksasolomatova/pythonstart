# задача1


list = [1,2,4,0]
print([x**2 for x in list])

#задача2
list1 = ['яблоко', 'груша', 'абрикос', 'персик', 'банан']
list2 = ['виноград', 'банан', 'яблоко', 'мандарин', 'груша']
print([i for i in list1 if i in list2])


# задача3
list = ['1', '3', '6', '536', '0']
print([x for x in list if x%3 == 0 and x >= 0 and x%4 !=0 ])

# задача1
import re
string = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'
found = re.findall(r"[a-z]+", string)
print(found)

#задача2
found = re.findall(r'[a-z]{2}([A-Z]+)[A-Z]{2}', string)
print(found)
git add . &&git commit -a -m "*" && git push origin
#задача3
import random
n = (random.randint(0, 9) for i in range(2500))
str = ''.join(str(i) for i in n)

with open('test.txt', 'w', ) as f:
    f.write(str)
    found = re.findall((r'(0+|1+|2+|3+|4+|5+|6+|7+|8+|9+)'), str)
    print(found)

#задание1
matrix = [[1, 0, 8],
          [3, 4, 1],
          [0, 4, 2]]
print(list(map(list, zip(*matrix))))

