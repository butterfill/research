%!TEX TS-program = xelatex
%!TEX encoding = UTF-8 Unicode

%\def \papersize {a5paper}
\def \papersize {a4paper}
%\def \papersize {letterpaper}

%\documentclass[14pt,\papersize]{extarticle}
\documentclass[12pt,\papersize]{extarticle}
% extarticle is like article but can handle 8pt, 9pt, 10pt, 11pt, 12pt, 14pt, 17pt, and 20pt text

\def \ititle { Notes on Folk Pscyhology   : It Began with Heider }
\def \isubtitle {}
\def \iauthor { Bart Geurts and Steve Butterfill }
\def \iemail{  }

\usepackage[xindy,toc]{glossaries}
\input{glossary}
\makeglossaries

\usepackage{longtable,booktabs,array}
\usepackage{calc} % for calculating minipage widths
\usepackage{etoolbox}
\makeatletter
\patchcmd\longtable{\par}{\if@noskipsec\mbox{}\fi\par}{}{}
\makeatother
% Allow footnotes in longtable head/foot
\IfFileExists{footnotehyper.sty}{\usepackage{footnotehyper}}{\usepackage{footnote}}
\makesavenoteenv{longtable}

\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}


% --- figures and footnotes
% thank you https://tex.stackexchange.com/questions/147350/how-to-test-if-im-currently-in-a-footnote-or-not?noredirect=1&lq=1
\newif\iffoot
\footfalse

\let\origfootnote\footnote
\renewcommand{\footnote}[1]{\foottrue\origfootnote{#1}\footfalse}

\newcommand{\fig}[3]{
\iffoot
\label{fig:#3}#2 \emph{Source}:#1\includegraphics[width=0.7\textwidth]{img/#3}
\else
  \begin{figure}
    \begin{center}
    \includegraphics[width=0.7\textwidth]{img/#3}
    \caption{
      \label{fig:#3}
      #2 \emph{Source}:#1
    }
    \end{center}
    \end{figure}
\fi
}
% ---
{% raw %}


\usepackage{microtype}
\input{./preamble_steve_paper5}
% \defaultfontfeatures{Ligatures=TeX,Numbers=OldStyle}

%for e reader version: small margins
% (remove all for paper!)
%\geometry{headsep=2em} %keep running header away from text
%\geometry{footskip=1.5cm} %keep page numbers away from text
%\geometry{top=1cm} %increase to 3.5 if use header
%\geometry{bottom=2cm} %increase to 3.5 if use header
%\geometry{left=1cm} %increase to 3.5 if use header
%\geometry{right=1cm} %increase to 3.5 if use header


%avoid overhang
\tolerance=5000



\usepackage{fancyhdr}
\pagestyle{fancy}
\lhead{\footnotesize Geurts \& Butterfill}
%\lhead{\footnotesize \sc}
\rhead{\footnotesize  \emph{ Notes on Folk Pscyhology}}


% do not indent paragraphs, increase space between them.
% \setlength{\parindent}{0cm}
% \setlength{\parskip}{5.5pt}
\usepackage{parskip}


\begin{document}

\setlength\footnotesep{1em}

%screws up word count for some reason:
\bibliographystyle{./mynewapa} %apalike

\date{ Monday, 14th November 2022 } %anon submit
\maketitle







In 1958 Heider published a book on what he called `naive psychology' and, interchangeably, `commonsense psychology'; now more commonly referred to as folk psychology. Although widely ignored,\footnote{The work is not cited in an recent collection of some of the best work on folk psychology \citep{hutto:2007_folk}; nor does Dennett, who claims to have introduced the term `folk psychology' \citep[pp.~73--74]{dennett:2014_intuition}, mention Heider's book. We have not seen it cited in any work on folk psychology.} no comparably detailed work on folk psychology has yet appeared.

Heider's overall aim is to advance `{[}t{]}he scientific study of interpersonal relations' or, as we say, social interactions \citep[p.~3]{heider:1958_psychology}. He views naive psychology as having a central role in achieving this aim.

Heider offers two ways of characterising naive psychology. On the first,

\begin{quote}
`the unformulated or half-formulated knowledge of interpersonal relations as it is expressed in our everyday language and experience {[}\ldots{]} will be referred to as common-sense or naive psychology' \citep[p.~4]{heider:1958_psychology}
\end{quote}

Like subsequent authors (including \citet[p.~140]{clark:1987_folk} and \citet[pp.~73--74]{dennett:2014_intuition}), Heider makes an analogy with naive physics:

\begin{quote}
`In the same way one talks about a naive physics which consists of the unformulated ways we take account of simple mechanical laws in our adapted actions, one can talk about a ``naive psychology'' which gives us the principles we use to build up our picture of the social environment and which guides our reactions to it.' \citep[p.~5]{heider:1958_psychology}
\end{quote}

What is the role of naive psychology in advancing the scientific study of interpersonal relations? Heider thinks of naive psychology as `unsurpassed for the description of even the most subtle relationships'. But science requires systematicity, which naive psychology lacks. Heider's project is therefore to provide:

\begin{quote}
`suggestions {[}drawing on both naive and scientific psychology{]} for the construction of a language that will allow us to represent, if not all, at least a great number of interpersonal relations, discriminated by conventional language in such a way that their place in a general system will become clearer.' (p.~9)
\end{quote}

Heider characterises the same work as offering:

\begin{quote}
`a preliminary approach to an analysis of basic components of our naive ideas about other people and social situations.' (p.~18)
\end{quote}

Heider is explicit that systematising naive psychology is one way of understanding social interaction:

\begin{quote}
`our main purpose is to make explicit the system of concepts that underlies interpersonal behavior' \citep[pp.~12]{heider:1958_psychology}
\end{quote}

In what sense does a system of concepts `underlie' interpersonal behaviour? As Heider specifies a `program for describing interpersonal relations' (p.\textasciitilde14), we might be tempted to construe \emph{underlying} something as merely a matter of being sufficient to provide a systematic description of it. Heider does, however, endorse a stronger thesis:

\begin{quote}
`The general features of the causal network are thus in some way internalized and mastered. They form the content of the cognitive matrix that underlies our interpretations of other people's behavior and our attempts to influence it.' \citep[pp.~297--8]{heider:1958_psychology}
\end{quote}

We can therefore regard Heider as responsible for introducing and defending three theses:

\begin{enumerate}
\def\labelenumi{\arabic{enumi}.}
\item
  `there is a system hidden in our {[}ordinary, everyday{]} thinking about interpersonal relations, and {[}\ldots{]} this system can be uncovered' (p.\textasciitilde14)
\item
  Uncovering this system enables us to describe interpersonal relations in a systematic, scientific way.
\item
  Humans' capacities to interact with others depend, in part\footnote{The system is suppose to show `only a part of what is going on between people, that part which, let us say, inclines toward the side of ``intellectualism.'' To complete the picture one would have to add other facets, for instance, one would have to give an account of the genetic sources of interpersonal behavior' \citep[p.~298]{heider:1958_psychology}.}, on them having `internalized and mastered' this system.
\end{enumerate}

How should `hidden' and `uncovered' in the first thesis be understood? Maybe the thinking contains only the slightest glimmers which provide inspiration and `uncovering' is imaginative construction, so that ethnography would be irrelevant to uncovering the system. In this case, there may be a large gap between naive psychology and the psychological bases of capacities for social interaction. Or maybe the uncovering should be understood as merely tidying up to reveal things that are already present but not easy to see. In that case, we could interpret Heider as committed to the claim that implicit knowledge of naive psychology just is a psychological basis of capacities for social interaction. We are pushed towards the second possibility by Heider's stress throughout on `analyzing the data through which our beliefs are revealed' \citep[p.~60]{heider:1958_psychology}. To illustrate, Heider's discussion of enabling conditions for perception is clearly presented as a case of tidying up what is already assumed in ordinary thought and talk about perceiving:

\begin{quote}
`to study the cognitions and actions directed toward the perceptions of another person, we have to explore our beliefs regarding the conditions and effects of perception. {[}\ldots{]} The common-sense assumptions about the conditions that make it possible for one person to recognize what another is perceiving are for the most part implicit. If people were asked about these conditions they probably would not be able to make a complete list of them. Nevertheless, these assumptions are a necessary part of interpersonal relations; if we probe the events of everyday behavior, they can be brought to the surface and formulated in more precise terms.' \citep[p.~60]{heider:1958_psychology}
\end{quote}

It seems safe to say that Heider views social interaction as made possible by the internalization and mastery of a system which can be characterised by tidying up naive psychology. This is confirmed by a second characterisation of naive psychology:

\begin{quote}
`naive psychology, the pretheoretical and implicit system which underlies interpersonal relations.' \citep[p.~58]{heider:1958_psychology}\footnote{In terms of the distinction introduced by \citet{stich:1994_whata}, Heider's first characterisation is folk psychology in the `external' sense whereas Heider's second characterisation is folk psychology in the `internal' sense.}
\end{quote}

Treating as equivalent the two ways of characterising naive psychology presupposes what we will call \emph{Heider's Thesis}:

\begin{quote}
\emph{Heider's Thesis} {[}broad version{]} All capacities for social interaction depend on representing commonsense psychological principles and making inferences from them.\footnote{In \citet{stich:1994_whata}'s terms, Heider's Thesis is roughly that internal folk psychology is external folk psychology. Because Stich and Ravenscroft (pp.\textasciitilde457--8) are concerned with a narrow set of social interactions than Heider, Heider's Thesis is a stronger claim.}
\end{quote}

According to \citet[p.~3]{molder:2016_mind}, `some philosophers and psychologists assume that our implicit grasp of folk psychology is the very thing that makes social cognition possible.' We take this to be endorsement of Heider's Thesis.

In case this thesis seems too obvious to be even worth formulating, consider some views which contradict it or at least justify considering whether it is true:

\begin{enumerate}
\def\labelenumi{\arabic{enumi}.}
\item
  There are no commonsense psychological principles (we take this view to be refuted by Heider's work).
\item
  Multiple, incommensurable systems of principles can be uncovered in commonsense thinking about social interactions (compare \citealp{stich:1994_whata}).
\item
  Commonsense psychological principles provide limited insight into social interactions (perhaps because their role is not only explanatory but also regulatory \citep{mcgeer:2007_regulative,zawidzki:2013_mindshaping} or normative).
\item
  Commonsense psychological principles vary more between cultures than do capacities for social interaction (compare \citealp{lillard:1998_ethnopsychologies}).
\item
  Human share capacities for social interaction with other animals that do not represent commonsense psychological principles.
\item
  Adults share capacities for social interaction with infants but infants do not represent commonsense psychological principles.
\end{enumerate}

One response to the last two views would be to retreat to a narrower version of Heider's Thesis:

\begin{quote}
\emph{Heider's Thesis} {[}narrow version{]} Capacities for social interaction involving communication about psychological things depend on representing commonsense psychological principles and making inferences from them.\footnote{\citet[p.~5]{molder:2016_mind} regards the narrow version as too obvious to need argument: `I will understand `folk psychology' primarily in the sense of a conceptual framework that includes certain familiar psychological terms as well as the links between them. Of course, this framework is put to practical use when we attribute mental states to others in order to make sense of their action}
\end{quote}

As \citet{stich:1994_whata} argue, even this weaker thesis is far from obvious.

\hypertarget{a-distinction}{%
\subsection{A Distinction}\label{a-distinction}}

We distinguish:

\begin{enumerate}
\def\labelenumi{\arabic{enumi}.}
\item
  commonsense principles---these are principles that are already present but not easy to see in everyday social interactions involving communication about psychological things;
\item
  implicit principles---these are principles whose truth would justify patterns of social interaction; they characterise how aspects of the world would have to be in order for social interactions to be successful or beneficial; and
\item
  internalized principles---in explaining aspects of agents' capacities for social interaction we may need to postulate representations; the internalized principles are those that enable us to identify what these representations are of.\footnote{We avoid insisting that agents represent internalized principles as we are agnostic on hardware implementation (compare \citealp{churchland:1989_folk}). In \citet{Marr:1982kx}'s terms, internalized principles are those which contribute to a computational description of capacities for social interaction.}
\end{enumerate}

Heider's Thesis entails that (3) coincides with, or is a subset of, (1).

\hypertarget{potential-opposition-to-heiders-thesis}{%
\subsection{Potential Opposition to Heider's Thesis}\label{potential-opposition-to-heiders-thesis}}

\hypertarget{stich-and-ravenscroft}{%
\subsection{Stich and Ravenscroft}\label{stich-and-ravenscroft}}

Although not their primary concern, by distinguishing \emph{internal} and \emph{external} notions of folk psychology they draw attention that the Thesis is a substantial claim \citet{stich:1994_whata}.

\hypertarget{gallese}{%
\subsection{Gallese}\label{gallese}}

\citet[p.~659]{gallese:2007_theory} opposes unargued acceptance of it:

\begin{quote}
`A growing sense of discomfort towards a blind faith in folk psychology to characterize social cognition is indeed surfacing within the field of philosophy of mind.'
\end{quote}

\begin{quote}
`the automatic translation of the folk psychology-inspired `flow charts' into encapsulated brain modules, specifically adapted to mind-reading abilities, should be carefully scrutinized. Language can typically play ontological tricks by means of its `constitutiveness'; that is, its capacity to give an apparent ontological status to the concepts words embody (Bruner 1986, p.~64).' \citep[p.~667]{gallese:2007_theory}
\end{quote}

\hypertarget{bermuxfadez}{%
\subsection{Bermúdez}\label{bermuxfadez}}

`the centrality of folk psychology in explaining what makes social interactions possible has rarely been challenged' \citep[p.~26]{bermudez:2003_domain}

`Granted that we sometimes do make reflective and explicit use of the concepts of folk psychology in making sense of the behaviour of others, should we conclude that our unreflective social understanding involves an implicit application of the concepts of folk psychology in the interests of explanation and prediction? Should we conclude that all our social understanding involves deploying the concepts and explanatory/predictive practices of folk psychology?' \citep[p.~27]{bermudez:2003_domain}

`According to the narrow construal, the domain of folk psychology should not be presumed to extend further than those occasions on which we explicitly and consciously deploy the concepts of folk psychology in the services of explanation and/or prediction. At the other end of the spectrum lies the broad construal, which makes all social understanding a matter of the attribution of mental states and the deployment of those attributed states to explain and predict behaviour.' \citep[p.~27]{bermudez:2003_domain}

Thesis: `one can act effectively in complicated social interactions without bringing to bear the explanatory and predictive apparatus of folk psychology' \citep[p.~42]{bermudez:2003_domain}

Key consideration for narrow view: `Sensitivity to emotional states feeds directly into action without any attribution of emotional states.' \citep[p.~38]{bermudez:2003_domain}

\hypertarget{pickering-and-chater}{%
\subsection{Pickering and Chater}\label{pickering-and-chater}}

This is a bit of a tangent (focus is on explaining cognition generally, not social cognition specifically):

\begin{quote}
`folk psychology applies to ``knowledge-rich'' aspects of cognition, which have proved completely unamenable to cognitive science, whereas cognitive science has been limited to ``knowledge-free'' aspects of cognition, about which folk psychology is silent.' \citep[p.~311]{pickering:1995_why}
\end{quote}

\begin{quote}
`The intractability of formalizing folk psychology explains why there has been a singular lack of success in attempting to provide a cognitive science of knowledge-rich mental processes; and why cognitive science has succeeded only by focusing on knowledge-free aspects of cognition, with which folk psychology is not concerned.' \citep[p.~312]{pickering:1995_why}
\end{quote}

\hypertarget{morton}{%
\subsection{Morton}\label{morton}}

Indirectly relevant: \citet{morton:2007_folk} argues for `the non-existence of folk psychology, as a single unitary capacity'.

\hypertarget{mcgeer-zawidzki}{%
\subsection{McGeer / Zawidzki}\label{mcgeer-zawidzki}}

\citet[p.~194]{zawidzki:2008_function}:

\begin{quote}
`I shall argue that the raison d'eˆtre of this practice {[}folk psychology{]} cannot be providing accurate representations of our fellows' mental states that support accurate predictions of their behavior. Rather, its raison d'eˆtre is more likely shaping our fellows' minds, in order to make coordination with them easier.'
\end{quote}

See also \citet{mcgeer:2007_regulative}.

\hypertarget{relation-to-other-questions}{%
\subsection{Relation to other questions}\label{relation-to-other-questions}}

Our project concerns relations between commonsense, implicit and internalized principles. By contrast philosophers have mostly considered these questions:

\begin{quote}
What are the commonsense psychological principles (Heider; \citealp{davidson:1963_orig}; \citealp{Bratman:1987xw})?
\end{quote}

\begin{quote}
To what extent do the various commonsense, implicit or internalized psychological principles contradict or complement scientific theories? (\citealp{churchland:1989_folk}; \citealp{Dennett:1991hr}; \citealp{Fodor:1987rt}; \citealp{hornsby:1997_simple})
\end{quote}

\begin{quote}
Do the internalized psychological principles constitute a theory?
\end{quote}

\begin{quote}
{[}Any missing?{]}
\end{quote}

\hypertarget{development-and-comparative-applications-of-heiders-thesis}{%
\subsection{Development and Comparative Applications of Heider's Thesis}\label{development-and-comparative-applications-of-heiders-thesis}}

The broad version of Heider's Thesis is presupposed by a body of comparative and developmental research. You can use Heider's Thesis to get from `individuals of this kind exhibit a certain capacity social interaction' to `individuals of this kind represent the corresponding folk psychological principles'.

Further, the thesis is confounded with the weaker view that certain social interactions depend on representing psychological principles though not necessarily \emph{folk} principles. One aim of what follows is to separate these views.










\printglossaries

%does latex not find bibliography file? Use `export "BIBINPUTS=~"`
\bibliography{endnote/phd_biblio}
\end{document}


