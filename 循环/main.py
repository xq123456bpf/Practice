from turtledemo.tree import tree


def main():
    """
    判断一个数是否为素数
    :return:
    """
    n = int(input("请输入一个数:"))
    is_prime = True
    if n == 2:
        is_prime = True
    elif n % 2 == 0:
        is_prime = False
    else:
        end = int(n ** 0.5)
        for i in range(2,end + 1,2):
            if n % i == 0:
                is_prime = False
                break
    if is_prime:
        print(f'{n}是素数')
    else:
        print(f'{n}不是素数')
    pass

if __name__ == '__main__':
    main()