<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# 

---

# 2. DeepSeek's Disruption: This section introduces DeepSeek, a Chinese AI company developing cost-effective and less energy-intensive AI models. While highlighting its technological advancements, it also raises concerns about data privacy and potential government access to user information

The emergence of DeepSeek as a formidable player in the artificial intelligence landscape represents one of the most significant disruptions to the established order of AI development in recent years. As of early 2025, this Chinese AI company has captured global attention with its innovative approach to creating powerful language models at a fraction of the cost and energy consumption of its Western counterparts. Founded in July 2023 and based in Hangzhou, Zhejiang, DeepSeek has rapidly evolved from a newcomer to a serious challenger to industry giants like OpenAI and Anthropic. This comprehensive analysis explores DeepSeek's technological breakthroughs, business strategy, and the growing concerns surrounding data privacy and security that accompany its rise to prominence.

## The Emergence of DeepSeek in the Global AI Landscape

DeepSeek, formally known as Hangzhou DeepSeek Artificial Intelligence Basic Technology Research Co., Ltd., has established itself as a disruptive force in the artificial intelligence sector since its founding in 2023. The company is owned and funded by the Chinese hedge fund High-Flyer, with High-Flyer co-founder Liang Wenfeng serving as CEO for both entities. As of May 2024, Liang maintained a significant 84% ownership stake in DeepSeek through two shell corporations, indicating tight control over the company's direction and operations[^1]. This concentrated ownership structure has allowed DeepSeek to maintain a focused research-oriented approach without the immediate pressures of commercialization that often affect startups in the technology sector.

The company's trajectory took a dramatic turn in January 2025 with the release of its DeepSeek-R1 model and accompanying chatbot, which demonstrated capabilities comparable to industry leaders like OpenAI's GPT-4o and o1. What made this achievement particularly remarkable was not merely the technical performance of the model but the reported efficiency with which it was developed. DeepSeek claimed to have trained its V3 model, a predecessor to R1, for approximately US\$6 million, a stark contrast to the estimated \$100 million spent by OpenAI on GPT-4 in 2023. Furthermore, the company asserted that its model required only about one-tenth of the computing power used for Meta's comparable Llama 3.1 model[^1]. This dramatic reduction in development costs while maintaining competitive performance capabilities sent shockwaves through the AI industry and financial markets.

The impact of DeepSeek's innovation extended beyond technical circles, affecting global financial markets in a profound way. The company's demonstration that advanced AI models could be developed without the massive computational resources previously thought necessary challenged the dominance of established players like Nvidia, whose specialized chips had become the de facto standard for AI development. This revelation contributed to a significant market correction, with Nvidia alone reportedly losing \$600 billion in market value in what was described as the largest drop in US stock market history[^1]. This financial tremor underscored the disruptive potential of DeepSeek's approach to AI development and raised questions about the sustainability of the high-cost model that had dominated the industry.

DeepSeek's rise has been characterized by industry observers as "upending AI," suggesting a fundamental shift in how artificial intelligence systems are developed and deployed. The company's ability to achieve comparable results to Western competitors at a fraction of the cost has been particularly notable in the context of ongoing trade tensions between the United States and China. Ironically, the company's cost-efficient approach was partly born of necessity, as Chinese firms have faced restricted access to advanced Nvidia chipsets due to US export controls implemented as part of the broader trade conflict between the two nations[^1]. This constraint forced DeepSeek to develop alternative approaches that ultimately proved more efficient, demonstrating how innovation can emerge from limitation.

## Technical Innovations and Model Development

DeepSeek's technical journey began in earnest with the release of the DeepSeek-LLM series in November 2023. This initial offering included models with 7 billion and 67 billion parameters in both Base and Chat configurations. The company's accompanying research paper claimed benchmark results that surpassed Llama 2 and most other open-source LLMs available at that time. These models were released under the source-available DeepSeek License, which provides some freedoms for use while maintaining certain restrictions[^1].

The architecture of these early models closely resembled that of Meta's Llama series, utilizing a pre-norm decoder-only Transformer with RMSNorm for normalization, SwiGLU in the feedforward layers, rotary positional embedding (RoPE), and grouped-query attention (GQA). Both the 7B and 67B parameter models featured a vocabulary size of 102,400 using byte-level BPE encoding and supported a context length of 4096 tokens. The training process involved approximately 2 trillion tokens of English and Chinese text, obtained through deduplication of Common Crawl data[^1]. This approach demonstrated DeepSeek's ability to leverage established architectural principles while optimizing for efficiency.

The technical specifications of these models revealed a thoughtful scaling strategy. The 7B parameter model featured 30 layers, a model dimension of 4096, an intermediate dimension of 11008, and 32 attention heads with 32 key-value heads. The significantly larger 67B parameter model increased these specifications to 95 layers, a model dimension of 8192, an intermediate dimension of 22016, 64 attention heads, but only 8 key-value heads[^1]. This configuration allowed for efficient scaling while managing computational requirements. The Chat versions of these models were developed through supervised fine-tuning (SFT) followed by direct policy optimization (DPO), reflecting standard practices in the field for adapting base models to conversational applications.

DeepSeek continued its rapid development pace with the release of the DeepSeek-V2 series in May 2024. This series expanded the company's offerings to include four models: two base models (DeepSeek-V2 and DeepSeek-V2 Lite) and two corresponding chatbots. The development of these models followed a systematic process that began with pretraining on a massive dataset of 8.1 trillion tokens, with a deliberate emphasis on Chinese content (12% more Chinese tokens than English ones). The context length was extended from 4K to 128K tokens using the YaRN technique, resulting in the base DeepSeek-V2 model[^1].

The subsequent refinement process involved supervised fine-tuning with 1.2 million instances focused on helpfulness and 300,000 instances targeting safety improvements. This produced an intermediate Chat SFT model that was not publicly released. The final stage employed reinforcement learning through GRPO (Guided Reinforcement from Policy Optimization) in two distinct phases. The first phase prioritized solving math and coding problems, utilizing a reward model trained on compiler feedback for coding tasks and ground-truth labels for mathematical problems. The second phase focused on making the model helpful, safe, and rule-adherent, employing three separate reward models. The helpfulness and safety reward models were trained on human preference data, while the rule-based reward model was manually programmed. All reward models used in this process were initialized from the Chat (SFT) model[^1]. This sophisticated training approach demonstrated DeepSeek's commitment to addressing both technical performance and alignment with human values.

The culmination of DeepSeek's development efforts came with the January 2025 release of DeepSeek-R1, which represented a significant leap forward in the company's capabilities. This model demonstrated performance comparable to industry leaders like GPT-4o and o1 but maintained the cost and efficiency advantages that had become DeepSeek's hallmark. Released under the MIT License, DeepSeek-R1 quickly gained attention for its combination of high performance and accessibility[^1]. The model's release coincided with the launch of DeepSeek's eponymous chatbot, which brought these capabilities to a broader audience and catalyzed the company's rise to prominence in the global AI conversation.

## Business Strategy and Market Impact

DeepSeek's business approach differs significantly from many of its competitors, with a pronounced emphasis on research rather than immediate commercialization. This strategy has allowed the company to focus on technological advancement without the pressures of short-term revenue generation that often influence corporate decision-making. Additionally, this research-oriented approach has enabled DeepSeek to navigate China's regulatory environment more effectively, as it allows the technology to avoid some of the most stringent provisions of China's AI regulations, which primarily target consumer-facing applications that must comply with government controls on information[^1].

The company's hiring practices reflect this research-first mentality, with a preference for technical abilities over extensive work experience. DeepSeek predominantly recruits recent university graduates or developers early in their AI careers, valuing fresh perspectives and technical aptitude over established industry experience. In an interesting diversification strategy, the company also deliberately hires individuals without computer science backgrounds to enhance its technology's understanding of various knowledge domains, including areas like poetry and China's challenging college admissions exams (Gaokao)[^1]. This interdisciplinary approach helps ensure that DeepSeek's models have broad knowledge capabilities beyond purely technical domains.

DeepSeek's impact on the AI market has been profound, particularly within China. The company's ability to deliver high-performance models at low prices has triggered what observers have described as "China's AI model price war." DeepSeek has been dubbed the "Pinduoduo of AI," referencing the Chinese e-commerce platform known for its budget-friendly approach. This comparison is apt, as DeepSeek's emergence prompted other Chinese tech giants, including ByteDance, Tencent, Baidu, and Alibaba, to reduce the prices of their own AI models in response[^1]. Despite its low-price strategy, DeepSeek has reportedly maintained profitability, contrasting with many of its competitors who operate at a loss to gain market share.

The global significance of DeepSeek's approach extends beyond pricing dynamics. The company's demonstration that advanced AI models can be developed at a fraction of the previously assumed cost challenges fundamental assumptions about the economics of AI development. This revelation has implications for the democratization of AI technology, potentially lowering barriers to entry for organizations and countries with fewer resources. However, it also raises questions about the sustainability of business models built around high-cost, high-performance AI systems, particularly as efficiency improvements continue to accelerate.

## Data Privacy Concerns and Security Implications

Despite DeepSeek's impressive technological achievements, the company's rapid rise has been accompanied by growing concerns regarding data privacy and security. These concerns have been particularly pronounced in Western countries, where regulators and security experts have raised questions about how user data is collected, stored, and potentially shared with the Chinese government.

In early 2025, data authorities across Europe launched investigations into DeepSeek's data collection practices. Information requests were initiated in multiple countries, including Italy, Ireland, Belgium, the Netherlands, and France, seeking to determine whether the AI company's collection of information breaches Europe's General Data Protection Regulation (GDPR) by transferring personal data to China[^2]. These concerns led to concrete actions in some jurisdictions, with Italian authorities blocking the app from Apple and Google app stores while they investigated what data was being collected, for what purpose, where it was being stored, and whether it had been used to train the company's latest AI model[^2].

According to DeepSeek's terms of use, the company collects three types of information from users: directly provided data such as names and email addresses, automatically collected information like IP addresses, and information from third-party sources such as Apple or Google logins[^2]. The agreement states that some of this information is collected through direct monitoring of interactions and usage across devices, and that the app determines when it needs to protect the safety and well-being of its community. This data can be stored "for as long as possible" and used for various purposes, including being shared with third parties such as advertisers, analytics companies, law enforcement, public authorities, and copyright holders[^2].

While such data collection practices are not unique to DeepSeek—OpenAI's ChatGPT and Anthropic's Claude employ similar approaches—the specific concern with DeepSeek relates to the potential transfer of this data to China and its accessibility to Chinese authorities. This concern is amplified by China's legal framework, which differs significantly from Western jurisdictions in terms of government access to private data.

Security researchers have identified potentially serious vulnerabilities in DeepSeek's applications. In February 2025, NowSecure, a mobile application security firm, conducted a comprehensive security and privacy assessment of the DeepSeek iOS mobile app, uncovering multiple critical vulnerabilities that led them to urge enterprises to prohibit its usage in their organizations[^7]. The assessment identified several key risks, including unencrypted data transmission, weak and hardcoded encryption keys, insecure data storage of usernames and passwords, extensive data collection and device fingerprinting, and the transmission of user data to servers in China governed by Chinese laws[^7].

More alarmingly, a report by ABC News in February 2025 claimed that DeepSeek's coding contained capabilities to transfer users' data directly to the Chinese government. According to cybersecurity experts cited in the report, DeepSeek's code included hidden programming with the capability to send user data to CMPassport.com, the online registry for China Mobile, a telecommunications company owned and operated by the Chinese government[^5]. This finding suggested that users who register or log in to DeepSeek might unknowingly be creating accounts in China, potentially making their identities, search queries, and online behavior visible to Chinese state systems[^5].

These security concerns have prompted responses from various organizations. The U.S. House of Representatives' Chief Administrative Officer warned members of Congress and their staff not to use the app, and two U.S. Representatives asked the Trump administration to strengthen existing restrictions on the sale of semiconductor chips to China in an effort to "outcompete" China in AI development and "safeguard Americans' data"[^4]. Similarly, military organizations have implemented bans on the app's use to protect sensitive information and national security interests[^7].

## Legal Framework and Government Access

The legal environment in which DeepSeek operates adds another layer of complexity to privacy concerns. Unlike Western tech companies, which can legally challenge government requests for data access, DeepSeek operates under China's National Intelligence Law, which compels companies to cooperate with government intelligence efforts without transparency or the ability to legally refuse[^8].

While governments worldwide—including the United States and European Union—can subpoena data from tech companies, Western companies typically have legal avenues to challenge these requests in court. Companies like OpenAI, Google, and Meta can push back against excessive government demands, appeal in independent courts, or refuse requests that violate privacy laws like GDPR. DeepSeek, however, lacks these legal protections and must comply with Chinese government demands for data access and content control[^8].

This legal framework has significant implications for user privacy and data security. If the Chinese government were to request access to user data or demand manipulation of AI-generated responses, DeepSeek would have no legal basis to refuse such requests. This situation creates a fundamental difference in the privacy guarantees that can be offered by DeepSeek compared to its Western counterparts, regardless of the technical security measures implemented in its products.

The terms of service for DeepSeek-V3 further highlight potential risks for users. According to an analysis shared on Reddit, DeepSeek's terms place full responsibility for data compliance on users (Section 4.1), stating that if any user data violates legal standards, the user is solely accountable[^6]. The data usage policy (Section 4.2) grants DeepSeek the right to utilize user inputs and outputs to "enhance services," with no straightforward opt-out mechanism, potentially exposing user data to various uses[^6]. Additionally, strict intellectual property clauses (Section 5.1) claim ownership over all content and software associated with DeepSeek's services, potentially leading to legal repercussions even for unintentional misuse[^6].

## Censorship and Content Control

Beyond data privacy concerns, DeepSeek's operation under Chinese jurisdiction raises questions about content censorship and control. Reports indicate that DeepSeek is already engaging in content filtering and censorship practices that align with Chinese government requirements[^8]. This censorship affects not only users in China but potentially all users of DeepSeek's services globally, as the company must comply with Chinese regulations regardless of where its services are accessed.

The implications of this censorship extend beyond political content to potentially include scientific, historical, and cultural information that may be deemed sensitive by Chinese authorities. This creates a situation where users might receive incomplete or biased information without being aware of the filtering taking place. Unlike Western AI companies, which typically disclose content moderation policies and provide transparency reports, DeepSeek operates in an environment with different expectations regarding transparency and disclosure.

The combination of data collection, potential government access, and content censorship creates a complex risk profile for DeepSeek users, particularly those in sensitive positions or handling confidential information. Organizations must weigh the technological benefits of DeepSeek's models against these privacy and security considerations when deciding whether to adopt these tools.

## Open Source Status and Technical Accessibility

One of DeepSeek's distinguishing features is its positioning as an "open weight" AI model, which provides some degree of transparency and accessibility compared to fully proprietary systems. However, this status falls short of true open-source software, as it places certain limitations on how the models can be modified and used[^1]. This distinction is important for understanding both the technical accessibility of DeepSeek's technology and its implications for security auditing and verification.

The "open weight" approach allows researchers and developers to examine certain aspects of DeepSeek's models, potentially identifying vulnerabilities or biases. However, the limitations on modification may restrict the ability of the broader community to address any issues discovered. This creates a situation where problems might be identifiable but not necessarily fixable without DeepSeek's involvement.

Despite these limitations, DeepSeek's relatively open approach has contributed to its rapid adoption and integration into various applications. The availability of model weights and certain technical details has enabled developers to experiment with and build upon DeepSeek's technology, accelerating its impact on the broader AI ecosystem. This openness, combined with the models' impressive performance and efficiency, has made DeepSeek an attractive option for many developers and organizations seeking advanced AI capabilities without the high costs associated with proprietary systems.

## Global Implications and Future Trajectory

The emergence of DeepSeek as a major player in the global AI landscape has significant implications for international technology competition, particularly in the context of US-China relations. DeepSeek's ability to develop high-performance AI models despite US export controls on advanced semiconductor technology demonstrates China's growing capability to innovate around such restrictions. This success story may influence future policy decisions regarding technology transfer and export controls, as it suggests that such measures may delay but not prevent technological advancement.

For the broader AI industry, DeepSeek's cost-efficient approach to model development challenges established assumptions about the resources required to create cutting-edge AI systems. This could accelerate the democratization of AI technology, making advanced capabilities accessible to a wider range of organizations and countries. However, it also raises questions about the sustainability of business models built around high-cost AI development and the potential for market consolidation as efficiency improvements continue.

The privacy and security concerns surrounding DeepSeek highlight the growing importance of data governance and sovereignty in the digital age. As AI systems become more powerful and ubiquitous, questions about who controls the data used to train these systems and who has access to the information they generate become increasingly critical. The divergent approaches to data privacy and government access between China and Western democracies create challenges for global technology adoption and regulation, potentially leading to a more fragmented digital landscape.

## Conclusion

DeepSeek represents a significant disruption to the established order of AI development, demonstrating that advanced language models can be created at a fraction of the previously assumed cost and computational requirements. The company's rapid rise to prominence highlights both the accelerating pace of AI innovation and the global nature of technological competition in this field. However, this technological achievement comes with important caveats regarding data privacy, security, and the legal framework in which DeepSeek operates.

The concerns raised by regulators, security researchers, and privacy advocates regarding DeepSeek's data collection practices and potential government access to user information cannot be dismissed as mere protectionism or competitive anxiety. They reflect genuine differences in legal frameworks and expectations regarding data privacy and government surveillance between China and Western democracies. Users and organizations considering DeepSeek's technology must carefully weigh these considerations against the technological benefits offered.

As the global AI landscape continues to evolve, the story of DeepSeek illustrates the complex interplay between technological innovation, economic competition, national security concerns, and individual privacy rights. Navigating this complexity will require thoughtful approaches from policymakers, industry leaders, and users alike, balancing the benefits of technological advancement with the protection of fundamental rights and values.

The disruption caused by DeepSeek may ultimately prove beneficial for the AI industry as a whole, driving efficiency improvements and cost reductions that make advanced AI capabilities more accessible. However, this progress must be accompanied by appropriate safeguards and transparency measures to ensure that these powerful technologies serve the broader public interest while respecting individual rights and democratic values.

<div style="text-align: center">⁂</div>

[^1]: https://en.wikipedia.org/wiki/DeepSeek

[^2]: https://www.euronews.com/next/2025/02/06/what-are-the-data-privacy-issues-plaguing-chinese-ai-deepseek-in-the-eu

[^3]: https://www.bbc.com/news/articles/c5yv5976z9po

[^4]: https://www.npr.org/2025/01/31/nx-s1-5277440/deepseek-data-safety

[^5]: https://abcnews.go.com/US/deepseek-coding-capability-transfer-users-data-directly-chinese/story?id=118465451

[^6]: https://www.reddit.com/r/LocalLLaMA/comments/1hvp5z1/about_deepseek_v3_privacy_concern/

[^7]: https://www.nowsecure.com/blog/2025/02/06/nowsecure-uncovers-multiple-security-and-privacy-flaws-in-deepseek-ios-mobile-app/

[^8]: https://proton.me/blog/deepseek

[^9]: https://www.bloomberg.com/news/articles/2025-02-25/deepseek-reopens-access-to-ai-model-as-chinese-rivalry-escalates

[^10]: https://www.reuters.com/technology/artificial-intelligence/deepseek-rushes-launch-new-ai-model-china-goes-all-2025-02-25/

[^11]: https://www.reuters.com/technology/artificial-intelligence/chinese-universities-launch-deepseek-courses-capitalise-ai-boom-2025-02-21/

[^12]: https://krebsonsecurity.com/2025/02/experts-flag-security-privacy-risks-in-deepseek-ai-app/

[^13]: https://www.nature.com/articles/d41586-025-00259-0

[^14]: https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html

[^15]: https://www.deepseek.com

[^16]: https://www.wired.com/story/deepseek-ai-china-privacy-data/

[^17]: https://www.cnn.com/2025/01/27/tech/deepseek-stocks-ai-china/index.html

[^18]: https://www.forbes.com/sites/larsdaniel/2025/02/01/deepseek-data-leak-exposes--1000000-sensitive-records/

[^19]: https://www.youtube.com/watch?v=hFTqQ4boR-s\&vl=en-US

[^20]: https://www.wiz.io/blog/wiz-research-uncovers-exposed-deepseek-database-leak

