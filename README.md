# superpermidi
A python script to make music from superpermutations

## Requirements
This is tested under Ubuntu Bionic with Python 3.6.7.
This should install all you need:
> sudo apt install wget python3 python3-pip timidity timgm6mb-soundfont

## Installation
Install the python requirements using
> sudo pip3 install -r requirements.txt

## Usage
Get a textfile with a superpermutation (or create your own)
> wget http://www.gregegan.net/SCIENCE/Superpermutations/7_5906_nsk666646664466646666_2SYMM_FS.txt

Run the script
> python3 superpermidi.py 7_5906_nsk666646664466646666_2SYMM_FS.txt

You should get a midi file with the same name and can play it
> timidity 7_5906_nsk666646664466646666_2SYMM_FS.mid
