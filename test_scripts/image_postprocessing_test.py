# Copyright 2020-2021 AIM-Harvard

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from skimage import measure
import numpy as np


def get_biggst_mask_array(mask_array):
    
    all_labels, noduleCount = measure.label(mask_array, connectivity=2, return_num=True)
    props = measure.regionprops(all_labels)
    areas = []
    for iii in range(len(props)):
        areas.append(props[iii].area)
    areas = sorted(areas, reverse=True)
    #     print( 'nodulecount:------------'+str(noduleCount), '[:10]:', areas[:10])
    #
    copyMaskData = mask_array
    # get blobs
    all_labels = measure.label(copyMaskData)

    # get number of blobs ( inlcuding background as zero
    noduleCount = all_labels.max()
    voxel_all_num = all_labels.sum()
    threshold = voxel_all_num * 0.03

    # list to populate
    maskDataList = []
    maskDataListVolume = []
    biggest_mask_array = mask_array
    # supress one mask and leave the others
    # 0 is the background - so dont deal with it
    for label in range(1, noduleCount + 1):

        # make an array of zeros
        tempMaskData = np.zeros((copyMaskData.shape[0], copyMaskData.shape[1], copyMaskData.shape[2]), dtype=np.int64)
        #
        arrays = np.where(all_labels == label)
        # just loop through lenght of one of the 3 arrays - they are all the same
        for k in range(len(arrays[0])):
            tempMaskData[arrays[0][k]][arrays[1][k]][arrays[2][k]] = 1.0

        # when array done

        volume_num = tempMaskData.sum()

        if volume_num > threshold:
            biggest_mask_array = tempMaskData
            threshold = volume_num
    return biggest_mask_array

def plot_rect_in_mid(mask_array):  
    
    shape_x,shape_y,shape_z = mask_array.shape    
    for i in range (10,shape_y -10):
        for j in range(-10,10):        
            mask_array[0 , i , shape_z - 20 + j] = 1 
            mask_array[0 , shape_y - 20 + j , i] = 1
    return mask_array
