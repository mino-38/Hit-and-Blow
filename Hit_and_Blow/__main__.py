import random
import sys
import argparse

def generate(n):
    num = str(random.randint(10**(n-1), 10**n))
    while not appropriate(num):
        num = str(random.randint(10**(n-1), 10**n))
    return num

def appropriate(num):
    return all(map(lambda s: num.count(s) == 1, num))

def argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--digits", type=lambda n: ((1<=n) and int(n)) or False, metavar="[1~...]", default=3, help="桁数")
    parser.add_argument("-p", "--duplicate", action="store_true", help="正解となる数字の重複を許可(正解に121, 111等の数字も含まれるようになる)")
    return parser.parse_args()

def main():
    args = argument()
    answer = generate(args.digits)
    count = 0
    while True:
        count += 1
        while True:
            print("あなたの予想を書いてください({}桁)> ".format(args.digits), end="")
            try:
                num = int(sys.stdin.readline())
                if len(num) != args.digits:
                    raise ValueError()
                break
            except ValueError:
                pass
        if num == answer:
            print("正解です！！\n答え: {}\n{}回で当てました！".format(answer, count))
            break
        hit = 0
        blow = 0
        for i, s in enumerate(num):
            if s == answer[i]:
                hit += 1
            elif s in answer:
                blow += 1
        print("{}ヒット {}ブロー".format(hit, blow))

if __name__ == "__main__":
    main()