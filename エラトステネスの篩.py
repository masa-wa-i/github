import json,time
def main():
    j = time.time()
    b = True
    c = 0
    number = []
    for a in range(10000000):
        number += [a+1]
    print("第一段階終了")
    while b:
        d = number[c]
        e = True
        f = []
        g = 2
        if not d == 1:
            while e:
                f += [d*g]
                g += 1
                if d*g > 10000000:
                    e = False
                    for h in range(len(f)):
                        i = f[h] in number
                        if i == True:
                            del number[number.index(f[h])]
        c += 1
        if c > len(number)-1:
            b = False
    file = open("エラトステネスの篩.json", "w",encoding="utf-8")
    json.dump(number, file, ensure_ascii=False)
    file.close()
    k = time.time()
    print("計算時間"+str(k-j))
if __name__ == '__main__':
    main()