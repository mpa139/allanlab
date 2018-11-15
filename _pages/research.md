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

Over the last four years, much of of our group's attention has focused on answering a  a fundamental question: what is the right abstraction to support scalable and available storage and retrieval of data in a distributed database?  The question is motivated by the rift that has occurred over the past decade between the proponents  of the ACID paradigm, typically embraced within the database community, and the advocates of an approach (named BASE, to distinguish it from ACID) based on more limited isolation guarantees and a more streamlined API, typically found within the systems community.  

Developers today are faced with a stark choice. In one corner are ACID transactions: through their guarantees of Atomicity, Consistency, Isolation, and Durability, they offer the programmer an elegant and powerful abstraction for structuring applications and reasoning about concurrency, while guaranteeing the consistency of the database despite failures. Such ease of programming, however, comes at a significant cost to performance and availability. For example, if the database is distributed, enforcing the ACID guarantees requires running a distributed commit protocol for each transaction while holding an exclusive lock on all the records touched during the transaction's entire execution.

In the other corner is the BASE approach (Basically-available, soft state, eventually consistent), recently popularized by several NoSQL systems, which has come to describe a set of programming guidelines whose goal is to eliminate the performance and availability bottlenecks of ACID transactions. Embracing the BASE paradigm, however, comes at the price of renouncing all ACID guarantees: the logic necessary to ensure consistency in the presence of concurrency and faults must now be explicitly coded in the application, increasing drastically both its development time and the possibility of introducing bugs. 

This research effort  aims to restore the promise of ease of programming combined with availability and performance that has become a casualty of the ACID vs BASE debate. The way in which we have pursued this goal has evolved over time.

Our initial approach was motivated by the observations (rooted in Pareto's classic principle)  that transactions are not equally demanding: for many applications there are only a few critical transactions that test the performance limits of ACID. Our vision was to enable these few performance-critical transactions to reap the performance benefits of the BASE paradigm without compromising the ACID guarantees enjoyed by the remaining transactions. 

develop the theoretical foundations (in particular, the necessary notions of isolation) that will enable the ACID and BASE paradigms to coexist in a single databases

2) develop Salt, a prototype of such a database.  We intend to do so by modifying MySQL cluster, a popular distributed databases that exports the read committed isolation property, while at the same time supporting a limited degree of multi-versioning (two copies for each object), a feature that guarantees that reads never block. 

3) Construct applications that demonstrate the benefits of our approach.

hile BASE transactions and Salt Isolation (discussed in our first year report)  had managed to dramatically reduce the programming effort required to achieve an order of magnitude performance improvement over a standard ACID implementation,  they still required developers to rewrite those few performance critical transactions as BASE transactions—a non-trivial exercise.

The result was the Callas system, discussed in detail in our second year report. Callas is a distributed database, derived from MySQL cluster, that instantiates Modular Concurrency Control (MCC), a new approach to federating concurrency controls that we have introduced. In a nutshell, the idea behind MCC is to partition transactions in groups, giving each group the flexibility to run its own private concurrency control mechanism. Being charged with regulating concurrency only for the transactions within their own groups, these mechanisms can be much more aggressive while still upholding safety. A separate cross-group CC mechanism handles conflicts among transactions in different groups. Our evaluation on the TPC-C benchmark and other applications shows that that Callas can improve throughput by close to an order of magnitude with no change to the application.

As we gained more experience with Callas and MCC, we came to realize that, to some degree, it ran the risk of becoming a casualty of its own success. The more  aggressive (and performant) the concurrency control mechanisms we were identifying, the narrower the set of conflicts they were designed to handle: the remaining conflicts were then "thrown over the fence" to the cross -group CC. This CC mechanism, designed for correctness rather than performance (in Callas, it is based on a straightforward 2PC protocol) was becoming a performance bottleneck.  During the third year we investigated how to eliminate the bottleneck.

The result was Tebaldi, a new distributed key-value  that more fully fulfills the promise of MCC by recursively applying the principles of modular concurrency control to the mechanism in charge of cross-group conflicts. Tebaldi's hierarchical MCC has taken modular concurrency control to a new level, both figuratively and, indeed, literally. In particular, Tebaldi achieves over 3.7 times the throughput of Callas.

The performance of Tebaldi, however, does not come for free. Developers need to understand deeply both their application and the characteristics of several different concurrency control mechanisms in order to identify the best performing configuration for Tebaldi's MCC hierarchy. So, our success in ensuring that using Tebaldi requires no application changes may perversely end up negating the project's main goal, namely, that of delivering much higher performance with minimal developer efforts. During the fourth year of this project we have investigated how to reduce these efforts.
