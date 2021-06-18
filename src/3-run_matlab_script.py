# INPUT:
#   1. working_dir = working directory to clone the datalad dataset
#   2. results_dir = path to the directory where to place the results
#   3. subject = subject id
#
# DESCRIPTION:
# This script clones the HCP datalad dataset (functional connectivity) and
# computes the whole-brain resting state connectome using the Schaefer atlas
# with 100 parcels.
#
# OUTPUT:
#   1. A file named {subject}_connectome.mat with the correlation matrix and
#      atlas labels stored in results_dir
#

# %%
# Imports
import sys
import subprocess
from pathlib import Path

import nilearn
import nilearn.datasets

import nest_asyncio
nest_asyncio.apply()

import datalad.api  # noqa

# %%
# Variables

# Path to the working directory (relative to CWD)
# working_dir = Path('../scratch')
working_dir = sys.argv[1]
# Path to the results
# results_dir = Path('../scratch')
results_dir = sys.argv[2]

# the subject to compute
# subject = '100206'
subject = sys.argv[3]

# matlab_bin = '/Applications/Polyspace/R2021a.app/bin/matlab'
matlab_bin = sys.argv[4]


print(f'INPUT working_dir = {working_dir}')
print(f'INPUT results_dir = {results_dir}')
print(f'INPUT subject = {subject}')
print(f'INPUT matlab bin = {matlab_bin}')

working_dir = Path(working_dir)
results_dir = Path(results_dir)

# %%
# Install datalad dataset

# Where to install the dataset

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
# Get rsFMRI

# Path to the subject RS data (relative to datalad dataset)
subject_dpath = Path(subject) / 'MNINonLinear' / 'Results' / 'rfMRI_REST1_LR'

# Path to the RS Nifti (relative to datalad dataset)
rsfmri_fname = subject_dpath / 'rfMRI_REST1_LR_hp2000_clean.nii.gz'

print(f'Getting data to {rsfmri_fname}')
dataset.get(rsfmri_fname)
print('data obtained')

# %%

# Path to the RS confounds (relative to datalad dataset)
confounds_fname = subject_dpath / 'Movement_Regressors.txt'
print(f'Getting data to {confounds_fname}')
dataset.get(confounds_fname)
print('data obtained')

# %%
# Get atlas

print('Fetching schaefer atlas')
atlas = nilearn.datasets.fetch_atlas_schaefer_2018(n_rois=100, resolution_mm=2)
atlas_filename = atlas.maps
print(f'Atlas located in {atlas_filename}')


# %%
# Several examples of what we can do
exec_string = f'matlab compute_connectome.m {subject}'

exec_string = f'matlab compute_connectome.m {rsfmri_fname.as_posix()}'

exec_string = f'matlab compute_connectome.m {rsfmri_fname.as_posix()} {atlas_filename} {results_dir.as_posix()}'

exec_string = f'/usr/bin/matlab99 -singleCompThread compute_connectome.m {rsfmri_fname.as_posix()} {atlas_filename} {results_dir.as_posix()}'

exec_string = f'{matlab_bin} -singleCompThread compute_connectome.m {rsfmri_fname.as_posix()} {atlas_filename} {results_dir.as_posix()}'

# exec_string = f'/bin/bash my_bash_script.sh {rsfmri_fname.as_posix()}'

exec_string = f'fslinfo {atlas_filename}'

print(exec_string)

# %%
process = subprocess.run(exec_string, shell=True, capture_output=True)

print(process.stdout)
# %%
