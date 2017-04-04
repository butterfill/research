---
title: "Serial vs Hierarchical Pattern Recognition"
author: 's.butterfill@warwick.ac.uk'
bibliography: /Users/stephenbutterfill/endnote/phd_biblio.bib
mainfont: Linux Libertine O
papersize: "a4paper"
header-includes:
  - \usepackage[utf8]{inputenc}
  - \usepackage{libertine}
fontsize: 12pt
compile_pdf: pandoc -s seminar_tasks.md -o seminar_tasks.md.pdf --filter pandoc-citeproc 
---

The distinction is between serial and hierarchical patterns is analogous to that between finite state and phrase structure grammars [@Chomsky:1956zj], but can be understood informally for present purposes.
Serial patterns involve relations among consecutive chunks of behaviour and so can be identified by relatively simple learning mechanisms that track statistical relations between pairs of consecutive chunks [@Conway:2001ik]. 
Some serial patterns arise from the fact that pursuit of a goal characteristically involves a sequence of adjacent chunks; for example, eating a burger involves grasping it and then repeatedly brining it to the mouth. 
Hierarchical patterns involve relations among non-consecutive chunks.
Such patterns sometimes occur because pursuit of a goal involves subgoals that can be performed in different orders, as when making a burger involves preparing the bun and fillings individually before bringing them together.
Patterns in the behavioural chunks that constitute burger-making activities cannot be learnt only by tracking relations between pairs of consecutive chunks.

The distinction between serial and hierarchical patterns occurs in thinking about speech perception, where the organisation of phonemes into words counts as a sequential pattern (ignoring, for simplicity, additional structure required to accommodate variability in the allophones that realise phonemes), whereas organisation of words into clauses counts as an hierarchical pattern.

# Sequential patterns

Consider the following sequence of mundane actions:

> … push door, walk through frame, walk to desk, grasp paper, orient to pen, reach for pen, write on paper, fold paper, place pen, reach for headphones, push button, …

Here the flow of movements is described in terms of phoneme-like chunks that infants and adults can readily identify [@Saylor:2007pj].  Infants (from around 9 months) and adults can also group these chunks into word-like units such as the letter-writing sequence in the above example: these are chunks that seem to belong together and to be separate from previous and ensuing chunks [@Saylor:2007pj].  The boundaries of these units are generally ‘intention-relevant’ [@Saylor:2007pj], corresponding to the completion of a goal or subgoal.

In some cases, subjects have prior knowledge of intention or purpose which guides the identification of word-like behaviour units [@Zacks:2004vd].  However, ascribing intention is not generally necessary for isolating these units.  There are at least two types of non-intentional cue to their boundaries. 
First, commencement and completion of a goal or subgoal typically coincide with dramatic changes in the physical features of the movements [@Zacks:2001vo].  Baldwin and Baird express this idea graphically with the notion of a ‘ballistic trajectory that provides a temporal contour or ‘envelope’ demarcating one intentional act from the next’ [@Baldwin:2001rn].  Research using schematic animations has shown that adults use a variety of movement features to group behavioural chunks into word-like units [@Zacks:2004vd; @Hard:2006gr]. 
The second non-intentional cue is statistical.  Chunks of behaviour that are all steps to a single goal or subgoal are more likely to occur in succession than chunks not so related; thus transitional probabilities in the sequence of chunks could in principle be used to identify intention-relevant units, much as phonemes can be grouped into words by means of tracking transitional probabilities [@Saffran:1996aj; @Baldwin:2008mw; @Gomez:2000jr].  In fact, Baldwin and colleagues demonstrated that adults can learn to group small chunks of behaviour into larger word-like units on the basis of statistical features alone [@Baldwin:2008mw].  And since the statistical learning mechanism required for discerning such units is automatic [@Fiser:2001cx], domain-general [@Kirkham:2002cj] and present in other species including monkeys [@Hauser:2001oo] and rats [@Toro:2005ma], it seems plausible to suppose that sensitivity to intention-relevant units in sequences of behavioural chunks can be found in individuals that lack the ability to ascribe intentions or goals.
	
In short, domain-general learning mechanisms enable chunks of behaviour to be grouped into word-like units on the basis of ballistic envelopes and transitional probabilities.  Just as words are semantically relevant units yet can be discerned without knowledge of semantics, so these behavioural units have boundaries corresponding to the fulfilment of goals and intentions but can be identified without knowledge of goals or intentions.

Note that discerning pattern in sequences of behaviour is not limited to intention-relevant units: behaviour reading may group behavioural chunks into units that have no clear relevance to a goal, as studies requiring subjects to segment behaviours using reversed animations and other manipulations show [@Hard:2006gr; @Baldwin:2008mw; @Kurby:2008bk].  Similarly, use of statistical cues to group phonemes into words does not yield only meaningful words.  Discerning intention-irrelevant units may be undesirable overgeneration or it may have predictive value.  The definition of behaviour-reading allows for the exploitation of any useful patterns, not just those induced by goals and intentions.

# Hierarchical patterns

In discussing sequential patterns we were concerned with grouping together strings of consecutive behavioural chunks.  But there are also patterns in behaviour connecting non-consecutive chunks.  For example, making a burger involves several steps whose order is only loosely constrained, where some of these steps can be omitted or replaced (veggie burger, hamburger) and where steps can be interspersed with irrelevant actions (answering the phone).  Grouping together all and only the behavioural units involved in making a burger therefore involves discerning hierarchical structure.  Clearly this is possible, but is it possible independently of ascribing intention?

Several researchers who appear to be addressing this question are actually concerned only with identifying word-like units [@Zacks:2001vo; @Hard:2006qm; @Hard:2006gr; @Kurby:2008bk].
They label this ‘hierarchical structure’ because flowing motion is first being divided into phoneme-like behavioural chunks whose organisation then defines boundaries of larger word-like units.  We can thus regard the chunks as parts of larger units, which justifies the label ‘hierarchical’.  However, discerning word-like units only requires sequential learning—that is, it only requires tracking associations between consecutive chunks.  Sensitivity to these ‘hierarchical structures’ does not imply that one can also detect patterns involving optional components or variable ordering, such as those involved in making a burger or preparing a nettle.  Following @Conway:2001ik, I therefore reserve the label ‘hierarchical’ for patterns involving relations among potentially non-consecutive chunks.

To my knowledge the question of learning hierarchal patterns in behaviour has not been directly addressed.  We do know from research in other domains that hierarchical patterns can be learnt by adults [@Newport:2004wi] and infants from 12-months or earlier [@Saffran:2008oc].  Learning hierarchical patterns differs from learning sequential patterns in that it requires attention and cannot occur when subjects are distracted by a secondary task [@Cohen:1990wp] and there appear to be constraints on the types of pattern that can be learnt [@Newport:2004wi]. 

There is uncertainty on whether non-humans are capable of learning hierarchical patterns of any kind.  Evidence for an absence of hierarchical learning has been offered for cotton-top tamarins [@Fitch:2004wj] and rats [@Toro:2005ma], and there is no convincing evidence for such learning in nonhumans generally [@Corballis:2007sg].  Inability to learn hierarchical patterns would limit the power of behaviour reading based on domain-general learning mechanisms to activities that are often uniformly realised (little or no variation in the steps taken or the order in which they are performed) and performed without interruption. 

In short, acting on hierarchically structured intentions and goals tends to create statistical and prosodic cues in the pattern of behaviours.  Discerning these cues makes it possible to recover the structure of the behaviour without knowledge of the goals or intentions responsible for them.  Such patterns can be discerned by humans, perhaps including infants, but probably not by other animals.  Learning these patterns is not automatic and requires attention to patterns of behaviour. 

# Other cues to hierarchical structure

Human infants use prosodic cues such as changes in pitch and pauses used by infants to identify clause boundaries [@Soderstrom:2005zy; @Seidl:2008zf].  It is possible that somewhat similar cues in behaviour---changes in motion features and pauses---make it possible to identify where hierarchically structured behaviours begin and end.  The availability of such cues to human infants may be boosted by ‘motionese’.  @Brand:2002by found that ‘mothers spontaneously modified their infant-directed actions in a number of ways … a higher level of interactiveness, greater repetitiveness and movements that were larger in scale but reduced in complexity.’  These modifications might in principle assist infants’ efforts to detect hierarchical patterns in behaviour, amplifying and inserting motion features and pauses to reduce infants’ dependence on statistics.

Richard Byrne has suggested that identifying the parts of hierarchically structured behaviours may be facilitated by comparison between different occasions  [@Byrne:2003wx].  In his study of Rwandan mountain gorillas’ preparation of nettles for eating, a complex task involving several sub- and sub-sub-goals, he found that repetitions, omissions, and substitutions indicate boundaries of significant units, as do points where one-off (and therefore probably extraneous) behaviours are interwoven. 

The existence of such cues suggests that, in special cases or where assisted by experts who use motionese, it may be possible in principle to identify plan-induced hierarchical patterns in behaviours without knowledge of intention and independently of any domain-general capacity for recognising hierarchical patterns. 

# References