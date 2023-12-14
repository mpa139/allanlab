---
title: "Daniel Soudry - Research"
layout: textlay
excerpt: "Daniel Soudry -- Research"
sitemap: false
permalink: /research/
---

# Research

**Motivation**

I am interested in a quantitative understanding of intelligence, both artificial and biological — and in the possible relationship between the two. I am mainly focused on neural network models, which are a canonical model for neural computation in the brain and are a central part of many modern artificial intelligence systems. 

Such [artificial neural networks](https://en.wikipedia.org/wiki/Artificial_neural_network) with deep architectures have dramatically improved the state-of-the-art in computer vision, speech recognition, natural language processing, and many other domains. 

Despite this impressive progress, artificial neural networks are still [far behind](https://en.wikipedia.org/wiki/Artificial_neural_network) the capabilities of [biological neural networks](https://en.wikipedia.org/wiki/Neural_circuit) in most areas: even the simplest fly is far more resourceful than our most advanced robots. This indicates we have much to improve! 

At the same time, if we wish to understand biological neural networks we must first be able to understand learning in the simplest non-linear artificial neural network – which still remains a mystery.

Therefore, my current research aims to uncover the fundamental mathematical principles governing both types of neural networks.

**Recorded Talks**
Talks for the general audience:
- [On the age of deep learning and the revolution in artificial intelligence](https://www.youtube.com/watch?v=MJ1w4ne3F3I)
- [On the age of deep learning and the revolution in artificial intelligence](https://www.youtube.com/watch?v=MJ1w4ne3F3I) 

## Research interests

My research covers all aspects of neural networks and deep learning.
See below for more information on a few open questions that interest me.

<h3 > <a href="#Deep Learning">Current research: Deep Learning</a></h3>

<ul>
  <li>Learning and optimization in artificial neural networks</li>
  <li>Resource efficient training and inference in artificial neural networks </li>
  <li>Hardware implementations of artificial neural networks</li>
</ul>

<div>
  <img src="/images/respic/research1.png" style="width: 30%; float: center; margin: 10px">
</div>

<h3 > <a href="#Neuroscience Methods">Post-Doc research: Neuroscience Methods</a></h3>

<ul>
  <li>Activity inference </li>
  <li>Model based connectivity </li>
  <li>Efficient simulation methods</li>
</ul>


<div>
  <img src="/images/respic/research2.JPG" style="width: 30%; float: center; margin: 10px;">
</div>

<h3 > <a href="#Neuroscience Theory">Post-Doc research: PhD research: Neuroscience Theorys</a></h3>

Modeling and analysis of
<ul>
  <li>Biological neural networks</li>
  <li>Neurons </li>
  <li> Synapses </li>
  <li> Ion channels </li>
</ul>


  <img src="/images/respic/research3.JPG" style="width: 20%; float: center; margin: 10px;">



<h2 id="Deep Learning">Machine Learning </h2>

There are several open theoretical questions in deep learning. Answering these theoretical questions will provide design guidelines and help with some important practicals issue (explained below). Two central questions are:

- <b>Low training error.</b> Neural Networks are often initialized randomly, and then optimized using local steps with stochastic gradient descent (SGD). Surprisingly, we often observe that SGD converges to a low training error:
 <img src="/images/respic/ML1.png" style="width: 100%; float: center; margin: 10px;">
  
Why is it happening?

- <b> Low generalization error.</b> Neural Networks are ofter trained in a regime where #parameters » #data samples. Surprisingly, these networks generalize well in such a regime, even when there is no explicit regularization. 

For example, as can be seen in the figure below from [Wu, Zu & E 2017](https://arxiv.org/abs/1706.10239) , polyomial curves (right) tend to overfit much more than neural networks (left):  
 <img src="/images/respic/ML2.png" style="width: 100%; float: center; margin: 10px;">
   
Why is it happening?

There are many <u> practical bottlenecks </u> in deep learining (the following fifures are from [Sun et al. 2017](https://arxiv.org/abs/1707.02968).Such bottlenecks occur since neural networks models are large, and keep getting larger over the years: 

 <img src="/images/respic/ML3.JPG" style="width: 70%; float: center; margin: 10px;">

- <b> Computational resources.</b> Using larger neural networks require more computational resources, such as power-hungry GPUs:
 <img src="/images/respic/ML4.png" style="width: 70%; float: center; margin: 10px;">

 How can we train and use neural networks more efficiently (i.e., better speed, energy, memory), without sacrificing accuracy? See my talk [here](https://www.youtube.com/watch?v=CaKlcxyBRP8) (in Hebrew) for some of our results on this.

- <b> Labeled data.</b> In order to train neural nets to high accuracy levels, large quantities of labeled data are required. Such datasets are hard to obtain. For example, for many years the size of the largest vision training data remained constant:
<img src="/images/respic/ML5.png" style="width: 70%; float: center; margin: 10px;">

How can we decrease the amount of label data required for training?

- <b> Choosing hyper-parameters.</b> Since larger models take longer to train, it becomes more challenging to choose model hyper-parameters (e.g., architecture, learning rate) in order to obtain good performance. 

For example, ad can be seen in this ([video](https://youtu.be/OJBFDSynsdU?si=AYkyuPznxZUc1nGy)) [Xiang&Li 2017](http://arxiv.org/abs/1704.03971) , small changes in the training procedure have a large effect on the network performance.

Can we find automatic and robust method to find the "optimal" hyper-parameters?


<h2 id="Neuroscience Methods">Neuroscience Methods </h2>

Neuroscience datasets are typically very challenging. They are usually very noise, of limited duration, and are affected by many unobserved latent variables. Analyzing and modeling these datasets becomes more and more challenging over the years, since the number of recorded neurons increases exponentially, similarly to "Moore's law" (Figure from [Stevenson&Kording 2011](https://www.nature.com/articles/nn.2731)):

 <img src="/images/respic/NM1.png" style="width: 50%; float: center; margin: 10px;">

In order to analyze neuroscience data, certain inference tasks are typically necessary to be able to interpret the data:

- <b> Activity inference.</b> Neural activity is often measured optically: each neuron is edited genetically so it emits fluorescent pulses whenever it fires a "spike". For example (from [Aherns et al. 2013](https://www.nature.com/articles/nmeth.2434)) see this [video](https://youtu.be/lppAwkek6DI) 

Can we infer the "spiking" firing patterns of each neuron from the observed movie? This includes automatic localization of each neurons, demixing of signals from nearby neurons, denoising and deconvlusion of the observed fluorescence to obtain the original "spikes".

- <b> Connectivity estimation.</b>Given the activity patterns of various neurons in the network, can we infer their synaptic and functional connectivity?

- <b> Efficient simulation.</b>Accurately simulating large network models, or even highly detailed single neuron models can be very slow and inefficient. Can we improve the simulation methods?



<h2 id="Neuroscience Theory">Neuroscience Theory </h2>

A central issue in neuroscience is to find the "appropriate" level of modeling: in every level and component of the nervous system we find complex biophysical machinery that affects their functional input output relation. There are many possible levels of modeling:

- <b>Network model.</b> Given some observed phenomenon, such as the formation of [hexgonal grid cells](https://en.wikipedia.org/wiki/Grid_cell#:~:text=A%20hexagonal%20lattice.,environment%20in%20a%20hexagonal%20pattern.)
see this [video](https://docs.google.com/file/d/0BxdUul7wciWqOWUzN3JvT3FhbFE/view?t=15&resourcekey=0-XkhB79FUw2JM53ooWwqkHA) 

<img src="/images/respic/NT2.JPG" style="width: 30%; float: center; margin: 10px;">

What is the simplest neural network model that reproduces this phenomenon, and produces useful (disprovable) predictions? Can we infer from this model the ["purpose"](https://en.wikipedia.org/wiki/Four_causes#End) of this neural circuit?

- <b>Neuron model.</b> Even a single neuron <u>in synaptic isolation</u>, given direct periodic pulse stimulation, can produce very complicated firing patterns over the timescales of days (Figure from [Gal et al. 2010](https://www.jneurosci.org/content/30/48/16332), a vector of response/no-response folded to matrix over 55 hours):

<img src="/images/respic/NT3.png" style="width: 30%; float: center; margin: 10px;">

Given such biophysical and functional complexity, how can we build and analyze useful neural models, with meaningful predictions? 

- <b>Neuronal components.</b> Even sub-cellular components such as a [synapses](https://www.google.co.il/search?q=synapse&rlz=1C1GGRV_enIL751IL751&oq=synapse&aqs=chrome..69i57j69i65j0l4.2656j0j4&sourceid=chrome&ie=UTF-8), or an [ion channel](https://en.wikipedia.org/wiki/Ion_channel) are incredibly complex and can respond stochasticly to stimuli on very long and multiple timescales. For example, here are synaptic strength seems to evolve stochasticaly over timescales weeks ([Minerbi et al. 2009](https://en.wikipedia.org/wiki/Ion_channel)). See this [video](https://docs.google.com/file/d/0BxdUul7wciWqZTgtRTVjazRKQXc/view?t=6&resourcekey=0-Q5ePXyHCbxHy5Om2heOSnQ).

<img src="/images/respic/NT4.JPG" style="width: 30%; float: center; margin: 10px;">

 How can memory of past events be retained in the brain despite these large changes? Can we find the simplest "effective" input-output relation that can be used to model single neurons?

 
