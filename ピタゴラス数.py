import time, json
def main():
    j = time.time()
    count = 100000
    number = []
    for a in range(count):
        number += [a+1]
    for m in range(count):
        d = number[m+1]
        b = int(count/d)-1
        for l in range(b):
            if (d*(l+2) in number) == True:
                del number[number.index(d*(l+2))]
        if d > count/2:
            break
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