# A nnU-Net v1 for liver segmenation

## Operating System and Hardware requirements
.


# Installation instructions
The nnU-Net v1 was implemented and tested on Linux (Ubuntu 18.04) with a RTX 3060 GPU (12GB VRAM).

1. install conda
2. conda activate dl-parenchymal
3. pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113 # CUDA 11.3
4. download data into the dir: nnUNet_raw_data_base/nnUNet_train_data_raw/, run file_op_to_prepare_training_nnunet.ipynb
