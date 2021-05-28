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

import nest_asyncio
nest_asyncio.apply()

import datalad.api  # noqa

# %%
# Variables

working_dir = Path('../scratch')

# %%
# Install datalad dataset

# Where to install the dataset
dataset_path = working_dir / 'dataset'

# Where the dataset is
dataset_url = ('https://github.com/datalad-datasets/'
               'hcp-functional-connectivity.git')

datalad.api.install(path=dataset_path, source=dataset_url)  # type: ignore

# %%
# Get rsFMRI

# %%
# Get atlas

# %%
# Apply Atlas

# %%
# Compute functional connectivity

# %%
# Save Connectome to file
