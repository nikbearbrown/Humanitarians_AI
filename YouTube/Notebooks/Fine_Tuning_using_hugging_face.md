# Fine-Tuning of a dataset using a pretrained model from hugging face
# Why Fine-Tune Instead of Training?

## Pre-trained Models:
- Models like **BERT**, **GPT**, and **DistilBERT** are trained on massive datasets (e.g., Wikipedia, books, web content).
- These models already understand general language patterns, syntax, and semantics.

## Task-Specific Needs:
- While pre-trained models are generalized, they may not perform optimally on a specific task (e.g., spam detection, sentiment analysis, medical diagnosis).
- **Fine-tuning** helps adapt the model to specialized domains using smaller datasets.

## Benefits:
- **Time-Saving**: Training a large model from scratch takes immense computational resources and time.
- **Data Efficiency**: Fine-tuning requires far less labeled data than training from scratch.
- **Performance Boost**: Leverages the existing knowledge of the model to quickly achieve high accuracy.

---

# How Fine-Tuning Works

### 1. Start with a Pre-Trained Model:
- Load a model like **DistilBERT**, **BERT**, or **GPT**, which has been trained on a general-purpose corpus.

### 2. Prepare the Task-Specific Dataset:
- **Label your dataset** for the specific task (e.g., spam vs. ham for spam detection).
- **Preprocess the data** (e.g., tokenization, padding).

### 3. Modify the Model:
- **Add task-specific layers** (e.g., classification head for spam detection).
- **Freeze some layers** (optional): Sometimes, earlier layers of the model (responsible for general language understanding) are frozen to retain general knowledge and speed up training.

### 4. Train on the New Dataset:
- Use the task-specific dataset to fine-tune the model’s weights for the desired outcome.
- This involves **fewer epochs** and **lower learning rates** to prevent "overwriting" the pre-trained knowledge.

---

# Example: Fine-Tuning DistilBERT for Spam Detection

### Pre-Trained Model Knowledge:
- **DistilBERT** already understands English grammar, context, and sentence structures.

### Fine-Tuning on Spam Dataset:

**Dataset**:
- **Labels**: spam or ham.
- **Messages**: "Free entry in 2 a weekly competition...", "Hey, what's up?", etc.

**Process**:
1. Add a **classification layer** (softmax) to the pre-trained DistilBERT model.
2. Fine-tune the model using the labeled dataset for a few epochs.
3. Train only the later layers (task-specific knowledge) while retaining the general language understanding in the earlier layers.

---

# Outcome

After fine-tuning, the model specializes in spam detection while still leveraging its general understanding of the English language.

### Example Predictions:
- **Input**: "Win a free iPhone now!"
  - **Output**: spam
- **Input**: "Hey, are you free to meet tomorrow?"
  - **Output**: ham

---

# When Should You Fine-Tune a Dataset?

- **Custom Tasks**: You have a domain-specific task like legal document analysis, medical diagnosis, or social media sentiment analysis.
- **Limited Data**: You have a smaller dataset that isn't sufficient for training a model from scratch.
- **Performance Boost**: To improve the performance of a general-purpose model on a specific task.

---

**Fine-tuning** is a practical way to adapt powerful pre-trained models to solve specific real-world problems effectively!

Let me know if you need further clarification.

# Spam Classification using DistilBERT

This project fine-tunes a pre-trained DistilBERT model for spam classification. The dataset includes labeled text messages ("ham" and "spam") that are tokenized and processed for training.

---

## Code Breakdown

### 1. Importing Libraries and Reading Data
```python
import pandas as pd

df = pd.read_csv('Collection.csv', sep='\t', names=["label", "message"])
print(df.head())
```
- Reads a tab-separated file (`SMSSpamCollection.txt`).
- Columns:
  - `label`: Indicates "ham" (non-spam) or "spam".
  - `message`: The actual text of the message.

---

### 2. Dataset Shape
```python
df.shape
```
- Returns the number of rows and columns in the dataset.

---

### 3. Separating Features and Labels
```python
X = list(df['message'])
y = list(df['label'])
```

---

### 4. Encoding Labels
```python
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
print(y)
```
- Converts labels (`ham`, `spam`) into numeric values (0, 1).

---

### 5. Splitting Data
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=40)
```

---

### 6. Tokenizing Data
```python
from transformers import DistilBertTokenizer
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
train_encodings = tokenizer(X_train, truncation=True, padding=True, max_length=512)
test_encodings = tokenizer(X_test, truncation=True, padding=True, max_length=512)
```

---

### 7. Converting Data to TensorFlow Dataset
```python
import tensorflow as tf
train_dataset = tf.data.Dataset.from_tensor_slices((dict(train_encodings), y_train))
test_dataset = tf.data.Dataset.from_tensor_slices((dict(test_encodings), y_test))
```

---

### 8. Loading Pre-trained DistilBERT Model
```python
from transformers import TFDistilBertForSequenceClassification
model = TFDistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=2)
```

---

### 9. Defining Training Arguments
```python
from transformers import TFTrainingArguments
training_args = TFTrainingArguments(
    output_dir='./results',
    num_train_epochs=2,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=16,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./logs',
    logging_steps=10
)
```

---

### 10. Fine-tuning the Model
```python
from transformers import TFTrainer

trainer = TFTrainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset
)
trainer.train()
```

---

### 11. Evaluating the Model
```python
results = trainer.evaluate()
print(results)
```

---

## Summary
This project:
1. Loads and preprocesses a labeled dataset.
2. Fine-tunes a pre-trained DistilBERT model for spam classification.
3. Evaluates the model's performance.

Feel free to modify or extend the code for your specific use case!

---
