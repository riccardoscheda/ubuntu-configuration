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
sudo bash
apt install git
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
To do so use:

```

```

