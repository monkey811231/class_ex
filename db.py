import time

class Db:
	def __init__(self, servername):
		self.sn = servername
		print(f'連接至{self.sn}')
		return

	def connection(self, username, password, dbname):
		print(f'{username}驗證中...')
		time.sleep(1)
		print(f'驗證完成，正在登入{dbname}')
		time.sleep(1)
		print('資料庫連結成功!')

	# def comment(self,comment):
		

#assignment (預設指令)
#instantiation (實體化 創作出物件)