# %%
from pathlib import Path

import nest_asyncio
nest_asyncio.apply()

import datalad.api  # noqa


# %%

working_dir = Path('../scratch')
# Path to the datalad dataset (relative to CWD)
dataset_path = working_dir / 'datasets_repo'

# Where the dataset is
dataset_url = 'git@jugit.fz-juelich.de:inm7/datasets/datasets_repo.git'

print(f'Cloning dataset in {dataset_path}')
dataset = datalad.api.install(  # type: ignore
    path=dataset_path, source=dataset_url)
print('Dataset cloned')

# %%
fcp_path = 'original/hcp/hcp_genetic'
dataset.get(fcp_path)
# %%
