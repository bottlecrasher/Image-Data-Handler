# Creator : Kim Jonghhyuk
# Create Validation set for machine learning or Deep learning algorithms
# All of the classes of dataset must in the direct subdirectory of original_path.
# This code DO NOT recursively find all the subdirectory of the original_path.
# Train and Test dataset is saved at <target_path>/train, <target_path>/test

import os
import shutil
import numpy as np
import time
import math
import argparse

parser = argparse.ArgumentParser(description='Validation Set Creater')
parser.add_argument('original_path', type=str, metavar='ORIGINAL_PATH', help='Original dataset path.')
parser.add_argument("target_path", type=str, metavar="TARGET_PATH", help="Target path for new dataset is preserved.")
parser.add_argument("--validation-size", type=float, default = 0.2, metavar="TEST_SIZE", help="Test size for the dataset")
args = parser.parse_args()

original_path = os.walk(args.original_path)

if os.path.exists(args.target_path) == False:
    os.mkdir(args.target_path)
target_path = args.target_path
validation_size = args.validation_size

passed_time = time.time()
# recurrently loop all of the filetree and split all of them.
for root, dirs, __ in original_path:
    if os.path.exists(os.path.join(target_path, "train")) == False:
        os.mkdir(os.path.join(target_path, "train"))
    if os.path.exists(os.path.join(target_path, "test")) == False:
        os.mkdir(os.path.join(target_path, "test"))
    for dir in dirs:
        if os.path.exists(os.path.join(target_path,"train",dir)) == False:
            os.mkdir(os.path.join(target_path,"train",dir))
        if os.path.exists(os.path.join(target_path,"test",dir)) == False:
            os.mkdir(os.path.join(target_path,"test",dir))

        for _ , __, files in os.walk(os.path.join(root, dir)):
            all_indexs = np.array(list(range(len(files))))
            np.random.shuffle(all_indexs)
            for index in all_indexs[:math.floor((len(files)*(1-validation_size)))]:
                original_file_path = os.path.join(root, dir, files[index])
                target_file_path = os.path.join(target_path,"train", dir, files[index])
                shutil.copy(original_file_path, target_file_path)
                print("{} copied into train folder".format(original_file_path))
            for index in all_indexs[math.floor((len(files)*(1-validation_size))):]:
                original_file_path = os.path.join(root, dir, files[index])
                target_file_path = os.path.join(target_path,"test",dir,files[index])
                shutil.copy(original_file_path, target_file_path)
                print("{} copied into test folder".format(original_file_path))
            break
    break
print("All of the process Done in {} seconds".format(time.time()-passed_time))
