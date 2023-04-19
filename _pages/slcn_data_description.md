---
title: "SLCN MICCAI Challenge"
layout: textlay
excerpt: "SLCN MICCAI 2023 Challenge"
sitemap: false
permalink: /slcn_data_description/
---

<img src="/images/pubpic/SLCN_Banner.png" alt="SLCN Banner" title="SLCN Banner" width="1100">

<button  onclick="window.location.href='https://metrics-lab.github.io/slcn/';">SLCN</button> <button  onclick="window.location.href='https://metrics-lab.github.io/slcn_data_access/';">Data Access</button> <button onclick="window.location.href='
https://metrics-lab.github.io/slcn_data_description/';">Data Description</button>  <button onclick="window.location.href='https://metrics-lab.github.io/slcn_cortical_surface_tools/';">Cortical Surface Tools</button>  <button onclick="window.location.href='https://metrics-lab.github.io/slcn_repositories/';">Repositories</button>  <button onclick="window.location.href='https://metrics-lab.github.io/slcn_timeline/';">Timeline</button> <button onclick="window.location.href='https://metrics-lab.github.io/slcn_submission/';">Submission</button> <button onclick="window.location.href='https://metrics-lab.github.io/slcn_evaluation/';">Evaluation</button> <button onclick="window.location.href='https://metrics-lab.github.io/slcn_prizes/';">Prizes</button> <button onclick="window.location.href='https://metrics-lab.github.io/slcn_organisers/';">Organisers</button> <button onclick="window.location.href='https://metrics-lab.github.io/slcn_references/';">References</button>


## Data Description
### Features
The challenge data set will include the same data sets and splits as used by [Fawaz et al., 2021](https://www.biorxiv.org/content/10.1101/2021.12.01.470730v1.full.pdf); [Dahan et al., 2022](https://openreview.net/pdf?id=mpp843Bsf-): these include cortical surface meshes and 4 cortical metric files (sulcal depth, cortical thickness, curvature and T1/T2 myelin maps; shown below). 

For this years challenge, we have expanded the imaging data that teams can use to build predictive surface-based models. This includes cortical diffusion and resting-state functional MRI. 

#### Diffusion
A total of five measures of cortical diffusion are available. Fractional anisotropy (FA) and mean diffusivity (MD) (video tutorial [here](https://www.youtube.com/watch?v=wWcCKHp09QA) were calculated using [MRtrix3](https://www.sciencedirect.com/science/article/pii/S1053811919307281) from the b=0 and b=1000 diffusion-weighted images as preprocesed using the [dHCP SHARD diffusion pipeline](https://www.sciencedirect.com/science/article/pii/S1053811920309228?via%3Dihub). 

The other three measures of cortical diffusion are intra-cellular volume fraction (ICVF - an index of white matter neurite density), isotropic or free water volume fraction (ISOVF) and orientation dispersion index (OD, a measure of within-voxel disorganisation). These features are generated based on [NODDI](https://pubmed.ncbi.nlm.nih.gov/22484410/). One important parameterisation of NODDI is the parallel diffusivity constant, which is typically set at 1.7 μm^2 ms^−1 (based on empirical data from adult white matter). Following the optimisation procedure described [here](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0217118), and consistent with their results, we found that the optimal parallel diffusivity for neonatal cortical grey matter was 1.3 μm^2 ms^−1. These maps were generated using [AMICO](https://pubmed.ncbi.nlm.nih.gov/25462697/) (a python implementation of NODDI). 

All diffusion metrics were mapped from the volume to the cortical ribbon, and then resampled from native surface space to template surface space. These metrics are then upsampled from a template space resolution of 32k vertices per hemisphere, to 40k vertices per hemisphere. 


#### Resting-state fMRI 
The resting-state fMRI data made available as part of this challenge were generated as part of of [Williams et al., 2023](https://www.nature.com/articles/s41562-023-01542-8.epdf?sharing_token=496sz0kFtXbvP88vPgKgSNRgN0jAjWel9jnR3ZoTv0N2J1Mmw77jNYZqEsDhD1R0IcziTQ8uX7YhUHHxeWKlzbG15diaFxqe3uiFCStXvuq4ubpPeV3h6iAF2XfmyWwImwH7jCVp6n3BTrD_D0c3sp48RoTqlG9QNBycd0SmctQ%3D). Preprocessing of the resting-state fMRI data has been described extensively [here]( https://www.sciencedirect.com/science/article/pii/S1053811920307898?via%3Dihub). Cleaned volumetric timeseries were mapped to the cortical surface, and smoothed with a kernel of sigma = 4 mm, and then resampled to template surface space. Timeseries data were concatenated across subjects, followed by dimensionality reduction using FSL MIGP (d=2000). The resulting ‘PCAseries’ (dimensionality-reduced timeseries) was then fed into FSL MELODIC, which performed group ICA at a dimensionality of 25. Of note, MIGP and group ICA were performed on the term neonatal cohort only. A total of 16 were classified as signal (see Williams et al., 2023). These 25 components were then dual regressed into individual subject timeseries, generating subject-specific component spatial maps, amplitudes and timeseries. Here:
- Spatial maps are given as a Z-statistic maps on the cortical surface, representing how correlated the timeseries of each vertex is with the timeseries of the group component. There is one spatial map per component. 
- Timeseries files are simple .csv files containing a matrix that is NTimepoints x NComponents, and represents the BOLD signal fluctuation over time for each component. 
- Amplitude files are also simple .csv files containing a vector that is NComponents long. Here, amplitude represents the standard deviation of the subject-specific timeseries for each component. 

As with the diffusion metrics, spatial maps were resampled from their template space resolution of 32k vertices to 40k vertices. 


<img src="/images/pubpic/SLCN_data_example.png" alt="Example Data" title="Example Data" width="900">
