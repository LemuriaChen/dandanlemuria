
# A toolkit for natural language processing

## Installation

```shell script
pip install dandanlemuria
```

## Features

### API integration

#### automatic translation

要使用自动翻译功能，需要先在百度翻译网站上注册个人开发者账号，点击[这里](https://api.fanyi.baidu.com/)注册。

**常用语言代码**

代码 | 名称 |
:-: | :-: |
zh | 中文 |
en | 英文 |
yue | 粤语 | 
wyw | 文言文 |
jp | 日文 |
fra | 法语 |

```python
import dandanlemuria as ddl

trans = ddl.Trans()
trans.add_app_id('')
trans.add_secret_key('')
trans.translate('好好学习，天天向上', from_lang='zh', to_lang='en')
```

#### automatic abbreviation

自动缩写功能整合了[allacronyms](https://www.allacronyms.com/)网站的功能，主要功能如下：

* 返回给定英文字符串的缩写（get_abbreviation）
* 返回给定英文字符串的全称（get_fullname）

```python
import dandanlemuria as ddl

ddl.Abbrev().get_abbreviation('Translation', verbose=True, best=False)
ddl.Abbrev().get_fullname('ABC', verbose=True)
```

### Service interface (To DO)

* machine translation
* dialogue system
* argumentation mining
* annotation system

