# csguide-hands-on

# Requirements

Install dependencies

```
conda install -c conda-forge git-annex datalad nilearn
```

if using jupyter-style
```

conda install -c conda-forge nest-asyncio
```

# Checks:
You are using datalad from the environment:

```
which datalad
/Users/fraimondo/anaconda3/envs/csguide/bin/datalad
```

Check that datalad works

```
datalad install https://github.com/datalad-datasets/hcp-functional-connectivity.git

cd hcp-functional-connectivity/100206/T1w

datalad get T1wDividedByT2w.nii.gz
```

# Problems:

1- Delete old KEYs (wrong key)

- Mostafa
- Shammi

2- Wrong key being red (new key not recognised)
- Sam

3- git-annex on M1 mac
- Tobias
- Mostafa

4- ipykernel keeps installing on environment
- Nevena

5- Path in VSCode different python version