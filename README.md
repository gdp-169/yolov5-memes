# yolov5-memes
人工智能课程设计

虚拟环境创建：

conda create --name xxx python=3.9

创建一个名为xxx的虚拟环境（安装了anaconda情况下）


激活虚拟环境：

在项目目录下输入

conda activate xxx

来启用虚拟环境


安装项目依赖库：

pip install -r requirements.txt


数据集划分：

将脚本中的源文件路径和目标文件路径修改完后运行image2jpg.py


数据标注：

在目标文件路径同级目录下创建一个labels文件夹后，并且目录下同样需创建train、val、test三个文件夹

即可在项目路径下的终端中输入labelimg打开标注插件，选择完源文件目录和标注文件目录后就可开始标注

仿照memes_data.yaml编写一个yaml文件来描述目标类别数及类别

模型训练：

python train.py --data memes_data.yaml --cfg memes_yolov5m.yaml --weights pretrained/yolov5m.pt --epoch 100 --batch-size 4 --device cpu

若安装了设备有nvidia显卡，且安装了cuda可以使用--device 0来调用显卡训练


模型评估：

python val.py --task test --data memes_data/memes_data.yaml --weights runs/train/exp/weights/best.pt 







