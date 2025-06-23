import os
import random
from PIL import Image
import shutil
from math import floor

def convert_and_split_images(source_dir, target_dir):
    # 支持的图片格式
    valid_formats = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tif', '.tiff', '.webp', '.jfif']
    
    # 创建目标文件夹结构
    for folder in ['train', 'val', 'test']:
        os.makedirs(os.path.join(target_dir, folder), exist_ok=True)
    
    # 收集所有符合条件的图片文件
    image_files = [f for f in os.listdir(source_dir) 
                  if os.path.splitext(f)[1].lower() in valid_formats]
    
    # 打乱文件顺序
    random.shuffle(image_files)
    total = len(image_files)
    
    # 计算分割点
    train_end = floor(total * 0.7)
    val_end = train_end + floor(total * 0.15)
    
    # 分割数据集
    train_files = image_files[:train_end]
    val_files = image_files[train_end:val_end]
    test_files = image_files[val_end:]
    
    # 转换和保存函数
    def process_files(files, set_name):
        for idx, filename in enumerate(files):
            try:
                img_path = os.path.join(source_dir, filename)
                # 转换图片为JPG
                with Image.open(img_path) as img:
                    # 处理透明通道
                    if img.mode in ('RGBA', 'P'):
                        img = img.convert('RGB')
                    # 保存为JPG（quality=95保证最高质量）
                    new_name = f"{set_name}_{idx}.jpg"
                    save_path = os.path.join(target_dir, set_name, new_name)
                    img.save(save_path, 'JPEG', quality=95)
                print(f"已处理: {filename} -> {new_name}")
            except Exception as e:
                print(f"处理文件 {filename} 时出错: {str(e)}")
    
    # 处理各数据集
    process_files(train_files, 'train')
    process_files(val_files, 'val')
    process_files(test_files, 'test')
    
    print(f"转换完成! 总计处理: {total}张图片")
    print(f"训练集: {len(train_files)}张, 验证集: {len(val_files)}张, 测试集: {len(test_files)}张")


if __name__ == "__main__":
    source_directory = "d:/code/python/object_detection/src"  # 替换为源文件夹路径
    target_directory = "memes_data/result"  # 替换为目标文件夹路径
    
    convert_and_split_images(source_directory, target_directory)