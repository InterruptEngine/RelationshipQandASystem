"""
关系:
{'堂姐', '连载平台', '侄孙媳妇', '合作人', '文学作品', '弟媳', '导师', '堂小舅子', '摄影作品', '大爷爷', '师爷', '作者',
 '继母', '办学性质', '未婚夫', '前夫', '姑妈', '恋人', '其他关系', '第三任妻子', '师妹', '主要配音', '第一任妻子',
 '养父', '对手', '养母', '发行专辑', '设立单位', '女儿', '原配', '挚爱', '主要演员', '义妹', '曾孙子', '成员', '侄孙子',
 '养女', '公公', '历任领导', '姨父', '堂侄', '丈夫', '第二任妻子', '办学团体', '岳父', '外祖父', '伯父', '学弟', '师父',
 '伴侣', '表哥', '学长', '妹夫', '姐姐', '师祖', '嫡母', '岳母', '男友', '曾外孙子', '舅母', '前女友', '堂兄', '老师',
 '爱人', '小叔子', '儿子', '女朋友', '奶奶', '综艺节目', '恩师', '外孙', '创始人', '员工', '执导', '侄子', '弟子',     --》陈鑫旺
 '师弟', '母亲', '堂哥', '前儿媳', '主要角色', '舅父', '妻子', '外孙女', '第二任丈夫', '生父', '旧爱', '代表作品',
 '朋友', '学校特色', '妻姐', '养子', '兄弟', '创办', '旗下艺人', '曾外祖父', '音乐视频', '前男友', '外曾孙子', '堂弟',
 '继子', '助理', '院系设置', '继父', '大伯哥', '徒弟', '知己', '儿媳', '堂伯父', '女婿', '亲家公', '曾祖父', '叔父',
 '姑母', '师傅', '歌曲原唱', '云孙', '外甥', '姑父', '学妹', '小姑子', '第四任妻子', '偶像', '前任', '表姨', '社长',
 '亲家母', '战友', '学校身份', '主要作品', '生母', '类别', '外曾祖母', '祖父', '毕业院校', '知名人物', '小舅子', '庶子',
 '所属机构', '表妹', '制作', '登场作品', '嫂子', '好友', '前公公', '义女', '师兄', '曾孙', '同学', '配音', '堂舅',  --》 陈伟
 '相关国内联盟', '外曾祖父', '男朋友', '叔叔', '大姨子', '侄女', '音乐作品', '简称', '义子', '曾祖母', '经纪人', '先夫',
 '未婚妻', '姨夫', '表姑父', '义兄', '为他人创作音乐', '表侄', '连襟', '姐夫', '出版社', '学生', '弟弟', '同门', '师生',
 '叔外公', '曾孙女', '教练', '侄孙', '老板', '妹妹', '前队友', '表兄', '孙子', '亡妻', '经纪公司', '代表', '大姑子',
 '第六任妻子', '搭档', '伯母', '祖母', '领导', '继任', '参演', '表叔', '伯乐', '婶母', '婆婆', '现任领导', '外曾孙女',
 '表弟', '外甥女婿', '第五任妻子', '编剧', '曾外祖母', '学姐', '义母', '类型', '孙女', '表姐', '姨母', '前妻',
 '合作院校', '继女', '叔外祖父', '妾', '专职院士数', '主持', '法人', '妯娌', '学校类别', '义弟', '哥哥', '大舅子',
 '义父', '伯伯', '父亲', '外祖母', '第一任丈夫', '外孙子', '玄孙', '姑姑', '师姐', '大舅哥', '队友', '外甥女', '小姨子',  --》陈满
 '堂妹'}

当前的结点{          # 将自己新增加的结点写入
‘人物','文学作品','文学作品平台'
'音乐组合'、'公司'、'学校'、'影视作品'、'综艺节目'
}
 """
if __name__ == '__main__':
    # relationship = set()  # 所有的关系集合
    infor = list()  # 所有的三元式列表
    # node = set()  # 所有的结点集合
    with open(r'data/kg(utf8).txt', 'r', encoding='utf-8') as fp:
        for line in fp.readlines():
            line = line.strip('\n')  # 切分 ‘\n'
            line_list = line.split('\t')  # 利用'\t'切分
            infor.append(line_list)  # 增加列表
            # node.add(line_list[0])
            # node.add(line_list[2])
            # relationship.add(line.split('\t')[1])  # 提取出所有的关系
            # print(line_list)
    # print(len(infor)) # 打印数组长度
    # print(node)
    # print(relationship, len(relationship), sep='\n')  # 打印所有的关系
    infor_dict = dict()
    for myInfor in infor:  # 属性可能相同，但属于不同结点
        if myInfor[1] == '相关国内联盟':
            #学术研究恳谈会	相关国内联盟	八大学工学系联合会
            if '人物' not in infor_dict:
                infor_dict['人物'] = set()
                infor_dict['人物'].add(myInfor[0])
                infor_dict['人物'].add(myInfor[2])
            else:
                infor_dict['人物'].add(myInfor[0])
                infor_dict['人物'].add(myInfor[2])
        elif myInfor[1] == '外曾祖父':  # 此为关系
            #李恒	外曾祖父	郭子仪
            if '人物' not in infor_dict:
                infor_dict['人物'] = set()
                infor_dict['人物'].add(myInfor[0])
                infor_dict['人物'].add(myInfor[2])
            else:
                infor_dict['人物'].add(myInfor[0])
                infor_dict['人物'].add(myInfor[2])
        elif myInfor[1] == '侄孙媳妇':
            # 何应钦 侄孙媳妇 温碧霞
            if '人物' not in infor_dict:
                infor_dict['人物'] = set()
                infor_dict['人物'].add(myInfor[0])
            else:
                infor_dict['人物'].add(myInfor[0])
            if '人物' not in infor_dict:
                infor_dict['人物'] = set()
                infor_dict['人物'].add(myInfor[2])
            else:
                infor_dict['人物'].add(myInfor[2])
        elif myInfor[1] == '合作人':
            # 洪金宝   合作人   袁和平
            if '人物' not in infor_dict:
                infor_dict['人物'] = set()
                infor_dict['人物'].add(myInfor[0])
            else:
                infor_dict['人物'].add(myInfor[0])
            if '人物' not in infor_dict:
                infor_dict['人物'] = set()
                infor_dict['人物'].add(myInfor[2])
            else:
                infor_dict['人物'].add(myInfor[2])
        elif myInfor[1] == '文学作品':
            # 蒋梦麟   文学作品   现代世界中的中国
            if '人物' not in infor_dict:
                infor_dict['人物'] = set()
                infor_dict['人物'].add(myInfor[0])
            else:
                infor_dict['人物'].add(myInfor[0])
            if '文学作品' not in infor_dict:
                infor_dict['文学作品'] = set()
                infor_dict['文学作品'].add(myInfor[2])
            else:
                infor_dict['文学作品'].add(myInfor[2])
        elif myInfor[1] == '弟媳':
            # 洪深   弟媳   钱似莺
            if '人物' not in infor_dict:
                infor_dict['人物'] = set()
                infor_dict['人物'].add(myInfor[0])
            else:
                infor_dict['人物'].add(myInfor[0])
            if '人物' not in infor_dict:
                infor_dict['人物'] = set()
                infor_dict['人物'].add(myInfor[2])
            else:
                infor_dict['人物'].add(myInfor[2])
        elif myInfor[1] == '导师':
            # 王巧   导师   陈爽
            if '人物' not in infor_dict:
                infor_dict['人物'] = set()
                infor_dict['人物'].add(myInfor[0])
            else:
                infor_dict['人物'].add(myInfor[0])
            if '人物' not in infor_dict:
                infor_dict['人物'] = set()
                infor_dict['人物'].add(myInfor[2])
            else:
                infor_dict['人物'].add(myInfor[2])
        # elif myInfor[1] == '堂小舅子':
        # elif myInfor[1] == '摄影作品':
        # elif myInfor[1] == '大爷爷':
        # elif myInfor[1] == '师爷':
        # elif myInfor[1] == '作者':
        # elif myInfor[1] == '继母':
        # elif myInfor[1] == '前夫':
        # elif myInfor[1] == '姑妈':
        # elif myInfor[1] == '恋人':
        # elif myInfor[1] == '其他关系':
        # elif myInfor[1] == '第三任妻子':
        # elif myInfor[1] == '师妹':
        # elif myInfor[1] == '第一任妻子':
        # elif myInfor[1] == '养父':
        # elif myInfor[1] == '对手':
        # elif myInfor[1] == '养母':
        # elif myInfor[1] == '发行专辑':
        # elif myInfor[1] == '设立单位':
        # elif myInfor[1] == '女儿':
        # elif myInfor[1] == '原配':
        # elif myInfor[1] == '挚爱':
        # elif myInfor[1] == '主要演员':
        # elif myInfor[1] == '义妹':
        # elif myInfor[1] == '曾孙子':
        # elif myInfor[1] == '成员':
        # elif myInfor[1] == '侄孙子':
        # elif myInfor[1] == '养女':
        # elif myInfor[1] == '公公':
        # elif myInfor[1] == '历任领导':
        # elif myInfor[1] == '姨父':
        # elif myInfor[1] == '堂侄':
        # elif myInfor[1] == '丈夫':
        # elif myInfor[1] == '第二任妻子':
        # elif myInfor[1] == '办学团体':
        # elif myInfor[1] == '岳父':
        # elif myInfor[1] == '外祖父':
        # elif myInfor[1] == '伯父':
        # elif myInfor[1] == '学弟':
        # elif myInfor[1] == '师父':
        # elif myInfor[1] == '伴侣':
        # elif myInfor[1] == '表哥':
        # elif myInfor[1] == '学长':
        # elif myInfor[1] == '妹夫':
        # elif myInfor[1] == '姐姐':
        # elif myInfor[1] == '师祖':
        # elif myInfor[1] == '嫡母':
        # elif myInfor[1] == '岳母':
        # elif myInfor[1] == '男友':
        # elif myInfor[1] == '曾外孙子':
        # elif myInfor[1] == '舅母':
        # elif myInfor[1] == '前女友':
        # elif myInfor[1] == '堂兄':
        # elif myInfor[1] == '老师':
        # elif myInfor[1] == '爱人':
        # elif myInfor[1] == '小叔子':
        # elif myInfor[1] == '儿子':
        # elif myInfor[1] == '女朋友':
        # elif myInfor[1] == '奶奶':
        # elif myInfor[1] == '综艺节目':
        # elif myInfor[1] == '恩师':
        # elif myInfor[1] == '外孙':
        # elif myInfor[1] == '创始人':
        # elif myInfor[1] == '员工':
        # elif myInfor[1] == '执导':
        # elif myInfor[1] == '侄子':
        # elif myInfor[1] == '弟子':
    print(infor_dict)  # 上传各个结点以及他们的属性
    #  上传所有的关系
