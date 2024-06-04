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
‘人物','文学作品','文学作品平台',‘摄影作品','其他结点','专辑','中国科学院院士','单位名','影视作品','组合名','学校','综艺节目'
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
        if myInfor[1] == '堂姐':
            # 李慎   堂姐   文安县主
            if '人物' not in infor_dict:
                infor_dict['人物'] = set()
                infor_dict['人物'].add(myInfor[0])
                infor_dict['人物'].add(myInfor[2])
            else:
                infor_dict['人物'].add(myInfor[0])
                infor_dict['人物'].add(myInfor[2])
        elif myInfor[1] == '连载平台':  # 此为关系
            # 花开满园   连载平台   起点中文网
            if '文学作品' not in infor_dict:
                infor_dict['文学作品'] = set()
                infor_dict['文学作品'].add(myInfor[0])  # '文学作品  节点'  '添加的内容  属性'
            else:
                infor_dict['文学作品'].add(myInfor[0])
            if '文学作品平台' not in infor_dict:
                infor_dict['文学作品平台'] = set()
                infor_dict['文学作品平台'].add(myInfor[2])
            else:
                infor_dict['文学作品平台'].add(myInfor[2])
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
        elif myInfor[1] == '堂小舅子':
            # 郭德纲   堂小舅子   王俣钦
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
        elif myInfor[1] == '摄影作品':
            # 赵小丁  摄影作品   长城
            if '人物' not in infor_dict:
                infor_dict['人物'] = set()
                infor_dict['人物'].add(myInfor[0])
            else:
                infor_dict['人物'].add(myInfor[0])
            if '摄影作品' not in infor_dict:
                infor_dict['摄影作品'] = set()
                infor_dict['摄影作品'].add(myInfor[2])
            else:
                infor_dict['摄影作品'].add(myInfor[2])
        elif myInfor[1] == '大爷爷':
            # 凌潇肃   大爷爷   凌子风
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
        elif myInfor[1] == '师爷':
            # 龙越   师爷   谢平安
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
        elif myInfor[1] == '作者':
            # 长歌行   作者   夏达
            if '文学作品' not in infor_dict:
                infor_dict['文学作品'] = set()
                infor_dict['文学作品'].add(myInfor[0])
            else:
                infor_dict['文学作品'].add(myInfor[0])
            if '人物' not in infor_dict:
                infor_dict['人物'] = set()
                infor_dict['人物'].add(myInfor[2])
            else:
                infor_dict['人物'].add(myInfor[2])
        elif myInfor[1] == '继母':
            # 张若昀   继母   刘蓓
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
        elif myInfor[1] == '前夫':
            # 唐宁  前夫   邓伟杰
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
        elif myInfor[1] == '姑妈':
            # 常乐公主   姑妈   同安公主
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
        elif myInfor[1] == '恋人':
            #  蔡康永   恋人   刘坤龙
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
        elif myInfor[1] == '其他关系':  # 可能有问题
            # 香港浸会大学   其他关系   王锦辉
            if '其他结点' not in infor_dict:
                infor_dict['其他结点'] = set()
                infor_dict['其他结点'].add(myInfor[0])
            else:
                infor_dict['其他结点'].add(myInfor[0])
            if '其他结点' not in infor_dict:
                infor_dict['其他结点'] = set()
                infor_dict['其他结点'].add(myInfor[2])
            else:
                infor_dict['其他结点'].add(myInfor[2])
        elif myInfor[1] == '第三任妻子':
            # 陈独秀   第三任妻子   潘兰珍
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
        elif myInfor[1] == '师妹':
            # 蒋璐霞   师妹   阎小乐
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
        elif myInfor[1] == '第一任妻子':
            # 毛泽东   第一任妻子   罗一秀
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
        elif myInfor[1] == '养父':
            # 萧赞   养父   萧衍
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
        elif myInfor[1] == '对手':
            # 富兰克林·罗斯福   对手   赫伯特·克拉克·胡佛
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
        elif myInfor[1] == '养母':
            # 李忠   养母   王皇后
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
        elif myInfor[1] == '发行专辑':
            # 吴青峰   发行专辑   陪我歌唱
            if '人物' not in infor_dict:
                infor_dict['人物'] = set()
                infor_dict['人物'].add(myInfor[0])
            else:
                infor_dict['人物'].add(myInfor[0])
            if '专辑' not in infor_dict:
                infor_dict['专辑'] = set()
                infor_dict['专辑'].add(myInfor[2])
            else:
                infor_dict['专辑'].add(myInfor[2])
        elif myInfor[1] == '设立单位':
            # 中国工程院院士   设立单位   中华人民共和国国务院
            if '中国科学院院士' not in infor_dict:
                infor_dict['中国科学院院士'] = set()
                infor_dict['中国科学院院士'].add(myInfor[0])
            else:
                infor_dict['中国科学院院士'].add(myInfor[0])
            if '单位名' not in infor_dict:
                infor_dict['单位名'] = set()
                infor_dict['单位名'].add(myInfor[2])
            else:
                infor_dict['单位名'].add(myInfor[2])
        elif myInfor[1] == '女儿':
            # 朱元璋  女儿   崇宁公主
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
        elif myInfor[1] == '原配':
            #   郭沫若   原配   张琼华
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
        elif myInfor[1] == '挚爱':
            # 张国荣   挚爱   唐鹤德
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
        elif myInfor[1] == '主要演员':
            # 再见歌舞伎町   主要演员   田口智朗
            if '影视作品' not in infor_dict:
                infor_dict['影视作品'] = set()
                infor_dict['影视作品'].add(myInfor[0])
            else:
                infor_dict['影视作品'].add(myInfor[0])
            if '人物' not in infor_dict:
                infor_dict['人物'] = set()
                infor_dict['人物'].add(myInfor[2])
            else:
                infor_dict['人物'].add(myInfor[2])
        elif myInfor[1] == '义妹':
            # 罗俊林   义妹   杨晨璐
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
        elif myInfor[1] == '曾孙子':
            # 朱瞻基   曾孙子   朱祐梈
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
        elif myInfor[1] == '成员':
            # 低调组合   成员   杨和苏
            if '组合名' not in infor_dict:
                infor_dict['组合名'] = set()
                infor_dict['组合名'].add(myInfor[0])
            else:
                infor_dict['组合名'].add(myInfor[0])
            if '人物' not in infor_dict:
                infor_dict['人物'] = set()
                infor_dict['人物'].add(myInfor[2])
            else:
                infor_dict['人物'].add(myInfor[2])
        elif myInfor[1] == '侄孙子':
            # 何应钦   侄孙子   何祖光
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
        elif myInfor[1] == '养女':
            # 章士钊   养女   章含之
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
        elif myInfor[1] == '公公':
            # 显肃皇后   公公   赵顼
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
        elif myInfor[1] == '历任领导':
            # 西南交通大学   历任领导   王伯群
            if '单位名' not in infor_dict:
                infor_dict['单位名'] = set()
                infor_dict['单位名'].add(myInfor[0])
            else:
                infor_dict['单位名'].add(myInfor[0])
            if '人物' not in infor_dict:
                infor_dict['人物'] = set()
                infor_dict['人物'].add(myInfor[2])
            else:
                infor_dict['人物'].add(myInfor[2])
        elif myInfor[1] == '姨父':
            # 丘崇   姨父   贺兰初真
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
        elif myInfor[1] == '堂侄':
            # 毛泽东   堂侄   毛远耀
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
        elif myInfor[1] == '丈夫':
            # 秦子越   丈夫   聂远
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
        elif myInfor[1] == '第二任妻子':
            # 汪道涵   第二任妻子   孙维聪
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
        elif myInfor[1] == '办学团体':
            # 香港华仁书院   办学团体   耶稣会
            if '学校' not in infor_dict:
                infor_dict['学校'] = set()
                infor_dict['学校'].add(myInfor[0])
            else:
                infor_dict['学校'].add(myInfor[0])
            if '组织名' not in infor_dict:
                infor_dict['组织名'] = set()
                infor_dict['组织名'].add(myInfor[2])
            else:
                infor_dict['组织名'].add(myInfor[2])
        elif myInfor[1] == '岳父':
            # 李元桂   岳父   金镛
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
        elif myInfor[1] == '外祖父':
            # 太穆皇后   外祖父   宇文泰
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
        elif myInfor[1] == '伯父':
            # 朱贵烰   伯父   朱棡
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
        elif myInfor[1] == '学弟':
            # 李健   学弟   孙岩
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
        elif myInfor[1] == '师父':
            # 张艺兴   师父   黄磊
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
        elif myInfor[1] == '伴侣':
            # 鲁迅   伴侣   许广平
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
        elif myInfor[1] == '表哥':
            # 李贤   表哥   武承嗣
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
        elif myInfor[1] == '学长':
            # 李健   学长   林家川
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
        elif myInfor[1] == '妹夫':
            # 李承乾   妹夫   薛瓘
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
        elif myInfor[1] == '姐姐':
            # 秦俊杰   姐姐   李玥
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
        elif myInfor[1] == '师祖':
            # 邓沐玮   师祖   裘盛戎
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
        elif myInfor[1] == '嫡母':
            # 李重茂   嫡母   韦皇后
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
        elif myInfor[1] == '岳母':
            # 柴绍   岳母   太穆皇后
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
        elif myInfor[1] == '男友':
            # 刘雨柔   男友   胡凯翔
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
        elif myInfor[1] == '曾外孙子':
            # 冯胜   曾外孙子   朱子墐
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
        elif myInfor[1] == '舅母':
            # 王美怡   舅母   焦姣
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
        elif myInfor[1] == '前女友':
            # 王阳明  前女友   张俪
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
        elif myInfor[1] == '堂兄':
            # 朱逊烇   堂兄   朱高炽
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
        elif myInfor[1] == '老师':
            # 张默   老师   黄定宇
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
        elif myInfor[1] == '爱人':
            # 艾略特·佩吉   爱人   艾玛·波特纳
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
        elif myInfor[1] == '小叔子':
            # 卢贵兰   小叔子   元湛
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
        elif myInfor[1] == '儿子':
            # 萧瑟瑟   儿子   耶律敖卢斡
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
        elif myInfor[1] == '女朋友':
            # 戚其义   女朋友   简慕华
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
        elif myInfor[1] == '奶奶':
            # 冯钟越   奶奶   吴清芝
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
        elif myInfor[1] == '综艺节目':
            # 香奈儿·辛普森   综艺节目   音乐快递
            if '人物' not in infor_dict:
                infor_dict['人物'] = set()
                infor_dict['人物'].add(myInfor[0])
            else:
                infor_dict['人物'].add(myInfor[0])
            if '综艺节目' not in infor_dict:
                infor_dict['综艺节目'] = set()
                infor_dict['综艺节目'].add(myInfor[2])
            else:
                infor_dict['综艺节目'].add(myInfor[2])
        elif myInfor[1] == '恩师':
            # 刘昊然   恩师   陈思诚
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
        elif myInfor[1] == '外孙':
            # 彭玉   外孙   孟阿赛
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
        elif myInfor[1] == '创始人':
            # 四川音乐学院   创始人   熊佛西
            if '学校' not in infor_dict:
                infor_dict['学校'] = set()
                infor_dict['学校'].add(myInfor[0])
            else:
                infor_dict['学校'].add(myInfor[0])
            if '人物' not in infor_dict:
                infor_dict['人物'] = set()
                infor_dict['人物'].add(myInfor[2])
            else:
                infor_dict['人物'].add(myInfor[2])
        elif myInfor[1] == '员工':
            # 黄子韬   员工   徐艺洋
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
        elif myInfor[1] == '执导':
            # 高峰   执导   雪狼
            if '人物' not in infor_dict:
                infor_dict['人物'] = set()
                infor_dict['人物'].add(myInfor[0])
            else:
                infor_dict['人物'].add(myInfor[0])
            if '作品' not in infor_dict:
                infor_dict['作品'] = set()
                infor_dict['作品'].add(myInfor[2])
            else:
                infor_dict['作品'].add(myInfor[2])
        elif myInfor[1] == '侄子':
            # 赵辉   侄子   朱逊炓
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
        elif myInfor[1] == '弟子':
            # 徐悲鸿   弟子   戴泽
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
    print(infor_dict)  # 上传各个结点以及他们的属性
    #  上传所有的关系
