# The Smart Home Project at CSIRO
Author: Meng Fang Date: 10 Nov 2015

There are three different parts: multi-tracker, uwb and miband. 
Before runing. Please make sure that you have installed scikit-learn.

## multi-tracker
It is implemented for presence tracking for multiple residents (here, we have 2 residents).

#### How to run?
The following is used for runing trackers implemented by NB.
```sh
$ python multiTracker_NB.py
```

The following is used for running trackers implemented by HMM.
```sh
$ python multiTracker_HMM.py
```

## uwb
It is used for testing uwb data.

#### How to run?
If you have train data and test data then use
```sh
$ python classification4uwb.py train_file test_file
```

If you have a dataset and want to apply cross-validation (here, we use 3 folds cv) then use
```sh
$ python classification_CV4uwb.py data_file
```

If you have a dataset and want to apply PCA for selecting features then use
```sh
$ python classification_PCA4uwb.py data_file num_of_features
```
For example, replace num_of_features as 3 and now 3 is the number of selected features.


## miband
It is used for testing miband data.

It contains three precedures: download data from remote mysql server, format the raw data and test the data.

To download data from remote mysql server, we use
```sh
$ python getDataFromDB.py "select .. where .. " output_raw_data_file
```
The "select .. where .. " should be replaced by your query string (sql query) according to requirement.

Data in output_file is a raw data. To format the raw data, please use
```sh
$ python preprocessData.py labels_file output_raw_data_file new_data_file
```
The labels_file is a file containing labels of data. The output_raw_data_file is the file name of raw data (from mysql). The new_data_file is the file name of an output file.

To test the data, please use
```sh
$ python test4miband.py new_data_file
```
In this testing, there are two algorithms implemented: one is maximal value and another one is nb-histogram.
 
