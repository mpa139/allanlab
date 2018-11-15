---
title: "Lorenzo's group - Research"
layout: textlay
excerpt: "Lorenzo's group -- Research"
sitemap: false
permalink: /research/
---

# Research

Our research aims to understand how to design and build distributed systems worthy of the  trust that government, businesses, and the public  increasingly put in them. We investigate both foundational and applied aspects of reliable distributed computing; at its best, our work leverages the former to shape the latter.

Over the years our work has focused on low overhead for tolerance techniques for benign failure (research highlights are here here and here) , Byzantine fault tolerance (highlights here, here and here), and the the intersection of Distributed Computing and Game Theory (highlights here, here, and here)
 
![]({{ site.url }}{{ site.baseurl }}/images/respic/layers_real.jpg){: style="width: 300px; float: right; border: 10px"}

Over the last four years, much of of our group's attention has focused on answering a  a fundamental question: what is the right abstraction to support scalable and available storage and retrieval of data in a distributed database?  The question is motivated by the rift that has occurred over the past decade between the proponents  of the ACID paradigm, which offers programmers an elegant and powerful abstraction for structuring applications and reasoning about concurrency, and the advocates of an alternative approach (referred to by the BASE acronym, to distinguish it from ACID -- #geeksrule) based on more limited isolation guarantees and a more streamlined API.  

This research effort  aims to restore the promise of ease of programming combined with availability and performance that has become a casualty of the ACID vs BASE debate. The way in which we have pursued this goal has evolved over time.

Our initial approach was motivated by the observations (rooted in Pareto's classic principle)  that transactions are not equally demanding: for many applications there are only a few critical transactions that test the performance limits of ACID. 
We leveraged this observation todevelop the theoretical foundations (in particular, the new abstraction of BASE transactions and the notions of isolation necessary to support it) that  enable the ACID and BASE paradigms to coexist in a single databases, and then proceeded to design and build Salt, a database that enables these few performance-critical transactions to reap the performance benefits of the BASE paradigm without compromising the ACID guarantees enjoyed by the remaining transactions. 

While Salt can dramatically reduce the programming effort required to achieve an order of magnitude performance improvement over a standard ACID implementation,  it does still still require developers to engage in the non-trivial exercise to rewrite those few performance critical transactions as BASE transactions.

we then decided to investigate an even more ambitious objective: bringing the performance of ACID applications within striking distance of BASE-reimplementation—but without requiring any programming effort from the developer.

The result was a new distributed database, called Callas (Callas is the most popular brand of SAlt in Greece, in addition to a legendary soprano). Callas is also derived from MySQL cluster; its secret sauce is Modular Concurrency Control (MCC), a new approach to federating concurrency controls.  MCC  partitions transactions in groups, giving each group the flexibility to run its own private concurrency control mechanism. Being charged with regulating concurrency only for the transactions within their own groups, these mechanisms can be much more aggressive while still upholding safety. A separate cross-group CC mechanism handles conflicts among transactions in different groups. Our evaluation on the TPC-C benchmark and other applications shows that that Callas can improve throughput by close to an order of magnitude with no change to the application.

As we gained more experience with Callas and MCC, we came to realize that, to some degree, it ran the risk of becoming a casualty of its own success. The more  aggressive (and performant) the concurrency control mechanisms we were identifying, the narrower the set of conflicts they were designed to handle: the remaining conflicts were then "thrown over the fence" to the cross -group CC. This CC mechanism, designed for correctness rather than performance (in Callas, it is based on a straightforward 2PC protocol) was becoming a performance bottleneck.  During the third year we investigated how to eliminate the bottleneck.

The result was Tebaldi, a new distributed key-value  that more fully fulfills the promise of MCC by recursively applying the principles of modular concurrency control to the mechanism in charge of cross-group conflicts. Tebaldi's hierarchical MCC has taken modular concurrency control to a new level, both figuratively and, indeed, literally. In particular, Tebaldi achieves over 3.7 times the throughput of Callas.

The performance of Tebaldi, however, does not come for free. Developers need to understand deeply both their application and the characteristics of several different concurrency control mechanisms in order to identify the best performing configuration for Tebaldi's MCC hierarchy. So, our success in ensuring that using Tebaldi requires no application changes may perversely end up negating the project's main goal, namely, that of delivering much higher performance with minimal developer efforts. During the fourth year of this project we have investigated how to reduce these efforts.
