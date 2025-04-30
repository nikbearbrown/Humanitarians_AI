### **Discriminating Terms for Identifying Job Listings: A Lexical and Statistical Approach**  

### **Abstract**  
Accurately distinguishing job postings from general web text is essential for building high-quality job search engines, recruitment tools, and labor market analytics. In this study, we introduce a **Discriminating Terms** approach—words and phrases that statistically differentiate job listings from generic text found on Wikipedia and random web pages. Our method involves compiling a dataset of **verified job postings and non-job-related text**, then applying **Poisson distribution-based statistical analysis** to identify terms that occur significantly more often in job listings. These Discriminating Terms are further expanded with **synonyms, abbreviations, and domain-specific jargon** to enhance classification accuracy. We then train machine learning models, including **Naïve Bayes, Logistic Regression, Support Vector Machines (SVM), and Transformer-based architectures (BERT, JobBERT)**, to automatically detect job listings in large text corpora.  

### **Introduction**  
Extracting job postings from web content is a fundamental task for job search platforms, workforce analytics, and recruitment automation. However, traditional keyword-based methods struggle with **ambiguity and overlap**, as job-related terms like "manager," "contract," or "apply" also frequently appear in unrelated contexts.  

To improve accuracy, we introduce a method based on **Discriminating Terms**—words and phrases statistically overrepresented in job postings compared to general web text. Our approach involves:  
1. **Compiling an expert-verified dataset** of job postings and non-job-related text.  
2. **Applying statistical methods** to identify terms that reliably indicate job-related content.  
3. **Enhancing terms lexically** through synonyms, abbreviations, and industry-specific variations.  
4. **Training machine learning classifiers** to automate job listing detection.  

Our findings contribute to **automated job text classification**, improving job aggregation, spam filtering, and labor market analytics.  

### **Methods**  

#### **1. Data Collection and Expert Curation**  
We compiled a dataset consisting of:  
- **Job Listings:** Scraped from job boards, company career pages, and recruitment sites.  
- **Non-Job Text:** Random Wikipedia articles, blogs, and general web pages.  

Human annotators verified the dataset to ensure clear separation between job-related and non-job-related content.  

#### **2. Identifying Discriminating Terms**  
We define **Discriminating Terms** as words that appear **significantly more frequently** in job postings than in general web text.  

1. **Text Preprocessing:**  
   - Convert text to lowercase.  
   - Remove stopwords (e.g., "the," "and," "is").  
   - Apply lemmatization (e.g., "manages" → "manage").  

2. **Statistical Term Comparison:**  
   - Compute word frequencies in job postings (\( C_{job} \)) and non-job text (\( C_{non-job} \)).  
   - Normalize frequencies:  
     $$ f_{job}(w) = \frac{C_{job}(w)}{\sum C_{job}} $$  
     $$ f_{non-job}(w) = \frac{C_{non-job}(w)}{\sum C_{non-job}} $$  
   - Apply **Poisson distribution analysis** to detect significant overrepresentation of terms in job postings.  

3. **Lexical Expansion:**  
   - **Synonyms & Variants:** ("position" → "role," "opening").  
   - **Acronyms & Abbreviations:** ("FT" → "full-time").  
   - **Industry-Specific Phrases:** ("remote work," "equity compensation").  

### **3. Building a Job Listing Classifier**  
We use **Discriminating Terms** as features in machine learning models:  
- **Naïve Bayes & Logistic Regression** for term frequency-based classification.  
- **SVMs** to learn optimal decision boundaries.  
- **Transformer-based models (BERT, JobBERT)** for deep semantic understanding.  

### **4. Evaluation and Validation**  
- **Performance Metrics:** Precision, recall, F1-score.  
- **Benchmarking Against Baseline Methods:** Comparison with keyword filtering and rule-based approaches.  
- **Error Analysis:** Manual review of misclassified texts to refine the Discriminating Terms.  

### **Conclusion**  
By identifying Discriminating Terms, we develop a robust **AI-driven method for detecting job postings**, improving job search accuracy and reducing irrelevant results. Our approach enhances job aggregation, recruitment automation, and labor market research.

