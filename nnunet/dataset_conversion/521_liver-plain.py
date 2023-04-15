import os
import json
import shutil


def save_json(obj, file, indent=4, sort_keys=True):
    with open(file, 'w') as f:
        json.dump(obj, f, sort_keys=sort_keys, indent=indent)
        
        
def maybe_mkdir_p(directory):
    directory = os.path.abspath(directory)
    splits = directory.split("/")[1:]
    for i in range(0, len(splits)):
        if not os.path.isdir(os.path.join("/", *splits[:i+1])):
            try:
                os.mkdir(os.path.join("/", *splits[:i+1]))
            except FileExistsError:
                # this can sometimes happen when two jobs try to create the same directory at the same time,
                # especially on network drives.
                print("WARNING: Folder %s already existed and does not need to be created" % directory)


def subdirs(folder, join=True, prefix=None, suffix=None, sort=True):
    if join:
        l = os.path.join
    else:
        l = lambda x, y: y
    res = [l(folder, i) for i in os.listdir(folder) if os.path.isdir(os.path.join(folder, i))
            and (prefix is None or i.startswith(prefix))
            and (suffix is None or i.endswith(suffix))]
    if sort:
        res.sort()
    return res


base = '../../nnUNet_raw_data_base/nnUNet_raw_data/Task_521_liver_raw'
out = "../../nnUNet_raw_data_base/nnUNet_raw_data/Task521_liver"
cases = subdirs(base, join=False)

maybe_mkdir_p(out)
maybe_mkdir_p(os.path.join(out, "imagesTr"))
maybe_mkdir_p(os.path.join(out, "imagesTs"))
maybe_mkdir_p(os.path.join(out, "labelsTr"))
maybe_mkdir_p(os.path.join(out, "labelsTs"))

Tr_list= []
Ts_list=[]
for c in cases:
    if 'checkpoints' not in c:
#         case_id = int(c.split("_")[-1])
        case_id = c
        print('c',c, 'case_id', case_id)
        if 'LIDC_IDRI' in case_id :
            Tr_list.append(case_id)
            shutil.copy(os.path.join(base, c, "imaging.nii.gz"), os.path.join(out, "imagesTr", c + "_0000.nii.gz"))
            shutil.copy(os.path.join(base, c, "segmentation.nii.gz"), os.path.join(out, "labelsTr", c + ".nii.gz"))
            
        if 'LIDC_IDRI_0698' in case_id :
            Ts_list.append(case_id)
            shutil.copy(os.path.join(base, c, "imaging.nii.gz"), os.path.join(out, "imagesTs", c + "_0000.nii.gz"))
            shutil.copy(os.path.join(base, c, "segmentation.nii.gz"), os.path.join(out, "labelsTs", c + ".nii.gz"))

        print(case_id,' done!')

json_dict = {}
json_dict['name'] = "colon"
json_dict['description'] = "liver segmentation at nonenhanced chest CT images"
json_dict['tensorImageSize'] = "3D"
json_dict['reference'] = "liver segmentation data for nnunet"
json_dict['licence'] = ""
json_dict['release'] = "0.0"
json_dict['modality'] = {
    "0": "CT",
}
json_dict['labels'] = {
    "0": "background",
    "1": "Liver",
}
json_dict['numTraining'] = len(Tr_list)
json_dict['numTest'] = len(Ts_list)
json_dict['training'] = [{'image': "./imagesTr/%s.nii.gz" % i, "label": "./labelsTr/%s.nii.gz" % i} for i in Tr_list]
json_dict['test'] = ["./imagesTs/%s.nii.gz" % i for i in Ts_list]

save_json(json_dict, os.path.join(out, "dataset.json"))
