# any variable we will create that  we will mention here
# aslo will note down all the path to the directories
# any initial setting that we want to perform
# any manual configuration we want to do
# can also do hyperparameter tuning

import pathlib
import os
import prediction_model

PACKAGE_ROOT = pathlib.Path(prediction_model.__file__).resolve().parent
DATAPATH = os.path.join(PACKAGE_ROOT,"datasets")

TRAIN_FILE = 'train.csv'
TEST_FILE = 'test.csv'

MODEL_NAME = "classification.pkl"
SAVE_MODEL_PATH = os.path.join(PACKAGE_ROOT,"trained_model")
# D:\mlproject\prediction_model\trained_model

TARGET = 'Loan_Status'

# final features used in the model
FEATURES = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
            'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
            'Loan_Amount_Term', 'Credit_History', 'Property_Area']

NUM_FEATURES = ['ApplicantIncome','LoanAmount','Loan_Amount_Term']

CAT_FEATURES = ['Gender', 'Married', 'Dependents', 'Education',
                'Self_Employed', 'Property_Area', 'Credit_History']

FEATURES_TO_ENCODE = ['Gender', 'Married', 'Dependents', 'Education',
                      'Self_Employed', 'Property_Area', 'Credit_History']

FEATURE_TO_MODIFY = ['ApplicantIncome']
FEATURE_TO_ADD = 'CoapplicantIncome'

DROP_FEATURES = ['CoapplicantIncome']

LOG_FEATURES = ['ApplicantIncome','LoanAmount']
