'''Mostre o salário atual e com 15% de aumento'''
s = float(input('\033[1:39:40mQual é o seu salário?\033[m '))
prc = float(15/100)
a = s + (s * prc)
print('\033[7:36:40mCom 15% de aumento, seu salário que era de {}R${:.2f}{}\033[7:36:40m passa a ser de {}R${:.2f}{}'.
      format('\033[7:31:40m', s, '\033[m', '\033[7:32:40m', a, '\033[m'))