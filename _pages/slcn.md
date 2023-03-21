---
title: "SLCN MICCAI Challenge"
layout: textlay
excerpt: "SLCN MICCAI 2023 Challenge"
sitemap: false
permalink: /slcn/
---

<img src="/images/pubpic/SLCN_Banner.png" alt="SLCN Banner" title="SLCN Banner" width="900">

## What is SLCN?
SLCN (Surface Learning for Clinical Neuroimaging) is a new MICCAI workshop aimed at promoting the development of deep learning methods suitable for cortical surface data. This year, participants are taksed with predicting developmental phenotypes (gestational age at birth) from cortical surface data acquired as part of the [Developing Human Connectome Project](http://www.developingconnectome.org/). 

## The challenge of identifying neurodevelopmental biomarkers
Detecting biomarkers from neuroimaging data is highly challenging, since the degree of topographic variability of cortical shape and functional organisation across individuals limits the accuracy with which brains can be compared through image registration ([Glasser et al., 2016](https://www.nature.com/articles/nature18933); [Kong et al., 2019](https://academic.oup.com/cercor/article/29/6/2533/5033556?login=true)). There is a clear need for precision imaging tools of the brain which are robust to these factors.

Recently, ([](); []()) proposed a novel benchmark for prototyping tools for cortical analysis based on the regression of clinical phenotypes from the dHCP ([Makropoulos et al., 2018](https://www.sciencedirect.com/science/article/pii/S1053811918300545?via%3Dihub); [Bozek et al., 2018](https://www.sciencedirect.com/science/article/pii/S1053811918305251?via%3Dihub#bib35)) - a unique open dataset of multimodal neonatal brain images, acquired from preterm and term neonates between 24 and 45 weeks' postmenstrual age. Over this period of late gestation, the human brain undergoes rapid growth and maturation, characterised by highly dynamic and organised cellular and molecular processes (Figure 1). Disruptions to these processes, for example due to preterm birth, can have serious consequences resulting in significant increased risk of those neonates developing neuropsychiatric conditions including autism spectrum disorder, attention deficit hyperactivity disorder (ADHD), schizophrenia, bipolar affective disorder and major depressive disorder in later life ([Nosarti et al., 2007](https://www.cambridge.org/core/journals/journal-of-the-international-neuropsychological-society/article/impaired-executive-functioning-in-young-adults-born-very-preterm/7844821C18D9B93A76A20815B07E5F91); [Nosarti et al., 2012](https://www.cambridge.org/core/journals/journal-of-the-international-neuropsychological-society/article/impaired-executive-functioning-in-young-adults-born-very-preterm/7844821C18D9B93A76A20815B07E5F91)).

## Tasks 
The goal of this challenge will therefore be to elicit submissions of novel methods for registration-free or registration-robust cortical phenotype regression, with emphasis on interpretable or explainable machine learning methods which deliver biomarkers predictive of risk for neurodevelopmental impairment. These will be benchmarked on the tasks of **regression of gestational age at birth** (seen as a correlate of prematurity) on both **registered and native space** cortical surface data. 
