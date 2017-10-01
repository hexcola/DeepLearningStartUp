# python 3.6.2
import re
from collections import Counter

def dualPhraseGen(fragment):
    """ 根据句子片段生成二元词组列表.
    """
    phrases = fragment.split(' ')
    dualPhrases = []
    for i in range(len(phrases) - 1):
        dualPhrases.append((phrases[i], phrases[i + 1]) )
    
    return dualPhrases


try:
    with open('happiness_seg.txt', 'r', encoding="utf8") as f:
        
        # 过滤掉所有空行，并将文章中的全角空格替换为`：`，例如：`第一章 　 什么 使人 不幸` 替换为`第一章 ： 什么 使人 不幸`
        lines = [ line.replace('\u3000', '：').strip() for line in f.readlines() if line.strip() != '' ]

        # 创建空的二元词组列表
        dualPhrases = []

        for line in lines:
            
            # 由于对[二元词组] 的定义不是很清楚，比如：二元词组必须有意义？ 
            # 如果必须有意义，则不能称为基本测试了。但诸如 [的 ，] 或 [“ 我] 组合肯定不能算作二元词组的。
            # 因此这里，仅将 章节名称或段落按标点符号分隔成片段。
            for fragment in re.split(u"[\.\!\/_,$%^*:(+\"\']+|[+——！，。？、~@#￥%……&*（）：；“”‘’《》―]+", line):

                # 若片段中没有空格分隔，则表示次片段只有一个词组，不足以形成二元词组
                if fragment.strip().find(' ') != -1:

                    # 将每个二元词组放到列表中去。
                    dualPhrases.extend(dualPhraseGen(fragment.strip()))

        # 统计并输出结果
        print(Counter(dualPhrases).most_common(10))

except OSError:
    print("file not found.")
