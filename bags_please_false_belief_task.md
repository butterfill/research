---
title: "Bags Please False Belief Game"
date: 2016-11-14
# author: s.butterfill@warwick.ac.uk
bibliography: /Users/stephenbutterfill/endnote/phd_biblio.bib
mainfont: Linux Libertine O
papersize: "a4paper"
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{libertine}
fontsize: 12pt
compile_pdf: pandoc bags_please_false_belief_task.md -o bags_please_false_belief_task.pdf --filter pandoc-citeproc -N --latex-engine=xelatex
---


False Belief Game partly inspired by ‘Papers Please’

# Ultimate goal

Identify some (or all) of the processes underpinning automatic belief-tracking, ideally with the  processes underpinning prospective embodied foraging. Determine in what sense, if any, these are mindreading processes.


# The Game

There is an array of numbered [or otherwise indexed] lockers.

Visitors arrive, place bags in the lockers and leave.

Some time later, a Visitor will return and ask you to open a locker for them by giving the index or number of the locker (this is the Requested Locker). Your task is to open the locker containing the thing they want, which is usually but not always the locker they specify in their request.  [or: your task is to open the locker they request? See ‘interference/helping’ below]

You sit in front of the lockers [or an array of buttons?]. You can open any locker by clicking on the locker [or clicking the corresponding button?].

Sometimes the Cleaner of Lockers moves a Visitor’s bag to another locker after the Visitor have placed it (in order to clean the locker).  This can happen in the Visitor’s presence (True Belief) or absence (False Belief Location).  

Some lockers have transparent doors.  Because most bags look different, the transparent doors eliminate the possibility of false beliefs about location.  Sometimes a visitor’s luggage is moved from a transparent locker after they have placed it and replaced with a visually indistinguishable piece of luggage.  This can happen in their presence (True Belief) or absence (False Belief Identity).

But they allow for the possibility of false beliefs about identity.


# What to measure

- Frequency of opening a locker other than the Requested Locker.  Prediction: this will differ between TB and FB conditions (replicates a standard helping false belief task).

- Frequency of errors (incorrect locker opened).  Ideally this would not vary between conditions.

- Movement onset time. ([@Wel:2013uq] found that MOT is longer in FB-Loc than TB-Loc, but only when people are explicitly instructed to think about beliefs.)

- Initial direction of movement. Prediction: this will vary between TB-Loc and FB-Loc but not TB-Id and FB-Id (unless MOT differs between TB-Id and FB-Id, and except possibly as a consequence of learning over the game).

- Degree of deviation of movement trajectory towards the Original Location (area)

- Changes in direction (frequency, pace).


# What to vary

- Number of visitors with unretrieved luggage, and of lockers

- Would be easy to introduce a secondary task

- Would be easy to vary timing of actions (e.g. impose varying time pressure, or introduce delays before responses are permitted (which should affect how strongly behaviour reflects automatic mindreading processes), ...)


# Questions

- Which measures reliably differ between TB-Loc and FB-Loc conditions? Do the same measures differ between TB-Id and FB-Id conditions? (Prediction: no)

- Does varying a factor like number of visitors with unretrieved luggage differentially affect which measures reliably differ between conditions?

- How does performance change with practice? (Automatization effects?)


# Interference/helping paradigms

We could have both helping (where the task is to open the locker actually containing the visitor’s luggage) and altercentric interference versions (where the task is to open the locker specified by the visitor---in this case we hope to observe some effect of the visitor’s false belief on some aspects of performance). Theoretically helping is initially more interesting because successful helping appears to involve a combination of tracking another’s belief and knowing where the luggage actually is.


# Details

- The starting point for movements to the lockers should ideally be fixed.  Achieve this by having players click on a door-release button to let each visitor into the room.

- The Cleaner of Lockers should ideally move bags to lockers following a pattern that ensures the changes involve a fixed distance and angle.

# References