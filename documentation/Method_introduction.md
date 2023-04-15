# Deep learning to select liver parenchyma for categorizing hepatic steatosis on multinational chest CT

## Background and objectives

Unenhanced liver attenuation alone is highly specific to indicate moderate-to-severe steatosis on CT images. Typically, the CT attenuation is measured by radiologists on parenchymal portions to represent the whole-liver fat content. Yet, this is time-consuming and thus requires an automated tool. Here, we aim to develop a deep-learning (DL) system that can automatically select parenchymal regions for measuring liver attenuation and categorizing moderate-to-severe hepatic steatosis in multinational unenhanced chest CT images.

## Materials (freely released to the public!)

This retrospective study included 1,014 CT images from cross-national databases. All CT images were reformatted to the Neuroimaging Informatics Technology Initiative (NIfTI) format, and linear interpolations were employed to resample them to a consistent voxel spacing of 0.7 x 0.7 x 2.5 mm/pixel. Curated CT images and ground truths can be freely downloaded by Google Drive https://drive.google.com/drive/folders/1-g_zJeAaZXYXGqL1OeF6pUjr6KB0igJX or Baidu Wangpan https://pan.baidu.com/s/1nRv-FJU4HtQ4nXi9H9145Q?pwd=2022 (passcode: 2022). 

## Methods
Firstly, imaged livers are segmented by a nn-unet model. Secondly, DL-based automated methods are purposed for measuring liver attenuation, namely DL-volumetric, DL-axial, and DL-parenchymal attenuation.The DL-parenchymal method leverages 3D auto-segmentation to place circular portions on the liver parenchyma. The center of the circular portion is positioned 20 mm to the right of the leftmost pixel on the axial slice. A circular area of approximately 20 mm² is selected to encompass the full spectrum of liver fat, with one region per slice and the three largest slices chosen at a distance of 5 mm.

![Deep learning system overview](https://user-images.githubusercontent.com/73850754/230751205-b5de553a-2d71-42ba-9b6a-d788d6d0f258.png)

Previous studies developed automated methods to measure CT attenuation, but their accuracy was limited due to the inclusion of non-parenchymal regions 26–30. In contrast, our study addressed these limitations by developing the DL-parenchymal method, which used deep learning-based liver segmentation to automatically select parenchymal portions. This novel method achieved expert-level accuracy, stable generalizability across various centers and countries, and independent objectivity over the inter-reader variability among human experts. By automating the parenchymal selection, our approach represented a significant improvement in the accuracy and efficiency of hepatic steatosis detection using CT scans.


### How does AI-ROI work?
**1. nnU-Net-V1 for liver segmentation**

- [Details of model implementation](documentation/installation_instructions.md)

The model is developed using this repository and applied into our DL system https://github.com/MIC-DKFZ/nnUNet/tree/nnunetv1

**2.  DL-parenchymal attenuation measurement**

- [DL_seg_to_select_parenchyma.ipynb](DL_seg_to_select_parenchyma.ipynb): Deep learning to select liver parenchyma for measuring attenuation

**3.  DL-parenchymal steatosis classification**

- [ DL-parenchymal cofusion matrix.ipynb](stats_to_figure/230402_github_Figure_S5_cofusion_matrix_95CI.ipynb): a threshold of DL-based attenuation < 40 HU was applied to categorize moderate-to-severe hepatic steatosis

### Where does AI-ROI perform well and where does it not perform?
AI-ROI only derives liver attenuation on unenhanced chest CT images, such as the routine screening for lung cancer or COVID-19. Abdominal CT or contrast-enhanced CT images are not applicable.
