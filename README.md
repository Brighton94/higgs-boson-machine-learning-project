# higgs-boson-machine-learning-project
### 1.1 The Problem
A simple definition of the problem is that we are trying to classify events into two categories:

- (1) the signal event and
- (2) background event.

The “signal” event here is the “tau tau decay of a Higgs boson” and “background” event is every other Higgs boson decay that occures that is not tau-tau. It is essentially a binary classification challenge.

### 1.2 The Dataset

The dataset was obtained from the [CERN Open Data Portal](http://opendata.cern.ch/record/328). In the notebook I provide a list of what each feature means.
However, here are some details to get started:

- all variables are floating point, except PRI_jet_num which is integer
- variables prefixed with PRI (for PRImitives) are “raw” quantities about the bunch collision as measured by the detector.
- variables prefixed with DER (for DERived) are quantities computed from the primitive features, which were selected by the physicists of ATLAS
- it can happen that for some entries some variables are meaningless or cannot be computed; in this case, their value is −999.0, which is outside the normal range of all variables

_It appears that values such as missing values might have been replaced by the CERN scientists with an outlier. In particular what I noticed was that missing values or NAN entries (if any) might have been replaced with an outlier that is not in the range of the values of the features; the outlier used is −999_.
