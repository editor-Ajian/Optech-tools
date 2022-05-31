def inclusion_check(para:str, tag:list):
	for element in tag:
		if element in para:
			return True
	return False


def get_a_item_via_location(paragraph, start_loc, end_char, identifer:list, end_char_2=''):
	# 顺序搜索，若 start_loc 到一个等于 end_char 的字符区间内含有 identifer，则传出这个区间
	for char in range(start_loc, len(paragraph)):
		if paragraph[char] == end_char or (end_char_2 != '' and paragraph[char] == end_char_2):
			end_loc = char
			if inclusion_check(paragraph[start_loc:end_loc+1], identifer):
				return paragraph[start_loc:end_loc+1], end_loc + 1
			else:
				continue
	return '', 0


def reversed_xiabiao(text, target):
	# 倒序返回 target 在 text 中的下标
    for n in range(1, len(text)):
        if text[-n] == target:
            return -n


def extract_be_linkd_word(something, mode=1):
	# 用于将 “[][]” 和 “[]()” 这样的字符截取出内容
	# 统一使用 “]” 作为分隔符
	split_loc = something.find(']')
	if mode == 1:
		return something[1:split_loc]
	if mode == 2:
		return something[1:split_loc], something[split_loc+1:]


def remove_huanhangfu(a_form):
	# 移除字符中的换行符，并将多个空格缩减为 1 个空格
	new_item = a_form
	new_item = new_item.replace('\n', ' ')

	while '  ' in new_item:
		new_item = ' '.join(new_item.split('  '))
		# print(new_item)

	return new_item


def add_order_number(check, form_item):
	some_A, some_B = extract_be_linkd_word(form_item, 2)
	form_str = '%#{}%#-[{}]{}'.format(str(check+1), some_A, some_B)
	table_str = '%#{}%#,{},{},'.format(str(check+1), some_A, some_B)
	return form_str, table_str


def write_str_to_a_file(file_name, target_str):
	# 将字符串写入文档
	with open(file_name, 'w', encoding='utf-8') as f:
		f.write(target_str)


def extract_forms_in_Optech_file(file_name):
	with open(file_name, 'r', encoding='utf-8') as f:
		content = f.read()
	#print(content)

	references = ''
	stop_iden = reversed_xiabiao(content, '}')
	references = content[stop_iden+2:]
	# print(references)
	content = content[:stop_iden+1]

	special_form = []
	order_table = []
	order_number = 1
	while '}' in content:
		for loc in range(0, len(content)):
			if content[loc] == '[':
				a_form_item, new_start = get_a_item_via_location(content, loc, ']', ['][', ']('], ')')
				a_form_item = remove_huanhangfu(a_form_item)
				# print(a_form_item)
				a_form_item, table_item = add_order_number(order_number, a_form_item)
				special_form.append(a_form_item)
				order_table.append(table_item)
				order_number = order_number + 1
				content = content[new_start:]
				break
			elif content[loc] == '{':
				a_form_item, new_start = get_a_item_via_location(content, loc, '}', ['%'])
				# print(a_form_item)
				special_form.append(a_form_item)
				content = content[new_start:]
				break

	#print(special_form)
	final_form = '\n\n'.join(special_form)
	final_form = final_form + '\n' + references
	write_str_to_a_file('final_form.md', final_form)
	link_and_order = '\n'.join(order_table)
	write_str_to_a_file('links_and_order_table.md', link_and_order)
	write_str_to_a_file('references.md', references)
	print('程序已经跑完。请到 final_form.md 处添加翻译，到 links_and_order_table.md 处添加超链词语的翻译。')


def use_html_to_fill_table(file_w_name):
	with open(file_w_name, 'r', encoding='utf-8') as f:
		content = f.read()

	links = []
	while '](' in content:
		for char in range(0, len(content)):
			if content[char] == '[':
				a_link_item, new_start = get_a_item_via_location(content, char, ')', [']('])
				be_linked, link = extract_be_linkd_word(a_link_item, 2)
				if  be_linked == '●':
					pass
				else:
					links.append(link[1:-1])
				content = content[new_start:]
				break

	with open('links_and_order_table.md', 'r', encoding='utf-8') as f:
		table_text = f.read()

		list_of_entry = table_text.split('\n')
		for n in range(0, len(list_of_entry)):
			shares = list_of_entry[n].split(',')
			# print(shares)
			if shares[-1] == '':
				list_of_entry[n] += shares[1]
			
			list_of_entry[n] += ',' + links[n]
			# print(list_of_entry[n])

	return list_of_entry


def get_determiner():
	with open('references.md', 'r', encoding='utf-8') as f:
		references_text = f.read()

	references = references_text.split('\n')

	be_covered_refer = []
	for re in references:
		be_covered = '[{}]'.format(extract_be_linkd_word(re))
		be_covered_refer.append(be_covered)

	# print(be_covered_refer)
	return be_covered_refer


def generate_final_file(file_w_name):
	final_table = use_html_to_fill_table(file_w_name)

	be_covered_refer = get_determiner()
	bottom_addition = '\n\n'

	with open('final_form.md', 'r', encoding='utf-8') as f:
		optech_translation = f.read()

	primitives_translation = optech_translation

	for entry in final_table:
		chips = entry.split(',')
		optech_hyperlink = '[{}]{}'.format(chips[3], chips[2])
		optech_translation = optech_hyperlink.join(optech_translation.split(chips[0]))
		
		if chips[2] not in be_covered_refer:
			primitives_hyperlink = '[{}][{}]'.format(chips[3], chips[1])
			bottom_addition += '[{}]: {}\n'.format(chips[1], chips[4])
		else:
			primitives_hyperlink = optech_hyperlink
		primitives_translation = primitives_hyperlink.join(primitives_translation.split(chips[0]))

	primitives_translation += bottom_addition

	write_str_to_a_file('optech_comptabile.md', optech_translation)
	write_str_to_a_file('primitives_comptabile.md', primitives_translation)
	print('程序已经跑完。optech_comptabile.md 和 primitives_comptabile.md 分别为兼容 Optech 和 PrimitivesLane 的版本。')


# extract_forms_in_Optech_file('#201.md')
# generate_final_file('#199-html.md')
# get_determiner()
# print(extract_be_linkd_word('[ssssd](sssdd)', mode=2))

