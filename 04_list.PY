#====p.296====

food = '삼겹살,라면,돈까스,피자'
food = food.split(',') #.split 하면 list로 변환 ['삼겹살', '라면', '돈까스', '피자']
print('내가 좋아하는 음식 : ', food)
print('type(food) : ', type(food))

sid_list = ['100', 101, food] 
print("sid_list: ", sid_list)
print("type(sid_list): ", type(sid_list))
print("sid_list[0]:", sid_list[0])                # 100 
print('type(sid_list[0]):', type(sid_list[0]))    # type(sid_list[0]): <class 'str'>

print("sid_list[1]:", sid_list[1])                # 101
print('type(sid_list[1]):', type(sid_list[1]))    # type(sid_list[1]): <class 'int'>

print("sid_list[2]:", sid_list[2])                # ['삼겹살', '라면', '돈까스', '피자']
print('type(sid_list[2]):', type(sid_list[2]))    # type(sid_list[2]): <class 'list'>