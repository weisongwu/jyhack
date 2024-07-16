import os
def write(fn,content):
	a=open(fn,'w',encoding='utf-8')
	a.write(content)
	a.close()
def main():

	with open('res/att.txt', 'r') as fp:
		atts = fp.readlines()
	with open('res/R1.GRP', 'rb') as fp:
		out = ""

		for i in range(418):
			data = fp.read(2) 
			text = int.from_bytes(data, byteorder='little', signed = 'true')
			out += atts[i].strip() + "," + str(text)+"\n"
		#print(out)
		write("data_export/att.csv",out)
		out = "代号,头像,生命增长,无用,姓名,外号 ,性别,等级,经验,生命,生命最大值,受伤,中毒,体力,物品修炼,,,,,,,,,,,,,,,,,,内力性质,内力,内力最大值,攻击力,轻功,防御力,医疗,用毒,解毒,抗毒,拳掌,御剑,耍刀,特殊,暗器,武学,品德,带毒,左右互搏,声望,资质,修炼物品,修炼点数,武功1,武功2,武功3,武功4,武功5,武功6,武功7,武功8,武功9,武功10,武功1等级,武功2等级,武功3等级,武功4等级,武功5等级,武功6等级,武功7等级,武功8等级,武功9等级,武功10等级,物品1,物品2,物品3,物品4,物品1数量,物品2数量,物品3数量,物品4数量\n"
		for i in range(320):
			for i in range(4):
				data = fp.read(2) 
				text = int.from_bytes(data, byteorder='little', signed = 'true')
				out += str(text)+","
			for i in range(2):
				str1 = fp.read(10)
				text = str1.decode('big5')
				out += str(text)+","
				#print(text)
			for i in range(77):
				data = fp.read(2) 
				text = int.from_bytes(data, byteorder='little', signed = 'true')
				out += str(text)+","
			out += "\n"
		write("data_export/role.csv",out)
		out = "代号,名称,说明,练出武功,暗器动画,使用人,装备类型,显示物品说明,类型,未知,未知,未知,加生命,加生命最大值,加中毒解毒,加体力,改变内力性质,加内力,加内力最大值,加攻击力,加轻功,加防御力,加医疗,加使毒,加解毒,加抗毒,加拳掌,加御剑,加耍刀,加特殊,加暗器,加武学,加品德,加攻击次数,加功夫带毒,仅修炼人物,需内力性质,需内力,需攻击力,需轻功,需用毒,需医疗,需解毒,需拳掌,需御剑,需耍刀,需特殊,需暗器,需资质,需经验,练出物品需经验,需材料,练出物品1,练出物品2,练出物品3,练出物品4,练出物品5,练出物品1数量,练出物品2数量,练出物品3数量,练出物品4数量,练出物品5数量\n"
		for i in range(200):
			for i in range(1):
				data = fp.read(2) 
				text = int.from_bytes(data, byteorder='little', signed = 'true')
				out += str(text)+","
			for i in range(1):
				str1 = fp.read(20)
				text = str1.decode('big5')
				out += str(text)+","
				#print(text)
			str1 = fp.read(20)
			str1 = fp.read(30)
			text = str1.decode('big5')
			#print(text)
			out += str(text)+","
			for i in range(59):
				data = fp.read(2) 
				text = int.from_bytes(data, byteorder='little', signed = 'true')
				out += str(text)+","
			out += "\n"
		write("data_export/item.csv",out)
		out = "代号,名称,出门音乐,进门音乐,跳转场景,进入条件,外景入口x1,外景入口y1,外景入口x2,外景入口y2,入口x,入口y,出口x1,出口x2,出口x3,出口y1,出口y2,出口y3,跳转口x1,跳转口y1,跳转口x2,跳转口y2\n"
		for i in range(84):
			for i in range(1):
				data = fp.read(2) 
				text = int.from_bytes(data, byteorder='little', signed = 'true')
				out += str(text)+","
			for i in range(1):
				str1 = fp.read(10)
				text = str1.decode('big5')
				out += str(text)+","
				#print(text)
			for i in range(20):
				data = fp.read(2) 
				text = int.from_bytes(data, byteorder='little', signed = 'true')
				out += str(text)+","
			out += "\n"
		write("data_export/scene.csv",out)
		out = "代号,名称,未知,未知,未知,未知,未知,音效,类型,动画,伤害类型,攻击范围,消耗内力,敌人中毒,1级攻击力,2级攻击力,3级攻击力,4级攻击力,5级攻击力,6级攻击力,7级攻击力,8级攻击力,9级攻击力,10级攻击力,1级移动范围,2级移动范围,3级移动范围,4级移动范围,5级移动范围,6级移动范围,7级移动范围,8级移动范围,9级移动范围,10级移动范围,1级杀伤范围,2级杀伤范围,3级杀伤范围,4级杀伤范围,5级杀伤范围,6级杀伤范围,7级杀伤范围,8级杀伤范围,9级杀伤范围,10级杀伤范围,1级加内力,2级加内力,3级加内力,4级加内力,5级加内力,6级加内力,7级加内力,8级加内力,9级加内力,10级加内力,1级杀伤内力,2级杀伤内力,3级杀伤内力,4级杀伤内力,5级杀伤内力,6级杀伤内力,7级杀伤内力,8级杀伤内力,9级杀伤内力,10级杀伤内力\n"
		for i in range(93):
			for i in range(1):
				data = fp.read(2) 
				text = int.from_bytes(data, byteorder='little', signed = 'true')
				out += str(text)+","
			for i in range(1):
				str1 = fp.read(10)
				text = str1.decode('big5')
				out += str(text)+","
				#print(text)
			for i in range(62):
				data = fp.read(2) 
				text = int.from_bytes(data, byteorder='little', signed = 'true')
				out += str(text)+","
			out += "\n"
		write("data_export/kongfu.csv",out)
		out = "物品1,物品2,物品3,物品4,物品5,物品1数量,物品2数量,物品3数量,物品4数量,物品5数量,物品1价格,物品2价格,物品3价格,物品4价格,物品5价格\n"
		for i in range(5):
			for i in range(15):
				data = fp.read(2) 
				text = int.from_bytes(data, byteorder='little', signed = 'true')
				out += str(text)+","
			out += "\n"
		write("data_export/shop.csv",out)
# fp.close()
if __name__ == "__main__":
    main()