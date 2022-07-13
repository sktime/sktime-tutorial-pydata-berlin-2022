<a href="https://sktime.org"><img src="https://github.com/alan-turing-institute/sktime/blob/main/docs/source/images/sktime-logo-no-text.jpg?raw=true)" width="175" align="right" /></a>

Welcome to the sktime tutorial at PyData Berlin 2022
====================================================

### advanced forecasting - probabilistic, global and hierarchical

:tv: [youtube link of tutorial](https://www.youtube.com/watch?v=4Rf9euAhjNc)

This tutorial is about [sktime] - a unified framework for machine learning with time series. sktime features various time series algorithms and modular tools for pipelining, ensembling and tuning. 

This tutorial is an **advanced tutorial** which explains sktime framework functionality for hierarchical and probabilistic forecasting.

[sktime]: https://sktime.org

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sktime/sktime-tutorial-pydata-berlin-2022/main?filepath=notebooks)

It is recommended to work through the **general sktime introduction tutorial** first:

:movie_camera: **[general sktime intro tutorial](https://github.com/sktime/sktime-tutorial-pydata-global-2021) from PyData Global 2021**\
:tv: [youtube video of sktime intro at PyData Global 2021](https://www.youtube.com/watch?v=ODspi8-uWgo)


## :bulb: Description

There has been a surge of recent interest in probabilistic forecasting, as well as global and hierarchical forecasting. Advances in research and benchmarking studies such as M5 have proven that composable pipelines achieve state-of-art performance.

One of the newest additions to sktime are interfaces for probabilistic forecasting, and forecasting with panel or hierarchical data.

**Probabilistic forecasting** is the task of making forecast predictions that include statements about the uncertainty of the forecast. It includes:

*	interval forecasts: producing intervals with a nominal probability of the observation to be contained in the interval
*	quantile forecasts: specifying one or multiple quantiles of a predictive forecast distribution
*	fully probabilistic (aka distributional) forecasts: producing a symbolic representation of a predictive forecast distribution
*	samples from probabilistic forecasts: producing a sample from the predictive forecast distribution

Probabilistic forecasts are evaluated using probabilistic forecast metrics; they can be obtained from, or partake in specific composition algorithms.

**Hierarchical forecasting** is forecasting in the context of "hierarchical time series", i.e., temporal observations where individual observations may be of an instance classified by one or multiple "hierarchy" variables, such as "hospital ID" or "patient ID". A special case is a panel of time series, which is simply a collection of time series. Forecasting with such time series may be improved by algorithms that use information across the different instances, or information that links time series to the hierarchy variables. Another term for this task is "global forecasting".

Lastly, a forecast may be both hierarchical and probabilistic, i.e., in a scenario where multiple time series with hierarchy variables are present, and where uncertainty statements of the forecast are of interest.

sktime's forecasting module provides a number of new interfaces for the above, some consolidating, some bleeding-edge with opportunities to contribute to implementation or design. As research on software interfaces and mathematical conceptualization in this area is still an ongoing endeavour, challenges will also be discussed. We welcome contributions from the pydata/numfocus community.

:movie_camera: **Check out our [previous tutorial](https://github.com/sktime/sktime-tutorial-pydata-global-2021) from PyData Global 2021!**\
:movie_camera: **Check out our [previous tutorial](https://github.com/sktime/sktime-tutorial-pydata-amsterdam-2020) from PyData Amsterdam 2020!**

## :rocket: How to get started

You have different options how to run the tutorial notebooks:

* Run the notebooks in the cloud on [Binder] - for this you don't have to install anything!
* Run the notebooks on your machine. [Clone] this repository, get [conda], install the required packages using `conda env create -f environment.yml` and launch Jupyter Lab by running: `jupyter lab`. For trouble shooting, see sktime's more detailed [installation instructions].

[Binder]: https://mybinder.org/v2/gh/sktime/sktime-pydata-global-2021-tutorial/main?filepath=notebooks
[clone]: https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository
[conda]: https://docs.conda.io/en/latest/
[installation instructions]: https://www.sktime.org/en/latest/installation.html

## :wave: How to contribute

If you're interested in contributing to sktime, you can find out more how to get involved [here](https://www.sktime.org/en/stable/get_involved.html).

Any contributions are welcome, not just code!
