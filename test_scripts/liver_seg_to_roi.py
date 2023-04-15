import numpy as np
import SimpleITK as sitk
import cv2
import os

def save_array_to_nii(mask_array, nii_template_path, nii_save_path):

    sitk_image_object = sitk.ReadImage(nii_template_path)
    output_spacing = sitk_image_object.GetSpacing()
    output_direction = sitk_image_object.GetDirection()
    output_origin = sitk_image_object.GetOrigin()
#     print(output_spacing ,output_direction,output_origin)

    nrrd_output = sitk.GetImageFromArray(mask_array)
    nrrd_output.SetSpacing(output_spacing)
    nrrd_output.SetDirection(output_direction)
    nrrd_output.SetOrigin(output_origin)

    nrrdWriter = sitk.ImageFileWriter()
    nrrdWriter.SetFileName(nii_save_path)
    nrrdWriter.SetUseCompression(True)
    nrrdWriter.Execute(nrrd_output)
    print(nii_save_path ,'saved')

def get_roi_array_from_2d_seg(seg_array_2d):  
    
    roi_array = np.zeros([seg_array_2d.shape[0],seg_array_2d.shape[1]])
    
    x_min = np.min(np.nonzero(seg_array_2d)[1])
    x = np.nonzero(seg_array_2d)
    y_target = x[0][np.where(x[1] == x_min)[0][0]]
#     print('x_min', x_min)
    x_target = x_min + 30 
#     print('x_target',x_target, 'y_target',y_target)   
#     print('roi_array.shape',roi_array.shape)
    roi_array [y_target, x_target ] = 1
#     print('roi_pixel_area_before_dilate',np.sum(roi_array))
    rad_dilate = 23          
    dilate_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (rad_dilate , rad_dilate ) )  
    roi_array = cv2.dilate(roi_array, dilate_kernel)  
#     print('roi_pixel_area_after_dilate',np.sum(roi_array))
    return roi_array
    
def get_roi_array_from_seg_volume(nii_input_path, nii_output_path): 
        
    vast_slice = 0
    vast_area = 0

    seg_sitk = sitk.ReadImage(nii_input_path)
    seg_array  = sitk.GetArrayFromImage(seg_sitk)
    shape_x,shape_y,shape_z = seg_array.shape 
    mask_array = np.zeros([shape_x,shape_y,shape_z])

    for idx in range(shape_x):    
        slice_array = seg_array[idx,:,:]
        
        if np.sum(slice_array) > vast_area:
            vast_slice = idx  
            vast_slice_array = slice_array
            vast_area = np.sum(slice_array)   
            
    slice_list = [vast_slice-2,vast_slice,vast_slice+2]
    if vast_slice < 2 : slice_list = [0,2,4]
    print('slice_list',slice_list)
        
    for slice_idx in slice_list: 
        
        roi_array = get_roi_array_from_2d_seg(seg_array[slice_idx,:,:])        
        mask_array[slice_idx,:,:] = roi_array

    return mask_array

def get_image_path_by_id(patient_id, image_dir):
    image_order  = patient_id
    file_name = [os.path.relpath(os.path.join(image_dir, x)) \
                    for x in os.listdir(image_dir) \
                    if os.path.isfile(os.path.join(image_dir, x)) and patient_id in x][0] 
    return file_name