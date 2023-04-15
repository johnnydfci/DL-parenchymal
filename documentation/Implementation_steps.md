# A nnU-Net v1 for liver segmenation

## Implementation instructions
The nnU-Net v1 was implemented and tested on Linux (Ubuntu 18.04) with a RTX 3060 GPU (12GB VRAM).

### Environment setup

- 1- install conda 
- 2- ```conda activate dl-parenchymal ``` 
- 3- ```pip3 install -r requirement.txt ``` 
- 4- ```pip3 install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113 # CUDA 11.3```

### Data and file paths prepare

- 5-  ```  nnUNet_raw_data_base/nnUNet_train_data_raw/ ``` # download training data into the dir

- 6-  ``` file_op_to_prepare_training_nnunet.ipynb  #  prepare data into the required format of nnunet: 1/2 step```

      python nnunet/dataset_conversion/521_liver-plain.py   #   prepare data into the required format of nnunet 2/2 step```
- 7- set nnunet enviornment 

                ``` cd /home/---(user name)/.bashrc                
                export nnUNet_raw_data_base="---(repo dir)/nnUNet_raw_data_base"
                export nnUNet_preprocessed="---(repo dir)/nnUNet_preprocessed"
                export RESULTS_FOLDER="---(repo dir)/nnUNet_trained_models"                ```
             
### nnunet scripts for training and test               
- 8- ```nnUNet_plan_and_preprocess  -t 521 --verify_dataset_integrity```
- 9- ```nnUNet_train 3d_fullres nnUNetTrainerV2 521 1```  # nnunet training, the last number stands for only training 1st fold of the five-fold cross validation
- 10- ```nnUNet_predict -i $nnUNet_raw_data_base/nnUNet_test_data/test_img_in_nii/ -o  $nnUNet_raw_data_base/nnUNet_test_data/test_seg_in_nii_raw/ -t 521 -m 3d_fullres -f 1```

### segmentation post-process and performance compute
- 11- ```liver_seg_curated_into_top1_mask.ipynb``` #  post-process the segmented mask to retain the biggest connected component
- 12- ```liver_seg_various_accuracy_compute.ipynb``` # compute segmentation performances, i.e., dsc, jc, hd, assd .
- 13- ```DL_seg_to_select_parenchyma.ipynb``` # select the parenchymal portion to compute liver attenuation using nnunet auto-segmentation









