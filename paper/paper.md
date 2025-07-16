---
title: "EU-ZEVAM: European Zero-Emission Vehicle Adoption Model"
tags:
  - zero-emission vehicles
  - electric vehicles
  - Europe
  - vehicle adoption model
  - modelling framework
  - Python
authors:
  - name: Gabriel Möring-Martínez
    orcid: 0009-0003-4380-3081
    affiliation: 1 # (Multiple affiliations must be quoted)
affiliations:
 - name: German Aerospace Center (DLR), Institute of Vehicle Concepts, Pfaffenwaldring 38-40, Stuttgart, 70569, Germany
   index: 1
   ror: 04bwf3e34
date: 16 July 2025
bibliography: paper.bib
---

# EU-ZEVAM: European Zero-Emission Vehicle Adoption Model

### Integrating transport simulation and fleet survival analysis to forecast Europe’s electric vehicle transition


# Summary

# Summary

Vehicle adoption models are essential tools for a wide range of stakeholders. Governments and policymakers use them to assess the alignment of existing policies with long-term decarbonization targets, guide infrastructure development, and evaluate the achievability of climate objectives [@Ellingsen.2016; @GomezVilchez.2020]. Meanwhile, original equipment manufacturers (OEMs) and industry players rely on these models to forecast future production demand, identify investment needs, and align their strategies with anticipated market shifts [@BloombergNEF.2021].

The core objective of vehicle adoption models is to simulate how the vehicle fleet will evolve under different policy, market, and technological scenarios. These models help to identify the key drivers of vehicle electrification and support decision-making by offering insight into long-term fleet composition trends [@Maybury.2022; @Kumar.2020].

However, many existing vehicle adoption models lack a strong theoretical foundation, leading to reduced transparency and reproducibility. This modeling flexibility can introduce inconsistencies across studies and hinder comparability. In contrast, approaches grounded in econometric theory offer greater methodological transparency and empirical robustness but typically require large, high-quality datasets [@jochem2018methods].

To address these limitations, we introduce `EU-ZEVAM`, a fully open-source framework that combines the outcome of a bottom-up transportation model—specifically, an agent-based model (ABM)—with a cohort model [@MoringMartinez.2025b]. The ABM simulates individual vehicle adoption decisions across heterogeneous agents in the population using the transportation model Vector21 [@InstituteofVehicleConcepts.2023] at an EU-level [@MoringMartinez.2024], while the cohort component incorporates cumulative survival probability curves to represent the longevity and phase-out of vehicles within national fleets [@Held.2021]. This hybrid architecture enables a dynamic and disaggregated representation of fleet evolution over time, capturing both behavioral and technical aspects of the transition.

`EU-ZEVAM` features a user-friendly interface for estimating electric vehicle stock adoption rates across EU countries through 2050. It uses new vehicle registration data under the STATS scenario from [@MoringMartinez.2024], though it remains flexible to alternative input scenarios or transportation models. Survival rates are computed empirically following the methodology in [@Held.2021], with default values provided for the base year 2021 [@MoringMartinez.2025b]. While updates to these rates are possible, they require considerable data collection and processing effort. A summary of the modelling framework can be found in the graphical abstract (cf. Figure \ref{fig:graphical-abstract}).

![Graphical abstract of the electric vehicle adoption model for European Union countries. The framework combines a transportation model for estimating electric vehicle new registrations [@MoringMartinez.2024] with a country-based cohort model [@Held.2021]. Figure extracted from [@MoringMartinez.2025b], licensed under CC BY 4.0.](CSP_Paper_Stock_Validation_Illustration_SH_GM.pdf){#fig:graphical-abstract}

The model outputs national electric vehicle stock projections under various assumptions, and includes two validation steps and several sensitivity analyses to assess the impact of survival rates. By integrating empirical data with a flexible modeling structure, `EU-ZEVAM` offers a transparent and extensible platform for analyzing electric vehicle adoption in line with climate and mobility goals.

# Statement of need

Numerous electric vehicle adoption models have been developed [@Kumar.2020], varying in geographic focus, explanatory variables, modeling approaches, and data sources [@Maybury.2022]. Yet most remain not transparent, hard to reproduce and difficult to adapt [@jochem2018methods], and—so far as we are aware—no fully open‑source implementation is publicly available.

We address this gap by introducing a transparent, EU‑wide electric vehicle adoption modelling framework, whose methodological foundation is supported by a peer‑reviewed article [@MoringMartinez.2025b]. The code is openly available and can be coupled either with the transport-demand outputs from [@MoringMartinez.2024], also included here, or with any alternative transportation model. The framework:

- estimates electric vehicle adoption rates using empirical survival rates
- supports sensitivity analyses on fleet-turnover assumptions and possible scenarios
- allows users to define alternative EV-registration trajectories to assess their impact on the vehicle fleet.

By providing open-source code and a modular structure, `EU-ZEVAM` facilitates reproducibility, transparency, and flexible exploration of policy scenarios.

Zero-emission vehicle adoption is a key objective of the European Union. To this end, the EU has implemented binding CO$_2$ emission standards that manufacturers must meet to avoid financial penalties [@EuropeanCommision.2022]. In addition, individual EU Member States support the deployment of zero-emission vehicles through varying national policies, including tax incentives, infrastructure development, and other supportive measures [@Neshat.2023].

Despite these EU-wide targets, most vehicle adoption models remain country-specific [@Maybury.2022]. Among the limited number of EU-wide models, several rely on strong simplifying assumptions—for example, applying Germany’s vehicle survival rates uniformly across all countries [@Ntziachristos]. However, multi-country analyses of future fleet compositions require country-specific survival modeling due to significant differences in used vehicle import and export dynamics [@Held.2021].

Furthermore, several studies have highlighted the lack of comprehensive datasets needed to compute country-specific cumulative survival probabilities. To address this, we present a country-level modeling framework using updated cumulative survival rates up to the year 2021. This builds upon earlier work by [@Held.2021] for 2016 and [@Oguchi.2015] for 2008.

By adopting a country-level approach, EU-ZEVAM enables the estimation of electric vehicle adoption rates at both national and EU-wide levels (cf. Figure \ref{fig:stock-shares} ). It supports evaluation of whether fleet electrification and decarbonization targets are on track, while facilitating cross-country coordination and compliance planning. This is particularly relevant because scrappage schemes can accelerate fleet renewal [@Marin.2020b; @Svoboda.2023], while insufficient infrastructure or incentives may slow it down—leading to increased demand for second-hand internal combustion engine vehicles [@Maybury.2022].

![Battery electric passenger car fleet shares estimated using country-level empirical cumulative survival rate probability curves for all EU-27 countries and Norway. A sensitivity analysis using survival rates from 2008 and 2016 is also presented. Figure extracted from [@MoringMartinez.2025b], licensed under CC BY 4.0.](sensitivity_analysis_with_historical_csp.pdf){#fig:stock-shares}


# Mathematics

Single dollars ($) are required for inline mathematics e.g. $f(x) = e^{\pi/x}$

Double dollars make self-standing equations:

$$\Theta(x) = \left\{\begin{array}{l}
0\textrm{ if } x < 0\cr
1\textrm{ else}
\end{array}\right.$$

You can also use plain \LaTeX for equations
\begin{equation}\label{eq:fourier}
\hat f(\omega) = \int_{-\infty}^{\infty} f(x) e^{i\omega x} dx
\end{equation}
and refer to \autoref{eq:fourier} from text.

# Citations

Citations to entries in paper.bib should be in
[rMarkdown](http://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html)
format.

If you want to cite a software repository URL (e.g. something on GitHub without a preferred
citation) then you can do it with the example BibTeX entry below for @fidgit.

For a quick reference, the following citation commands can be used:
- `@author:2001`  ->  "Author et al. (2001)"
- `[@author:2001]` -> "(Author et al., 2001)"
- `[@author1:2001; @author2:2001]` -> "(Author1 et al., 2001; Author2 et al., 2002)"

# Figures

<!--
Figures can be included like this:
![Caption for example figure.\label{fig:example}](figure.png)
and referenced from text using \autoref{fig:example}.

Figure sizes can be customized by adding an optional second parameter:
![Caption for example figure.](figure.png){ width=20% }
-->

# Acknowledgements

We acknowledge contributions from Brigitta Sipocz, Syrtis Major, and Semyeong
Oh, and support from Kathryn Johnston during the genesis of this project.

# References