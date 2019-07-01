# Poems_genre_classification-NLP-
This project is regarding classifying genre of the poems that whether they are methology/folkare,love,nature or art/science.
## INSTALL
This project requires Python and the following Python libraries installed:
* NumPy
* Pandas
* nltk
* scikit-learn
* selenium
 You will also need to have software installed to run and execute a PyCharm Software.

If you do not have Python installed yet, it is highly recommended that you install the python.

## IDE USED -  
* pycharm(for scraping).
* jupyter notebook(for preprocessing and developing model).

## PROCEDURE - 
### Data Collection:-
* 1.The existing data file of poems in csv format is used from www.kaggle.com .
* 2.But the data was not enough for training the model and the differnce between types of poem is very high that
             could lead to baised model.
* 3.So more data were scraped from www.poemsfoundation.org with the help of selenium.
* 4.After collecting all the data in different csv files, they all are merged into single file and some data preprocessing is done using pandas.
 
 ### Developing the Model:-
 * 1.Pandas and numpy is imported and final_poem_data.csv is loaded.
           * 2.Feature variable values are stored in x and target values in y.
           * 3.Nltk functions are imported and then the preprocessing function is defined for cleaning the data.
           * 4.bag_words function is defined for tokening words and making dictionary for nltk.naivebayes.
           * 5.data is split into traing and testing with test_size = 0.20.
           * 6.Model 1(NaiveBayes) is imported from nltk library and testing data is predicted.
           * 7.TfidfVectorizer is imported to convert the test data into integers
           * 8.Model 2(Logistic Regression) is used and data is predicted.
           * 9.Model 3(SVM-Linear),Model4(Multinomial NaiveBayes),Model5(DecisionTree) are also used for prediction.
             
## RESULT:-
### Accuracy scores:-
*  Model1(NaiveBayes)         -  41%
* Model2(Logistic Regression)-  56%
* Model3(SVM)                -  60%
* Model4(Multinomial NB)     -  56%           
* Model5(Decision Tree)      -  42%
   
  Hence, no model is perfect but SVM comes out to be best of all. Some more preprocessing of data and using deeplearing algos 
  may help in improving the accuracy of the model.

## HOW TO RUN:-
       * As final data file is included so there is no need to run poem_scrap.py and dataframe_setting.ipynb file 
       * Just run predictions_model.ipynb file
       * Install python 3.7
       * pip install all other required libraries  

