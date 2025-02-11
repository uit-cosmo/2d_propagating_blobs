---
title: 'Blobmodel: A Python package for generating superpositions of pulses in two dimensions'
tags:
  - Python
  - pulses
  - imaging data 
  - tokamaks
  - turbulence
authors:
  - name: Juan M. Losada
    orcid: 0000-0003-2054-1384
    equal-contrib: true
    affiliation: 1
  - name: Gregor Decristoforo
    orcid: 0000-0002-7616-0946
    equal-contrib: true # (This is how you can denote equal contributions between multiple authors)
    affiliation: 2
affiliations:
 - name: UiT, The Arctic University of Norway
   index: 1
   ror: 00hx57361
date: 10 February 2025
bibliography: paper.bib

---

# Summary

`blobmodel` is a Python library for generating synthetic data that mimics the behavior
of moving pulses in a turbulent environment. It creates controlled datasets where the
true motion of each pulse is known, allowing researchers to test and improve tracking 
algorithms for analyzing turbulent flows. While originally developed for studying
turbulence in fusion experiments, `blobmodel` can be applied to any field where
turbulence leads to the generation of structures propagating in two dimensions.
The software is open source, easy to use, and designed to support reproducible research.

# Statement of need

Understanding and analyzing the motion of structures in turbulent systems is crucial
in many areas of research, including plasma physics `[@dippolito:2011]`, fluid dynamics `[@fiedler:1988]`, and atmospheric 
science `[@nosov:2009]`. In experimental studies, imaging diagnostics are often used to capture the 
evolution of these structures `[@zweben:2017]`, but extracting reliable velocity information from such 
data remains challenging `[@offeddu:2023]`. Many existing analysis methods rely on assumptions about 
the underlying dynamics and must be tested against known reference data to ensure
accuracy.

`blobmodel` addresses this need by providing a framework for generating synthetic 
datasets resulting from a superposition of uncorrelated pulses:
$$\begin{equation}
    \Phi(x,y,t) = \sum_{k=1}^{K} a_k \varphi\left( \frac{x-v_k(t-t_k)}{\ell_{x, k}}, \frac{(y-y_k)-w_k(t-t_k)}{\ell_{y, k}}\right) ,
\end{equation}$$
where the pulse amplitudes $a_k$, velocity components $v_k$ and $w_k$, arrival times $t_k$, 
arrival positions $y_k$ and sizes $\ell_{x, k}$ and $\ell_{y, k}$ are random variables. 
Additionally, each pulse may be tilted an angle given by an additional random variable
$\theta_k$ with respect to its centre.

The framework allows an explicit definition of all relevant process parameters, including:
* All pulse parameters if defined as degenerate random variables.
* All distribution functions of the pulse parameters otherwise.
* Spatial and temporal resolution.
* Degree of pulse overlap.
* Signal length.

This allows researchers to systematically test and benchmark
tracking algorithms and velocity estimation techniques in a controlled setting. 
Originally developed for studying turbulence-driven transport in fusion plasma
experiments, blobmodel is applicable to any system where turbulence leads to the
formation of moving structures in two-dimensional space. By offering an open-source
and easily accessible tool, blobmodel supports the development and validation of 
analysis methods used in experimental and computational research.

The package has been used to generate synthetic data to study and compare the robustness of
velocity estimation techniques on coarse-grained imaging data `@losada:2024`.

# Acknowledgements

This work was supported by the UiT Aurora Centre Program, UiT The Arctic University of Norway (2020).

# References