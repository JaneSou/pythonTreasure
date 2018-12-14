#!/use/bin/env python
# -*- coding: utf-8 -*-

'''
    根据预设种子字符，生成八位随机密码，剔除了O.o.0、1.l等易于错认的字符，

'''

from __future__ import print_function
import random
import string

num = input('生成密码数量：')
seed = "23456789abcdefghijkmnopkrstuvwxyzABCDEDGHIJKLMNPQRSTUVWXYZ"
for i in range(int(num)):
    sa = []
    for j in range(8):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    print(salt)

