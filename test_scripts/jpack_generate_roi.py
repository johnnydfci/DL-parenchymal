import numpy as np
import SimpleITK as sitk
from skimage import measure
import glob
import os
import matplotlib.pyplot as plt
import cv2


def seg_in_roi_by_screenshots(img_nii_path,seg_nii_path,screenshots_dir,patient_id):  

    
    operator =  seg_nii_path.split('_')[-1][:2]
    slice_folder = screenshots_dir +'/'
    if not os.path.isdir(slice_folder ):
        os.mkdir(slice_folder )  

    im_sitk = sitk.ReadImage(img_nii_path)
    im_array  = sitk.GetArrayFromImage(im_sitk)       
    auto_seg_sitk = sitk.ReadImage(seg_nii_path)
    auto_seg_array  = sitk.GetArrayFromImage(auto_seg_sitk)    
    print('im_array.shape[0]', im_array.shape[0], 'auto_seg_array.shape[0]',auto_seg_array.shape[0])

    im_array[im_array<-135]=-135
    im_array[im_array>215]=215  #  40L 350W
    
    roi_slice_list = []


    for k in range(im_array.shape[0]-1):
        if ( np.sum(auto_seg_array[k,:,:])!=0):
            roi_slice_list.append(k)
            if len(roi_slice_list)>=3:
                break
   
    print('roi_slice_list',roi_slice_list)
    

    for i in roi_slice_list:
        slice_png_path = slice_folder + patient_id +'_slice'+str(i)+'.png'
        if not os.path.exists(slice_png_path):
#         if True:        
            fig, ax = plt.subplots()
            ax.imshow(im_array[i,:,:], cmap=plt.cm.gray)

            auto_seg_slice = auto_seg_array[i,:,:]
            contours_1 = measure.find_contours(auto_seg_slice, 0.5)
            for n, contour in enumerate(contours_1):
                ax.plot(contour[:, 1], contour[:, 0], linewidth=1, color='red')      #      '#00bcffff'      
            contours_2 = measure.find_contours(auto_seg_slice, 1.5)
            for n, contour in enumerate(contours_2):
                ax.plot(contour[:, 1], contour[:, 0], linewidth=1, color='#00bcffff')
                
            ax.set_xticks([])
            ax.set_yticks([])
            fig.set_size_inches(8, 8)
            plt.title(patient_id+'_'+operator +'/'+' slice:'+str(i))
            fig.savefig(slice_png_path , dpi=256)
            plt.close('all')
#         print(slice_folder +'slice'+str(i)+'.png: saved') 
    return 