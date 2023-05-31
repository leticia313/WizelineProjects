from collections import defaultdict
dogs=['sparky','hunter','loki','astro','sparky','rocky','roky','toby','chelsea','maple','maya','loki','sparky','toby','sparky','dexter','fido','sparky']
dog_dic = defaultdict(int)
for dog in dogs:
    dog_dic[dog] += 1
    print('rocky->',dog_dic['rocky'])
    print('sparky->',dog_dic['sparky'])
    print(list(dog_dic.keys()))


