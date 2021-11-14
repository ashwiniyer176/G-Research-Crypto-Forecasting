# G-Research Crypto Forecasting Challenge

 This is the repository for my work on the [G-Research Crypto Forecasting](https://www.kaggle.com/c/g-research-crypto-forecasting) on Kaggle  The folder structure is as follows:
<br>

## Structure:

1. data : This folder consists of all the input files and data for your machine learning project. If you are working on NLP projects, you can keep your embeddings here. If you are working on image projects, all images go to a subfolder inside this folder. This folder has not been provided by me as the size is too large. To get it working, you can download the data from the Kaggle link provided and create the folder as: <br>
`G-Research-Crypto-Forecasting/data/<Your downloaded dataset from Kaggle>`


2.  src: We will keep all the python scripts associated with the project here. If I talk about a python script, i.e. any *.py file, it is stored in the src folder. 


3.  models: This folder keeps all the trained models.   


4.  notebooks: All jupyter notebooks (i.e. any *.ipynb file) are stored in the notebooks folder. 


5.  README.md: This is a markdown file where you can describe your project and write instructions on how to train the model or to serve this in a production environment. 


6.  LICENSE: This is a simple text file that consists of a license for the project, such as MIT, Apache, etc. Going into details of the licenses is beyond the scope of this book.
<br>

## Dataset
This dataset contains information on historic trades for several cryptoassets, such as Bitcoin and Ethereum. Your challenge is to predict their future returns.

As historic cryptocurrency prices are not confidential this will be a forecasting competition using the time series API. Furthermore the public leaderboard targets are publicly available and are provided as part of the competition dataset. Expect to see many people submitting perfect submissions for fun. Accordingly, THE PUBLIC LEADERBOARD FOR THIS COMPETITION IS NOT MEANINGFUL and is only provided as a convenience for anyone who wants to test their code. The final private leaderboard will be determined using real market data gathered after the submission period closes.

### Files
`train.csv` - The training set <br>
`example_test.csv` - An example of the data that will be delivered by the time series API.<br>

`example_sample_submission.csv` - An example of the data that will be delivered by the time series API. The data is just copied from train.csv. <br>

`asset_details.csv` - Provides the real name and of the cryptoasset for each Asset_ID and the weight each cryptoasset receives in the metric.<br>
`supplemental_train.csv` - After the submission period is over this file's data will be replaced with cryptoasset prices from the submission period. In the Evaluation phase, the train, train supplement, and test set will be contiguous in time, apart from any missing data. The current copy, which is just filled approximately the right amount of data from train.csv is provided as a placeholder.<br>

### Columns
`timestamp` - A timestamp for the minute covered by the row.<br>
`Asset_ID` - An ID code for the cryptoasset.<br>
`Count` - The number of trades that took place this minute.<br>
`Open` - The USD price at the beginning of the minute.<br>
`High` - The highest USD price during the minute.<br>
`Low` - The lowest USD price during the minute.<br>
`Close` - The USD price at the end of the minute.<br>
`Volume` - The number of cryptoasset units traded during the minute.<br>
`VWAP` - The volume weighted average price for the minute.<br>
`Target` - 15 minute residualized returns. See the 'Prediction and Evaluation' section of this notebook for details of how the target is calculated.<br>


## Usage: (Not Updated for Time Series yet!)
1. Use the notebook `notebooks/EDA.ipynb` to explore the dataset and do the required preprocessing
2. Save the dataset after preprocessing as `final_train.csv`
3. Use the notebook `notebooks/EDA.ipynb` for Exploratory Data Analysis and shortlisting models
4. Open `src/config.py`
5. Select a model (sklearn model instance) and a metric (sklearn metric)
6. Configure number of folds required
7. Open Command Prompt and run the `createFoldsAndRun.bat`
