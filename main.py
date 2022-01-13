# 다국어 키 밸류 읽기
def parse_i18n_excel_file(key_file_path, val_file_path):
    key_file_lines = ''
    with open(key_file_path, 'r', 1, 'utf-8') as f1:
        key_file_lines = f1.readlines()

    val_file_lines = ''
    with open(val_file_path, 'r', 1, 'utf-8') as f2:
        val_file_lines = f2.readlines()

    print(key_file_lines)
    print(val_file_lines)

    i18n_dic = dict()
    if key_file_lines.__len__() == val_file_lines.__len__():
        length = key_file_lines.__len__()
        for i in range(length):
            key = key_file_lines[i].strip('\n')
            val = val_file_lines[i].strip('\n')
            i18n_dic[key] = val

    print(i18n_dic)
    return i18n_dic


# js파일 replace
def replace_i81n_file_js(js_file_path, parsed_i18n_dic) :
    new_text_content = ''
    with open(js_file_path, 'r', 1, 'utf-8') as f:
        lines = f.readlines()
        for i, l in enumerate(lines):
            this_key = ''
            this_val = ''
            for dic_key in parsed_i18n_dic:
                if l.find(dic_key + '=') > -1:
                    this_key = dic_key
                    this_val = parsed_i18n_dic[dic_key]

            if this_key != '':
                # 다국어 JS포맷
                new_string = 'var ' + this_key + '="' + this_val + '";'
            else:
                new_string = l.strip('\n')

            if new_string:
                new_text_content += new_string + '\n'
            else:
                new_text_content += '\n'

    with open(js_file_path, 'w', 1, 'utf-8') as f:
        f.write(new_text_content)


# properties 파일 replace
def replace_i81n_file_properties(properties_file_path, parsed_i18n_dic) :
    new_text_content = ''
    with open(properties_file_path, 'r', 1, 'utf-8') as f:
        lines = f.readlines()
        for i, l in enumerate(lines):
            this_key = ''
            this_val = ''
            for dic_key in parsed_i18n_dic:
                if l.find(dic_key.strip('\n') + '=') > -1:
                    this_key = dic_key.strip('\n')
                    this_val = parsed_i18n_dic[dic_key].strip('\n')

            if this_key != '':
                # 다국어 PROPERTIES 포맷
                new_string = this_key + '=' + this_val
            else:
                new_string = l.strip('\n')

            if new_string:
                new_text_content += new_string + '\n'
            else:
                new_text_content += '\n'

    with open(properties_file_path, 'w', 1, 'utf-8') as f:
        f.write(new_text_content)

#
# if __name__ == '__main__':
#     i18n_key_file_path = 'C:/Users/vkv65/Desktop/다국어/takM/tj_key.txt'
#     i18n_val_file_path = 'C:/Users/vkv65/Desktop/다국어/takM/tj_val.txt'
#     i18n_js_file_path = 'C:/Users/vkv65/IdeaProjects/spc_gw7/src/main/webapp/resources/biz/i18n/takMessages_zh.js'
#     i18n_dict = parse_i18n_excel_file(i18n_key_file_path, i18n_val_file_path)
#     replace_i81n_file_js(i18n_js_file_path, i18n_dict)

if __name__ == '__main__':
    i18n_key_file_path = 'C:/Users/vkv65/Desktop/다국어/takM/tj_key.txt'
    i18n_val_file_path = 'C:/Users/vkv65/Desktop/다국어/takM/tj_val.txt'
    i18n_properties_file_path = 'C:/Users/vkv65/IdeaProjects/spc_gw7/src/main/resources/com/naon/biz/i18n/takMessages_zh.properties'
    i18n_dict = parse_i18n_excel_file(i18n_key_file_path, i18n_val_file_path)
    replace_i81n_file_properties(i18n_properties_file_path, i18n_dict)
