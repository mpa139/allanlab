

# Getting Started on IU's supercomputers

Prerequisites: These instructions will assume that you're familiar with the material covered in [Software Carpentries Unix Shell Lesson](http://swcarpentry.github.io/shell-novice).  This lesson material will cover how to use the shell to move around and manipulate files on a computer.  You may also be interested in [learning some about version control](https://swcarpentry.github.io/git-novice/) as the code the lab deploys on the supercomputer is managed with git.

### Carbonate and Big Red 3
The lab works primarily on two of the supercomputers, Carbonate (Matlab works more readily on this one) and Big Red 3.

## Create computing accounts.
To use Carbonate, Big Red 3 and/or Slate you will need to ["create additional computing accounts" with IU](https://access.iu.edu/Accounts/Create).  Select the systems you want to create an account on and click create accounts.  Provide any additional information that they request.  Once you've created the accounts it will take a couple of hours for the request to be processed.  Then you will be able to log-in via SSH with your IU username and password. 

Note -- We have had some difficulty with initial user accounts on this system.  If after you can log-in you are unable to run a supercomputer job on slurm and it gives the following error:

 `Unable to allocate resources: Invalid account or account/partition combination specified.`
 
Then you should reach out to the [High Performance Systems](https://mailform.kb.iu.edu/email.php?cid=26) team and describe the error.  They should be able to finalize your account and resolve the issue.  In general the HPC support folks are responsive and helpful. When you reach out to them, please always describe the problem in detail (including what system you were on, what you were trying to do, what error you received).  The way to think about it is that they need to be able to reproduce the problem in order to solve it.

### Storage
[A current overview of the storage available in conjunction with IU's supercomputers](https://kb.iu.edu/d/avkm).

On each supercomputer you will have a home directory with an allocation of 100GB.  You may also request additional storage (default 800GB and up to 1.6TB) on Slate.  For projects with larger storage needs or a project with data shared across multiple users, we can request space on Slate-Project where we can request up to 15TB for free (with charges for larger storage requests).


## Logging in to the supercomputer for the first time


## An easier way to log-in

## Using Sublime as your text editor

## Using RED desktop (a.k.a. I don't like this command-line stuff)

## Moving / Copying large amounts of data
Use rclone...

## Current Slate-Project Accounts
Infant-Image-Statistics
