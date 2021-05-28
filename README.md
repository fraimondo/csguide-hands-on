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

## Problem #1 I entered the wrong credentials or the credentials changed

So you need to delete the old credentials.

### Deleting the credentials

1. Check that you are in the right environment:
   
```
which datalad
```

2. Check where the credentias are stored:

```
datalad wtf -S credentials
```

The output should be like that:

```
(csguide)juseless ➜  ~  datalad wtf -S credentials
# WTF
## credentials 
  - keyring: 
    - active_backends: 
      - PlaintextKeyring with no encyption v.1.0 at /home/fraimondo/.local/share/python_keyring/keyring_pass.cfg
    - config_file: /home/fraimondo/.local/share/python_keyring/keyringrc.cfg
    - data_root: /home/fraimondo/.local/share/python_keyring
```

You can see there all the active backends (`active_backends`). If there is more
than one, you need to see where the credentials are, and how to delete them.

### PlaintextKeyring

This backend means that the credentials are stored in one file. In the example, in `/home/fraimondo/.local/share/python_keyring/keyring_pass.cfg`. The file will have keys stored like in this example:

```
[datalad_2Dhcp_2Ds3]
key_5fid = 
	QUtJQVhPNjHDVDU3SkY3UFFQT1k=
secret_5fid = 
	NVlEOGxsVjdJWjJnUGdYQ3pwddasdzJvdjZuV2lWY0tJMlhxVS9oaw==
	
```

Edit that file and delete the key that is not working. For HCP, it will be `[datalad_2Dhcp_2Ds3]`. Delete that line, as well as key_5fid and secret_5fid.


### macOS Keyring

This means that your keys are installed in the macOS keyring. 
1- In your mac, open the Keychain Access application.
2- In the left panel, select "System" under "System Keychains".
3- In the search bar (top right), type "datalad".
4- If there are any keys named `datalad-XXXX`, these are the credentials. For HCP, you will find two instances of `datalad-hcp-s3`. Delete them both.

### Other:

Please contact me. I don't know how to solve the problems as I dont have windows nor mac.

2- Wrong key being red (new key not recognised)
- Sam

3- git-annex on M1 mac
- Tobias
- Mostafa

4- ipykernel keeps installing on environment
- Nevena

5- Path in VSCode different python version