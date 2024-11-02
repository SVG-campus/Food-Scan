import os
import torch
import pytorch_lightning as pl
from models.yolo import YOLOv5  # Make sure you have YOLOv5 correctly set up
from pytorch_lightning.callbacks import ModelCheckpoint

# Load dataset path and model configuration
dataset_yaml = "dataset.yaml"
model = YOLOv5()

# Set up checkpoints
checkpoint_callback = ModelCheckpoint(
    dirpath='model/',
    filename='best_model',
    monitor='val_loss',
    mode='min',
    save_top_k=1,
)

# Prepare trainer
trainer = pl.Trainer(
    max_epochs=50,
    callbacks=[checkpoint_callback],
    gpus=1 if torch.cuda.is_available() else 0,
)

# Start training
trainer.fit(model, dataloaders=dataset_yaml)
