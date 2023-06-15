---
title: "METRICS Lab - newMSM"
layout: textlay
excerpt: "METRICS Lab -- Resources"
sitemap: false
permalink: /newMSM/
---

# newMSM - the new, reworked version of Multimodal Surface Matching software

## Download and install
NewMSM is available to download from FSL or Github. Please follow the steps described below. (Note: tested on Ubuntu Linux and MacOS.)

### Download and install binary

1. Download and install FSL. For more information, please visit the FSL [webpage](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/).
2. Download and install newMSM from the FSL developer branch by executing the following command on Terminal:
```console
fsl/bin/conda create --override-channels -c https://fsl.fmrib.ox.ac.uk/fsldownloads/fslconda/development/ -c https://fsl.fmrib.ox.ac.uk/fsldownloads/fslconda/public/ -c conda-forge -p ./msm-env fsl-newmsm
```
3. Activate this environment:
```console
conda activate ./msm-env/
```
4. You can test with the `newmsm -p` command.

### Install from source

1. Download and install FSL. For more information, please visit the FSL [webpage](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/).
2. Create a directoy where you can download sources:
    ```console
    mkdir newmsm_sources
    cd newmsm_sources
    ```
3. Download and install newMSM sources.
    1.  newresampler library
        ```console
        git clone https://github.com/rbesenczi/msm-newresampler.git
        cd msm-newresampler/src
        git checkout tags/v0.3.1
        make && make install
        cd ../..
        ```
    2. newmesreg library
        ```console
        git clone https://github.com/rbesenczi/msm-newmeshreg.git
        cd msm-newmeshreg/src
        git checkout tags/v0.3.1
        make && make install
        cd ../..
        ```
    3. newMSM application
        ```console
        git clone https://github.com/rbesenczi/newMSM.git
        cd newMSM/src
        git checkout tags/v0.3.1
        make && make install
        cd ../..
        ```
3. The binary `newmsm` should be in the folder `${FSLDEVDIR}/bin`.
4. You can test it with the `${FSLDEVDIR}/bin/newmsm -p` command.

Most features remained the same as it was in the original MSM implementation. A detailed "user guide" will be published soon.

## Links

FSL download and install [instructions](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FslInstallation).

Newresampler GitHub [repository](https://github.com/rbesenczi/msm-newresampler).

Newmeshreg GitHub [repository](https://github.com/rbesenczi/msm-newmeshreg).

NewMSM GitHub [repository](https://github.com/rbesenczi/newMSM).
