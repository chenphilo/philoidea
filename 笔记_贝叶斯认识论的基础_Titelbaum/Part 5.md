## 11. Memory Loss and Self-locating Credences

### 11.1 Memory loss
----

> if I am assumed to satisfy Temporal Conditionalization at every time from t1 to t2, it must be the case that I be as certain of S at t2 as I was at t1.

假设S表示“我在1989-5-15晚饭吃肉夹馍”，事实确实如此。我会在任何时候更新为确信度1，但如果我忘记这件事，则会可能根据某段时间频率推测，则违背条件化更新。
- R: Bayesian epistemology describe the doxastic behavior of an **ideally rational agent**
  - whether an agent would in some sense be more perfect were she to permanently retain information

**Shangri La** (Frank Arntzenius 2003, p. 356)
> There are two paths to Shangri La, the Path by the Mountains, and the Path by the Sea. A fair coin will be tossed by the guardians to determine which path you will take: if heads you go by the Mountains, if tails you go by the Sea. Ifyou go by the Mountains, nothing strange will happen: while traveling you will see the glorious Mountains, and even after you enter Shangri La, you will forever maintain your memories of that Magnificent Journey. If you go by the Sea, you will revel in the Beauty of the Misty Ocean. But, just as you enter Shangri La, your memory ofthis Beauteous Journey will be erased and be replaced by a memory of the Journey by the Mountains.  (at t1 the guardians of Shangri La have just explained this arrangement to you)

- 硬币还没抛，对正面： $cr_1 (H) = \frac{1}{2}$
- 在海上 $cr_2 (H) = 0$
- 到达香格里拉 $cr_3 (H) = \frac{1}{2}$

A theorist who holds that any loss of memory is a rational failing will see no counterexample to Conditionalization here. But:
- 在山上 $cr_2 (H) = 1$
- 到达香格里拉 $cr_3 (H) = \frac{1}{2}$

In the Shangri La story it’s rational to violate Conditionalization not only when you suffer memory loss, **but also when you merely suspect that you may have forgotten something.**

#### A possible solution

用 **Hypothetical Representability** 代替 Conditionalization 作为贝叶斯动态更新原则。

Given any finite series ofcredence distributions $\{cr_1, cr_2,\dots, cr_n\}$ that the agent assigns over time, there exists at least one regular probability distribution $Pr_H$ such that for all $1\leq i\leq n$,
$$cr_i (\cdot) = Pr_H (\cdot |E_i)$$

- Hypothetical Priors Theorem told us that any agent who conditionalizes is representable by a hypothetical prior. But the converse of that theorem is false.
- in which an agent loses no information — Hypothetical Representability yields the same results as Conditionalization.
- reverse temporal conditionalization: an agent's credence at the **earlier time** equals her credence at the **later time** conditional on the evidence she **loses** between those two times. 
- Suppose that between times $t_j$ and $t_k$, an agent gains a body of evidence representable by the conjunction $E$, but loses evidence representable by the conjunction $D$: 
  $$Cr_k(H|D) = Cr_j(H|E)$$

- Dutch Strategies
- diachronic accuracy arguments

#### Suppositional Consistency

an agent's credences are representable by a hypothetical prior, then at any two times at which her total evidence is the same, her credences must be the same as well. **Why might rationality require an agent to maintain the same epistemic standards over time?**
- Objective Bayesian: Uniqueness Thesis, of course
- Subjective Bayesian: Dutch Strategy arguments
  - holds only when agent's evidence remains constant across times
  - a Dutch Strategy argument may establish that it’s rational to **plan** to update in a particular fashion, it can't establish the **diachronic principle** that an agent is rationally required at a later time to do what she planned earlier on.
  
Proof (?): Hypothetical Representability $\Rightarrow$ Suppositional Consistency

**Suppositional Consistency**: Given any propositions $A$, $B$, and $C$ in $\mathfrak{L}$, 
$$Cr_A(B|C) = Cr_C(B)$$
If you're suppositionally consistent over time, then whenever the conjunction of your evidence and your suppositions comes to the same thing, you'll assign the same credence to a given proposition.
-  treating supposed and real evidence symmetrically

If rationality requires agents to keep their ultimate **epistemic standards constant**, and those epistemic standards are also required to be **suppositionally consistent**, then **Hypothetical Representability** is a requirement of rationality.

Sum: The traditional Bayesian Conditionalization norm makes rational agents representable by a hypothetical prior, but also forbids them to lose information. Yet it's possible to satify Hypothetical Representability over a period of time even if evidence is sometimes lost during that period. To do so, an agent must keep the same epistemic standards throughout, and those epistemic standards must satisfy Suppositional Consistency.

----
### 11.2 Self-locating credences
----
**Sleeping Beauty Problem**
> Some researchers are going to put you to sleep. During the two days that your sleep will last, they will briefly wake you up either once or twice, depending on the toss of a fair coin(Heads: once; Tails: twice). After each waking, they will put you back to sleep with a drug that makes you forget that waking. When you are first awakened, to what degree ought you believe that the outcome ofthe coin toss is Heads?

#### The problem
Traditional possible worlds don't provide enough information to settle the truth-values ofpropositions like its now 1 p.m. The most common response to this problem, following in the tradition of David Lewis(1979), is to augment traditional possible worlds by adding **centers** to them. Given a traditional possible world, a center picks out a particular individual at a particular time and place within that world. **An ordered pair of a world and a center** in it is then called a **centered possible world**. (The traditional possible worlds without centers are called **uncentered worlds**. )
- But **Conditionalization** also retains certainties, so if I keep conditionalizing, I will remain certain of that centered proposition. Yet this may not be rational.
- Namjoong Kim(2009) argues that **Jeffrey Conditionalization** doesn’t interact well with self-location either.

#### The HTM approach
Halpern (2004, 2005), Meacham (2008).
1. Suppose that between times $t_i$ and $t_j$, an agent gains evidence $E$. Her first updating step is to redistribute her credence over uncentered worlds by conditionalizing.
2. The agent now has to distribute her credences over the centered worlds associated with **each of the remaining uncentered worlds**.

Q: Now that we know how the HTM approach works, how can we tell if it's a rational procedure for updating self-locating credences?

- Dutch Strategy or accuracy-based arguments:
  - Briggs (2010) argues that which Dutch Strategy and which accuracy argument you accept for Sleeping Beauty should depend on whether you endorse **Causal or Evidential Decision Theory**.
  - I don’t think Dutch Strategy or accuracy-based arguments are going to adjudicate the Sleeping Beauty Problem any time soon.
- **Relevance-Limiting Thesis**: If an update doesn’t eliminate any uncentered possible worlds, then it does not change the agents credence distribution over uncentered propositions.
  - mystery bag example
    > Ten people are arranged in a circle in a cylindrical room. One of them is you. You have no qualitative way of distinguishing yourselffrom the others in the room—you are all dressed alike, you all look identical, and you have no memories ofanything that happened before this moment. (You don’t even knowyour own name!) Your onlyway ofpickingyourselfout uniquelyamong the members of the room is with indexical expressions(“me”, “the person currently having this thought”, etc. ). A fair coin is flipped to determine the contents of a bag. If the coin comes up heads, the bag will contain nine black balls and one white ball. Ifthe coin comes up tails, the bag will contain one black ball and nine white balls. You do not receive any direct information about the outcome ofthe coin flip, but once the bag is filled it is passed around the room. Each person draws out one ball and passes the bag until the bag is entirely empty. You cannot see the ball anyone else has drawn, but your ball is black.
    - according to the Relevance-Limiting Thesis, picking a black ball should not change your credence in heads versus tails. Yet intuitively, observing a black ball should dramatically increase your confidence in heads.

- A simple fix: restrict the applicability of the HTM approach: only when the following condition is met: At each time under consideration, for each centered proposition P, the agent has an uncentered proposition P' which she is certain forms a true biconditional: $P\leftrightarrow P'$.
  - mystery bag example: this condition fails for the centered proposition ``I pick a black ball."
  - Sleeping Beauty: lacks any uncentered proposition that she's certain has the same truth-value as ``Today is Tuesday."