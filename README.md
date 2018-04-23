# 数据挖掘第一次大作业——决策树


#### 利用C4.5算法生成决策树，仅针对二分类问题

其中决策树停止条件

1.信息增益小于0.1

2.没有多余的属性



#### 程序输入输出

输入格式.csv文件，输出使用决策树预测结果的准确率(仅当前训练集)





#### 测试集

训练的测试集使用了sample.csv和play_golf.csv



| **年龄** | **有工作** | **有自己的房子** | **信贷情况** | **类别** |
| -------- | ---------- | ---------------- | ------------ | -------- |
| **青年** | 否         | 否               | 一般         | 0        |
| **青年** | 否         | 否               | 好           | 0        |
| **青年** | 是         | 否               | 好           | 1        |
| **青年** | 是         | 是               | 一般         | 1        |
| **青年** | 否         | 否               | 一般         | 0        |
| **中年** | 否         | 否               | 一般         | 0        |
| **中年** | 否         | 否               | 好           | 0        |
| **中年** | 是         | 是               | 好           | 1        |
| **中年** | 否         | 是               | 非常好       | 1        |
| **中年** | 否         | 是               | 非常好       | 1        |
| **老年** | 否         | 是               | 非常好       | 1        |
| **老年** | 否         | 是               | 好           | 1        |
| **老年** | 是         | 否               | 好           | 1        |
| **老年** | 是         | 否               | 非常好       | 1        |
| **老年** | 否         | 否               | 一般         | 0        |

> sample.csv 该数据集来自 《统计学习方法》李航



| **Outlook**  | **Temperature** | **Humidity** | **Windy** | **Play Golf?** |
| ------------ | --------------- | ------------ | --------- | -------------- |
| **Rainy**    | Hot             | High         | FALSE     | No             |
| **Rainy**    | Hot             | High         | TRUE      | No             |
| **Overcast** | Hot             | High         | FALSE     | Yes            |
| **Sunny**    | Mild            | High         | FALSE     | Yes            |
| **Sunny**    | Cool            | Normal       | FALSE     | Yes            |
| **Sunny**    | Cool            | Normal       | TRUE      | No             |
| **Overcast** | Cool            | Normal       | TRUE      | Yes            |
| **Rainy**    | Mild            | High         | FALSE     | No             |
| **Rainy**    | Cool            | Normal       | FALSE     | Yes            |
| **Sunny**    | Mild            | Normal       | FALSE     | Yes            |
| **Rainy**    | Mild            | Normal       | TRUE      | Yes            |
| **Overcast** | Mild            | High         | TRUE      | Yes            |
| **Overcast** | Hot             | Normal       | FALSE     | Yes            |
| **Sunny**    | Mild            | High         | TRUE      | No             |

> Play_golf.csv 该数据集来自于University of Toronto data-mining 的讲义



#### 测试结果

对两例测试准确率均为1