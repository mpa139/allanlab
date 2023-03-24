---
title: "SLCN MICCAI Challenge"
layout: textlay
excerpt: "SLCN MICCAI 2023 Challenge"
sitemap: false
permalink: /slcn_evaluation/
---

<img src="/images/pubpic/SLCN_Banner.png" alt="SLCN Banner" title="SLCN Banner" width="900">

<button  onclick="window.location.href='https://slcn.grand-challenge.org/';">Data Access</button> <button onclick="window.location.href='https://slcn.grand-challenge.org/';">Data Description</button>  <button onclick="window.location.href='https://slcn.grand-challenge.org/';">Cortical Surface Tools</button>  <button onclick="window.location.href='https://slcn.grand-challenge.org/';">Repositories</button>  <button onclick="window.location.href='https://slcn.grand-challenge.org/';">Timeline</button> <button onclick="window.location.href='https://slcn.grand-challenge.org/';">Submission</button> <button onclick="window.location.href='https://slcn.grand-challenge.org/';">Evaluation</button> <button onclick="window.location.href='https://slcn.grand-challenge.org/';">Prizes</button> <button onclick="window.location.href='https://slcn.grand-challenge.org/';">Organisers</button> <button onclick="window.location.href='https://slcn.grand-challenge.org/';">References</button>


## Evaluation
Submissions will be evaluated across two domains, and the final ranking will be determined as an aggregate of performance across each. These two domains are: 
1. Birth age (template space) (mean absolute error; MAE)
2. Birth age (native space) (MAE)

The following steps will be used to rank participants:
* Step 1: Separate rankings will be computed based on each domain (for both domains, lower MAE = better)
* Step 2: From the two ranking tables, the mean ranking of each participant will be computed as the numerical mean of the single rankings (domain 1 = 75% weighting, domain 2 = 25% weighting)
* Step 3: In case of equal ranking, the achieved MAE in domain 1 will be used as a tie-break
* Step 4: If equal MAE is achieved in domain 1, then the achieved MAE in domain 2 will be used as the tie-break

## MLCN Workshop paper
Participants are invited to also submit an extended paper to Machine Learning for Clinical Neuroimaging (MLCN) deadline 1st July. These papers will undergo peer review and the best papers will be presented at the MLCN MICCAI workshop in September 2022. MLCN submissions include some for of interpretable visualisation method, evaluated on the cortical surface. Peer review criteria will equally weight model performance (on the validation set) and clinical interpretability of the findings.
