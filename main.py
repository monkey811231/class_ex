from db import Db

if __name__ == '__main__':
	db = Db('127.0.0.1')
	login = ['username','password','dbname']
	login_info = []
	for ip in login:
		print('■■■■■■■■■■')
		output = input(f'輸入{ip} : ')
		login_info.append(output)
	db.connection(login_info[0],login_info[1],login_info[2])






# class Player:
# 	def __init__(self, name, atk):
# 		self.name = name #assignment (預設指令)
# 		self.hp = 100
# 		self.atk = atk


# p1 = Player('Eden', 10) #instantiation (實體化 創作出物件)
# p2 = Player('Shirley', 5)

# print(f'player: {p1.name} atk: {p1.atk}')
# print(f'player: {p2.name} atk: {p2.atk}')
# #assignment (預設指令)
# #instantiation (實體化 創作出物件)
