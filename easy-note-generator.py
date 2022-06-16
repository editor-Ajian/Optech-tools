# 本程序的目的是帮助生成注释
# 输入英文字符串，它就会返回注释

import utility


def easy_to_generate():
	while True:
		en_words = input('请输入需要转化成注释的英文字符串，按回车结束：')
		print(utility.dasher())


if __name__ == '__main__':
	easy_to_generate()



