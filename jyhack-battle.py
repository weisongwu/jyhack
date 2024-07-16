import os
def main():
	with open('res/WAR.STA', 'rb') as fp:
		out = "代号,名称,地图,经验,音乐,手动1,手动2,手动3,手动4,手动5,手动6,自动1,自动2,自动3,自动4,自动5,自动6,x1,x2,x3,x4,x5,x6,y1,y2,y3,y4,y5,y6,敌人1,敌人2,敌人3,敌人4,敌人5,敌人6,敌人7,敌人8,敌人9,敌人10,敌人11,敌人12,敌人13,敌人14,敌人15,敌人16,敌人17,敌人18,敌人19,敌人20,敌人x1,敌人x2,敌人x3,敌人x4,敌人x5,敌人x6,敌人x7,敌人x8,敌人x9,敌人x10,敌人x11,敌人x12,敌人x13,敌人x14,敌人x15,敌人x16,敌人x17,敌人x18,敌人x19,敌人x20,敌人y1,敌人y2,敌人y3,敌人y4,敌人y5,敌人y6,敌人y7,敌人y8,敌人y9,敌人y10,敌人y11,敌人y12,敌人y13,敌人y14,敌人y15,敌人y16,敌人y17,敌人y18,敌人y19,敌人y20\n"
		for i in range(140):
			data = fp.read(2) 
			text = int.from_bytes(data, byteorder='little', signed = 'true')
			out += str(text)+","
			str1 = fp.read(10)
			text = str1.decode('big5')
			out += str(text)+","
			for i in range(87):
				data = fp.read(2) 
				text = int.from_bytes(data, byteorder='little', signed = 'true')
				out += str(text)+","
			out += "\n"
		
	a=open(r'data_export/battle.csv','w',encoding='utf-8')
	a.write(out)
	a.close()

if __name__ == "__main__":
    main()