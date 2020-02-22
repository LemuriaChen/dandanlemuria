
import setuptools


long_description = """
dandanlemuria
=====
自然语言处理小工具
完整文档见 ``README.md``
GitHub: https://github.com/LemuriaChen/dandanlemuria

功能
====
-  支持单词缩写功能
-  支持单词翻译功能
-  MIT 授权协议

安装说明
========
-  ``pip install dandanlemuria``
"""


setuptools.setup(
    name='dandanlemuria',
    version='0.42.1',
    description='A toolkit for natural language processing',
    long_description=long_description,
    author='dandanlemuria',
    author_email='18110980003@fudan.edu.cn',
    url='https://github.com/LemuriaChen/dandanlemuria',
    license="MIT",
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic',
      ],
    keywords='NLP, toolkit',
    packages=setuptools.find_packages(),
)

