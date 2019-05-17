# -*- coding: utf-8 -*-
import random
import time


def powMod(a,b,c):
    res = 1
    a %= c
    while b :
        if b&1 :
            res = (res * a) % c
        a = (a * a) % c
        b >>= 1
    return res

def gcd(a,b):
    while a!=0:
        a,b = b % a, a
    return b

#定义一个函数，参数分别为a,n，返回值为b
def modReverse(a,m):#这个扩展欧几里得算法求模逆

    if gcd(a,m)!=1:
        return None
    u1,u2,u3 = 1,0,a
    v1,v2,v3 = 0,1,m
    while v3!=0:
        q = u3//v3
        v1,v2,v3,u1,u2,u3 = (u1-q*v1),(u2-q*v2),(u3-q*v3),v1,v2,v3
    return u1%m

def rabinMiller(num):
    s = num - 1
    t = 0
    while s % 2 == 0:
        s = s // 2
        t += 1

    for trials in range(5):
        a = random.randrange(2, num - 1)
        v = powMod(a, s, num)
        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True


def isPrime(num):
    # 排除0,1和负数
    if num < 2:
        return False

    # 创建小素数的列表,可以大幅加快速度
    # 如果是小素数,那么直接返回true
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
    if num in small_primes:
        return True

    # 如果大数是这些小素数的倍数,那么就是合数,返回false
    for prime in small_primes:
        if num % prime == 0:
            return False

    # 如果这样没有分辨出来,就一定是大整数,那么就调用rabin算法
    return rabinMiller(num)


# 得到大整数,默认位数为1024
def getPrime(key_size=1024):
    while True:
        num = random.randrange(2**(key_size-1), 2**key_size)
        if isPrime(num):
            return num

#加密操作 m：明文 e：加解密指数默认为65537 n：大模数（p*q）
def encrypt(m,e,n):
    return powMod(m,e,n)

#解密操作 c：密文 d：与e对应，由e计算而来 n：大模数
def decrypt(c,d,n):
    return powMod(c,d,n)

'''
如用于签名，其中，保密参数为 p q d， 公开参数为 e n 
'''

'''#字符转UNICODE
def char2ascii(inputStr):
    output = ''
    #inputStr = str(inputStr)
    for i in range(len(inputStr)):
        #output.append(ord(inputStr[i]))
        asc = str(ord(inputStr[i]))
        output += '0'*(5-len(asc)) + asc
    return int(output)'''

'''#unicode转字符
def ascii2char(inputStr):
    output = ''
    #inputStr = str(inputStr)
    inputStr = (len(inputStr)%5)*'0' + inputStr
    for i in range(int(len(inputStr)/5)):
        asc = int(inputStr[i*5:i*5+5])
        output += chr(asc)
    return output'''

if __name__ == '__main__':
    #获取大素数以作为密码
    p = getPrime()
    q = getPrime()
    n = p * q
    #n的欧拉函数
    eul = (p - 1) * (q - 1)
    #设置加密解密指数
    e = 65537
    d = modReverse(65537,eul)
    m = '4648465468735165616548765135132168453654321564651321354643213'
    m = input('请输入要加密的数字')
    t = time.time()
    c = encrypt(m,e,n)

    print('p:'+str(p))
    print('q:'+str(q))
    print('加密后：'+ str(c))
    print('解密后：',encrypt(c,d,n))
    t = time.time() - t
    print(t)