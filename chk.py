password='123456'
t=3
while t >= 1:
  pwd = input('請輸入密碼：')
  if pwd == password:
      print('登入成功！')
      break
  else:
      t = t-1
      print('密碼錯誤, 還有',t,'次機會')
