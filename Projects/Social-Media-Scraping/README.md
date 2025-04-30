# **Instagram Scraper: Automated Image and Data Extraction with AI-Driven Captioning**  

#### **Overview**  
This project is an **Instagram scraper** built using Python, specifically leveraging the **Instaloader library** to extract **images, captions, metadata, and user engagement details** from Instagram posts. It includes advanced **anti-detection mechanisms**, **proxy management**, and an **AI-powered image captioning model** to generate descriptions for scraped images. The extracted data is structured into a **pandas DataFrame** and saved in an **Excel sheet** for further analysis.

---

### **Key Features**  

1. **Instagram Post Scraping**  
   - Fetches images, captions, likes, comments, post URLs, and timestamps from a specified Instagram profile.  
   - The number of posts to extract is customizable via the **Max Post** parameter.  

2. **Anti-Ban Mechanisms**  
   - Uses a **proxy rotation system** to prevent IP bans by Instagram.  
   - Employs **random user-agent spoofing** to mimic human browsing behavior.  
   - Implements **randomized request delays** to avoid detection and throttling.  

3. **AI-Powered Image Captioning**  
   - Uses the **BLIP Base Model** from Hugging Face to generate automatic captions for downloaded images.  
   - The AI-generated captions are stored alongside the original Instagram captions for comparison.  

4. **Data Storage and Organization**  
   - Downloads images and saves them in a **user-specific folder**.  
   - Extracted metadata is compiled into a **pandas DataFrame** and exported to an **Excel (.xlsx) file**.  
   - After processing, the **image folder is automatically deleted**, leaving only structured tabular data.  

5. **Error Handling & Logging**  
   - Implements error-handling mechanisms to prevent crashes during data extraction.  
   - Logs **proxy usage, request status, and data retrieval progress** for transparency and debugging.  

---

### **How the Instagram Scraper Works**  

#### **1. Proxy Management & Anti-Ban Measures**  
   - A **list of proxies** is stored in a file and loaded at runtime.  
   - **Random proxies** are assigned to each request to reduce the risk of detection.  
   - **User-agent strings** are dynamically generated to mimic a real browser session.  
   - **Request delays** are introduced between interactions to simulate natural browsing behavior.  

#### **2. Downloading Instagram Data**  
   - The script initializes a session with **Instaloader** and loads a **specified Instagram username**.  
   - A loop iterates through the target profile’s posts, extracting:  
     - **Post URLs**  
     - **Images**  
     - **Original captions**  
     - **Like and comment counts**  
     - **Date of publication**  
   - Every **two posts**, the scraper **switches to a new proxy** to minimize detection risk.  

#### **3. Image Processing and Caption Generation**  
   - Downloaded images are processed through the **BLIP Base Model** from Hugging Face.  
   - The AI model generates a **caption based on the image content**.  
   - Captions are stored alongside original Instagram captions for comparison.  

#### **4. Data Structuring and Storage**  
   - The extracted data is **compiled into a pandas DataFrame**.  
   - It includes fields such as:  
     - **Post URL**  
     - **Generated AI Caption**  
     - **Original Instagram Caption**  
     - **Likes and Comments Count**  
     - **Post Date**  
     - **Image URL**  
   - The DataFrame is then **exported to an Excel file** for structured storage.  
   - Once processing is complete, **all downloaded images are deleted** to save space.  

---

### **Demo Example**  

1. **Running the Script**  
   ```bash
   python scraper.py <instagram_username>
   ```

2. **Data Output Example (Excel Format)**  

| Post URL | AI Caption | Instagram Caption | Likes | Comments | Date | Image URL |
|----------|-----------|-------------------|-------|----------|------|-----------|
| post_url_1 | "A dog sitting on a beach" | "Enjoying the sunset with my pup" | 500 | 20 | 2024-03-01 | image_url_1 |
| post_url_2 | "A person skiing in the snow" | "Fresh powder today!" | 750 | 45 | 2024-03-02 | image_url_2 |

3. **Proxy Rotation Example (Console Output)**  
   ```
   Using proxy: 192.168.1.10:8080
   Fetching post 1/5...
   Switching proxy...
   Using proxy: 192.168.1.20:8080
   Fetching post 2/5...
   ```

---

### **Potential Use Cases**  
- **Market Research:** Analyze engagement metrics, content trends, and audience behavior.  
- **Social Media Monitoring:** Track brand mentions, influencer posts, and hashtag usage.  
- **Dataset Generation:** Collect labeled image datasets for AI/ML training.  
- **Content Curation:** Automate image captioning for social media accounts.  

---

### **Future Enhancements**  
- **Hashtag Analysis:** Extract and analyze hashtags from posts.  
- **Multi-Profile Scraping:** Allow batch processing of multiple Instagram accounts.  
- **Sentiment Analysis:** Use NLP to analyze post sentiment based on captions and comments.  
- **GUI Interface:** Develop a user-friendly UI for non-technical users.  

---

### **Conclusion**  
This **Instagram Scraper** automates **image and metadata extraction** while integrating **AI-driven captioning**. With **proxy rotation, request delays, and user-agent spoofing**, it efficiently gathers **structured social media insights** without triggering detection. The tool offers a **scalable, customizable**, and **anti-ban** solution for **social media analytics, content research, and AI dataset generation**.
