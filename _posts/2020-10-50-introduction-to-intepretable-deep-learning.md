---
layout: post
title:  "Interpretable Deep Learning Part I: What is Interpretability in Deep Learning?"
date:   2020-10-05 20:00
author: Mariana da Silva 
excerpt: An introduction to interpretability in deep learning 
---
###What is interpretable deep learning? 

In this series of blogs we look at the rising field of Interpretable Deep Learning, with a focus on computer vision tasks. Before digging into specific methods of interpretability, it is important to understand the motivations behind this hot-topic.

Deep learning (DL) models have achieved superior performance in comparison with traditional methods in a myriad of applications. However, as networks grow in complexity, and the deeper they become, the harder it becomes to interpret how DL models make their prediction. 

Popular DL architectures, like Resnets, U-nets and GANs are often employed as black-box models for tasks of classification, regression and segmentation. Understanding the reasons behind predictions of DL methods is a crucial step towards a responsible implementation of these types of methods. An important motivating example is the use of DL models in the medical field, where it is particularly necessary to consider transparency and accountability. Take for example a DL algorithm that tries to diagnose a disease from medical data. It is important to understand if the algorithm is making its decisions based on features that are biologically meaningful for that particular disease, as opposed to making biased predictions solely based on noise, or concurrent symptoms from another unrelated disease.

Besides being useful for end-users and even ethical committees and regulatory agencies, interpretability methods can also be very helpful for developers and DL engineers. Visualizing and understanding predictions made by networks allows for sanity-checks and identification of biases and potential adversarial attacks, and can ultimately lead to improved performance of models.

Owing to these multiple motivations, the field of Interpretable Deep Learning has therefore gained a lot of momentum in recent years. But what is interpretability? 

###Interpretability vs Explainability

There is no formal definition of what interpretability in DL entails, or even a common notion of how it is measured and evaluated. **Interpretability** and **explainability** are often used interchangeably in the context of deep learning, although these two terms are not in fact identical: 
1. **Interpretability** is about the extent to which humans can consistently  predict what is going to happen to a model’s result, given a change in input or in model parameters.
2. **Explainability** can be defined as - more than just being able to discern the mechanics of a model - the extent to which these mechanics and cause-effect relations can be understood and explained in human concepts. 

Even though there is a subtle difference between these two concepts, it is not hard to understand that they are highly related, and that interpretability is a necessary condition to ultimately allow for explainability. Because these two concepts are often used with the same meaning, it is frequent to refer to the result of interpretability methods as **explanations**.

###Types of interpretability

Methods  of  interpretable  deep  learning  can  be  grouped  into  two  main  categories:  
1. **Intrinsic interpretability** is achieved with models that are inherently interpretable in their structure. This includes  models  where the decision process can be “followed”, such  as  decision- tree types of models and the use of  attention mechanisms,  and also models with incorporated  interpretability  constraints, such as the learning of disentangled features. These methods are further explained and discussed in Part III of this blog series.

2. **Post-hoc interpretability** refers to the application of methods that analyze a model’s decisions after its training. Examples  of  this include  feature  visualization  and  feature  attribution  methods. 

| <img src="/images/blogs/genetics/second-blog/transcription.jpg" alt="Transcription" title="Transcription" width="900"> |
|:--:| 
| **Figure 1.** Examples of intrinsic and post-hoc interpretability methods.|

With further subsets, they can be classified based on their scope:
1. **Global interpretability**: understanding how the model makes decisions, based on an integrated analysis of its structure and learned parameters. 
2. **Local interpretability**: reflecting model behaviour for individual instances, by analysing specific decisions of the network.

Methods of interpretability can also be categorized as model-agnostic or model-specific. **Model-agnostic** tools can be used on any machine learning model and, by definition, do not  have  access  to  model  internals  such  as  weights  or  structural  information, being applied after training (post-hoc) by analyzing feature input and output pairs. In contrast, **model-specific** interpretability methods are applied to either a particular model, or a type of model. An example of the latter are methods that can only be applied to Convolutional Neural Networks (CNNs), such as popular methods based on back-propragation of gradients, like Grad-CAM. Grad-CAM and similar algorithms are further discussed in Part II of this blog series.
