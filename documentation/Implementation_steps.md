# Deep learning model for liver segmentation

A nnU-Net v1 model is developed using this repository https://github.com/MIC-DKFZ/nnUNet/tree/nnunetv1. The nnU-Net v1 was implemented and tested on Linux (Ubuntu 18.04) with an RTX 3060 GPU (12GB VRAM). 

### Environment setup

```conda create -n lipa python=3.8.5``` # create a conda environment with python3.8.5; ```conda remove -n lipa --all ```if you want to delete this conda environment. 'lipa' stands for liver parenchymal

```conda activate lipa```  # activate the conda environment

```conda install nb_conda_kernels```  # Install jupyter notebook

```pip3 install -r requirements.txt``` # Once you change directories into the root path of the project

 ```pip3 install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113```# install pytorch under CUDA 11.3
 
 ```pip3 install nnunet==1.7.1```# install nnunet==1.7.1
 
 ### nnunet paths setup 
 
 -  set nnunet environment path, replace the following with your own user name and repo dir
 -  suppose user name is 'zhongyi' and repo dir is '/home/zhongyi/Desktop/nn-unet_train'

                ```
                cd /home/zhongyi/.bashrc     
                       
                export nnUNet_raw_data_base="/home/zhongyi/Desktop/nn-unet_train/nnUNet_raw_data_base"
                export nnUNet_preprocessed="/home/zhongyi/Desktop/nn-unet_train/nnUNet_preprocessed"
                export RESULTS_FOLDER="/home/zhongyi/Desktop/nn-unet_train/nnUNet_trained_models"                ```                
 
 ### nnunet scripts to segment new CT images
 
 ```nnUNet_raw_data_base/nnUNet_test_data/test_img_in_nii_raw/ ``` # download open-source data into the dir, one image is stored in our repository as an example
 
 ```file_op_to_infer_by_nnunet.ipynb```  # prepare data into the required format, where each nifty image name has to end with '0000.nii.gz'
 
  ```nnUNet_trained_models/ ``` # download pre-trained model from Gdrive or baiduwangpan ```Files_for_running_github/nnUNet_trained_models.zip``` dir. This model was trained with 319 CT images. The required paths are shown in this [screenshot.png](Pre_trained_model_paths.png)
   
 ```nnUNet_predict -i $nnUNet_raw_data_base/nnUNet_test_data/test_img_in_nii/ -o  $nnUNet_raw_data_base/nnUNet_test_data/test_seg_in_nii_raw/ -t 521 -m 3d_fullres -f 1```
  

### segmentation post-process and performance compute
```liver_seg_curated_into_top1_mask.ipynb``` #  post-process the segmented mask to retain the biggest connected component
```liver_seg_various_accuracy_compute.ipynb``` # compute segmentation performances, i.e., dsc, jc, hd, assd 


### -optional: training your own model 

-  ```  nnUNet_raw_data_base/nnUNet_train_data_raw/ ``` # download training data into the dir. 5 CT images can be a toy example, which can be downloaded from Gdrive or baiduwangpan ```Files_for_running_github/nnUNet_train_data_raw.zip``` dir. Required paths are shown in this [screenshot.png](Images_paths_for_training.png)

-  ``` file_op_to_prepare_training_nnunet.ipynb```  #  prepare data into the required format of nnunet: 1/2 step

-   ```python nnunet/dataset_conversion/521_liver-plain.py```   #   prepare data into the required format of nnunet 2/2 step

-   ```python  nnunet/experiment_planning/nnUNet_plan_and_preprocess.py -t 521 --verify_dataset_integrity```    # pre-process the data using nnunet scripts
             
-   ```nnUNet_train 3d_fullres nnUNetTrainerV2 521 1```  # nnunet training, the '1' stands for training 1st fold of the five-fold cross validation
