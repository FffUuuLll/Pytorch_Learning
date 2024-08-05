from torch.utils.data import Dataset
from PIL import Image
import os

class MyData(Dataset):

    # 初始化数据与标签
    def __init__(self,root_dir,label_dir):
        #读取根路径（ex：train）
        self.root_dir = root_dir
        self.label_dir = label_dir
        #读取标签路径（ex：ants）
        self.path = os.path.join(self.root_dir, self.label_dir)
        #为文件夹建立列表（ex：ants列表，ants[0,1,...]='xxx.jpg'）
        self.img_path=os.listdir(self.path)

    # 通过索引获取样本和标签
    def __getitem__(self,idx):
        #获取列表中的样本路径
        img_name=self.img_path[idx]
        img_item_path=os.path.join(self.root_dir,self.label_dir,img_name)
        #获取图片
        img=Image.open(img_item_path)
        #获取标签
        label=self.label_dir
        return img, label

    #返回数据集长度
    def __len__(self):
        return len(self.img_path)

root_dir='D:\\PythonProject\\Dataset\\hymenoptera_data\\train'
ants_label_dir='ants'
bees_label_dir='bees'
#返回的是数据集的img和label
ants_dataset=MyData(root_dir,ants_label_dir)
bees_dataset=MyData(root_dir,bees_label_dir)


'''选择一个样本检验
img,label=ants_dataset[0]
找到图片，临时显示图像
img.show()'''

#把两个训练样本加起来
train_dataset=ants_dataset+bees_dataset

'''
检验训练样本集
len(ants_dataset)
-->output:124
len(bees_dataset)
-->output:121
img,label=ants_dataset[120]
-->output:ants
img,label=ants_dataset[125]
-->output:bees
'''









#注：self是全局变量







#from PIL import Image
#获取图片地址
# img_path="D:\\PythonProject\\PytorchProject_1\\hymenoptera_data\\train\\ants\\0013035.jpg"
#选择一张图片0013035.jpg，定义其为img
# img=Image.open(img_path)
#展示图片
# img.show()

#import os
#选择一个文件夹，定义为dir_path
# dir_path='D:\\PythonProject\\PytorchProject_1\\hymenoptera_data\\train\\ants'
#将文件夹下的内容变为一个列表，定义为img_path_list
# img_path_list=os.listdir(dir_path)
#查看该列表其中一个,输出为第一个图片名称
#img_path_list[0]
#output:  '0013035.jpg'
#os包合并路径
'''
root_dir='hymenoptera_data/train'
label_dir='ants'
path=os.path.join(root_dir,label_dir)'''


#def __init__(self,data,labels):
#初始化数据与标签
'''#创建实例
data = torch.tensor([[1, 2], [3, 4], [5, 6], [7, 8]])
labels = torch.tensor([0, 1, 0, 1])
dataset = MyData(data, labels)'''

'''以下是发生的事情：
1、实例化
dataset = MyDataset(data, labels) 创建了一个新的 MyDataset 类的实例
Python 调用 MyDataset 类的 __init__ 方法
2、self 的赋值:
self 被自动设置为新创建的 MyDataset 实例
data 和 labels 参数分别接收传入的 data 和 labels 变量
3、初始化属性:
self.data = data 将传入的 data 赋值给实例的 data 属性
self.labels = labels 将传入的 labels 赋值给实例的 labels 属性'''


