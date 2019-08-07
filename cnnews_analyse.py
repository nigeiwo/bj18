#十分抱歉，因为时间紧迫，所以这里只能以此文件代替博客，
# 观察了一下数据集，只有标签和标签，并且三个文件可以合并
# 1.这里我们将训练文本，验证文本以及测试数据合并生成词典。
# 2.将所有的训练文本中的所有词转换为数字，标签页装换Wie数字
# 3. 将转换完的数据保存，具体的文件在

import pandas as pd
import jieba
from collections import Counter
import pickle
train = pd.read_csv(r'cnews\cnews.train.txt', header=None, sep=r'\t', encoding='utf8')
print(train)
test = pd.read_csv(r'cnews\cnews.test.txt', header=None, sep=r'\t', encoding='utf8')
print(test)
val = pd.read_csv(r'cnews\cnews.val.txt', header=None, sep=r'\t', encoding='utf8')
print(val)

all_data = pd.concat((train, test), axis=0)
all_data = pd.concat((all_data, val), axis=0)
print("all_train")
print(all_data[60000:62000])
print(str(all_data[4:5][1]))
stopword = ['，', '。', '！', '@', '、', '？', '+', '#', '%', '（',
            '）', '……', '*', '《', '》', '=', '[', ']', '‘', '’']
all_word = []



for i in range(len(all_data)):
    text = all_data[i:i+1][1]
    text = str(text)
    word = list(jieba.cut(text))
    for w in word:

        all_word.append(w)
print(all_word)
print(len(all_word))
all_word = set(all_word)
print(all_word)

word2id = {}
for w in all_word:
    word2id[w] = len(word2id) + 1


categories = ['体育', '财经', '房产', '家居', '教育', '科技', '时尚', '时政', '游戏', '娱乐']
cate2id = {}
for c in categories:
    cate2id[c] = len(cate2id)

print(word2id)
print(cate2id)

with open('train_data2id.txt', 'w', encoding='utf8') as f:
    for i in range(len(all_data)):
        text = all_data[i:i + 1][1]
        label = str(all_data[i:i+1][0])
        label = label.split()
        label = label[1]
        print(label)
        label_id = cate2id[label]
        text = str(text)
        word = list(jieba.cut(text))
        id_to_wf = []
        for w in word:
            w1 = word2id.get(w, 0)
            id_to_wf.append(w1)
        print(id_to_wf)
        id_to_wf = ' '.join('%s' %id for id in id_to_wf)
        f.write(str(label_id) + '\t' + id_to_wf + '\n')



with open('word2id', 'wb') as f:
    pickle.dump(word2id, f)

with open('cate2id', 'wb') as f:
    pickle.dump(cate2id, f)
