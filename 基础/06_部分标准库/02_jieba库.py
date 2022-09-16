# jieba.lcut(s): 精准模式，返回一个列表类型
import jieba
txt = input('请输入一个中文文本：')
ls = jieba.lcut(txt)
print('{:.1f}'.format(len(txt)/len(ls)))

# 例题：键盘输入“俄罗斯举办世界杯”，屏幕输出“中文字符数为8，中文词语数为2”
txt = input('请输入：')
n = len(txt)
m = len(jieba.lcut(txt))
print('中文字符数为{}, 中文词语数为{}'.format(n, m))