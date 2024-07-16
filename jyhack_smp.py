import os
from png import Writer
import png
# width, height = (3, 3)
# pixels = [[255, 0, 0,255], [255, 0, 0,255], [255, 0, 0,255],[255, 0, 0,255], [255, 0, 0,255], [255, 0, 0,255],[255, 0, 0,255], [255, 0, 0,255], [255, 0, 0,255]]

# writer = Writer(width, height)

# png.from_array([[255,0,0,50, 0,255,0,50, 0,0,255,50],[255,255,0,0, 255,0,255,50, 0,255,255,100]], "RGBA", ).save("04.png")

# print(pixels)
# with open("output.png", "wb") as f:
#     writer.write(f, pixels)
def savepng(name,data):
    png.from_array(data, "RGBA", ).save(name+".png")
# 读取颜色表 
def col():
    with open('res/MMAP.COL', 'rb') as fp:
        col_data = []
        pix_table = []
        for idx in range(16):
            row_pix = []
            for idx in range(16):
                pix = []
                r = int.from_bytes(fp.read(1), byteorder='little', signed = False)
                g = int.from_bytes(fp.read(1), byteorder='little', signed = False)
                b = int.from_bytes(fp.read(1), byteorder='little', signed = False)
                pix.append(r*4)
                pix.append(g*4)
                pix.append(b*4)
                pix.append(255)
                row_pix += pix
                pix_table.append(pix)
        # print(pix_table)
            col_data.append(row_pix)
        savepng("img_export/col.png",col_data)
        return pix_table
# 解析索引数据
def read_idx():
    index_table = []
    cur = 0
    
    with open('res/SDX000', 'rb') as fp:
        while 1:
            data = fp.read(4) 
            text = int.from_bytes(data, byteorder='little', signed = False)
            # print(text)
            if text == 0:
                break
            index_table.append(text - cur)
            cur = text
    return index_table
def main():
    os.makedirs("./img_export/smp", exist_ok=True)
    
    null_color = [0,0,0,0]
    colors = col()
    index_table = read_idx()
    
    with open('res/SMP000', 'rb') as fp:
        file_name = 0
        for index_data in index_table:
            if index_data > 0:
                data = []
                w = int.from_bytes(fp.read(2), byteorder='little', signed = False)
                h = int.from_bytes(fp.read(2), byteorder='little', signed = False)
                offx = int.from_bytes(fp.read(2), byteorder='little', signed = False)
                offy = int.from_bytes(fp.read(2), byteorder='little', signed = False)
                # print(w,h,offx,offy,index_data,file_name)
                row_idx = 0
                while 1:
                    # 用来存放读取来的 本行颜色数据
                    row_pix = []
                    # 本行颜色数据的byte长度
                    row_byte_count = int.from_bytes(fp.read(1), byteorder='little', signed = False)
                    # 本行颜色数据 已读取的byte长度
                    row_read_count = 0
                    # 本行颜色 像素数 已填充数量
                    row_pix_count = 0
                    # 遍历 section，一行颜色 包含多个section
                    # print(" -  "+str(row_byte_count))
                    if row_byte_count == 0:
                        for idx in range(w):
                            row_pix = row_pix + null_color
                        
                    else:
                        while 1:
                            # 透明颜色数量
                            null_count = int.from_bytes(fp.read(1), byteorder='little', signed = False)
                            # 不透明颜色数量
                            col_count = int.from_bytes(fp.read(1), byteorder='little', signed = False)
                            # 在像素数据中填充 透明像素点
                            for idx in range(null_count):
                                row_pix = row_pix + null_color
                            
                            # 读取不透明颜色 并填充
                            # print(col_count)
                            for idx in range(col_count):
                                col_idx = int.from_bytes(fp.read(1), byteorder='little', signed = False)
                                row_pix = row_pix + colors[col_idx]
                            row_read_count += 2
                            row_read_count += col_count
                            row_pix_count += null_count
                            row_pix_count += col_count
                            # 本行数据 读取结束 补齐结尾的透明点
                            if row_read_count == row_byte_count:
                                if row_pix_count < w:
                                    for idx in range(w - row_pix_count):
                                        row_pix = row_pix + null_color
                            # print(null_count,col_count)
                                break
                        # print(count)
                    data.append(row_pix)
                    
                    row_idx += 1
                    if row_idx == h:
                        break
        
                savepng("img_export/smp/"+str(file_name),data)
            file_name += 1
        # for idx in range(400):
        #     data = fp.read(4) 
        #     text = int.from_bytes(data, byteorder='little', signed = 'true')
        #     print(text)

            
if __name__ == "__main__":
    main()