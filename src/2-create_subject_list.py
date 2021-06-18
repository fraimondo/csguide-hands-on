# %%
from pathlib import Path

import nest_asyncio
nest_asyncio.apply()

import datalad.api  # noqa


# %%

working_dir = Path('../scratch')
# Path to the datalad dataset (relative to CWD)
dataset_path = working_dir / 'dataset'

# Where the dataset is
dataset_url = ('https://github.com/datalad-datasets/'
               'hcp-functional-connectivity.git')

print(f'Cloning dataset in {dataset_path}')
dataset = datalad.api.install(  # type: ignore
    path=dataset_path, source=dataset_url)
print('Dataset cloned')

# %%

search_pattern = '*/MNINonLinear/Results/rfMRI_REST1_LR/*_hp2000_clean.nii.gz'

subject_list = []
for fname in dataset_path.glob(search_pattern):
    this_subject = fname.parent.parent.parent.parent.name
    print(this_subject)
    subject_list.append(this_subject)
# %%

with open('subject_list2.txt', mode='w') as subject_file:
    for this_subject in subject_list:
        subject_file.write(f'{this_subject}\n')

# %%
