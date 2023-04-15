# A nnU-Net v1 for liver segmenation

## Operating System and Hardware requirements
 on Linux (Ubuntu 18.04) with a RTX 3060 GPU (12GB VRAM).


# Installation instructions
We strongly recommend that you install nnU-Net in a virtual environment! Pip or anaconda are both fine. If you choose to 
compile PyTorch from source (see below), you will need to use conda instead of pip. 

Use a recent version of Python! 3.9 or newer is guaranteed to work!

**nnU-Net v2 can coexist with nnU-Net v1! Both can be installed at the same time.**

1) Install [PyTorch](https://pytorch.org/get-started/locally/) as described on their website (conda/pip). Please 
install the latest version with support for your hardware (cuda, mps, cpu).
**DO NOT JUST `pip install nnunetv2` WITHOUT PROPERLY INSTALLING PYTORCH FIRST**. For maximum speed, consider 
[compiling pytorch yourself](https://github.com/pytorch/pytorch#from-source) (experienced users only!). 
2) Install nnU-Net depending on your use case:
    1) For use as **standardized baseline**, **out-of-the-box segmentation algorithm** or for running 
     **inference with pretrained models**:

       ```pip install nnunetv2```

    2) For use as integrative **framework** (this will create a copy of the nnU-Net code on your computer so that you
   can modify it as needed):
          ```bash
          git clone https://github.com/MIC-DKFZ/nnUNet.git
          cd nnUNet
          pip install -e .
          ```
3) nnU-Net needs to know where you intend to save raw data, preprocessed data and trained models. For this you need to
   set a few environment variables. Please follow the instructions [here](setting_up_paths.md).
4) (OPTIONAL) Install [hiddenlayer](https://github.com/waleedka/hiddenlayer). hiddenlayer enables nnU-net to generate
   plots of the network topologies it generates (see [Model training](how_to_use_nnunet.md#model-training)). 
To install hiddenlayer,
   run the following command:
    ```bash
    pip install --upgrade git+https://github.com/julien-blanchon/hiddenlayer.git
    ```

Installing nnU-Net will add several new commands to your terminal. These commands are used to run the entire nnU-Net
pipeline. You can execute them from any location on your system. All nnU-Net commands have the prefix `nnUNetv2_` for
easy identification.

Note that these commands simply execute python scripts. If you installed nnU-Net in a virtual environment, this
environment must be activated when executing the commands. You can see what scripts/functions are executed by 
checking the entry_points in the setup.py file.

All nnU-Net commands have a `-h` option which gives information on how to use them.
