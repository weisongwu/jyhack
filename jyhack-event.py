import os
def main():
	with open('res/KDEF.GRP', 'rb') as fp:
		out = ""
		arr = [0,3,2,13,3,2,4,0,
				1,2,1,2,0,0,0,1,
				3,5,3,2,2,1,0,2,
				0,4,5,3,5,5,4,3,
				2,3,2,4,3,1,4,1,
				1,3,2,3,6,2,2,2,
				2,2,7,0,0,0,0,4,
				1,0,0,0,5,2,6,2,
				0,0,1,1]
		idx = 0
		while idx < 60607:
			data = fp.read(2) 
			#print(data)
			text = int.from_bytes(data, byteorder='little', signed = 'true')
			out += str(text)+","
			idx=idx+1
			# print(idx,text)
			if	text > 0 and text < 68:
				
				for j in range(arr[text]):
					data = fp.read(2) 
					text = int.from_bytes(data, byteorder='little', signed = 'true')
					#print(text)
					out += str(text)+","
					idx=idx+1
			out += "\n"
		
	a=open(r'data_export/event.csv','w',encoding='utf-8')
	a.write(out)
	a.close()

if __name__ == "__main__":
    main()