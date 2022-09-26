import time, json
def main():
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
    print("計算時間"+str(f-e))
if __name__ == '__main__':
    main()