# INPUT:
#
# DESCRIPTION:
# This script clones the HCP datalad dataset (functional connectivity) and
# computes the whole-brain resting state connectome using the Schaefer atlas
# with 100 parcels.
#
# OUTPUT:
#
#

# %%
# Imports
from pathlib import Path

from scipy import io as sio

import nilearn
import nilearn.datasets
from nilearn.input_data import NiftiLabelsMasker
from nilearn.connectome import ConnectivityMeasure

import nest_asyncio
nest_asyncio.apply()

import datalad.api  # noqa

# %%
# Variables

# Path to the working directory (relative to CWD)
working_dir = Path('../scratch')

# Path to the results
results_dir = Path('../scratch')

# the subject to compute
subject = '100206'

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
# Apply Atlas
print('Creating Nifti Labels Masker')
masker = NiftiLabelsMasker(labels_img=atlas_filename, standardize=True,
                           verbose=5)

# Here we go from nifti files to the signal time series in a numpy
# array. Note how we give confounds to be regressed out during signal
# extraction
full_rsfmri_fname = dataset_path / rsfmri_fname
full_confounds_fname = dataset_path / confounds_fname

# Convert Path to string before calling
print('Masking time series')
time_series = masker.fit_transform(
    full_rsfmri_fname.as_posix(),
    confounds=full_confounds_fname.as_posix())


# %%
# Compute functional connectivity
print('Computing connectivity')
correlation_measure = ConnectivityMeasure(kind='correlation')
correlation_matrix = correlation_measure.fit_transform([time_series])[0]
print('Connectivity done')

# %%
# Plot to check
# Plot the correlation matrix
# import numpy as np
# from nilearn import plotting
# # Make a large figure
# # Mask the main diagonal for visualization:
# np.fill_diagonal(correlation_matrix, 0)
# # The labels we have start with the background (0), hence we skip the
# # first label
# # matrices are ordered for block-like representation
# labels = atlas.labels

# plotting.plot_matrix(correlation_matrix, figure=(10, 8), labels=labels,
#                      vmax=0.8, vmin=-0.8, reorder=True)

# %%
# Save Connectome to file
print(f'Creating results directory {results_dir.as_posix()}')
results_dir.mkdir(exist_ok=True, parents=True)
results_fname = results_dir / f'{subject}_connectome.mat'

to_save = {
    'connectome': correlation_matrix,
    'labels': atlas.labels
}
print(f'Saving .MAT results to {results_fname}')
sio.savemat(results_fname, to_save)
# %%

print('Compute COMPLETED YAY!!!!')