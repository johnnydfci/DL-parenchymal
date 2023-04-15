# A nnU-Net v1 for liver segmenation

The nnU-Net v1 model is developed using this repository and applied into our DL system https://github.com/MIC-DKFZ/nnUNet/tree/nnunetv1. The nnU-Net v1 was implemented and tested on Linux (Ubuntu 18.04) with a RTX 3060 GPU (12GB VRAM). 

### Environment setup

```conda create -n dl_parenchymal python=3.8.5``` # create a conda environment with python3.8.5; ```conda remove -n dl_parenchymal --all ```if you want to delete this conda environment

```conda activate dl_parenchymal```  # activate the conda environment

```conda install nb_conda_kernels```  # Install jupyter notebook

```pip3 install -r requirements.txt``` # Once you change directories into the root path of the project

 ```pip3 install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113```# install pytorch under CUDA 11.3

### Data and file paths prepare

-  ```  nnUNet_raw_data_base/nnUNet_train_data_raw/ ``` # download training data into the dir

-  ``` file_op_to_prepare_training_nnunet.ipynb```  #  prepare data into the required format of nnunet: 1/2 step

      ```python nnunet/dataset_conversion/521_liver-plain.py```   #   prepare data into the required format of nnunet 2/2 step
-  set nnunet enviornment path, replace the following with your own user name and repo dir

                ``` cd /home/---(user name)/.bashrc                
                export nnUNet_raw_data_base="---(repo dir)/nnUNet_raw_data_base"
                export nnUNet_preprocessed="---(repo dir)/nnUNet_preprocessed"
                export RESULTS_FOLDER="---(repo dir)/nnUNet_trained_models"                ```
                
-  set nnunet data path                 
    ```nnUNet_plan_and_preprocess  -t 521 --verify_dataset_integrity```             
### nnunet scripts for training 
              
 - optional ```nnUNet_train 3d_fullres nnUNetTrainerV2 521 1```  # nnunet training, the last number stands for only training 1st fold of the five-fold cross validation

### nnunet scripts to segment liver (infer)
 ```nnUNet_predict -i $nnUNet_raw_data_base/nnUNet_test_data/test_img_in_nii/ -o  $nnUNet_raw_data_base/nnUNet_test_data/test_seg_in_nii_raw/ -t 521 -m 3d_fullres -f 1```

### segmentation post-process and performance compute
```liver_seg_curated_into_top1_mask.ipynb``` #  post-process the segmented mask to retain the biggest connected component
```liver_seg_various_accuracy_compute.ipynb``` # compute segmentation performances, i.e., dsc, jc, hd, assd 
