---
title: "SLCN MICCAI Challenge"
layout: textlay
excerpt: "SLCN MICCAI 2023 Challenge"
sitemap: false
permalink: /slcn_repositories/
---

<img src="/images/pubpic/SLCN_Banner.png" alt="SLCN Banner" title="SLCN Banner" width="900">

<button  onclick="window.location.href='https://slcn.grand-challenge.org/';">Data Access</button> <button onclick="window.location.href='https://slcn.grand-challenge.org/';">Data Description</button>  <button onclick="window.location.href='https://slcn.grand-challenge.org/';">Cortical Surface Tools</button>  <button onclick="window.location.href='https://slcn.grand-challenge.org/';">Repositories</button>  <button onclick="window.location.href='https://slcn.grand-challenge.org/';">Timeline</button> <button onclick="window.location.href='https://slcn.grand-challenge.org/';">Submission</button> <button onclick="window.location.href='https://slcn.grand-challenge.org/';">Evaluation</button> <button onclick="window.location.href='https://slcn.grand-challenge.org/';">Prizes</button> <button onclick="window.location.href='https://slcn.grand-challenge.org/';">Organisers</button> <button onclick="window.location.href='https://slcn.grand-challenge.org/';">References</button>


## Code repositories
There are two Github repositories that are relevant for this challenge: 

### Benchmarking Surface Deep Learning
This repository contains the code used in [Fawaz et al., 2021](https://github.com/Abdulah-Fawaz/Benchmarking-Surface-DL). Links to other geometric deep learning repositories can be found within README.md. 

### Surface Vision Transformer
This repository contains code to apply vision transformers on surface data, as demonstrated in [Dahan et al. 2022](https://github.com/metrics-lab/surface-vision-transformers).

| <img src="/images/pubpic/SLCN_Banner.png" alt="SLCN Banner" title="SLCN Banner" width="900"> |
| --- |
| *Figure 1. Surface vision transformer architecture*. The cortical data is first resampled, using barycentric interpolation, from its template resolution (32492 vertices) to a sixth order icosphere (mesh of 40962 equally spaced vertices). The regular icosphere is divided into triangular patches of equal vertex count (b, c) that fully cover the sphere (not shown), which are flattened into feature vectors (d), and then fed into the transformer model. | 
