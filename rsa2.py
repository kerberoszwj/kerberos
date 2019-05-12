#!/usr/bin/env python3
# coding:utf-8

import random
import binascii
import argparse  # 导入读取命令行参数的模块
import sys
import hashlib
import socket
sys.setrecursionlimit(100000)  # 设置迭代次数限制


# 生成大素数，20次MillerRabin算法缩小出错的概率
def BigPrime():
    Min = 1 << 511;
    Max = 1 << 512;
    p = 0
    while (1):
        p = random.randrange(Min, Max, 1)
        for i in range(20):
            if MillerRabin(p) == 0:
                break
            elif i == 19:
                return p

# 素性检验
def MillerRabin(n):
    "利用Miller-Rabin算法检验生成的奇数是否为素数"
    m = n - 1
    k = 0
    while (m % 2 == 0):
        m = m // 2
        k = k + 1
    a = random.randint(2, n)
    # b=a**m%n
    b = MRF(a, m, n)
    if (b == 1):
        return 1
    for i in range(k):
        if (b == n - 1):
            return 1
        else:
            b = b * b % n
    return 0


def MRF(b, n, m):
    a = 1
    x = b
    y = n
    z = m
    binstr = bin(n)[2:][::-1]  # 通过切片去掉开头的0b，截取后面，然后反转
    for item in binstr:
        if item == '1':
            a = (a * b) % m
            b = (b ** 2) % m
        elif item == '0':
            b = (b ** 2) % m
    return a


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
        # 求逆元


def Ex_Euclid(x, n):
    r0 = n
    r1 = x % n
    if r1 == 1:
        y = 1
    else:
        s0 = 1
        s1 = 0
        t0 = 0
        t1 = 1
        while (r0 % r1 != 0):
            q = r0 // r1
            r = r0 % r1
            r0 = r1
            r1 = r
            s = s0 - q * s1
            s0 = s1
            s1 = s
            t = t0 - q * t1
            t0 = t1
            t1 = t
            if r == 1:
                y = (t + n) % n
    return y


def Build_key():
    # 产生p,q,n,e,d
    p = BigPrime()
    q = BigPrime()
    n = p * q
    _n = (p - 1) * (q - 1)  # n的欧拉函数
    e = 0
    while (1):
        e = random.randint(1, _n + 1)
        if gcd(e, _n) == 1:
            break
    d = Ex_Euclid(e, _n)
    return (n, e, d)


def a2hex(raw_str):
    hex_str = ''
    for ch in raw_str:
        hex_str += hex(ord(ch))[2:]
    return hex_str


def hex2a(raw_str):
    asc_str = ''
    for i in range(0, len(raw_str), 2):
        asc_str += chr(int(raw_str[i:i + 2], 16))
    return asc_str


# 加密，传入公钥，通过读取明文文件进行加密
def encrypt(m, e, n):
    m = int(a2hex(m), 16)
    c = MRF(m, e, n)
    C1 = hex(c)
    return C1



def decrypt(c,d,n):
    c = int(c, 16)
    m = MRF(c, d, n)
    M = str(hex(m))
    M = hex2a(M[2:])
    return M


