# spam-detection

## Overview

This project is a spam detection system built using scikit-learn for the machine learning model and FastAPI for the web framework. The system can classify text as spam or not spam.

[![](https://skillicons.dev/icons?i=sklearn,fastapi&theme=light)]()

## Datasets

This project utilizes multiple datasets for training and testing:

- [Dataset 1](https://www.kaggle.com/datasets/venky73/spam-mails-dataset)
- [Dataset 2](https://www.kaggle.com/datasets/jackksoncsie/spam-email-dataset)
- [Dataset 3](https://www.kaggle.com/datasets/purusinghvi/email-spam-classification-dataset)
- [Dataset 4](https://www.kaggle.com/datasets/prishasawhney/email-classification-ham-spam)

## Installation
`pip install -r requirements.txt`

## Usage
### Running the FastAPI Server
`python main.py`

### Endpoints
1. **/spam**
   #### Ex Request:
   ```bash
   curl -X 'POST' \
    'http://127.0.0.1:8000/predict' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "text": "You have won $1000!"
   }'
   ```
   #### Ex Respense:
   ```bash
     {
       "prediction": "spam"
     }
   ```
