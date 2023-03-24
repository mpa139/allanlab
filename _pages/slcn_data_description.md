---
title: "SLCN MICCAI Challenge"
layout: textlay
excerpt: "SLCN MICCAI 2023 Challenge"
sitemap: false
permalink: /slcn_data_description/
---

<img src="/images/pubpic/SLCN_Banner.png" alt="SLCN Banner" title="SLCN Banner" width="900">

<button  onclick="window.location.href='https://metrics-lab.github.io/slcn_data_access/';">Data Access</button> <button onclick="window.location.href='
https://metrics-lab.github.io/slcn_data_description/';">Data Description</button>  <button onclick="window.location.href='https://metrics-lab.github.io/slcn_cortical_surface_tools/';">Cortical Surface Tools</button>  <button onclick="window.location.href='https://metrics-lab.github.io/slcn_repositories/';">Repositories</button>  <button onclick="window.location.href='https://metrics-lab.github.io/slcn_timeline/';">Timeline</button> <button onclick="window.location.href='https://metrics-lab.github.io/slcn_submission/';">Submission</button> <button onclick="window.location.href='https://metrics-lab.github.io/slcn_evaluation/';">Evaluation</button> <button onclick="window.location.href='https://metrics-lab.github.io/slcn_prizes/';">Prizes</button> <button onclick="window.location.href='https://metrics-lab.github.io/slcn_organisers/';">Organisers</button> <button onclick="window.location.href='[https://slcn.grand-challenge.org/](https://metrics-lab.github.io/slcn_references/)';">References</button>


## Data Description
### Features
The challenge data set will include the same data sets and splits as used by [Fawaz et al., 2021](https://www.biorxiv.org/content/10.1101/2021.12.01.470730v1.full.pdf); [Dahan et al., 2022](https://openreview.net/pdf?id=mpp843Bsf-): these include cortical surface meshes and 4 cortical metric files (sulcal depth, cortical thickness, curvature and T1/T2 myelin maps; shown below) acquired from 514 neonates scanned as part of the dHCP project, of which 95 are born preterm (<37 weeks’ gestational age). We have also included white and pial surfaces, which participants might find useful for the derivation of other morphological features such as surface area.

An example script for resampling the cortical surfaces and metrics to a regularly-tessellated sixth-order icosphere is included alongside the data. 

<img src="/images/pubpic/SLCN_data_example.png" alt="Example Data" title="Example Data" width="900"
