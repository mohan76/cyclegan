import torch
import albumentations as A
from albumentations.pytorch import ToTensorV2

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
TRAIN_DIR = "../drive/MyDrive/data/cyclegan/images/monet/train"
VAL_DIR = "../drive/MyDrive/data/cyclegan/images/monet/val"
BATCH_SIZE = 1
LEARNING_RATE = 1e-5
LAMBDA_IDENTITY = 0.0
LAMBDA_CYCLE = 10
NUM_WORKERS = 4
NUM_EPOCHS = 10
LOAD_MODEL = True
SAVE_MODEL = True
CHECKPOINT_GEN_H = "../drive/MyDrive/data/cyclegan/pretrained/genh.pth.tar"
CHECKPOINT_GEN_Z = "../drive/MyDrive/data/cyclegan/pretrained/genz.pth.tar"
CHECKPOINT_CRITIC_H = "../drive/MyDrive/data/cyclegan/pretrained/critich.pth.tar"
CHECKPOINT_CRITIC_Z = "../drive/MyDrive/data/cyclegan/pretrained/criticz.pth.tar"

transforms = A.Compose(
    [
        A.Resize(width=256, height=256),
        A.HorizontalFlip(p=0.5),
        A.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5], max_pixel_value=255),
        ToTensorV2(),
     ],
    additional_targets={"image0": "image"},
)
