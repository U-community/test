ls = [["1","hello","world","my god"], \
      ["2","hello","world","my god"], \
      ["3","hello","world","my god"]]  #二维列表
fname = "mytxt3_.csv"
f = open(fname,mode='a',encoding='utf-8')
for item in ls:
    f.write(','.join(item) + '\n')
f.close()