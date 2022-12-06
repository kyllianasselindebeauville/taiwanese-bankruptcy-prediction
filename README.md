# Taiwanese Bankruptcy Prediction

A company faces bankruptcy when they are unable to pay off their debts. The goal is to predict whether a company will go bankrupt or not, given a number of attributes from the Taiwan Economic Journal for the years 1999 to 2009.

The dataset [Taiwanese Bankruptcy Prediction](https://archive.ics.uci.edu/ml/datasets/Taiwanese+Bankruptcy+Prediction) was created by UCI Machine Learning Repository in 2020. This dataset is composed of 6819 instances, 95 features and 1 target (Bankruptcy) in the dataset.

We can ask ourselves to what extent parameters such as those studied in the dataset (the profit, the sales, the revenue...) have an influence on the bankruptness of a company, and therefore how they can help predict the bankruptness?

To do this, we will visualise the key data and build predictive models.

To carry out the study of our dataset **(\*)**, we splitted our project into different parts :

1. Setup
2. Data collection
3. Data cleaning
4. Exploratory Data analysis
5. Data preprocessing
6. Data visualisation
7. Modeling
8. Evaluation of the models

**(\*) To see the complete notebook, download the [html](reports/notebook.html) or [ipynb](notebooks/final_project.ipynb) file and open it locally.**

## Authors

- [Kyllian Asselin de Beauville](https://www.github.com/kyllianasselindebeauville)
- [Arnaud Cournil](https://www.github.com/arnaudcournil)
- [Julia Cuvelier](https://www.github.com/juliacuvelier)

## Run Locally

- Clone the repository and change directory into it.

```shell
git clone https://github.com/kyllianasselindebeauville/taiwanese-bankruptcy-prediction.git
cd taiwanese-bankruptcy-prediction
```

- Create a virtual environment and install the requirements.

```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

> You may need to use `python` instead of `python3` depending on your environment.

- Migrate and run the django server.

```shell
python3 manage.py migrate
python3 manage.py runserver
```
