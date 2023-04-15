# Deep learning to select liver parenchyma for categorizing hepatic steatosis on multinational chest CT

### Method introduction

DL-parenchymal method can automatically select parenchymal portion for measuring liver attenuation on CT images. This novel method can enhance incidental assessments of moderate-to-severe hepatic steatosis detection using unenhanced chest CT images.

- [Methodology details is shown here](documentation/Method_introduction.md)

### Implementation scripts

**1. nnU-Net-V1 for liver segmentation**

Please refer to this text: [nnunet implementation.md](documentation/installation_instructions.md)


**2.  DL-parenchymal attenuation measurement**

- [DL_seg_to_select_parenchyma.ipynb](DL_seg_to_select_parenchyma.ipynb): Use DL segmentation to select parenchyma for measuring attenuation

**3.  DL-parenchymal steatosis classification**

- [ DL-parenchymal cofusion matrix.ipynb](stats_to_figure/230402_github_Figure_S5_cofusion_matrix_95CI.ipynb): a threshold of DL-based attenuation < 40 HU was applied to categorize moderate-to-severe hepatic steatosis

## Data availability (freely released to the public!)

Our deep learning system was developed and externally validated on a total of 1,014 CT images from cross-national databases. All CT images were reformatted to the NIfTI format and resampled to a consistent voxel spacing of 0.7 x 0.7 x 2.5 mm/pixel. Curated CT images and liver segmentations can be freely downloaded by Google Drive https://drive.google.com/drive/folders/1-g_zJeAaZXYXGqL1OeF6pUjr6KB0igJX or Baidu Wangpan https://pan.baidu.com/s/1nRv-FJU4HtQ4nXi9H9145Q?pwd=2022 (passcode: 2022). 

Of note, our method only derives liver attenuation on unenhanced chest CT images, such as the screening cohorts of lung cancer or COVID-19. Abdominal CT or contrast-enhanced CT images are not applicable.
