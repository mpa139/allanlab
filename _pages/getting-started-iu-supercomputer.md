---
title: "Vision in Action Lab - Positions"
layout: textlay
excerpt: "IU Supercomputers -- Getting Started"
sitemap: false
permalink: /resources/getting-started-iu-supercomputers
---

# Getting Started on IU's supercomputers

Prerequisites: These instructions will assume that you're familiar with the material covered in [Software Carpentries Unix Shell Lesson](http://swcarpentry.github.io/shell-novice).  This lesson material will cover how to use the shell to move around and manipulate files on a computer.  You may also be interested in [learning some about version control](https://swcarpentry.github.io/git-novice/) as the code the lab deploys on the supercomputer is managed with git.

## Carbonate and Big Red 3
The lab works primarily on two of the supercomputers, Carbonate (Matlab works more readily on this one) and Big Red 3.

## Create computing accounts.
To use Carbonate, Big Red 3 and/or Slate you will need to ["create additional computing accounts" with IU](https://access.iu.edu/Accounts/Create).  Select the systems you want to create an account on and click create accounts.  Provide any additional information that they request.  Once you've created the accounts it will take a couple of hours for the request to be processed.  Then you will be able to log-in via SSH with your IU username and password. 

Note -- We have had some difficulty with initial user accounts on this system.  If after you can log-in you are unable to run a supercomputer job on slurm and it gives the following error:

 `Unable to allocate resources: Invalid account or account/partition combination specified.`
 
You should reach out to the [High Performance Systems](https://mailform.kb.iu.edu/email.php?cid=26) team and describe the error.  They should be able to finalize your account and resolve the issue.  

In general the HPC support folks are responsive and helpful. When you reach out to them, please always describe the problem in detail (including what system you were on, what you were trying to do, what error you received).  The way to think about it is that they need to be able to reproduce the problem in order to solve it.

## Storage
[A current overview of the storage available in conjunction with IU's supercomputers](https://kb.iu.edu/d/avkm).

On each supercomputer you will have a home directory with an allocation of 100GB.  You may also request additional storage (default 800GB and up to 1.6TB) on Slate.  For projects with larger storage needs or a project with data shared across multiple users, we can request space on Slate-Project where we can request up to 15TB for free (with charges for larger storage requests).

On the supercomputer
Slate-project storage is found at: `/N/project/your-project-name`
Slate storage is found at: `/N/slate/your-user-name`

## Using RED desktop
IU provides this very cool tool to make the supercomputing resources more accessible to all users, particular those new to programming, computing and supercomputers.  Using [RED desktop](https://kb.iu.edu/d/apum), you're able to interact with the supercomputers using a desktop interface.  You will still need to [create a Carbonate account](https://access.iu.edu/Accounts/Create) using the same process I've described above.

Once you have your Carbonate account, there are two ways to get to RED desktop.
1. [Download, install, and configure ThinLinc Client.](https://kb.iu.edu/d/aput)
2. Use your web browser and navigate to [https://red.uits.iu.edu](https://red.uits.iu.edu). If prompted, log in with your IU username and passphrase.

Then it's like a desktop.  You'll see your home directory on the desktop, as well as slurm which is the job manager.  If you go up a directory, then you'll see the path of your home directory is /N/u/kbonnen/Carbonate.  You can also navigate to other storage locations from here (like slate and slate-project, see [section on Storage](#storage) above. 

Note: Most of the documentation provided here will focus on using the commandline to accomplish tasks, but I suspect that almost anything can also be done from RED desktop.


## Accomplishing tasks on the supercomputer (commandline)

### Logging in to the supercomputer for the first time
Yay! You have an account and you're ready to go.  Let's do it.

1. Once your account is created, you can use any SSH2 client to access `bigred3.uits.iu.edu`. 

- **On a Mac or Linux machine**, open up Terminal and type the following command:

`ssh your-user-name@bigred3.uits.iu.edu`

Where your-user-name is your IU username. You will be prompted for a password.  Type in your IU password.

- **On Windows** you will open up [PuTTY](https://www.putty.org/) and ssh into bigred3.uits.iu.edu with your IU username and password.

2. Once you've logged in with your IU username and password you will be prompted to authenticate via DUO.  Follow the instructions.
3. You should see a welcome message that looks something like this:

> Last login: Sun Apr  3 17:09:55 2022 from 149.161.198.253
>
>            Welcome to Indiana University's Big Red 3 Cluster
>               Email questions and comments to hps-admin@iu.edu.
>
>        For information about this cluster see https://kb.iu.edu/d/aoku.
  
  4. Congratulations!!

### Running your first slurm job.

### An easier way to log-in
coming soon -- (for Mac and Linux users)
#### Part 1 -- typing bigred 

#### Part 2 -- encryption keys

### Using Sublime as your text editor

## Moving / Copying large amounts of data
coming soon -- [Globus](https://kb.iu.edu/d/bdqp)

## List of Current Slate-Project Accounts
infant-image-statistics:  Collaboration with Linda Smith's lab on XXXXXX dataset.
