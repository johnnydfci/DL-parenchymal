# Welcome to the AI-ROI!

## Why AI-ROI is purposed?

Background and objectives: Unenhanced liver attenuation alone is highly specific to indicate moderate-to-severe steatosis on CT images. Typically, the CT attenuation is measured by radiologists on a circular region of interest (ROI) to represent the whole-liver fat content. Yet, it is time-consuming and requires an automated tool. 

## What is AI-ROI?

Here, we develop a fully automated artificial-intelligence (AI) system using deep learning auto-segmentation to measure liver attenuation on AI-selected ROIs, called AI-ROI, and to categorize moderate-to-severe steatosis using AI-ROI attention. The AI-ROI attenuation was derived from three circular portions (ROI) of the parenchymal region on the automated segmentation. Using the AI-ROI method, liver attenuation was obtained while eliminating the need for laborious and subjective selections of manual ROI.

## What is the novelty of AI-ROI?

Previous studies developed automated methods to measure CT attenuation, but their accuracy was limited due to the inclusion of non-parenchymal regions. In contrast, the AI-ROI method addressed these limitations by using AI auto-segmentation to automatically select ROI portions of the liver parenchyma, eliminating the need for manual selection. Notably, AI-ROI method achieved expert-level accuracy, making it a reliable approach for population-based screening of hepatic steatosis using non-enhanced chest CT scans. By overcoming these limitations, our approach represented a significant improvement in the accuracy and efficiency of hepatic steatosis detection using CT scans.

## What can AI-ROI do for you?
If you are an **AI researcher** developing segmentation methods, AI-ROI provides 1,014 unenhanced chest CT images and 3D liver masks for your development or transfer learning.

If you are a **clinican or radiologist** looking to analyze your own chest CT images, AI-ROI provides an out-of-the-box solution to derive the unenhanced liver attenuation to assess moderate-to-severe steatosis on multicenter cross-national cohort.

### How does AI-ROI work?
To automate the process of liver segmentation and attenuation measurements, a deep learning model was developed in our AI system:  nnU-Net-V1

### How to infer CT images using the trained nnU-Net?
Read these:
- [Installation instructions](documentation/installation_instructions.md)
- [Dataset conversion](documentation/dataset_format.md)
- [Usage instructions](documentation/how_to_use_nnunet.md)


### Where does AI-ROI perform well and where does it not perform?
AI-ROI only derives liver attenuation on unenhanced chest CT images, such as the routine screening for lung cancer or COVID-19. Abdominal CT or contrast-enhanced CT images are not applicable.
