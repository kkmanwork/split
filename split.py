
def read_file(filename):
	lines = []
	with open(filename, "r", encoding = "utf-8-sig") as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):#格式轉換
	Allen_word_cnt = 0
	Viki_word_cnt = 0
	Allen_stick_cnt = 0
	Viki_stick_cnt = 0
	Allen_image_cnt = 0
	Viki_image_cnt = 0
	for line in lines:
		s = line.split(" ")#s 是一個清單
		name = s[1]
		if name == "Allen":
			if s[2] == "貼圖":
				Allen_stick_cnt += 1
			elif s[2] == "圖片":
				Allen_image_cnt +=1
			else:
				for m in s[2:]:
					Allen_word_cnt += len(m)


		elif name == "Viki":
			if s[2] == "貼圖":
				Viki_stick_cnt += 1
			elif s[2] == "圖片":
				Viki_image_cnt += 1
			else:
				for m in s[2:]:
					Viki_word_cnt += len(m)

	print("Allen 輸入了幾個字:", Allen_word_cnt, ",傳了", Allen_stick_cnt, "個貼圖",",傳了", Allen_image_cnt, "個圖片")
	print("Viki 輸入了幾個字:", Viki_word_cnt, ",傳了", Viki_stick_cnt, "個貼圖", ",傳了", Viki_image_cnt, "個圖片" ) 

def write_file(filename,lines):
	with open(filename, "w", encoding = "utf-8") as f:#f 就是檔案
		for line in lines:
			f.write(line + "\n")

def main():
	lines = read_file("LINE-Viki.txt")
	lines = convert(lines)#把聊天紀錄存在lines 裡面投進去
	#write_file("output.txt", lines)

main()

