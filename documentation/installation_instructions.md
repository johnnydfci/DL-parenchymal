# A nnU-Net v1 for liver segmenation

## Implementation instructions
The nnU-Net v1 was implemented and tested on Linux (Ubuntu 18.04) with a RTX 3060 GPU (12GB VRAM).

1. install conda
2. pip3 install -r requirement.txt
3. conda activate dl-parenchymal
4. pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113 # CUDA 11.3
5. download training data into the dir: nnUNet_raw_data_base/nnUNet_train_data_raw/, run file_op_to_prepare_training_nnunet.ipynb 
6. python nnunet/dataset_conversion/521_liver-plain.py  #  preprae data into the required format of nnunet
7. cd /home/zhongyi/.bashrc
export nnUNet_raw_data_base="/home/zhongyi/data_1t/nnunet_v1/nnUNet_raw_data_base"
export nnUNet_preprocessed="/home/zhongyi/data_1t/nnunet_v1/nnUNet_preprocessed"
export RESULTS_FOLDER="/home/zhongyi/data_1t/nnunet_v1/nnUNet_trained_models"
8. nnUNet_plan_and_preprocess  -t 521 --verify_dataset_integrity
9. nnUNet_train 3d_fullres nnUNetTrainerV2 521 1  # nnunet training, the last number stands for only training 1st fold of the five-fold cross validation
10. nnUNet_predict -i /home/zhongyi/data_1t/liver_project/data/img_in_nii_test/img_div_by_60/external_sub2-4/ -o /home/zhongyi/data_1t/liver_project/data/seg_in_nii_test/nnunet_seg_sub2-4/ -t 521 -m 3d_fullres -f 1
11.liver_seg_curated_into_top1_mask.ipynb #  post-process the segmented mask to retain the biggest connected component
12. liver_seg_various_accuracy_compute.ipynb # compute segmentation performances, i.e., dsc, jc, hd, assd .
13. DL_seg_to_select_parenchyma.ipynb # select the parenchymal portion to compute liver attenuation using nnunet auto-segmentation









