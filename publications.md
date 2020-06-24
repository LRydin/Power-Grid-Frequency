---
Title: Publications

menus:
  main:
    weight: 1
    title: Publications
layout: single
toc: true
toc_label: "Publications"
---

A collection of power-grid-frequency related articles can be found here. We report on the main articles that brought about the creation of this power-grid frequency database, as well as a collection of other related research publications and websites.

## Publications associated with this database

### Power grid frequency data base
R. Jumar, H. Maaß, B. Schäfer, L. Rydin Gorjão, V. Hagenmeyer  
arXiv:2006.01771, 2020 [<a href="https://arxiv.org/abs/2006.01771" class="Blau">preprint</a>]

> The transformation of the electrical energy system due to the increasing infeed from renewable energy sources has attracted much attention in diverse research communities. Novel approaches for grid control, grid modeling, and grid architectures are widely proposed. However, data from actual power system operation are rarely available but are critically necessary to analyze real-world scenarios or to evaluate models. In the present paper, we introduce a precisely time-stamped data set comprising power grid frequency measurements from twelve independent synchronous areas of different sizes in one-second resolution. Furthermore, the data includes a synchronized measurement of the frequency within the Continental European synchronous area with measurement points in Portugal, Germany, and Turkey, maximizing the geographical span. Finally, we provide excerpts of the underlying raw data. Data were collected using a self-developed Phasor-Measurement-Unit(PMU)-like device, the Electrical Data Recorder (EDR), connected mostly to conventional low-voltage power outlets.

### Open data base analysis of scaling and spatio-temporal properties of power grid frequencies
L. Rydin Gorjão, R. Jumar, H. Maass, V. Hagenmeyer, J. Kruse, M. Timme, C. Beck, D. Witthaut, B. Schäfer  
arXiv:2006.02481, 2020 [<a href="https://arxiv.org/abs/2006.02481" class="Blau">preprint</a>]

>The electrical energy system has attracted much attention from an increasingly diverse research community. Many theoretical predictions have been made, from scaling laws of fluctuations to propagation velocities of disturbances. However, to validate any theory, empirical data from large-scale power systems are necessary but are rarely shared openly. Here, we analyse an open data base of measurements of electric power grid frequencies across 17 locations in 12 synchronous areas on three continents. The power grid frequency is of particular interest, as it indicates the balance of supply and demand and carries information on deterministic, stochastic, and control influences. We perform a broad analysis of the recorded data, compare different synchronous areas and validate a previously conjectured scaling law. Furthermore, we show how fluctuations change from local independent oscillations to a homogeneous bulk behaviour. Overall, the presented open data base and analyses may constitute a step towards more shared, collaborative energy research.

## Other publications on power-grid frequency studies

### Data-Driven Model of the Power-Grid Frequency Dynamics
L. Rydin Gorjão, M. Anvari, H. Kantz, C. Beck, D. Witthaut, M. Timme, B. Schäfer  
IEEE Access **8**, pp. 43082─43097, 2020, [<a href="https://doi.org/10.1109/ACCESS.2020.2967834" class="Blau">article</a>] [<a href="https://arxiv.org/abs/1909.08346" class="Blau">preprint</a>]

>The energy system is rapidly changing to accommodate the increasing number of renewable generators and the general transition towards a more sustainable future. Simultaneously, business models and market designs evolve, affecting power-grid operation and power-grid frequency. Problems raised by this ongoing transition are increasingly addressed by transdisciplinary research approaches, ranging from purely mathematical modelling to applied case studies. These approaches require a stochastic description of consumer behaviour, fluctuations by renewables, market rules, and how they influence the stability of the power-grid frequency. Here, we introduce an easy-to-use, data-driven, stochastic model for the power-grid frequency and demonstrate how it reproduces key characteristics of the observed statistics of the Continental European and British power grids. Using data analysis tools and a Fokker-Planck approach, we estimate parameters of our deterministic and stochastic model. We offer executable code and guidelines on how to use the model on any power grid for various mathematical or engineering applications.

### Stochastic properties of the frequency dynamics in real and synthetic power grids
M. Anvari, L. Rydin Gorjão, M. Timme, D. Witthaut, B. Schäfer, H. Kantz  
Phys. Rev. Research **2**, 013339, 2020,
[<a href="https://doi.org/10.1103/PhysRevResearch.2.013339">article</a>]
[<a href="https://arxiv.org/abs/1909.09110" class="Blau">preprint</a>]

>The frequency constitutes a key state variable of electrical power grids. However, as the frequency is subject to several sources of fluctuations, ranging from renewable volatility to demand fluctuations and dispatch, it is strongly dynamic. Yet, the statistical and stochastic properties of the frequency fluctuation dynamics are far from fully understood. Here, we analyse properties of power grid frequency trajectories recorded from different synchronous regions. We highlight the non-Gaussian and still approximately Markovian nature of the frequency statistics. Further, we find that the frequency displays significant fluctuations exactly at the time intervals of regulation and trading, confirming the need of having a regulatory and market design that respects the technical and dynamical constraints in future highly renewable power grids. Finally, employing a recently proposed synthetic model for the frequency dynamics, we combine our statistical and stochastic analysis and analyse in how far dynamically modelled frequency properties match the ones of real trajectories.

## Intra-area oscillations
### Spectral estimation of low-frequency oscillations in the Nordic grid using ambient synchrophasor data under the presence of forced oscillations.
L. Vanfretti, S. Bengtsson, V. S. Peric, S., J. O. Gjerde  
2013 IEEE Grenoble Conference, pp. 1-6, 2013,
[<a href="https://doi.org/10.1109/ptc.2013.6652190">article</a>]

>Spectral analysis applied to synchrophasor data can provide valuable information about lightly damped low-frequency modes in power systems. This paper demonstrates application of two non-parametric spectral estimators focusing on mode frequency estimation. The first one is the well-known Welch spectral estimator whereas the application of Multitaper method is proposed here. In addition, the paper discusses mode estimator tuning procedures and the estimators' performances in the presence of “forced” oscillations. The validity of the proposed application of the non-parametric estimators and tuning procedures is verified through both simulated data and PMU data originating from the high-voltage grid of the Nordic power system. Special attention is given to the analysis of the behaviour of different low frequency modes present in the Nordic grid, including that of forced oscillations.

## Applications in Machine Learning

### Predictability of Power Grid Frequency

J. Kruse, B. Schäfer, D. Witthaut  
arXiv:2004.09259, 2020 [<a href="https://arxiv.org/abs/2004.09259" class="Blau">preprint</a>]

>The power grid frequency is the central observable in power system control, as it measures the balance of electrical supply and demand. A reliable frequency forecast can facilitate rapid control actions and may thus greatly improve power system stability. Here, we develop a weighted-nearest-neighbor (WNN) predictor to investigate how predictable the frequency trajectories are. Our forecasts for up to one hour are more precise than averaged daily profiles and could increase the efficiency of frequency control actions. Furthermore, we gain an increased understanding of the specific properties of different synchronous areas by interpreting the optimal prediction parameters (number of nearest neighbors, the prediction horizon, etc.) in terms of the physical system. Finally, prediction errors indicate the occurrence of exceptional external perturbations. Overall, we provide a diagnostics tool and an accurate predictor of the power grid frequency time series, allowing better understanding of the underlying dynamics.



## Estimation of Electromechanical Oscillations

### Application of Ambient Analysis Techniques for the Estimation of Electromechanical Oscillations from Measured PMU Data in Four Different Power Systems

L. Vanfretti, L. Dosiek, J. W. Pierre, D. Trudnowski, J. H. Chow, R. García-Valle, U. Aliyu  
European Transactions on Electrical Power, **21**(4), 1640–1656, 2010 [<a href="https://onlinelibrary.wiley.com/doi/abs/10.1002/etep.507">article</a>]

>The application of advanced signal processing techniques to power system measurement data for the estimation of dynamic properties has been a research subject for over two decades. Several techniques have been applied to transient (or ringdown) data, ambient data, and to probing data. Some of these methodologies have been included in off-line analysis software, and are now being incorporated into software tools used in control rooms for monitoring the near real-time behavior of power system dynamics. In this paper we illustrate the practical application of some ambient analysis methods for electromechanical mode estimation in different power systems. We apply these techniques to phasor measurement unit (PMU) data from stored archives of several hours originating from the US Eastern Interconnection, the Western Electricity Coordinating Council, the Nordic Power System, and time-synchronized Frequency Disturbance Recorder (FDR) data from Nigeria. It is shown that available signal processing tools are readily applicable for analysis of different power systems, regardless of their specific dynamic characteristics. The discussions and results in this paper are of value to power system operators and planners as they provide information of the applicability of these techniques via readily available signal processing tools, and in addition, it is shown how to critically analyze the results obtained with these methods.
