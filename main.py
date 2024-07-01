from fastapi import FastAPI,Body
import uvicorn
# load my model
import joblib
from pydantic import BaseModel

loaded_model = joblib.load('spam_classifier_model.pkl')
loaded_vectorizer = joblib.load('tfidf_vectorizer.pkl')


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


class Email(BaseModel):
    data: str = ""

@app.post("/spam")
def predict_spam(email: Email = None):
    # vectorize the input
    data_vectorized = loaded_vectorizer.transform([email.data])
    # make a prediction
    prediction = loaded_model.predict(data_vectorized)
    return {"prediction": int(prediction[0])}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)