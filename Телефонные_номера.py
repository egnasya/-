import re


tel_add = input('')
already_exist1, already_exist2, already_exist3 = input(), input(), input()
tel_add = re.sub('[(|)|-]', '', tel_add)
already_exist1, already_exist2, already_exist3 = (re.sub('[(|)|-]', '', already_exist1),
                                                  re.sub('[(|)|-]', '', already_exist2),
                                                  re.sub('[(|)|-]', '', already_exist3))
tel_list = [tel_add, already_exist1, already_exist2, already_exist3]
for i in range(len(tel_list)):
    if len(tel_list[i]) == 11:
        tel_list[i] = tel_list[i][1:11]
    elif len(tel_list[i]) == 12:
        tel_list[i] = tel_list[i][2:12]
    if len(tel_list[i]) == 7:
        tel_list[i] = '495' + tel_list[i]
tel = tel_list[0]
for i in range(1,len(tel_list)):
    if tel_list[i] == tel:
        print('YES')
    else:
        print('NO')
