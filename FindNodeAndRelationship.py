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
‘人物','文学作品','文学作品平台',‘摄影作品','其他结点','专辑','单位名','影视作品','组合名','学校','综艺节目'
‘人物','文学作品','文学作品平台'，'学校','特色','音乐视频作品','院系','歌曲名','学校里的身份','作品','学校类别','单位名','机构','影视作品'
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
            if '影视作品' not in infor_dict:
                infor_dict['影视作品'] = set()
                infor_dict['影视作品'].add(myInfor[2])
            else:
                infor_dict['影视作品'].add(myInfor[2])
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
            if '其他结点' not in infor_dict:
                infor_dict['其他结点'] = set()
                infor_dict['其他结点'].add(myInfor[0])
            else:
                infor_dict['其他结点'].add(myInfor[0])
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
        elif myInfor[1] == '师弟':
            # 冯巩  师弟	李增瑞
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
        elif myInfor[1] == '母亲':
            # 李仙蕙	母亲	韦皇后
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
        elif myInfor[1] == '堂哥':
            # 李贤	堂哥	李象
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
        elif myInfor[1] == '前儿媳':
            # 英若诚	前儿媳	宋丹丹
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
        elif myInfor[1] == '主要角色':
            # 天字一号	主要角色	杨震
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
        elif myInfor[1] == '舅父':
            # 同安公主	舅父	独孤罗
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
        elif myInfor[1] == '妻子':
            # 孙红雷	妻子	王骏迪
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
        elif myInfor[1] == '外孙女':
            # 朱一锦	外孙女	景天瞳
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
        elif myInfor[1] == '第二任丈夫':
            # 武则天	第二任丈夫	李治
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
        elif myInfor[1] == '生父':
            # 江泽民	生父	江世俊
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
        elif myInfor[1] == '旧爱':
            # 卡拉·迪瓦伊	旧爱	米歇尔·罗德里格兹
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
        elif myInfor[1] == '代表作品':
            # 迈克尔·杰克逊	代表作品	bad
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

        elif myInfor[1] == '朋友':
            # 金玟岐	朋友	刘思涵
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
        elif myInfor[1] == '学校特色':
            # 香港大学	学校特色	中国大学校长联谊会
            if '学校' not in infor_dict:
                infor_dict['学校'] = set()
                infor_dict['学校'].add(myInfor[0])
            else:
                infor_dict['学校'].add(myInfor[0])
            if '特色' not in infor_dict:
                infor_dict['特色'] = set()
                infor_dict['特色'].add(myInfor[2])
            else:
                infor_dict['特色'].add(myInfor[2])
        elif myInfor[1] == '妻姐':
            # 钱学森	妻姐	蒋雍
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
        elif myInfor[1] == '养子':
            # 慕容宝	养子	慕容云
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
        elif myInfor[1] == '兄弟':
            # 毕公	兄弟	康叔
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
        elif myInfor[1] == '创办':
            # 中国社会科学出版社	创办	中国社会科学院
            if '单位名' not in infor_dict:
                infor_dict['单位名'] = set()
                infor_dict['单位名'].add(myInfor[0])
            else:
                infor_dict['单位名'].add(myInfor[0])
            if '院系' not in infor_dict:
                infor_dict['院系'] = set()
                infor_dict['院系'].add(myInfor[2])
            else:
                infor_dict['学校'].add(myInfor[2])
        elif myInfor[1] == '旗下艺人':
            # 周迅	旗下艺人	张婧仪
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
        elif myInfor[1] == '曾外祖父':
            # 朱子墐	曾外祖父	冯胜
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
        elif myInfor[1] == '音乐视频':
            # 吴婉芳	音乐视频	烟花雪
            if '人物' not in infor_dict:
                infor_dict['人物'] = set()
                infor_dict['人物'].add(myInfor[0])
            else:
                infor_dict['人物'].add(myInfor[0])
            if '音乐视频作品' not in infor_dict:
                infor_dict['音乐视频作品'] = set()
                infor_dict['音乐视频作品'].add(myInfor[2])
            else:
                infor_dict['音乐视频作品'].add(myInfor[2])
        elif myInfor[1] == '前男友':
            # 徐若瑄	前男友	吴奇隆
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
        elif myInfor[1] == '外曾孙子':
            # 亚历山大王子	外曾孙子	菲利普·蒙巴顿
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
        elif myInfor[1] == '堂弟':
            # 朱高煦	堂弟	朱逊炓
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
        elif myInfor[1] == '继子':
            # 张庭	继子	林禹
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
        elif myInfor[1] == '助理':
            # 黄昆	助理	朱邦芬
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
        elif myInfor[1] == '院系设置':
            # 墨尔本大学	院系设置	墨尔本商学院
            if '学校' not in infor_dict:
                infor_dict['学校'] = set()
                infor_dict['学校'].add(myInfor[0])
            else:
                infor_dict['学校'].add(myInfor[0])
            if '院系' not in infor_dict:
                infor_dict['院系'] = set()
                infor_dict['院系'].add(myInfor[2])
            else:
                infor_dict['院系'].add(myInfor[2])
        elif myInfor[1] == '继父':
            # 秦沛	继父	尔光
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
        elif myInfor[1] == '大伯哥':
            # 韦皇后	大伯哥	李贤
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
        elif myInfor[1] == '徒弟':
            # 黄磊	徒弟	张艺兴
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
        elif myInfor[1] == '知己':
            # 费雯·丽	知己	约翰·梅里韦尔
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
        elif myInfor[1] == '儿媳':
            # 李道河	儿媳	萧珊
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
        elif myInfor[1] == '堂伯父':
            # 孙释颜	堂伯父	孙孚凌
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
        elif myInfor[1] == '女婿':
            # 李悟	女婿	王元逵
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
        elif myInfor[1] == '亲家公':
            # 柳婕妤	亲家公	王同皎
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
        elif myInfor[1] == '曾祖父':
            # 元举	曾祖父	拓跋桢
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
        elif myInfor[1] == '叔父':
            # 刘休仁	叔父	刘义恭
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
        elif myInfor[1] == '姑母':
            # 李秀	姑母	东阳公主
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
        elif myInfor[1] == '师傅':
            # 宋小宝	师傅	赵本山
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
        elif myInfor[1] == '歌曲原唱':
            # 世界	歌曲原唱	林宥嘉
            if '歌曲名' not in infor_dict:
                infor_dict['歌曲名'] = set()
                infor_dict['歌曲名'].add(myInfor[0])
            else:
                infor_dict['歌曲名'].add(myInfor[0])
            if '人物' not in infor_dict:
                infor_dict['人物'] = set()
                infor_dict['人物'].add(myInfor[2])
            else:
                infor_dict['人物'].add(myInfor[2])
        elif myInfor[1] == '云孙':
            # 傅友德	云孙	傅宗龙
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
        elif myInfor[1] == '外甥':
            # 厉绥之	外甥	施锡祉
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
        elif myInfor[1] == '姑父':
            # 宝安县主	姑父	韦正矩
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
        elif myInfor[1] == '学妹':
            # 朱一龙	学妹	柴碧云
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
        elif myInfor[1] == '小姑子':
            # 贞懿皇后	小姑子	郯国公主
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
        elif myInfor[1] == '第四任妻子':
            # 毛泽东	第四任妻子	江青
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
        elif myInfor[1] == '偶像':
            # 杨培安	偶像	张雨生
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
        elif myInfor[1] == '前任':
            # 林元和	前任	朱振中
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
        elif myInfor[1] == '表姨':
            # 刘亦菲	表姨	周雯琼
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
        elif myInfor[1] == '社长':
            # 李灿熺	社长	李先镐
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
        elif myInfor[1] == '亲家母':
            # 李娥姿	亲家母	独孤伽罗
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
        elif myInfor[1] == '战友':
            # 张陆	战友	刘洋
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
        elif myInfor[1] == '学校身份':
            # 福特汉姆大学	学校身份	爱国者联盟
            if '人物' not in infor_dict:
                infor_dict['人物'] = set()
                infor_dict['人物'].add(myInfor[0])
            else:
                infor_dict['人物'].add(myInfor[0])
            if '学校里的身份' not in infor_dict:
                infor_dict['学校里的身份'] = set()
                infor_dict['学校里的身份'].add(myInfor[2])
            else:
                infor_dict['学校里的身份'].add(myInfor[2])
        elif myInfor[1] == '主要作品':
            # 唐家三少	主要作品	斗罗大陆外传唐门英雄传
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
        elif myInfor[1] == '生母':
            # 江泽民	生母	吴月清
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
        elif myInfor[1] == '类别':
            # 二松学舍大学	类别	私立大学
            if '学校' not in infor_dict:
                infor_dict['学校'] = set()
                infor_dict['学校'].add(myInfor[0])
            else:
                infor_dict['人物'].add(myInfor[0])
            if '学校类别' not in infor_dict:
                infor_dict['学校类别'] = set()
                infor_dict['学校类别'].add(myInfor[2])
            else:
                infor_dict['学校类别'].add(myInfor[2])
        elif myInfor[1] == '外曾祖母':
            # 李重茂	外曾祖母	荣国夫人
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
        elif myInfor[1] == '祖父':
            # 元略	祖父	元桢
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
        elif myInfor[1] == '毕业院校':
            # 徐少华	毕业院校	山东艺术学院
            if '人物' not in infor_dict:
                infor_dict['人物'] = set()
                infor_dict['人物'].add(myInfor[0])
            else:
                infor_dict['人物'].add(myInfor[0])
            if '学校' not in infor_dict:
                infor_dict['学校'] = set()
                infor_dict['学校'].add(myInfor[2])
            else:
                infor_dict['学校'].add(myInfor[2])
        elif myInfor[1] == '知名人物':
            # 南开大学	知名人物	金守光
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
        elif myInfor[1] == '小舅子':
            # 赵昚	小舅子	郭师禹
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
        elif myInfor[1] == '庶子':
            # 张皇后	庶子	李倓
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
        elif myInfor[1] == '所属机构':
            # 西南大学	所属机构	中华人民共和国教育部
            if '单位名' not in infor_dict:
                infor_dict['单位名'] = set()
                infor_dict['单位名'].add(myInfor[0])
            else:
                infor_dict['单位名'].add(myInfor[0])
            if '机构' not in infor_dict:
                infor_dict['机构'] = set()
                infor_dict['机构'].add(myInfor[2])
            else:
                infor_dict['机构'].add(myInfor[2])
        elif myInfor[1] == '表妹':
            # 黄晓明	表妹	陈梦
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
        elif myInfor[1] == '制作':
            # 陈玉珊	制作	千金百分百
            if '人物' not in infor_dict:
                infor_dict['人物'] = set()
                infor_dict['人物'].add(myInfor[0])
            else:
                infor_dict['人物'].add(myInfor[0])
            if '影视作品' not in infor_dict:
                infor_dict['影视作品'] = set()
                infor_dict['影视作品'].add(myInfor[2])
            else:
                infor_dict['影视作品'].add(myInfor[2])
        elif myInfor[1] == '登场作品':
            # 姚莫婉	登场作品	凤唳九天
            if '人物' not in infor_dict:
                infor_dict['人物'] = set()
                infor_dict['人物'].add(myInfor[0])
            else:
                infor_dict['人物'].add(myInfor[0])
            if '影视作品' not in infor_dict:
                infor_dict['影视作品'] = set()
                infor_dict['影视作品'].add(myInfor[2])
            else:
                infor_dict['影视作品'].add(myInfor[2])
        elif myInfor[1] == '嫂子':
            # 谢婷婷	嫂子	张柏芝
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
        elif myInfor[1] == '好友':
            # 宣萱	好友	吕颂贤
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
        elif myInfor[1] == '前公公':
            # 宋丹丹	前公公	英若诚
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
        elif myInfor[1] == '义女':
            # 贾静雯	义女	Rhea
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
        elif myInfor[1] == '师兄':
            # 吴雨霏	师兄	古巨基
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
        elif myInfor[1] == '曾孙':
            # 袁世凯	曾孙	袁缉燕
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
        elif myInfor[1] == '同学':
            # 朱玮菱	同学	李晓明
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
        elif myInfor[1] == '配音':
            # 亚历克·鲍德温	配音	猫狗大战
            if '人物' not in infor_dict:
                infor_dict['人物'] = set()
                infor_dict['人物'].add(myInfor[0])
            else:
                infor_dict['人物'].add(myInfor[0])
            if '影视作品' not in infor_dict:
                infor_dict['影视作品'] = set()
                infor_dict['影视作品'].add(myInfor[2])
            else:
                infor_dict['影视作品'].add(myInfor[2])
        elif myInfor[1] == '堂舅':
            # 郭麒麟	堂舅	王俣钦
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

    for key in infor_dict:
        with open(f'processed_file//{key}.txt', 'w', encoding='utf-8') as fp:
            fp.write("\n".join(infor_dict[key]))
    print(type(infor_dict['人物']),infor_dict['人物'])  # 上传各个结点以及他们的属性
    #  上传所有的关系
