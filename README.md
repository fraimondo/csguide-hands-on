# csguide-hands-on

# Requirements

1. Create an environment

```
conda create -n csguide python=3.9
```

2. Activate the environment
   
```
conda activate csguide
```

3. Install dependencies

```
conda install ipython flake8
conda install -c conda-forge datalad nilearn
```

if using jupyter-style execution
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
1. In your mac, open the Keychain Access application.
2. In the search bar (top right), type "datalad".
3. If there are any keys named `datalad-XXXX`, these are the credentials. For HCP, you will find two instances of `datalad-hcp-s3`. Delete them both.


### Other:

Please contact me. I don't know how to solve the problems as I dont have windows nor mac.

## Problem #2 Can't download data (`datalad get`)
```
The error looks like this:
[ERROR  ] Failed to download from any of 1 locations [datalad.py:_transfer:162]                                                                                                                                                                                                   
| Failed to download from any of 1 locations [datalad.py:_transfer:162]
| Failed to download from any of 1 locations [datalad.py:_transfer:162] [get(/mnt/c/Users/svickery/Documents/CS_course/csguide_hands_on/scratch/dataset/100307/T1w/T1w_acpc_dc.nii.gz)] 
get(error): 100307/T1w/T1w_acpc_dc.nii.gz (file) [Failed to download from any of 1 locations [datalad.py:_transfer:162]
Failed to download from any of 1 locations [datalad.py:_transfer:162]
Failed to download from any of 1 locations [datalad.py:_transfer:162]]

```
This happened to Sam using windows with WSL1.

We are working on it. Maybe using WSL2 will help.

## Problem #3  git-annex on M1 mac

So the problem is that git-annex is not available for M1 macs, natively.

Solution:

1- Install Rosetta 2: Open a terminal and execute
```
/usr/sbin/softwareupdate --install-rosetta --agree-to-license
```

2- Download the git-annex DMG file from here: https://downloads.kitenet.net/git-annex/OSX/current/10.10_Yosemite/git-annex.dmg

3- Open the DMG file. Drag and drop the git-annex app to the /Applications folder.

4- In the terminal, run:
```
/Applications/git-annex.app/Contents/MacOS/git-annex
```
Once you do that, a message will appear saying that you can't execute that.

5- Open the System Preferences. Go to Security & Privacy. In the general tab, click on "Open anyway". Another message will apear, click open.

6- In the terminal, run:
```
/Applications/git-annex.app/Contents/MacOS/git-annex
```
You should see the output of git-annex.

7- Create a symbolic link so it's always on the path.

```
cd /usr/local/bin
sudo ln -s /Applications/git-annex.app/Contents/MacOS/git-annex
```

## Problem #4 keeps installing an environment

This was related to having anaconda/miniconda installed before the course. It needed to update `conda`. To do so, in the base environment:

```
conda update conda
```

Then activate the csguide environment:
```
conda activate csguide
```

and update all the packages:
```
conda update --all
```

## Problem #5 Path in VSCode different python version
- Lya

## Problem #6 It hangs while downloading files with `datalad get` at 0%

Check if you have a file using this command

```
ls ~/.cache/datalad/locks/downloader-auth.lck
```

If you have it, delete it:

```
rm ~/.cache/datalad/locks/downloader-auth.lck
```

