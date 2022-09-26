import time, json
def main():
    j = time.time()
    b = True
    c = 0
    number = []
    for a in range(100000):
        number += [a+1]
    while b:
        d = number[c]
        e = True
        f = []
        g = 2
        if not d == 1:
            while e:
                f += [d*g]
                g += 1
                if d*g > 100000:
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
    print("素数の計算時間"+str(k-j))
    p = []
    e = time.time()
    json_open = open("エラトステネスの篩.json", "r",encoding="utf-8")
    d = json.load(json_open)
    json_open.close()
    for h in range(len(d)):
        for i in range(len(d)):
            if h > i:
                m = d[h]
                n = d[i]
                if not (m - n)%2 == 0:
                    a = m**2 - n**2
                    b = 2*m*n
                    c = m**2 + n**2
                    p += [[a,b,c]]
    file = open("ピタゴラス数.json", "w",encoding="utf-8")
    json.dump(p, file, ensure_ascii=False)
    file.close()
    f = time.time()
    print("原始ピタゴラス数の計算時間"+str(f-e))
if __name__ == '__main__':
    main()