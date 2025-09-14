password='123456'
t=3
while t >= 1:
  pwd = input('請輸入密碼：')
  if pwd == password:
    print('登入成功！')
    t = 0
    else:
        print('密碼錯誤, 還有',t,'次機會')
        t = t-1