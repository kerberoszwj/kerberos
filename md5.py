import hashlib
def md5(data):
    m=hashlib.md5()
    m.update(data.encode('utf-8'))
    return m.hexdigest()
print('请输入：')
m=input()
print(md5(m))