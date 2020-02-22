
import dandanlemuria as ddl

ddl.Abbrev().get_abbreviation('Translation', verbose=False, best=True)
ddl.Abbrev().get_abbreviation('Translation', verbose=True, best=False)
ddl.Abbrev().get_fullname('ABC', verbose=True)


trans = ddl.Trans()
trans.add_app_id('20200116000375850')
trans.add_secret_key('iDqPKmfLykIvbtp1JWV6')
trans.translate('向老板汇报工作时的话术', from_lang='zh', to_lang='jp')

# 常用语言列表
# zh  中文
# en  英文
# yue 粤语
# wyw 文言文
# jp  日文
# fra 法语

long_description = """
dandanlemuria
=====
自然语言处理小工具
完整文档见 ``README.md``
GitHub: https://github.com/LemuriaChen/dandanlemuria
功能
=====
-  支持单词缩写功能
-  支持单词翻译功能
-  MIT 授权协议
安装说明
=====
-  pip install ``dandanlemuria``
"""