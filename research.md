---
title: "Allan Lab - Research"
layout: textlay
excerpt: "Allan Lab -- Research"
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

## Research interests

My research covers all aspects of neural networks and deep learning.
See below for more information on a few open questions that interest me.

<h3 > <a href="#Deep Learning">Current research: Deep Learning</a></h3>


<ul>
  <li>Learning and optimization in artificial neural networks</li>
  <li>Resource efficient training and inference in artificial neural networks </li>
  <li>Hardware implementations of artificial neural networks</li>
</ul>

![]({{ site.url }}{{ site.baseurl }}/images/respic/research1.png){: style="width: 30%; float: right; margin: 5px"}


<h3 > <a href="#Neuroscience Methods">Post-Doc research: Neuroscience Methods</a></h3>

<ul>
  <li>Activity inference </li>
  <li>Model based connectivity </li>
  <li>Efficient simulation methods</li>
</ul>

![]({{ site.url }}{{ site.baseurl }}/images/respic/research2.JPG){: style="width: 30%; float: center; margin: 10px"}

<h3 > <a href="#Neuroscience Theory">Post-Doc research: PhD research: Neuroscience Theorys</a></h3>

Modeling and analysis of
<ul>
  <li>Biological neural networks</li>
  <li>Neurons </li>
  <li> Synapses </li>
  <li> Ion channels </li>
</ul>

![]({{ site.url }}{{ site.baseurl }}/images/respic/research3.JPG){: style="width: 30%; float: center; margin: 10px"}

<h2 id="Deep Learning">Deep Learning </h2>

There are several open theoretical questions in deep learning. Answering these theoretical questions will provide design guidelines and help with some important practicals issue (explained below). Two central questions are:
  
<ul>
  <li> <b>Low training error.</b> Neural Networks are often initialized randomly, and then optimized using local steps with stochastic gradient descent (SGD). Surprisingly, we often observe that SGD converges to a low training error:
 

  
  </li>
  ![]({{ site.url }}{{ site.baseurl }}/images/respic/ML1.png){: style="width: 30%; float: center; margin: 10px"} 

Why is it happening?

  <li><b>Low generalization error.</b> Neural networks are often trained in a regime where #parameters » #data samples. Surprisingly, these networks generalize well in such a regime, even when there is no explicit regularization. For example, as can be seen in the figure below (from <a href=https://arxiv.org/abs/1706.10239>Wu, Zu & E 2017 </a>), polyomial curves (right) tend to overfit much more than neural networks (left): 
  
![]({{ site.url }}{{ site.baseurl }}/images/respic/ML2.png){: style="width: 70%; float: center; margin: 10px"} 

Why is it happening?

There are many practical bottlenecks in deep learning (the following figures are from Sun et al. 2017). Such bottlenecks occur since neural networks models are large, and keep getting larger over the years:

  
![]({{ site.url }}{{ site.baseurl }}/images/respic/ML3.png){: style="width: 70%; float: center; margin: 10px"} 

  
  </li>
 <li><b>Computational resources.</b> Using larger neural networks require more computational resources, such as power-hungry GPUs:
   
[]({{ site.url }}{{ site.baseurl }}/images/respic/ML4.png){: style="width: 70%; float: center; margin: 10px"} 

    
</ul>


<h2 id="Neuroscience Methods">Neuroscience Methods </h2>

<h2 id="Neuroscience Theory">Neuroscience Theory </h2>








Our overarching goal is to explore and understand new quantum states of electronic matter on the atomic scale. To do so, we use and develop novel spectroscopic-imaging scanning tunneling microscopy (SI-STM) tools to visualize the relevant quantum mechanical degrees of freedom.

Our goal is to build instruments and develop techniques that enable us to address the questions we find most interesting. This is possible thanks also to Milan's broad background with different research themes and technologies: he learned his trade in [Seamus Davis’ SI-STM lab](http://davisgroup.lassp.cornell.edu/) and with [Felix Baumberger](http://dpmc.unige.ch/gr_baumberger/index.html), and later moved as an [ETH fellow](http://www.ethfellows.ethz.ch/) to [Andreas Wallraff’s qudev lab](http://www.qudev.ethz.ch/) where he investigated coupled cavity arrays in circuit QED. We further have group members with different background and interests, working together on physics and instrumentation.

Here are some themes and techniques that we currently work on:

**Scanning tunneling noise spectroscopy (STNS).** We have developed a novel cryogenic MHz amplifier that allows us to measure not only the average tunneling current, but also its fluctuation! This has many applications: one can detect the fluctuations of the electronic states, peculiar tunneling processes, and shot noise. We have used this instrument to discover charge trapping in the insulating layer of the cuprates, connected to the c-axis mystery, and to measure the doubling of the charge due to Andreev processes to the superfluid in a lead sample.


**Mott physics and high-temperature superconductivity.** Questions of interest include: (i), How does the Mott state collapse upon doping and how is this related to the complex phase diagram of high-temperature superconductors? (ii), What is the strange metal phase seen in correlated electron systems? Is this an exotic long-range entangled state? What is the mechanism of dissipation in that state? (iii), Why is the transition temperature in high-temperature superconductors so high? We have worked on iridates, rhodates, and cuprates.

**Nanofabricated "Smart Tips"**.
![]({{ site.url }}{{ site.baseurl }}/images/respic/SmartTip.png){: style="width: 250px; float: left; margin: 0px  10px"}
One of the  projects back from my job-proposal is to develop nanofabricated STM tips. The idea behind these “smart tips” is to use the technologies that were developed over decades in nanofabrication and make them available for scanning probe by using a nano-device instead of the traditional STM tungsten tip. One gains the flexibility of using different functionalities that are known from the fields of nanofabrication and mesoscopic physics. We are collaborating with the group Simon Groeblacher at TU Delft to realize this concept, benefitting from their unparalleled micro/nano fabrication know how.  A prototype of a smart tip is shown to the left. See publications in Microsyst Nanoeng, Nanotechnology, and PRB.

**Josephson STM.** Josephson STM has the ability to gain insight into spatial variations of the order parameter, or superfluid density. We have managed to, for the first time, use JSTM with atomic resolution on a quantum material.
We have used atomic-resolution Josephson scanning tunneling microscopy to reveal a strongly inhomogeneous superfluid in the iron-based superconductor FeTe0.55Se0.45. The results and their implications are published in Nature.

We also detected and investigated a quite particular YSR state in the same material.

**Ultra-stable SI-STM instrument.**  ![]({{ site.url }}{{ site.baseurl }}/images/respic/STMHead.png){: style="width: 250px; float: right; margin: 0px 10px"}
For SI-STM, having the most stable STM head is key. We have used finite element simulations, good choices in material science, and craftsmanship to build the most stable STM head in the world, to our knowledge. See publication in RSI.


**Strange Metals.** The strange metal phase might be the most mysterious phase of high-temperature superconductors. Here, the electrical resistivity grows linearly with temperature T in large areas of the phase diagram, with a mean free path that diminishes to a fraction of the interatomic distance. T-linear resistivity is often associated with quantum critical points and marginal-Fermi-liquid physics. In strange metals, the mystery seems to go even further: we deal with something that looks like a quantum critical phase over an extended range of the phase diagram instead of cumulating in a point. There exists no consistent theory for strange metals, leading to more adventurous new approaches including the holographic theories that use insights from gravity to explain strange metals (a recent textbook on this was written by our colleagues at Leiden University, Schalm and Zaanen).
We are part of the 'Strange Metal consortium NL' that includes the groups of Hussey, Golden, van Heumen, Zaanen, Schalm, Stoof and Vandoren. 

**Magnetic fluctuations and electron spin resonance.**
![]({{ site.url }}{{ site.baseurl }}/images/respic/SpinFluc.png){: style="width: 70%; float: center; margin: 10px"}

**Twisted bilayer graphene and other material with super-periodicities.**
We have proposed that artificial super-periodicities can lead to improved superconductivity, both because of increased density of states and because of phase space arguments (see image from our SciPost publication below). Perhaps for different reasons, twisted bilayer graphene has been shown to superconduct! We are investigate this material with the groups of Efetov, Baumberger, and van der Molen.

![]({{ site.url }}{{ site.baseurl }}/images/respic/SciPost.png){: style="width: 70%; float: center; margin: 0px"}

### ... and more.
