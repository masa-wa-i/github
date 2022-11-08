import json,time
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
    del number[0]
    file = open("エラトステネスの篩.json", "w",encoding="utf-8")
    json.dump(number, file, ensure_ascii=False)
    file.close()
    k = time.time()
    print("素数の計算時間"+str(k-j))
if __name__ == '__main__':
    main()