import os
import utility


def function_1():
	# 该函数用于处理Optech Github 库原文件
	# 它会抽取出超链接的格式和其他用代码处理的特殊格式
	# 它会形成三个文件：
	# （1）final_form 文件，提供了所有特殊格式，用于形成译文
	# 注意，在翻译的时候只应把 “%#n%#” 的字样留下作为标记，不应留下超链接的形式
	# （2) links_and_order_table 文件，用于标记各超链接的位置，可用于后续替换和生成
	# （3）references 文件，用于保存原文件文末的链接内容，用于后续替换和生成
	file_G = input('请输入 Optech Github 库原文件的名称：')
	# file_G = '#198.md'
	utility.extract_forms_in_Optech_file(file_G)


def function_2():
	# 本函数用于在译本完成后,根据已有的文件生成最终的版本
	# 需要提供的不仅有 function_1 所生成的文件，还有译本
	# 以及一个从 optech 最终网页上拉取下来，包含了 html 信息的文件
	file_W = input('请输入表示 Optech 网页最终效果的原文件的名称：')
	utility.generate_final_file(file_W)


if __name__ == '__main__':
	print('\n请通过输入数字选择你要执行的计算：\n\n\n')
	print('1. 从 Optech Github 库原文件中抽取出链接和特殊格式\n')
	print('2. 从译本和已有的文件中生成两个最终文件，一个兼容 Optech，一个兼容 PrimitivesLane\n')
	while True:
		purpose = input('请输入：')
		if purpose == '1':
			function_1()
		elif purpose == '2':
			function_2()
		else:
			print('输入错误！请重新输入')