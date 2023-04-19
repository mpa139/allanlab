---
title: "SLCN MICCAI Challenge"
layout: textlay
excerpt: "SLCN MICCAI 2023 Challenge"
sitemap: false
permalink: /slcn_repositories/
---

<img src="/images/pubpic/sit_git.gif.png" alt="SLCN Banner" title="SLCN Banner" width="900">

<button  onclick="window.location.href='https://metrics-lab.github.io/slcn/';">SLCN</button> <button  onclick="window.location.href='https://metrics-lab.github.io/slcn_data_access/';">Data Access</button> <button onclick="window.location.href='
https://metrics-lab.github.io/slcn_data_description/';">Data Description</button>  <button onclick="window.location.href='https://metrics-lab.github.io/slcn_cortical_surface_tools/';">Cortical Surface Tools</button>  <button onclick="window.location.href='https://metrics-lab.github.io/slcn_repositories/';">Repositories</button>  <button onclick="window.location.href='https://metrics-lab.github.io/slcn_timeline/';">Timeline</button> <button onclick="window.location.href='https://metrics-lab.github.io/slcn_submission/';">Submission</button> <button onclick="window.location.href='https://metrics-lab.github.io/slcn_evaluation/';">Evaluation</button> <button onclick="window.location.href='https://metrics-lab.github.io/slcn_prizes/';">Prizes</button> <button onclick="window.location.href='https://metrics-lab.github.io/slcn_organisers/';">Organisers</button> <button onclick="window.location.href='https://metrics-lab.github.io/slcn_references/';">References</button>


## Code repositories
There are two Github repositories that are relevant for this challenge: 

### Benchmarking Surface Deep Learning
This repository contains the code used in [Fawaz et al., 2021](https://github.com/Abdulah-Fawaz/Benchmarking-Surface-DL). Links to other geometric deep learning repositories can be found within README.md. 

### Surface Vision Transformer
This repository contains code to apply vision transformers on surface data, as demonstrated in [Dahan et al. 2022](https://github.com/metrics-lab/surface-vision-transformers).

| <img src="/images/pubpic/surface_transformer.jpeg" alt="SLCN Banner" title="SLCN Banner" width="900"> |
| --- |
| *Figure 1. Surface vision transformer architecture*. The cortical data is first resampled, using barycentric interpolation, from its template resolution (32492 vertices) to a sixth order icosphere (mesh of 40962 equally spaced vertices). The regular icosphere is divided into triangular patches of equal vertex count (b, c) that fully cover the sphere (not shown), which are flattened into feature vectors (d), and then fed into the transformer model. | 
