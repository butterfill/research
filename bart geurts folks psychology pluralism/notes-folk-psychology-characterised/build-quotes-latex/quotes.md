%!TEX TS-program = xelatex
%!TEX encoding = UTF-8 Unicode

%\def \papersize {a5paper}
\def \papersize {a4paper}
%\def \papersize {letterpaper}

%\documentclass[14pt,\papersize]{extarticle}
\documentclass[12pt,\papersize]{extarticle}
% extarticle is like article but can handle 8pt, 9pt, 10pt, 11pt, 12pt, 14pt, 17pt, and 20pt text

\def \ititle { Notes on How Folk Psychology   : How It’s Characterised }
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
\rhead{\footnotesize  \emph{ Notes on How Folk Psychology}}


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







Here we are just interested in how researchers characterise folk psychology.

(TODO: move the sections on Bermudez \& Gallese)

\hypertarget{encyclopedia-articles-textbooks-introductions}{%
\subsection{Encyclopedia articles, textbooks, introductions}\label{encyclopedia-articles-textbooks-introductions}}

\citet[pp.~73--74]{dennett:2014_intuition} claims to have introduced the term ``folk psychology'':

\begin{quote}
`I proposed folk psychology as a term for \textbf{the talent} we all have for interpreting the people around us---and the animals and the robots and even the lowly thermostats---as agents with information about the world they act in (beliefs) and the goals (desires) they strive to achieve, choosing the most reasonable course of action, given their beliefs and desires. {[}\ldots{]} Folk physics then, in parallel fashion, is the talent we have for expecting liquids to flow, unsupported things to drop, hot substances to burn us, water to quench our thirst, and rolling stones to gather no moss. {[}\ldots{]} Folk psychology is \textbf{``what everyone knows''} about their minds and the minds of others {[}\ldots{]} It is \textbf{like an idealized model} in science---maximally abstract and stripped down to the essentials' (first part is quoted in \citep[p.~3]{molder:2016_mind}).
\end{quote}

Interesting that Dennett characterises folk psychology both as a talent and as an object of knowledge.

\citet[p.~54]{davies:1998_folk} characterise folk psychology as a practice rather than an object of knowledge:

\begin{quote}
`What should we mean by this term ``folk psychology''? {[}\ldots{]} Instead of beginning with folk psychology as what the folk know or believe about psychology, we do better to start with folk psychological practice---a practice in which we all engage on an everyday basis. We describe people as bearers of psychological states. We explain people's behaviour (or decisions, or judgements or other psychological states) by appeal to their psychological states. We predict people's behaviour (or decisions, or judgements or other psychological states) by relying on assumptions about their psychological states.'
\end{quote}

This characterisation of folk psychology as a practice matches \citet[p.~14]{kim:2019_philosophy} \ldots{}

\begin{quote}
`our ordinary psychological thinking and theorizing (``folk psychology'')'
\end{quote}

\ldots{} and \citet[p.~25]{bermudez:2003_domain}:

\begin{quote}
`I shall use the expression ``folk psychology'' in what I take to the standard way---namely, as picking out certain practices of ascribing propositional attitudes (and other mental states) to other agents and explaining/predicting their behaviour on the basis of those attributions.'
\end{quote}

\citet[p.~2]{molder:2016_mind} distinguishes three notions (and on p.\textasciitilde5 opts for the last of these):

\begin{quote}
`In the weakest sense, one can say that folk psychology is just the practice of attributing mental states to other people. Somewhat more substantially, ``folk psychology'' can be taken to mean the ability to understand others' behavior in terms of mental states. \ldots{} Third, ``folk psychology'' might mean merely the commonsense conceptual framework that comprises the mentalistic terms used in the folk practice.'
\end{quote}

Churchland also goes for the third of these notions:

\begin{quote}
`\,``folk psychology'' denotes the prescientific, common-sense conceptual framework that all normally socialized humans deploy in order to comprehend, predict, explain, and manipulate the behaviour of humans and the higher animals.' (Churchland 1994, 308) quoted by \citep[p.~4]{molder:2016_mind}
\end{quote}

Some characterise folk psychology as theory of mind:

\begin{quote}
`we have a common-sense theory of mind, or a ``folk psychology'', which implicitly defines ordinary psychological concepts' \citep[p~10]{botterill:1999_philosophy} --- their key contrast is between folk and scientific psychology.
\end{quote}

The same folk psychology = theory of mind equation is offered in one of the two SEP articles with folk psychology in the title:

\begin{quote}
`The capacity for ``mindreading'' is understood in philosophy of mind and cognitive science as the capacity to represent, reason about, and respond to others' mental states. Essentially the same capacity is also known as ``folk psychology'', ``Theory of Mind'', and ``mentalizing''.
\end{quote}

\begin{quote}
`An example of everyday mindreading: you notice that Tom's fright embarrassed Mary and surprised Bill, who had believed that Tom wanted to try everything.
\end{quote}

\begin{quote}
`Mindreading is of crucial importance for our social life: our ability to predict, explain, and/or coordinate with others' actions on countless occasions crucially relies on representing their mental states.' \citep{barlassina:2017_folk}
\end{quote}

The other SEP article states:

\begin{quote}
`Folk psychology is a name traditionally used to denote our everyday way of understanding, or rationalizing, intentional actions in mentalistic terms.' \citep{hutto:2021_folk}
\end{quote}

\citet[p.~659]{gallese:2007_theory}:

\begin{quote}
`humans are able to understand the behaviour of others in terms of their mental states-----intentions, beliefs and desires-----by exploiting what is commonly designated as ``folk psychology''\,'
\end{quote}

\citet{andrews:2020_introduction} offer a broader definition:

\begin{quote}
`\,``Folk psychology'' refers to the way that ordinary people come to understand and navigate the social world around them. {[}\ldots{]} Pluralistic folk psychology presents a new way of thinking about social cognition. Its central thesis is that folk psychology involves a variety of strategies and goals. On this view, terms like mindreading, mentalizing, and theory of mind refer to more strategies than just propositional attitude attribution, and are used for goals beyond behavior prediction and explanation.'
\end{quote}

\hypertarget{things-written-about-folk-psychology}{%
\subsection{Things written about folk psychology}\label{things-written-about-folk-psychology}}

\citet[p.~110]{kim:2019_philosophy} claims that it's universal

\begin{quote}
`if there were a culture, past or present, for whose members the central principles of our folk psychology, such as the one that relates belief and desire to action, did not hold true, its institutions and practices would hardly be intelligible to us, and its language would be untranslatable into our own. {[}\ldots{]} it seems clear that folk psychology enjoys a degree of stability and universality that eludes scientific psychology.'
\end{quote}

\citet[p.~227]{churchland:1989_folk} on laws:

\begin{quote}
`thorough perusal of the explanatory factors that typically appear in our commonsense explanations of our internal states and our overt behavior sustains the quick 'reconstruction' of a large number of universally quantified conditional statements, conditionals with the conjunction of the relevant explanatory factors as the antecedent and the relevant explanandum as the consequent. It is these universal statements that are supposed to constitute the `laws' of folk psychology.'
\end{quote}

\hypertarget{books-or-articles-on-folk-psychology}{%
\subsection{Books or articles on folk psychology}\label{books-or-articles-on-folk-psychology}}

`Folk psychology is supposed to be the means by which people in ordinary life understand the minds of other people.' \citep[p.~211]{morton:2007_folk}

`We have evolved, biologically and culturally, to be able to attribute states of mind, to be able to have and use folk psychology. And we are this way because we are social creatures; we have a very particular kind of sociality, in fact, which makes most of our activities cooperative while forcing us to manage them by a mixture of reasoning, social shaping, and imagination, without very many innate social routines.' \citep[p.~119]{Morton:1996gu}

`People don't merely go through the world acting or behaving or responding. They also cognize about those actions, behaviors, and responses. In particular, they attempt to understand, explain, and predict their own and others' psychological states and overt behavior by making use of an array of ordinary psychological notions. I shall refer to these cognitive efforts as our folk psychological practices and to the concepts we employ in engaging in these folk psychology practices as our folk psychological concepts.' \citep[p.~24]{voneckardt:1997_empirical} --- Note that \citet[footnote 3, p.~29]{voneckardt:1997_empirical} goes on to identify folk psychology with \emph{ordinary explanatory psychology}, `the psychology which ordinary people use to predict, explain, and understand their own and each other's behavior' \citep[p.~28]{voneckardt:1997_empirical}.

`our everyday practices of psychological description, explanation, and prediction -- practices often referred to as folk psychology' \citep[p.~1]{frankish:2007_mind} Qualification: `The term ``folk psychology'' is often used to refer to the putative theory underpinning our everyday practices of psychological explanation and prediction, as well as to the practices themselves. To avoid confusion, I shall use the term only in its broader sense, to refer to the practices.' \citep[footnote 1 to p.~1]{frankish:2007_mind}

`In our everyday dealings with one another we invoke a variety of commonsense psychological terms including 'believe', `remember', `feel', `think', `desire', `prefer', `imagine', `fear', and many others. The use of these terms is governed by a loose knit network of largely tacit principles, platitudes, and paradigms which constitute a sort of folk theory. Following recent practice, I will call this network folk psychology.' \citep[p.~1]{stich:1983_folk}

`folk psychology or ``theory of mind,'' the understanding of others as psychological beings having mental states such as beliefs, desires, emotions, and intentions' \citep[p.~838]{meltzoff:1995_understanding}

`Folk psychology is a network of principles which constitutes a sort of common-sense theory about how to explain human behavior.' \citep[p.~197]{horgan:1985_folk}

`Folk psychology, by contrast, is the unscientific understanding of the mind as possessed by, for want of better terms, laypeople or folk---people with no special training in the formal academic or scientific study of the mind. {[}\ldots{]} the term ``folk psychology'' mirrors the term `folk physics,' which similarly distinguishes the putatively commonsensical theory of physics ubiquitous among laypeople from the kind of physics taught in formal academic settings.' \citep[p.~23]{hartner:2016_folk} --- `the lay capacity designated by the term ``folk psychology'' actually consists of two related activities: the primary act of mindreading, and the closely associated linguistic practice of description that may well reveal something about that primary behavior' \citep[p.~24]{hartner:2016_folk}

`I take folk psychology to be the basis---whatever it is---of our ability to describe, interpret, and predict each other by attributing beliefs, desires, hopes, feelings, and other familiar mental states.' \citep[p.~1]{godfrey-smith:2005_folk}

`a folk psychology or ``theory of mind'' (ToM)--- the conceptual framework of propositional attitudes with which we describe and explain each other' \citep[p.~2]{rakoczy:2015_defense}.

`Numerous motives, ranging from self-preservation to simple curiosity, impel people the world over to try to make sense of themselves and other people, and doing that requires a folk psychology.' \citep[p.~13]{flavell:2004_development} {[}folk psychology as the thing that enables the understanding{]}

`the cognitive capacities that underlie such social interactions. The capacity to understand and interact with other agents is called folk psychology' \citep[p.~1]{spaulding:2018_how}

`In giving such an explanation we would be indulging in what has become known as folk-psychology. For we would be using a certain theory of the mental (viz.~one which appeals to combinations of beliefs and desires to explain actions) to make sense of other people's behaviour.' \citep[p.~139]{clark:1987_folk} \ldots{} `Whilst accepting that folk-psychology constitutes a kind of primitive theory of the mental, I shall attempt to deny that that theory need be thought of as mere folk speculation. Instead, I suggest that we should accord our common-sense ideas of the mental something of the status we accord our common-sense conceptions of the physical. I thus propose that we talk not of folk-psychology but of naive psychology where this is conceived along the lines of Hayes' (1979) notion of a naive physics. The general argument in favour of this conjecture will be that just as a roughly accurate grasp of some basic physical principles is vital to a mobile organism, so too will some roughly accurate grasp of basic psychological principles be vital to a social organism.' \citep[p.~140]{clark:1987_folk}

``Folk psychology stricto sensu . . . the practice of making sense of a person's actions using belief/desire propositional attitude psychology' (Hutto 2008, 3, original emphasis).' \citep[p.~194]{zawidzki:2008_function}

`a widely shared commonsense psychological theory -- ``folk psychology'' as it is often called. Folk psychology, the Premise maintains, underlies our everyday discourse about mental states and processes, and terms like ``belief'' and ``desire'' can be viewed as theoretical terms in this folk theory.' \citep{stich:1996_deconstructing}

`The term ``folk psychology'' is employed in philosophy and cognitive science to mean our commonsense, everyday ability to understand each other and negotiate the social world.' \citep[p.~31]{ratcliffe:2006_folk}

\hypertarget{helen-steward}{%
\subsection{Helen Steward}\label{helen-steward}}

\citet{steward:2012_metaphysics} combines:

\begin{enumerate}
\def\labelenumi{\arabic{enumi}.}
\tightlist
\item
  a priori or informal observation approach to folk psychology
\item
  strong claims about folk psychological commitments
\item
  reliance on premises about folk psychology to support conclusions about metaphsyics
\end{enumerate}

`According to folk psychology, weakness of will is, sadly, an all-too-common phenomenon'\citep[p.~147]{steward:2012_metaphysics}

`The need for folk psychology, I shall insist, arises out of the fact that the settling of matters by animals genuinely is a very special form of causation indeed, so that it is not at all surprising that evolution has endowed us with specialized cognitive systems for its discernment.' \citep[p.~106]{steward:2012_metaphysics}

`The mental states are simply not thought of by our folk psychology, I maintain, as independent causally efficacious entities. They are thought of rather as features of a substantive entity---an agent---which must act if any bodily movement is to result from its desires and beliefs and whose actions are thought of as explicable by appeal to, but not as deterministically caused by, those desires and beliefs.' \citep[p.~77]{steward:2012_metaphysics}

\citet[p.~71--2]{steward:2012_metaphysics} features of `a mature conception of agency' = agents as centers of subjectivity etc \ldots{}

`it seems so utterly obvious to me that folk psychology involves a commitment to the existence of agents whose exertions are required if anything is ever to be done, and which exertions are conceptualized by us as bearing only indeterministic relationships to their causal antecedents, so that they are spontaneous inputs into the course of nature, that I find it hard to know how to argue for it \ldots{} Is there any way of establishing empirically, for instance, that folk psychology really does conceive of agents in the way I have suggested it does?' \citep[p.~97]{steward:2012_metaphysics} (Potential counter?: `In Japanese, the person is lexicalized as ``a location in which the act takes place'' \citep[p.~314]{ikegami:1991_language}. In contrast, in English, the person is a clearly identified agent, the source of action.' \citep{lillard:1998_ethnopsychologies}; `In contrast to the English tendency to emphasize the notion of agentivity, Japanese has a way of weakening or even effacing the notion. One linguistic means serving this purpose is the 'locationalization' of the agent, that is, the agent is not represented as a person who acts, but as a location in which the act takes place. {[}\ldots{]} Sentence (67) literally means Tn the Emperor, (it) became (to) the planting of rice seedlings' or somewhat more idiomatically, Tn the Emperor, the planting of rice seedlings came to pass.' The Emperor is de­ prived of all his agentivity --- `de-agentivized' as it were --- and the event is represented not in terms of someone DOing something, but in terms of something coming to pass --- BECOMing something.' \citep[p.~147]{ikegami:1991_language}; could also consider \citep{yamamoto:2006_agency})

`Substantial portions of folk psychology, I shall suggest, are meant to be for animals, too.' \citep[p.~85]{steward:2012_metaphysics}

`I think it must be seriously doubted whether anything still recognizable as folk psychology can tolerate the very different idea that all reasons may be quantitatively weighed against one another in such a way that a determinate outcome is necessitated by these in-principle antecedently attributable relative weightings.' \citep[p.~147]{steward:2012_metaphysics}










\printglossaries

%does latex not find bibliography file? Use `export "BIBINPUTS=~"`
\bibliography{endnote/phd_biblio}
\end{document}


