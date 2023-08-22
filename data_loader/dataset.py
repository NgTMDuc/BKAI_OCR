import os
import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import torch
import random
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils

class HandWritttenDataset(Dataset):
    """Hand Writtten dataset."""

    def __init__(self, label_file, root_dir, transform=None):
        """
        Arguments:
            label_file (string): Path to the label file.
            root_dir (string): Directory with all the images.
            transform (callable, optional): Optional transform to be applied
                on a sample.
        """
        self.labels = pd.read_csv(label_file, sep='\t', header=None)
        self.root_dir = root_dir
        self.transform = transform

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        img_name = os.path.join(self.root_dir,
                                self.labels.iloc[idx,0])
        image = Image.open(img_name)
        label = self.labels.iloc[idx, 1]
        
        return image,label
    
if __name__ == "__main__":
    train_dataset = HandWritttenDataset("/kaggle/input/handwrittenocr-split/train_list.txt", "/kaggle/working/new_train")
    val_dataset = HandWritttenDataset("/kaggle/input/handwrittenocr-split/val_list.txt", "/kaggle/working/new_train")