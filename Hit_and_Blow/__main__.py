import random
import sys
import argparse

def generate(n, duplicate, zero):
    num = str(random.randint(10**(n-1), 10**n))
    while not duplicate and not appropriate(num, zero):
        num = str(random.randint(10**(n-1), 10**n))
    return num

def appropriate(num, zero):
    return all(map(lambda s: num.count(s) == 1 and (zero or s != "0"), num))

def argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--digits", type=lambda n: ((1<=int(n)) and int(n)) or False, metavar="[1~...]", default=3, help="桁数")
    parser.add_argument("-p", "--duplicate", action="store_true", help="正解となる数字の重複を許可(正解に121, 111等の数字も含まれるようになる)")
    parser.add_argument("-i", "--include-zero", action="store_true", help="正解となる数字に0も含めることを許可(必ず入るわけではない)")
    return parser.parse_args()

def main():
    args = argument()
    if (9 if args.include_zero else 10) < args.digits and not args.duplicate:
        raise ValueError("重複不可能かつ桁数が大きすぎるから正解の数字が生成出来ません")
    answer = generate(args.digits, args.duplicate, args.include_zero)
    count = 0
    while True:
        count += 1
        while True:
            print("\nあなたの予想を書いてください({}桁)> ".format(args.digits), end="")
            sys.stdout.flush()
            try:
                num = str(int(sys.stdin.readline()))
                if len(num) != args.digits:
                    raise ValueError()
                break
            except ValueError:
                print("\033[1F\033[0J", end="")
        if num == answer:
            print("\n正解です！！\n答え: {}\n{}回で当てました！".format(answer, count))
            break
        hit = 0
        blow = 0
        for i, s in enumerate(num):
            if s == answer[i]:
                hit += 1
            elif s in answer:
                blow += 1
        print("{}ヒット {}ブロー".format(hit, blow))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
