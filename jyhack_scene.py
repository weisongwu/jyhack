import os
import json
def main():
	os.makedirs("./data_export/scene_data", exist_ok=True)
	
	with open('res/S1.GRP', 'rb') as fp:
		out = ""
		for idx in range(100):
			md = {}
			for i in range(6):
				layer = []
				for j in range(4096):
					data = fp.read(2) 
					text = int.from_bytes(data, byteorder='little', signed = 'true')
					if text > 0:
						text = round(text /2)
					layer.append(text)
					# out += str(text)+"\n"
				md['layer'+str(i)] = layer
			a=open(r'data_export/scene_data/scene'+str(idx)+'.json','w',encoding='utf-8')
			a.write(json.dumps(md))
			a.close()
if __name__ == "__main__":
	
    main()