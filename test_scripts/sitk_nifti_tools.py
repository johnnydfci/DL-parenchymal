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

import SimpleITK as sitk

def get_nifti_from_array_via_interspacing(input_array, inter_spacing, target_sitk):
    
    sitk_inter = sitk.GetImageFromArray(input_array)
    sitk_inter.SetSpacing(inter_spacing)
    sitk_inter.SetOrigin(target_sitk.GetOrigin())
    sitk_inter.SetDirection(target_sitk.GetDirection())
    
    resample = sitk.ResampleImageFilter()
    resample.SetOutputSpacing(target_sitk.GetSpacing())
    resample.SetSize(target_sitk.GetSize())
    resample.SetOutputDirection(target_sitk.GetDirection())
    resample.SetOutputOrigin(target_sitk.GetOrigin())
    resample.SetTransform(sitk.Transform())
    
    sitk_output = resample.Execute(sitk_inter) 

    return sitk_output


def nifiti_save_into_path(sitk_output, path):
    nrrdWriter = sitk.ImageFileWriter()
    nrrdWriter.SetFileName(path)
    nrrdWriter.SetUseCompression(True)
    nrrdWriter.Execute(sitk_output)
    return
