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
'人物','文学作品','文学作品平台'


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
    node_list = ['人物', '学术会', '联盟', '音乐作品', '学院', '英文名', '文学作品', '出版社', '音乐组合', '公司', '学校', '影视作品', '综艺节目', '学院', '协会', '单位', '学校类别' ]
    for i in node_list:
        infor_dict[i] = set()
    for myInfor in infor:  # 属性可能相同，但属于不同结点
        if myInfor[1] == '相关国内联盟':
            # 学术研究恳谈会	相关国内联盟	八大学工学系联合会
            infor_dict['学术会'].add(myInfor[0])
            infor_dict['联盟'].add(myInfor[2])
        if myInfor[1] == '外曾祖父':
            # 李恒	外曾祖父	郭子仪
            # 薛崇胤	外曾祖父	李世民
            # 安藤樱	外曾祖父	犬养毅
            # 安藤桃子	外曾祖父	犬养毅
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '男朋友':
            # 朱晨丽	男朋友	古思宇
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '叔叔':
            # 赵仲斀	叔叔	赵宗晟
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '大姨子':
            # 周道务	大姨子	东阳公主
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '侄女':
            # 大名公主	侄女	陈留郡主
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '音乐作品':
            # 杨钰莹	音乐作品	悲哀的恋情
            infor_dict['人物'].add(myInfor[0])
            infor_dict['音乐作品'].add(myInfor[2])
        if myInfor[1] == '简称':
            #哈佛商学院	简称	HBS
            infor_dict['学院'].add(myInfor[0])
            infor_dict['英文名'].add(myInfor[2])
        if myInfor[1] == '义子':
            #伊能静	义子	夏健强
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '曾祖母':
            #赵机	曾祖母	高滔滔
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '经纪人':
            #张学友	经纪人	陈淑芬
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '先夫':
            #翁静晶	先夫	刘家良
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '未婚妻':
            #阿尔菲·艾伦	未婚妻	杰美·温斯顿
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '姨夫':
            #长孙延	姨夫	韦正矩
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '表姑父':
            #蓝心妍	表姑父	胡友林
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '义兄':
            #刘家辉	义兄	刘家荣
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '为他人创作音乐':
            #徐佳莹	为他人创作音乐	毛毛雨
            infor_dict['人物'].add(myInfor[0])
            infor_dict['音乐作品'].add(myInfor[2])
        if myInfor[1] == '表侄':
            #沈从文	表侄	黄永玉
            #沈从文	表侄	黄永厚
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '连襟':
            #王小利	连襟	关小平
            #关小平	连襟	王小利
            #郭京飞	连襟	陆毅
            #陆毅	连襟	郭京飞
            #蒋介石	连襟	孔祥熙
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '姐夫':
            #朱椿	姐夫	张麟
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '出版社':
            #飘香剑雨	出版社	珠海出版社
            infor_dict['文学作品'].add(myInfor[0])
            infor_dict['出版社'].add(myInfor[2])
        if myInfor[1] == '学生':
            #梅葆玖	学生	李胜素
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '弟弟':
            #朱樉	弟弟	朱桂
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '同门':
            #王君安	同门	萧雅
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '师生':
            #李志希	师生	胡金铨
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '叔外公':
            #李小龙	叔外公	何东
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '曾孙女':
            #李治	曾孙女	临晋公主
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '教练':
            #刘京	教练	陈映红
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '侄孙':
            #许崇智	侄孙	许绍雄
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '老板':
            #张婧仪	老板	周迅
            #周也	老板	李冰冰
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '妹妹':
            #赵缨络	妹妹	赵珠珠
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '前队友':
            #高世名	前队友	李宁
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '表兄':
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '孙子':
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '亡妻':
            #梁思成	亡妻	林徽因
            #杨振宁	亡妻	杜致礼
            #莫科	亡妻	王凡
            #陆定一	亡妻	唐义贞
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '经纪公司':
            #black queen	经纪公司	北京梦明时代文化传媒有限公司
            #BOYFRIEND	经纪公司	STARSHIP Entertainment
            if '音乐组合' not in infor_dict:
                infor_dict['音乐组合'] = set()
            if '公司' not in infor_dict:
                infor_dict['公司'] = set()
            infor_dict['音乐组合'].add(myInfor[0])
            infor_dict['公司'].add(myInfor[2])
        if myInfor[1] == '代表':
            #私立大学	代表	哈佛大学
            if '学校' not in infor_dict:
                infor_dict['学校'] = set()
            infor_dict['学校'].add(myInfor[0])
            infor_dict['学校'].add(myInfor[2])
        if myInfor[1] == '大姑子':
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '第六任妻子':
            #朱德	第六任妻子	康克清
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '搭档':
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '伯母':
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '祖母':
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])

        if myInfor[1] == '领导':
            if '大学' in myInfor[0]  or '中学' in myInfor[0]:
                infor_dict['学校'].add(myInfor[0])
            elif '学院' in myInfor[0] or '研究生院' in myInfor[0] or '系' in myInfor[0]:
                infor_dict['学院'].add(myInfor[0])
            elif '联合会' in myInfor[0] or '协会' in myInfor[0] or '委员会' in myInfor[0] or '学会' in myInfor[0] or '体育总局' in myInfor[0]:
                infor_dict['协会'].add(myInfor[0])
            elif '保障局' in myInfor[0] or '人民政府' in myInfor[0] or '法院' in myInfor[0] or '研究院' in myInfor[0] or '法院' in myInfor[0] or '工业和信息化部' in myInfor[0] or '银行' in myInfor[0]:
                infor_dict['单位'].add(myInfor[0])
            elif '出版社' in myInfor[0]:
                infor_dict['出版社'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])

        if myInfor[1] == '继任':
            #杨伟光	继任	赵化勇
            #赵启正	继任	吕新华
            #詹福瑞	继任	周和平
            #顾秉林	继任	陈吉宁
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '参演':
            infor_dict['人物'].add(myInfor[0])
            infor_dict['影视作品'].add(myInfor[2])
        if myInfor[1] == '表叔':
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '伯乐':
            #马思纯	伯乐	苏有朋
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '婶母':
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '婆婆':
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])

        if myInfor[1] == '现任领导':
            if '大学' in myInfor[0] or '中学' in myInfor[0]:
                infor_dict['学校'].add(myInfor[0])
            elif '学院' in myInfor[0] or '研究生院' in myInfor[0] or '系' in myInfor[0]:
                infor_dict['学院'].add(myInfor[0])
            elif '联合会' in myInfor[0] or '协会' in myInfor[0] or '委员会' in myInfor[0] or '学会' in myInfor[
                0] or '体育总局' in myInfor[0]:
                infor_dict['协会'].add(myInfor[0])
            elif '保障局' in myInfor[0] or '人民政府' in myInfor[0] or '法院' in myInfor[0] or '研究院' in myInfor[
                0] or '法院' in myInfor[0] or '工业和信息化部' in myInfor[0] or '银行' in myInfor[0]:
                infor_dict['单位'].add(myInfor[0])
            elif '出版社' in myInfor[0]:
                infor_dict['出版社'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])


        if myInfor[1] == '外曾孙女':
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '表弟':
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '外甥女婿':
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '第五任妻子':
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])

        if myInfor[1] == '编剧':
            if '影视作品' not in infor_dict:
                infor_dict['影视作品'] = set()
            infor_dict['人物'].add(myInfor[0])
            infor_dict['影视作品'].add(myInfor[2])


        if myInfor[1] == '曾外祖母':
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '学姐':
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '义母':
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])

        if myInfor[1] == '类型':
            #中西部高校综合实力提升工程	类型	综合性大学
            #玛利诺修院学校	类型	女子学校
            infor_dict['学校'].add(myInfor[0])
            infor_dict['学校类别'].add(myInfor[2])


        if myInfor[1] == '孙女':
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '表姐':
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '姨母':
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '前妻':
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])

        if myInfor[1] == '合作院校':
            #同志社大学	合作院校	中国海洋大学
            infor_dict['学校'].add(myInfor[0])
            infor_dict['学校'].add(myInfor[2])
        if myInfor[1] == '继女':
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '叔外祖父':
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])
        if myInfor[1] == '妾':
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])

        if myInfor[1] == '专职院士数':
            #浙江大学	专职院士数	中国科学院
            #湖南师范大学	专职院士数	中国工程院院士
            #合肥工业大学	专职院士数	中国工程院院士
            #武汉大学	专职院士数	中国科学院
            #北京理工大学	专职院士数	中国科学院
            #清华大学	专职院士数	中国科学院
            infor_dict['学校'].add(myInfor[0])
            infor_dict['学院'].add(myInfor[2])

        if myInfor[1] == '主持':
            #何炅	主持	大侦探第七季
            infor_dict['人物'].add(myInfor[0])
            infor_dict['综艺节目'].add(myInfor[2])

        if myInfor[1] == '法人':
            #社会科学文献出版社	法人	谢寿光
            infor_dict['出版社'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])

        if myInfor[1] == '妯娌':
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])

        if myInfor[1] == '学校类别':
            #厦门大学	学校类别	综合类大学
            infor_dict['学校'].add(myInfor[0])
            infor_dict['学校类别'].add(myInfor[2])

        if myInfor[1] in ['义弟', '哥哥', '大舅子', '义父', '伯伯', '父亲', '外祖母', '第一任丈夫', '外孙子', '玄孙', '姑姑', '师姐', '大舅哥', '队友', '外甥女', '小姨子', '堂妹']:
            infor_dict['人物'].add(myInfor[0])
            infor_dict['人物'].add(myInfor[2])

'''    with open('ddd.txt', 'w+', encoding='utf-8') as file:
        for i,j in infor_rela.items():
            for k in j:
                #print(k)
                file.write(f'{k[0]}\t{k[1]}\t{k[2]}\n')'''

