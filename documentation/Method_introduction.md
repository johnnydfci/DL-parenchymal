#  DL-parenchymal method for measuring liver attenuation

![DLsystem_Github](https://user-images.githubusercontent.com/73850754/232229870-df9e2fad-2649-4041-9f29-38855c957a76.png)


## Background and objectives

Unenhanced liver attenuation alone is highly specific to indicate moderate-to-severe steatosis on CT images. Typically, the CT attenuation is measured by radiologists on parenchymal portions to represent the whole-liver fat content. Yet, this is time-consuming and thus requires an automated tool. Here, we aim to develop a deep-learning (DL) system that can automatically select parenchymal regions for measuring liver attenuation and categorizing moderate-to-severe hepatic steatosis in multinational unenhanced chest CT images.

## Methods
Firstly, imaged livers are segmented by a nn-unet model. Secondly, DL-based automated methods are purposed for measuring liver attenuation, namely DL-volumetric, DL-axial, and DL-parenchymal attenuation.The DL-parenchymal method leverages 3D auto-segmentation to place circular portions on the liver parenchyma. The center of the circular portion is positioned 20 mm to the right of the leftmost pixel on the axial slice. A circular area of approximately 20 mm² is selected to encompass the full spectrum of liver fat, with one region per slice and the three largest slices chosen at a distance of 5 mm.

## Novelty
Previous studies developed automated methods to measure CT attenuation, but their accuracy was limited due to the inclusion of non-parenchymal regions 26–30. In contrast, our study addressed these limitations by developing the DL-parenchymal method, which used deep learning-based liver segmentation to automatically select parenchymal portions. This novel method achieved expert-level accuracy, stable generalizability across various centers and countries, and independent objectivity over the inter-reader variability among human experts. By automating the parenchymal selection, our approach represented a significant improvement in the accuracy and efficiency of hepatic steatosis detection using CT scans.
