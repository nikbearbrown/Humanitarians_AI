# Guide to Hugging Face

![Hugging Face Logo](https://huggingface.co/front/assets/huggingface_logo.svg)

## Table of Contents
- [Introduction](#introduction)
- [Core Components](#core-components)
- [Usage and Pricing](#usage-and-pricing)
- [Getting Started](#getting-started)
- [API Integration](#api-integration)
- [Advantages of Hugging Face](#advantages-of-hugging-face)
- [Limitations of Hugging Face](#limitations-of-hugging-face)
- [When to Use Hugging Face](#when-to-use-hugging-face)
- [When to Consider Alternatives to Hugging Face](#when-to-consider-alternatives-to-hugging-face)

## Introduction

Hugging Face is the leading platform for machine learning, hosting over 300,000 models and 50,000 datasets (as of 2024). Originally focused on NLP, it now supports a wide range of AI tasks including computer vision, speech processing, and reinforcement learning.

## Core Components

### 1. Model Hub
- 300,000+ pre-trained models
- Multiple frameworks support (PyTorch, TensorFlow, JAX)
- Version control and model cards
- Automated model evaluation

### 2. Datasets
- 50,000+ datasets available
- Streaming support for large datasets
- Built-in preprocessing tools
- Version control and documentation

### 3. Spaces
- Interactive ML app hosting
- Support for Gradio and Streamlit
- Easy deployment and sharing
- Custom domain support

## Usage and Pricing

### Free Tier
- CPU-only runtime
- 2 vCPUs, 16GB RAM
- 1000 requests/day
- 5GB storage
- 30,000 API calls/month

### Pro Tier ($9/month)
- GPU access (T4)
- Increased compute limits
- 100GB storage
- Unlimited API calls

### Enterprise
- Custom hardware
- Dedicated support
- Private deployments
- Custom usage limits

![Image Description](https://github.com/nikbearbrown/ENGR-0201-Organizing-Academic-Success-AI-for-Personalized-Learning/blob/main/ENGR_0201/HF_2.jpg)

## Getting Started

### Installation
```bash
pip install transformers
pip install torch
pip install datasets
```

### Example Usage of a Sentiment Analysis Model
```python
from transformers import pipeline 

# Load the sentiment-analysis pipeline
classifier = pipeline('sentiment-analysis')

# Test sentences
sentences = [
    "The product was amazing! I'm very satisfied with the quality.",
    "I am extremely disappointed with the customer service experience.",
    "The weather today is quite pleasant and perfect for a picnic.",
    "I can't believe how terrible the movie was. Total waste of time.",
    "The food was decent, but the service could have been better."
]

# Analyze sentiment
results = classifier(sentences)

# Display formatted results
for sentence, result in zip(sentences, results):
    label = result['label']
    score = round(result['score'], 4)
    print(f"Sentence: '{sentence}'")
    print(f"Predicted Sentiment: {label} (Confidence: {score})\n")

```

![Image Description](https://github.com/nikbearbrown/ENGR-0201-Organizing-Academic-Success-AI-for-Personalized-Learning/blob/main/ENGR_0201/HF_1.jpg)


## API Integration:
### Benefits of API Integration
1. **Serverless Deployment**
   - No need to manage model weights locally
   - Reduced infrastructure complexity
   - Automatic model updates and improvements

2. **Cost Efficiency**
   - Pay per API call rather than maintaining GPU infrastructure
   - No need for expensive hardware
   - Scalable pricing based on usage

3. **Easy Scalability**
   - Handle varying load automatically
   - No need to manage scaling infrastructure
   - Built-in load balancing

4. **Multiple Model Access**
   - Use different models without downloading them
   - Easy A/B testing of models
   - Quick model switching based on performance

5. **Production Ready**
   - High availability
   - Production-grade infrastructure
   - Built-in monitoring and logging

### Common Use Cases
- Web applications needing AI capabilities
- Mobile apps requiring light-weight integration
- Microservices architecture
- Multi-model inference pipelines
- Testing different models in production

## Getting Your Hugging Face Token
### Steps to Create API Token
1. **Create Account**
   - Visit [Hugging Face](https://huggingface.co)
   - Click on "Sign Up" or "Login"
   - Complete the registration process

2. **Access Token Settings**
   - Log into your account
   - Click on your profile picture
   - Select "Access Tokens" from the dropdown


![Image Description](https://github.com/nikbearbrown/ENGR-0201-Organizing-Academic-Success-AI-for-Personalized-Learning/blob/main/ENGR_0201/HF_3.jpg)


3. **Generate New Token**
   - Click "New token"
   - Enter a name for your token (e.g., "My-API-Token")
   - Select appropriate permissions:
     - `read`: For using models and datasets
     - `write`: For uploading models and datasets
     - `role`: For organization management
   - Click "Generate token"


![Image Description](https://github.com/nikbearbrown/ENGR-0201-Organizing-Academic-Success-AI-for-Personalized-Learning/blob/main/ENGR_0201/HF_4.jpg)


### HF Token Security Best Practices
1. **Environment Variables**
   ```python
   # Store in .env file
   HF_TOKEN=your_token_here
   
   # Load in Python
   import os
   from dotenv import load_dotenv
   
   load_dotenv()
   token = os.getenv('HF_TOKEN')
   ```

2. **Token Rotation**
   - Regularly rotate tokens (every 30-90 days)
   - Revoke unused tokens
   - Use different tokens for development and production

3. **Access Management**
   - Use read-only tokens when possible
   - Limit token scope to necessary permissions
   - Never share tokens in code repositories

4. **Monitoring**
   - Monitor token usage regularly
   - Set up alerts for unusual activity
   - Keep track of active tokens

### Named Entity Recognition using REST API Example
```python
import requests

# Replace 'YOUR_API_TOKEN' with your Hugging Face API token
API_URL = "https://api-inference.huggingface.co/models/dbmdz/bert-large-cased-finetuned-conll03-english"
headers = {"Authorization": f"Bearer YOUR_API_TOKEN"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Example text for entity recognition
texts = [
    "Barack Obama was born in Hawaii and served as the 44th President of the United States.",
    "Apple Inc. was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in Cupertino, California.",
    "The Eiffel Tower is located in Paris, France, and is one of the most visited landmarks in the world.",
]

# Extract named entities
for text in texts:
    result = query({"inputs": text})

    if isinstance(result, list):
        print(f"Text: '{text}'\n")
        print("Recognized Entities:")
        for entity in result:
            word = entity.get('word', '')
            entity_type = entity.get('entity_group', '')
            score = round(entity.get('score', 0), 4)
            print(f"  - {word} ({entity_type}, Confidence: {score})")
        print("\n" + "-"*60 + "\n")
    else:
        print(f"Unexpected response for text: '{text}'")
        print(f"Response: {result}\n")

```

![Image Description](https://github.com/nikbearbrown/ENGR-0201-Organizing-Academic-Success-AI-for-Personalized-Learning/blob/main/ENGR_0201/HF_5.jpg)


### What is Named Entity Recognition

Named Entity Recognition (NER) is a subtask of Natural Language Processing (NLP) that involves identifying and classifying named entities in text into predefined categories such as people, organizations, locations, dates, and more.

Some use cases include:

**1. Information Extraction**
  - Extract meaningful information from large volumes of text
  - Examples:
      - Extracting company names from business articles.
      - Identifying product names in customer reviews.

**2. Document Summarization**
  - Summarize key points by extracting relevant entities.
  - Examples:
      - Summarizing legal documents by highlighting people, dates, and important terms
      - Generating summaries from news articles.

**3. Search Engine Optimization (SEO)**
  - Enhance search engines by tagging important entities in web pages.
  - Examples:
      - Tagging products, brands, and locations to improve search visibility.
  
## Advantages of Hugging Face

**1. Accessibility**
  - Thousands of pre-trained models across multiple domains.

**2. Ease of Deployment**
  - Easy to fine-tune and deploy models for various tasks.

**3. Community**
  - A large, active community that contributes models and datasets.

**4. Interoperability**
  - Supports integration with PyTorch, TensorFlow, and JAX.

**5. Efficiency**
  - Reduces computational cost and time by providing pre-trained models.

**6. Collaboration**
  - Enables sharing and collaborative development through Spaces and Datasets.

## Limitations of Hugging Face

**1. Performance Limitations**
  - Pre-trained models may not perform well on domain-specific tasks without fine-tuning.

**2. Dependency on Cloud Infrastructure**
  - Large models may require powerful hardware or cloud services.

**3. Resource Intensive**
  - Large models and datasets may demand significant memory and storage.

## When to Use Hugging Face

1. **Rapid Prototyping**  
   - **Quick AI Capability Testing**: Test pre-trained models in minutes using Hugging Face’s APIs.  
   - **Proof-of-Concept Development**: Build minimal viable products without deep ML expertise.  
   - **Hackathons**: Leverage pre-built models for competitive, time-constrained events.  

2. **Research Projects**  
   - **Model Comparison**: Evaluate different models for various tasks like sentiment analysis or translation.  
   - **Academic Research**: Conduct experiments using cutting-edge models with minimal setup.  
   - **Experimentation**: Try out innovative approaches by customizing pre-trained models.  

3. **Medium-Scale Production**  
   - **Moderate Traffic Applications**: Support apps with consistent but moderate user traffic.  
   - **Standard AI Capabilities**: Use models for tasks like text classification, object detection, or chatbots.  
   - **Quick Deployment Needs**: Deploy AI-powered applications with minimal infrastructure management.  

4. **Education**  
   - **Learning AI/ML**: Explore state-of-the-art models for hands-on learning and practice.  
   - **Workshops**: Use Hugging Face as a teaching tool in educational sessions and bootcamps.  
   - **Demonstrations**: Create live demos showcasing AI capabilities for events or presentations.

## When to Consider Alternatives to Hugging Face

1. **High Performance Needs**  
   - If your application requires ultra-low latency (sub-millisecond) and high-throughput processing, Hugging Face's hosted solutions may not be the best fit.
   - For real-time tasks like high-frequency trading, real-time language translation, or AI-powered chatbots handling thousands of queries per second, consider deploying models directly on specialized hardware (e.g., NVIDIA GPUs or TPUs). This ensures maximum performance and responsiveness.  

3. **Specialized Tasks**  
   - Applications involving custom machine learning architectures, unique algorithms, or domain-specific models may require tailored solutions beyond Hugging Face's pre-trained models.
   - Research-intensive projects like drug discovery, genome analysis, or proprietary models for autonomous driving often demand highly specialized pipelines that Hugging Face may not fully support.  

4. **Cost-Sensitive Applications**  
   - Running large-scale machine learning models continuously can become costly due to computational resource demands, especially when GPU usage is required.
   - For tasks involving extensive data processing, frequent retraining, or 24/7 API availability, consider alternatives like self-hosting models using open-source libraries (TensorFlow, PyTorch) on cloud providers with more cost-effective compute options or even on-premises servers. This can significantly reduce operational expenses while maintaining control over resources.
