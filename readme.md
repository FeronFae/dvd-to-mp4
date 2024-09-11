# *<u>Python-based DVD to MP4 converter — Automated DVD Digitalizer</u>*

## 1. Dependencies
### 1.1 HandBrakeCLI
For starters, this python3 code was made to run on linux using the [HandBrakeCLI](https://handbrake.fr/docs/en/latest/cli/cli-options.html), which can be downloaded [here](https://handbrake.fr/downloads2.php). Please make sure to install the **correct** HandBrakeCLI; **do <u>NOT</u> just run e.g.**

```
sudo apt-get install HandBrakeCLI
```

The package exists but may [**not** the officially supported](https://handbrake.fr/downloads.php) by the [developers](https://github.com/HandBrake) of HandBrake.

#### Installing HandBrakeCLI:
For a universal Linux download, we'll use [flatpak](https://flatpak.org/). In my case (and for other Debian-based distros), simply run

```
sudo apt install flatpak
```

- Once you have flatpak installed, you may run

    `flatpak install fr.handbrake.ghb`

    for a full installation of HandBrake. 

- Alternatively, if you wish to only install HandBrakeCLI, head to the [HandBrakeCLI downloads page](https://handbrake.fr/downloads2.php) and download the latest available flatpak and run

    `flatpak install '/path/to/HandBrakeCLI.flatpak'`

### 1.2 dvdbackup
As most DVDs are encrypted (especially the ones in .video object .VOB format of copyright-protected media), we're going to have to create a *readable and decrypted* "Identical Storage image of Optical media" or ISO file of the disk, which is what we need the [dvdbackup](https://dvdbackup.sourceforge.net/) package for. To install it, simply run

```
sudo apt-get install dvdbackup
```

or equivalent for your specific distro.

### 1.3 Other libraries
Make sure all libraries that are required for reading data from a DVD are also installed:
- [genisoimage](https://packages.debian.org/sid/genisoimage)
- [libdvd-pkg](https://packages.debian.org/buster/libdvd-pkg)
- [libdvdcss2](https://packages.debian.org/buster/libdvdcss2) (provided by libdvd-pkg)
- [libdvdread8](https://packages.debian.org/unstable/libs/libdvdread8)
- [libdvdnav4](https://packages.debian.org/es/sid/libdvdnav4)

by running 
```
dpkg --get-selections | grep -E 'dvd|iso'
```

or your distro-specific equivalent. If any of these are missing, simply run
```
sudo apt-get install <Missing Package Name>
```
or your distro-specific equivalent.

### 1.4 Python 3
Make sure you have [python 3.4 or higher](https://www.python.org/downloads/) installed; most linux distros come with python 3 preinstalled, just make sure the version is high enough! This script is meant to be run from the terminal with any of the `py`, `python` or `python3` commands.

## 2. Setup
First, clone the repository to a directory of your liking and open the directory with

```
git clone <INSERT LINK TO REPO>
cd <REPO NAME>
```

Once inside the directory, run the setup with

```
python3 setup.py
```
(or your `python` or `py` equivalents)

- Enter the output directory for your converted video files. I like to have mine on my Desktop, so e.g.:
```
$ Please enter the desired output file directory
$ >>> /home/<username>/Desktop/
```

- If you don't have a single optical drive, enter `y` and give the directory to the drive you'll be using, e.g. I have 2 optical drives and insert my DVDs into the second one under `/dev/sr1` instead of the default `/dev/sr0` for single drive devices:
```
$ Does your device have more than one optical drive? [y/n]
$ >>> y
$ Please enter the directory of the drive you will be using
$ >>> /dev/sr1
```

## 3. Run the program
Once you have finished the quick setup process, insert the disk into the optical drive and wait for it to be detected by your system. As soon as this is the case, simply run the program from Terminal and wait for it to finish.
```
python3 dvd-to-mp4.py
```

## 4. Why this program over HandBrake's GUI?
If you're familiar with HandBrake, you'll know that installing the latest GUI release is a lot more user-friendly and gives you way better customization over the DVDs you may be converting. The reason I made this code is to automatize the conversion process for people that need to digitalize many DVDs in their original quality and don't want to open HandBrake every single time to convert a single disk.

Another reason why I created this script is because HandBrake wouldn't properly decrypt the data contained in my DVDs, which is why I incorporated the extra `dvdbackup` and `genisoimage (mkisofs)` steps into the code to circumvent this issue.

It is certainly a lot easier to use HandBrake instead of this code if you're looking to convert only a few DVDs or if you want full control over the conversion process. If you're still having issues with HandBrake, consider using `dvdbackup` and `mkisofs` to decrypt, copy and convert the files from the disk first.

## 5. Why in Pyhton?
I know this code is rather unnecessarily coded *in* python because all of this could be done with a simple shell script, but python is the only language I only have thorough experience with, so... yeah! Feel free to convert my code into a shell script and remove the python dependency of the conversion process entirely :). 
