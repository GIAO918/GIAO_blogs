 # 现有字典 d= {'a':24,'g':52,'i':12,'k':33}请按value值进行排序?
d= {'a':24,'g':52,'i':12,'k':33}
print(sorted(d.items(),key = lambda x:x[1]))