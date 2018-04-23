import pandas as pd
import math

data = pd.read_csv('sample.csv')
x = data.iloc[:, :-1]
y = data.iloc[:, -1]
attributes = x.columns.tolist()


# 计算信息增益 其中cat_pos 为每种属性对应的正样本的数目，
# cat_num 为每种属性对应的样本的数目
def Cal_Igr(cat_pos, cat_num):
    ratio = [x / sum(cat_num) for x in cat_num]  # 每一个节点所占的比重
    node = [[x, y - x] for x, y in zip(cat_pos, cat_num)]  # 每一个节点对应的正负样本个数
    node_entropy = [cal_entropy(x) for x in node]  # 计算每个节点对应的熵
    entropy = [x * y for x, y in zip(ratio, node_entropy)]  # 计算加权的熵和
    return sum(entropy)


# 计算熵
def cal_entropy(num):
    ratio = [x / sum(num) for x in num]
    return -sum([x * math.log2(x) if x else 0 for x in ratio])


# 树的节点
class TreeNode(object):

    def __init__(self, data, y, attributes):
        self.son = list()  # son表示一个子节点列表
        self.data = data  # data,y表示当前节点中的数据
        self.y = y
        self.entropy = cal_entropy(y.value_counts().tolist())  # entropy表示当前节点的熵
        self.attributes = attributes.copy()  # 表示还有多少可以使用的属性
        self.attr = None  # None表明这个节点为叶节点，否则表示这个节点分裂时所用的属性
        self.key = list()  # 表示对应的子树的属性取值
        self.label = max(y.value_counts().to_dict())  # 表示该节点的标签值

    def generate_son(self):  # 根据信息熵的增益添加子节点
        if self.entropy is 0 or attributes is None:
            return self.son
        entropy = list()  # 记录每个属性对应的entropy
        for attribute in self.attributes:
            attri_dict = self.data[attribute].value_counts().to_dict()
            catagory_num = list(attri_dict.values())  # 用来存放每个key对应的样本数目
            catagory_pos = list()  # 用来存放每个key对应的正样本数目
            for key in attri_dict.keys():
                catagory_pos.append((self.y[self.data[attribute] == key]).sum())
            entropy.append(self.entropy - Cal_Igr(catagory_pos, catagory_num))
        info_gain = (dict(zip(self.attributes, entropy)))
        # print(entropy)
        if info_gain[max(info_gain)] > 0.1:  # 如果满足分裂的条件
            self.attr = max(info_gain)
            self.attributes.remove(self.attr)  # 移除使用过的属性
            for key in self.data[self.attr].value_counts().to_dict().keys():
                data_ = self.data[self.data[self.attr] == key].reset_index(drop=True)
                y_ = (self.y[self.data[self.attr] == key]).reset_index(drop=True)
                self.son.append(TreeNode(data_, y_, self.attributes))
                self.key.append(key)
        return self.son


def predict(X):  # 进行值的预测
    y_ = list()
    for i in range(len(X)):
        row = X.iloc[i]
        node = tree
        while node.attr:
            node = node.son[node.key.index(row[node.attr])]
        y_.append(node.label)
    y_ = pd.Series(y_, name=y.name)
    return y_


def cal_precison(Y, Y_):  # 计算精确度
    print(sum(Y == Y_) / len(Y))


tree = TreeNode(data, y, attributes)
sons = tree.generate_son()

while (sons):  # 对样本进行训练，逐层向下生长树
    temp = list()
    for son in sons:
        a = son.generate_son()
        temp.extend(a)
    sons = temp

cal_precison(y, predict(x))   #计算该次分类的精确度
