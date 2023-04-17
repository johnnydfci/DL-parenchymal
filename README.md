# Deep learning to select liver parenchyma for categorizing hepatic steatosis on multinational chest CT

Welcome to our GitHub repository for the DL-parenchymal method, an automated deep-learning (DL) system for detecting moderate-to-severe hepatic steatosis on unenhanced chest CT images. This repository provides the implementation of our method, including a nnunet for liver segmentation, the script to pick parenchymal portions using DL auto-segmentation, as well as the dataset used for development and validation.

### Method introduction

The DL-parenchymal method can automatically select the parenchymal portion for measuring liver attenuation on CT images. This novel method can enhance incidental assessments of moderate-to-severe hepatic steatosis detection using unenhanced chest CT images. [Method details.md](documentation/Method_introduction.md)

### Implementation steps

1. nnU-Net-V1 for liver segmentation: [Implementation_steps.md](documentation/Implementation_steps.md)

2. use auto-segmentation to select parenchyma and measure attenuation: [DL_seg_to_select_parenchyma.ipynb](DL_seg_to_select_parenchyma.ipynb)

3. categorize moderate-to-severe hepatic steatosis: [230402_github_Figure_S5_cofusion_matrix_95CI.ipynb](stats_to_figure/230402_github_Figure_S5_cofusion_matrix_95CI.ipynb)  

4. plot figures of results: ```dir: stats_to_figure/ ```

Our deep learning system was developed and externally validated on a total of 1,014 CT images from cross-national databases. All CT images were reformatted to the NIfTI format and resampled to a consistent voxel spacing of 0.7 x 0.7 x 2.5 mm/pixel. Curated CT images and liver segmentations can be freely downloaded by Google Drive https://drive.google.com/drive/folders/1-g_zJeAaZXYXGqL1OeF6pUjr6KB0igJX or Baidu Wangpan https://pan.baidu.com/s/1nRv-FJU4HtQ4nXi9H9145Q?pwd=2022 (passcode: 2022). 

Of note, our method only derives liver attenuation on unenhanced chest CT images, such as the screening cohorts of lung cancer or COVID-19. Abdominal CT or contrast-enhanced CT images are not applicable.

## Publication

Preprint: A version of this DL system has been uploaded to arXiv as a preprint with a perpetual and non-exclusive license and a DOI (https://doi.org/10.48550/arXiv.2210.15149).

Peer-reviewed article: to be updated

## License

Apache License, Version 2.0
