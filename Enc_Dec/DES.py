import Data as des_data
import time
#字符转UNICODE
def char2unicode_ascii(inputStr):
    output = []
    for i in range(len(inputStr)):
        output.append(ord(inputStr[i]))
    return output

#unicode 转 bit
def unicode2bit(inputStr):
    output = []
    for i in range(len(inputStr)*16):
        output.append((inputStr[int(i / 16)]>>(i % 16)) &1 ) #左移1bit
    return output

#ascii转bit
def byte2bite(inputStr):
    output = []
    for i in range(len(inputStr) * 8):
        output.append((inputStr[int(i / 8)] >> (i % 8)) & 1)  # 左移1bit
    return output

#将bit转为Unicode码
def bit2unicode(inbit):
    out=[]
    temp=0
    for i in range(len(inbit)):
        temp=temp|(inbit[i]<<(i%16))
        if i%16==15:
            out.append(temp)
            temp=0
    return out
#将bit转为ascii 码
def bit2byte(inbit):
    out=[]
    temp=0
    for i in range(len(inbit)):
        temp=temp|(inbit[i]<<(i%8))
        if i%8==7:
            out.append(temp)
            temp=0
    return out

#将unicode码转为字符（中文或英文）
def unicode2char(inbyte):
    out=""
    for i in range(len(inbyte)):
        out=out+chr(inbyte[i])
    return out

def hex2unicode(inhex):
    out = []
    for i in range(int(len(inhex)/4)):
        temp = inhex[i*4:i*4+4]
        out.append(int(temp,16))
    return out

def unicode2hex(inbyte):
    out = ''
    for i in range(len(inbyte)):
        temp = hex(inbyte[i])
        temp = temp[2:]
        out += (4-len(temp)) * '0' + temp
    return out
    pass

# 置换函数，用于执行各种置换操作
def Displace( source, table):
    target = []
    for i in table:
        target.append(source[i-1])
    return target

def XOR( source1, source2):
    length = len(source1)
    target = []
    for i in range(length):
        target.append(source1[i] ^ source2[i])
    return target

#F函数
def F( R, currentKey):
    #将输入的部分先由32位扩充到48再与密钥做异或
    XORresult = XOR(Displace( R, des_data.E_table),currentKey)
    depart = [XORresult[:6],XORresult[6:12],XORresult[12:18],XORresult[18:24],XORresult[24:30],XORresult[30:36],XORresult[36:42],XORresult[42:]]
    S_Result = [0] * 32
    pos = 0
    for j in range(8):
        m = (depart[j][0] << 1) + depart[j][5] #计算行
        n = (depart[j][1] << 3) + (depart[j][2] << 2) + (depart[j][3] << 1) + (depart[j][4])  # 计算列
        v = des_data.S[j][(m << 4) + n]  # m*16 + n
        # 转换成二进制
        S_Result[pos] = (v & 8) >> 3
        S_Result[pos + 1] = (v & 4) >> 2
        S_Result[pos + 2] = (v & 2) >> 1
        S_Result[pos + 3] = v & 1
        pos += 4
    return Displace(S_Result,des_data.P_table)

def getKeys(inputKey):
    Keys = []
    ascKey = char2unicode_ascii(inputKey)
    bitKey = unicode2bit(ascKey)
    bitKey = Displace(bitKey,des_data.Condense_table1)
    #56位密钥进行置换操作
    for i in range(16):
        if(i == 0 or i == 1 or i == 8 or i == 15):
            move = 1
        else:
            move = 2
        for j in range(move):
            for k in range(8):
                temp = bitKey[k*7]
                for m in range(7*k,7*k+6):
                    bitKey[m] = bitKey[m+1]
                bitKey[k*7+6] = temp
            temp = bitKey[0]
            for k in range(27):
                bitKey[k] = bitKey[k+1]
            bitKey[27] = temp
            temp = bitKey[28]
            for k in range(28,55):
                bitKey[k] = bitKey[k+1]
            bitKey[55] = temp

        Keys.extend( Displace(bitKey,des_data.Condense_table2))

    return Keys
def Des(pString,kString):
    keyRes = getKeys(kString)
    tempStr = [0 for i in range(48)] #用于存储IP逆置换之前L+R合并的结果
    #extendR = [0 for i in range(48)] #用于存储R部分的扩展结果
    unicodeStr = char2unicode_ascii(pString) #转码
    #IP置换
    IP_TranStr = Displace(unicode2bit(unicodeStr),des_data.IP_table)
    #拆分成L+R两部分
    L = [IP_TranStr[i] for i in range(32)]
    R = [IP_TranStr[i] for i in range(32,64)]
    #print("pString:" + unicode2bit(unicodeStr))
    #16轮运算
    for i in range(16):
        tempR = R
        #获取本轮密钥
        currentKey = [keyRes[j] for j in range(i*48,i*48+48)]
        PRes = F(tempR,currentKey)
        #P盒置换结果与L部分异或
        XORLRes = XOR(PRes,L)
        #重置下一轮输出
        L = tempR
        R = XORLRes
    #交换LR
    L,R = R,L
    tempStr = L
    tempStr.extend(R)
    #IP逆置换
    finalRes = Displace(tempStr,des_data._IP_table)
    return unicode2hex(bit2unicode(finalRes))

def DeDes(pString,kString):
    keyRes = getKeys(kString)
    tempStr = [0 for i in range(48)]  # 用于存储IP逆置换之前L+R合并的结果
    # extendR = [0 for i in range(48)] #用于存储R部分的扩展结果
    unicodeStr = hex2unicode(pString)  # 转码
    # IP置换
    IP_TranStr = Displace(unicode2bit(unicodeStr), des_data.IP_table)
    # 拆分成L+R两部分
    L = [IP_TranStr[i] for i in range(32)]
    R = [IP_TranStr[i] for i in range(32, 64)]
    # print("pString:" + unicode2bit(unicodeStr))
    # 16轮运算
    for i in range(15,-1,-1):
        tempR = R
        # 获取本轮密钥
        currentKey = [keyRes[j] for j in range(i * 48, i * 48 + 48)]
        PRes = F(tempR, currentKey)
        # P盒置换结果与L部分异或
        XORLRes = XOR(PRes, L)
        # 重置下一轮输出
        L = tempR
        R = XORLRes
    # 交换LR
    L, R = R, L
    tempStr = L
    tempStr.extend(R)

    # IP逆置换
    finalRes = Displace(tempStr, des_data._IP_table)
    #print(finalRes)

    return unicode2char(bit2unicode(finalRes))


'''str = "xzx"
str1 = char2unicode_ascii(str)
str2 = unicode2hex(str1)
str3 = hex2unicode(str2)
print(str3)
print(unicode2char(str3))'''

'''if __name__ == '__main__':
    text = input("请输入文本：")
    length = len(text)
    text = text + (4-(length%4))*" "
    length = len(text)
    passwd = input("请输入8位密码:")
    while(len(passwd)!=8):
        print("密码需要为8位!")
        passwd = input("请输入8位密码:")
    print("加密后：")
    finalRes = ""
    timeStart = time.time()
    for i in range(int(length/4)):
        tempText = [text[j] for j in range(i*4,i*4+4)]
        finalRes = finalRes + Des(tempText,passwd)
    timeEnd = time.time()

    length = len(finalRes)
    finalRes1 = ""
    print("解密后：")

    length = len(finalRes)
    for i in range(int(length/16)):
        tempText = finalRes[i*16:i*16+16]
        finalRes1 = finalRes1 + DeDes(tempText,passwd)
    print(finalRes1)
    print(timeEnd - timeStart)
    pass'''