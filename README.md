# ubuntu-configuration
## Repo for the configuration of Ubuntu after minimal installation

This repo is useful for configuration of ubuntu and installation of useful packages for my work.
The configuration will be composed by:
- Installation of git
- Installation of gnome-tweaks
- Installation of miniconda and python libraries
- Mount external volumes

## Installation of git
To install git use:
```
sudo apt install git
```

## Installation of gnome-tweaks
To install gnome-tweaks use:
```
apt install gnome-tweaks
```

## Installation of miniconda and python libraries

To install miniconda first we have to clone this repository:
```
git clone https://github.com/riccardoscheda/ubuntu-configuration
```
 
Then we have to run bash files:
```
cd ubuntu-configuration
bash install-conda.sh
```

During installation press Enter and yes when asked.
Then we can install python libraries and also Spyder:

```
bash pylabraries.sh
```

Now we have ubuntu configurated.

## Mount external volumes

To mount external volumes (ntfs) we have modify the file /etc/fstab. So, first we have to create the mount point:

```
mkdir /media/dati 
```
Then, we have to take the information of the volume we want to mount.
First, use fdisk command to list of all partitions:

```
sudo fdisk -l
```
The output will be something like that:
```
Device         Start       End   Sectors  Size Type
/dev/sda1       2048    534527    532480  260M EFI System
/dev/sda2     534528    567295     32768   16M Microsoft reserved
/dev/sda3     567296 188228801 187661506 89,5G Microsoft basic data
/dev/sda5  189360128 860399615 671039488  320G Microsoft basic data
/dev/sda6  860399616 982095871 121696256   58G Linux filesystem
/dev/sda7  982095872 999192575  17096704  8,2G Microsoft basic data

```

