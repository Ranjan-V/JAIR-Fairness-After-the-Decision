# Novelty and literature audit

Audit date: 2026-09-26  
Scope: primary papers and publisher/proceedings records located through focused
searches on algorithmic contestability, appeals, recourse fairness,
machine-assisted human decisions, selective labels, partial identification,
and fairness auditing. This is a defensible positioning audit, not proof of
priority or an exhaustive systematic review.

## Decision

The project's narrow contribution remains defensible, but no “first work”
claim is warranted. The literature already establishes that contestability is
important, that appeal design affects perceived procedural fairness, that
human discretion can change the fairness of machine-assisted decisions, that
recourse costs can differ across groups, and that selective labels create
identification problems. The credible wedge is the combination:

> exact fairness-specific transformations induced by self-selected entry into
> a post-decision human correction channel, linked to endogenous access costs,
> appeal-log partial identification, randomized auditing, and assistance
> allocation.

The operator factorization, generic convex/KKT facts, knapsack reduction, and
generic missing-data concentration are not independently novel. They support
the contestation-specific theory and should not be advertised as standalone
breakthroughs.

## Closest literatures

### Contestability and reviewability

- Kaminski and Urban's *The Right to Contest AI* develops the legal and
  institutional case for an individual right to contest AI decisions, rather
  than a quantitative group-fairness transformation model
  ([Columbia Law Review / SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3965041)).
- Cobbe, Lee, and Singh frame reviewability as a socio-technical record-keeping
  and accountability property spanning the full decision process
  ([FAccT 2021](https://arxiv.org/abs/2102.04201)).
- Lyons, Velloso, and Miller map competing meanings of contestability
  ([arXiv:2103.01774](https://arxiv.org/abs/2103.01774)); Lyons et al. then
  study preferences over review-process design, participation, reviewer, and
  timeliness ([CHI 2022](https://dl.acm.org/doi/10.1145/3491102.3517606)).
- Freiesleben, Meding, and König distinguish evidence-based contestability
  from recourse and argue that ordinary explanation methods are insufficient
  for challenging an allegedly incorrect decision
  ([arXiv:2605.16041](https://arxiv.org/abs/2605.16041)).

These works occupy the broad claims that contestability matters, differs from
explanation/recourse, and should be institutionally supported. They do not, in
the sources reviewed, provide the project's exact group-confusion-rate
preservation conditions for self-selected appeals.

### Human–AI decision fairness

- Gillis, McLaughlin, and Spiess show theoretically and experimentally that a
  human decision-maker can reverse familiar relationships between algorithm
  design and ultimate disparities
  ([arXiv:2110.15310](https://arxiv.org/abs/2110.15310)).
- Angelova, Dobbie, and Yang study discretionary overrides of algorithmic bail
  recommendations and find substantial heterogeneity in override quality
  ([NBER Working Paper 31747](https://www.nber.org/papers/w31747)).

These are close motivation and must be cited prominently. The distinction is
that the present model is post-decision, claimant-initiated selection into
review, with latent non-appellant labels and policy acting on access to that
channel—not general human discretion over all algorithm-assisted cases.

### Fair recourse and heterogeneous burden

- von Kügelgen et al. formalize group and individual fairness of causal
  recourse and show that prediction fairness and recourse fairness are
  complementary ([arXiv:2010.06529](https://arxiv.org/abs/2010.06529)).
- Kavouras et al.'s FACTS framework audits subgroup fairness using the
  distribution of recourse costs and effectiveness within a budget
  ([NeurIPS 2023](https://papers.nips.cc/paper_files/paper/2023/hash/b60161e93f3e0e4207081a3b4ef5e8d8-Abstract-Conference.html)).

This literature substantially overlaps the heterogeneous-cost motivation and
CDF language. The paper must distinguish changing features to obtain a future
model decision from supplying evidence/access to correct an already-issued
decision. Theorem 7--8 novelty should be claimed only for the latter mechanism
and its exact post-contestation fairness consequence.

### Selective labels and partial identification

- De-Arteaga, Dubrawski, and Chouldechova analyze learning under selectively
  observed outcomes in algorithm-assisted decisions
  ([arXiv:1807.00905](https://arxiv.org/abs/1807.00905)).
- Kilbertus et al. learn fair decision policies when labels depend on prior
  decisions ([AISTATS 2020](https://proceedings.mlr.press/v108/kilbertus20a.html));
  Wei studies optimal online policies under selective labels
  ([ICML 2021](https://proceedings.mlr.press/v139/wei21a.html)).
- Coston, Rambachan, and Chouldechova characterize predictive fairness over
  good models under selective labels and conditional unconfoundedness
  ([arXiv:2101.00352](https://arxiv.org/abs/2101.00352)).
- Chen, Li, and Mao give exact and partial identification results using
  multiple historical decision-makers as instruments
  ([ICML 2025](https://proceedings.mlr.press/v267/chen25al.html)).
- Recent work now studies long-term fairness with selective labels
  ([arXiv:2605.22291](https://arxiv.org/abs/2605.22291)) and sharp
  fairness–accuracy frontiers under selective labels
  ([arXiv:2606.14977](https://arxiv.org/abs/2606.14977)).

Theorems 13--15 therefore must not claim generic novelty for non-identification,
partial identification, or random exploration/auditing. Their contribution is
the appeal-specific observed-data law, the one-dimensional sharp FNR bounds,
and the explicit connection to final post-contestation group disparity.

## Claim map after audit

| Proposed claim | Audit decision |
|---|---|
| Contestability is important or distinct from explanation | Prior art; motivation only |
| Human review can change fairness | Prior art; motivation only |
| Group recourse/access costs can differ | Prior art; motivation only |
| Exact one-sided contestation transformation and fairness-specific preservation conditions | Retain as a technical contribution, without priority language |
| Conditional impossibility under strictly ordered appeal-cost CDFs | Retain narrowly; cite fair-recourse cost-distribution work |
| Appeal-log observational equivalence and sharp appeal-specific FNR bounds | Retain narrowly; foreground selective-label/partial-identification overlap |
| Random representative audits restore identification | Supporting design result, not a broad novelty claim |
| Fairness-aware assistance allocation | Retain as integration/design contribution; convex/KKT/knapsack facts are classical |

## Required manuscript language

Use “we characterize,” “we derive,” and “in this model.” Avoid “first,”
“unprecedented,” “introduce contestability,” or claims that appeals, recourse
fairness, selective labels, or human-in-the-loop unfairness are new. State that
the real-data evaluation is semisynthetic and that E6 only partially passes:
Adult is stable, while German Credit supports directional effects for two
models but not broad absolute-gap amplification.
