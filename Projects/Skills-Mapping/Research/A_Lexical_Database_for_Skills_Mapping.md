This paper introduces \"AI4ED Lex,\" an innovative lexical database
specifically designed to refine the process of skills mapping across a
variety of job-related texts, including job descriptions and educational
materials such as course syllabi. Our method utilizes a comparative
analysis that scrutinizes word frequencies within job descriptions
against those in a comprehensive dataset of Wikipedia articles,
culminating in the creation of a lexicon parallel to WordNet. The
Poisson distribution is applied within our approach to predict the
occurrence of specific, employment-related terms.

Central to our database are \"Discriminating Terms,\" also known as
\"Tags\" which are indicative of employment-related content and serve as
linear discriminators. These terms are optimized for text mining by
mapping them to their spelling variants, synonyms, meronyms, hyponyms,
acronyms, and stemmed versions. Additionally, we meticulously categorize
each job tag into one of six classifications: Certification, Language,
Job Title, Sector, Skill, or Trait. For instance, a \"Certification\"
like CISCO Certified Network Professional, a \"Language\" such as
Castilian Spanish or programming languages like C++, a \"Job Title\"
like .NET Engineer, a \"Sector\" such as Biotech, a \"Skill\" like
Apache Spark, and \"Traits\" such as the ability to lift 50 lbs are all
systematically organized and interconnected within AI4ED Lex.

By organizing English job-related terminology into synonym sets with
semantic linkages, our database enriches the traditional WordNet
structure with a focus on the professional lexicon, thus enabling a
deeper understanding of the language used in the employment and
education domains. AI4ED Lex also incorporates Large Language Models
(LLMs) to verify and augment the lexicon, ensuring it remains a dynamic
and contemporary linguistic resource.

The AI4ED Lex serves as an advanced tool that significantly improves the
tagging of free text, leading to more efficient and precise skill and
requirement mapping. Integrating time-honored lexicographic data with
cutting-edge computational techniques, AI4ED Lex delivers a versatile
database configured for machine-based analysis, ready to address the
needs of the constantly transforming spheres of employment and
education.

# Introduction

Skills ontologies have become essential tools in the evolving landscape
of employment, education, and workforce development. They serve as
structured repositories of knowledge that describe the relationships
between skills, tasks, and occupational roles. Despite the presence of
various skills ontologies, many remain proprietary and are not openly
accessible. Moreover, none of these frameworks adequately address the
complexities of parsing free text, which includes dealing with spelling
variants, synonyms, meronyms, hyponyms, acronyms, and stemmed versions
of terms.

Furthermore, the challenge of polysemy---where a single word can have
multiple meanings---presents a significant hurdle for systems designed
to process natural language input. For instance, the word \"Java\" could
refer to an island in Indonesia, a type of coffee, or a popular
programming language. Our \"Discriminating Terms\" methodology is
specifically tailored to overcome this obstacle by enabling the
Contextual Representations of words. This approach allows us to discern
the intended meaning of a term like \"Java\" in a given context; for
example, when the term appears alongside other job tags such as
\"programming,\" it effectively signals the computer science-related
usage.

Several existing skills ontologies and frameworks, while useful, lack
this level of nuanced interpretation:

-   ESCO: Offers a multilingual classification of skills, competences,
    qualifications, and occupations, yet does not fully delve into the
    intricacies of language variances.

-   O\*NET: Provides a rich database of comprehensive worker attributes
    and job characteristics, but it does not specifically focus on the
    challenges posed by free-form text analysis.

-   SFIA: Acts as a globally recognized IT skills framework, which is
    invaluable for structured IT skill assessment but does not address
    broader linguistic complexities.

-   CaSS Framework: Useful for documenting, tracking, and sharing
    competencies, skills, and achievements, yet lacks the semantic depth
    to parse and understand free text effectively.

-   ACSF: Assists with the core skills in literacy and numeracy across
    various performance levels, but does not provide a mechanism for
    disambiguating polysemous terms.

\"AI4ED Lex\" aims to fill these gaps by providing an open-source
lexicon that not only draws on the structured information of these
ontologies but also enhances it by capturing the multifaceted nature of
language as it appears in real-world text. Our goal is to create a
comprehensive tool that accurately maps skills and qualifications,
bridging the divide between rigid taxonomies and the dynamic, sometimes
ambiguous, language of the job market.

For each skill tag in the AI4ED Lex database, we meticulously document
the following fields to ensure comprehensive coverage and utility:

Tag Name: This field specifies the unique identifier or name of the
skill tag.

Definition: A concise explanation or description of the skill tag,
providing clarity on its meaning and application.

Class: This field categorizes the skill tag into one of six predefined
classes:

-   Certification

-   Language

-   Job Title

-   Sector

-   Skill

-   Trait

Semantic Relations:

-   Synonymy: Utilizes sets of synonyms (synsets) to represent word
    senses, serving as AI4ED Lexs fundamental relation. It is a
    symmetric relation between word forms, indicating similarity or
    interchangeability in context.

-   Antonymy: Represents a symmetric semantic relation between word
    forms that denote opposite meanings, particularly significant in
    structuring the meanings of adjectives and adverbs.

-   Hyponymy and Hypernymy: These transitive relations between synsets
    define a hierarchical structure, with hyponymy indicating a more
    specific instance (sub-name) and hypernymy a more general category
    (super-name).

-   Meronymy and Holonymy: Complex semantic relations that describe
    part-whole relationships. WordNet differentiates among component
    parts, substantive parts, and member parts within this category.

-   Troponymy: Analogous to hyponymy for nouns, troponymy relates to
    verbs, describing a manner or method of action, though resulting in
    shallower hierarchies.

Acronyms: This field lists the recognized abbreviations or acronyms
related to the skill tag, facilitating identification and understanding
of shortened forms.

Spelling Variants: Captures various spellings of the skill tag,
acknowledging regional differences and common misspellings to enhance
searchability and recognition.

Each of these fields plays a crucial role in enriching the AI4ED Lex
database, ensuring that users have access to a detailed and navigable
resource for exploring skills, their definitions, classifications, and
related semantic nuances. Through this structured approach, AI4ED Lex
aims to support a wide array of applications, from job description
analysis to educational content development, by providing a clear and
organized lexicon of skills and competencies.

# Methods

## Discriminating Terms

In our quest to establish a robust set of \"Discriminating Terms,\" we
embarked on an extensive analysis of one million job descriptions
sourced from Kaggle datasets, alongside one million randomly selected
Wikipedia articles. This comparative analysis hinged on the application
of a Poisson distribution, allowing us to discern the probability of
encountering specific job-related terms within a dataset.

The formula employed is as follows:

(eq. 1) Poisson distribution:
$$p(n | N, f) = e^{-Nf} \cdot \frac{(Nf)^n}{n!}$$

Where: - $n$ is the frequency of a job-related term within a category of
job descriptions. - $N$ represents the total count of terms within that
job description category. - $f$ indicates the term's overall frequency
in the combined corpus, ascertained by the ratio of term count in
Wikipedia articles to the total term count in Wikipedia.

To avoid floating-point errors, we reformulate the Poisson equation in
logarithmic terms:

(eq. 2) $$\ln p(n | N, f) = -Nf + n \ln(Nf) - \ln(n!)$$

When handling larger term counts, $n$, we compute $n!$ using Stirling's
approximation. This statistical approach led us to isolate a collection
of \"Discriminating Terms\" that signify job-related content. These
terms serve as linear discriminators within our lexical database,
forming the basis of a likelihood statistic that, together with other
data features, is used to classify job descriptions.

## Enhancing Semantic Annotation with NLTK, spaCy, and PyDictionary

In our endeavor to augment the AI4ED Lex database with detailed
linguistic features for job tags, we integrated three distinguished
Python libraries for their exceptional natural language processing (NLP)
capabilities: NLTK, spaCy, and PyDictionary. These tools were
instrumental in offering a rich tapestry of synonyms, hyponyms,
meronyms, and crucially, definitions, which played a pivotal role in
comprehending the essence of job-related terms.

While all three libraries contributed significantly to building semantic
relationships, NLTK and PyDictionary were particularly valuable for
incorporating definitions into our database. These definitions provide
straightforward explanations or descriptions of terms, enhancing the
databases utility for users seeking to understand complex or unfamiliar
job-related terminology.

*NLTK (Natural Language Toolkit)*

NLTK is a comprehensive library for natural language processing (NLP) in
Python. It includes access to the WordNet database, which is a large
lexical database of English. WordNet links words into semantic relations
including synonyms, hyponyms (more specific terms), and meronyms
(part-of relations).

-   Synonyms: Can be found using synonym sets (synsets).

-   Hyponyms: Can be accessed through synset relations.

-   Meronyms: Also accessible via synset

![Lexical mapping with NLTK and
WordNet](Art/WordNet.png){#fig:Lexical mapping with NLTK and WordNet
width="90%"}

NLTK (Natural Language Toolkit): NLTKs integration with the WordNet
database was pivotal, not just for mapping synonyms, hyponyms, and
meronyms, but also for accessing the definitions of terms within the
WordNet lexicon. This added a layer of depth to our semantic
annotations, enabling a richer understanding of each terms context and
usage.

*spaCy*

spaCy is another powerful and modern library for advanced NLP. While
spaCy itself is more focused on syntax than semantics, it integrates
well with other resources and can be used alongside WordNet through
extensions or additional packages like spacy-wordnet

![Lexical mapping with
spaCy](Art/Spacy.png){#fig:Lexical mapping with spaCy width="90%"}

*PyDictionary*

PyDictionary is a dictionary module for Python that can be used to find
meanings, translations, synonyms, and antonyms of words. It works by
scraping websites, so its reliability might depend on the structure of
the source websites.

Although primarily used for its quick access to synonyms and antonyms,
PyDictionarys ability to scrape definitions from various online sources
was equally beneficial. This feature allowed us to compile a diverse set
of explanations for a wide range of terms, further enriching the AI4ED
Lex database.

*Acronym Annotation Limitation*

Despite the comprehensive capabilities of these libraries, its important
to note that none were inherently designed to facilitate the annotation
of acronyms directly. Recognizing this gap, we employed heuristic
methods specifically developed for acronym detection within our dataset.
This approach enabled us to identify and annotate acronyms effectively,
albeit without the direct support of our chosen NLP libraries.

*Semantic Annotation Methodology Summary*

Our methodology for semantic annotation involved:

-   Semantic Analysis: Utilizing NLTK and spaCy for deep linguistic
    analysis, extracting synonyms, hyponyms, meronyms, and leveraging
    NLTK's access to WordNet for definitions.

-   Lexical Lookup: Employing PyDictionary for additional definitions,
    expanding our databases explanatory content.

-   Deduplication and Annotation: Carefully removing duplicates from the
    collated data to ensure uniqueness and applying enriched semantic
    annotations to job tags, including synonyms, related terms, and
    definitions. However, the annotation of acronyms was conducted
    through custom-developed heuristic tests, given the limitations of
    the libraries in this aspect.

By meticulously combining these resources and approaches, we succeeded
in creating a semantically enriched, definition-inclusive job tag
lexicon for the AI4ED Lex database. This enhanced lexicon not only aids
in deciphering the language of employment but also advances the
precision of skill mapping in the employment and education sectors,
bridging linguistic gaps with the latest in computational linguistics
and NLP technology.

## Acronym Detection Heuristics

Acronym identification poses distinct challenges, as conventional
linguistic tools are not designed to recognize acronyms based on
synonyms, hyponyms, meronyms, and definitions directly. To tackle this,
we developed a heuristic methodology aimed at identifying acronyms
within a broad dataset of job descriptions and Wikipedia articles. This
method analyzes word sequences (n-grams) to find potential acronyms,
outlined in four heuristic tests:

*Classic Acronym Test:* This test matches each acronym letter with the
initial letters of corresponding words in its full form, omitting common
stop words like \"of\", \"the\", and \"and\". For example:

-   Project Management Professional (PMP): Validates project management
    skills, certified by the Project Management Institute (PMI).

-   Certified Information Systems Security Professional (CISSP):
    Confirms information security expertise, offered by (ISC)².

-   Registered Health Information Administrator (RHIA): Signifies
    expertise in patient health information management.

*Skip-a-Word Acronym Test:* This test allows skipping a word in the
acronyms expanded form, recognizing phrases where one word isnt
represented in the acronym. Examples include:

-   Certified in Risk and Information Systems Control (CRISC): By ISACA,
    for IT professionals to manage risks and control information
    systems.

-   Technology Infrastructure Library (ITIL): Focuses on aligning IT
    services with business needs through a set of detailed practices.

*Substitution Acronym Test:* Focuses on acronyms formed from non-initial
letters of words. This test breaks down compound words into basic
components to identify acronyms. Examples are:

-   Certified Wireless Network Administrator (CWNA): Indicates expertise
    in wireless network administration.

-   Microsoft Certified: Azure Fundamentals (AZ-900): Demonstrates
    foundational knowledge of cloud services with Microsoft Azure.

*Composite Acronym Test:* Identifies acronyms that combine phrases with
acronyms, recognizing when an acronym is part of a larger term. Examples
include:

-   Bachelor of Science in Nursing (BSN-RN): Indicates a nursing degree
    followed by licensure.

-   Doctor of Pharmacy (PharmD): Signifies the achievement of a
    doctorate in pharmacy.

Our approach was validated through a manual review of 500 randomly
selected acronym/long-form pairs from our dataset, resulting in a 97.9%
accuracy rate. This high degree of precision highlights the
effectiveness of our heuristic methodology in acronym detection.

## Contextual Rolling Window Classification (CRWC)

The technique of using a rolling 50-word window for classifying terms
into categories such as Certification, Language, Job Title, Sector,
Skill, or Trait leverages the contextual proximity of specific keywords
or phrases to the term in question. This approach is particularly useful
in large textual datasets like job descriptions where specific terms
need to be accurately identified and categorized. The following outlines
the effective implementation of this technique:

1.  **Rolling Window Concept:** A rolling window of 50 words is moved
    through the text sequentially. At each step, the window encompasses
    a portion of the text for analysis, focusing on the presence of
    specific keywords or phrases indicative of the six classifications.

2.  **Keyword Frequency Analysis:** Within each window, perform a
    frequency analysis of keywords associated with each of the six
    categories. For example, words like "certificate" or "certification"
    are indicators of the Certification category. The unusually high
    frequency of these keywords in proximity to a term suggests the
    classification of that term.

3.  **Contextual Proximity:** Evaluate the proximity of discriminative
    keywords to the target term within the window. If keywords relevant
    to a specific category (e.g., Certification) are found within one or
    two sentences of the target term, it strongly suggests that the term
    belongs to that category.

4.  **Discriminating Terms or Tags:** Utilize "Discriminating Terms" or
    "Tags" that serve as linear discriminators. These are optimized for
    text mining by mapping them to their spelling variants, synonyms,
    meronyms, hyponyms, acronyms, and stemmed versions. This
    optimization aids in the accurate classification of terms even when
    they appear in varied forms.

5.  **Classification:** Once the analysis within the rolling window
    identifies a strong association between the target term and
    discriminative keywords for a category, classify the term
    accordingly. For instance, if the term is closely associated with
    keywords like "certification," it is classified under Certification.

6.  **Systematic Organization:** Following classification,
    systematically organize each job tag within the AI4ED Lex database.
    This involves placing the term in its respective category, whether
    it be a Certification like "CISCO Certified Network Professional," a
    Language such as "Castilian Spanish," a Job Title like ".NET
    Engineer," a Sector such as "Biotech," a Skill like "Apache Spark,"
    or a Trait such as "the ability to lift 50 lbs."

This technique, by leveraging both the frequency of category-specific
keywords and their proximity to target terms within a rolling window,
enables a nuanced and contextually aware classification system. It is
particularly effective in parsing and understanding complex datasets,
thereby enhancing the precision and utility of the AI4ED Lex database in
mapping employment-related content.

*Statistical Method for Associating Tags with Categories*

To determine when the occurrence of contextual words like
\"certification\" related to a given tag is statistically unusual enough
to confidently make an association, statistical significance testing
methods, such as the z-score, can be employed.

*Step 1: Hypothesis Definition* Define the Null Hypothesis ($H_0$) and
the Alternative Hypothesis ($H_1$):

-   $H_0$: The occurrence of the word \"certification\" near a given tag
    happens by chance at a known average rate ($\mu$) in the corpus.

-   $H_1$: The occurrence of \"certification\" near the tag is
    significantly higher than the population mean, indicating a
    non-random association.

*Step 2: Calculate the Test Statistic* Compute the z-score, which
indicates the number of standard deviations an observation is from the
mean: $$z = \frac{(\bar{x} - \mu)}{\sigma / \sqrt{n}}$$ Where:

-   $\bar{x}$ is the sample mean (average occurrence of
    \"certification\" in the 50-word window around the tag).

-   $\mu$ is the population mean.

-   $\sigma$ is the population standard deviation.

-   $n$ is the sample size.

*Step 3: Significance Level* Choose a significance level ($\alpha$),
such as 0.05 or 0.01, which represents the probability of rejecting the
null hypothesis when it is actually true.

*Step 4: Compare z-score to Critical Value* Determine the critical value
from a z-table corresponding to the chosen $\alpha$. If the calculated
z-score exceeds this value, reject $H_0$ in favor of $H_1$.

*Step 5: Making the Association* If $H_0$ is rejected, conclude that the
occurrence of \"certification\" near the tag is statistically
significant, thus confidently associating the tag with the
\"Certification\" category.

*Considerations:*

-   This method assumes the normal distribution of word occurrences,
    which might require validation or alternative tests if not met.

-   Adjust for multiple comparisons if testing numerous tags to avoid
    Type I error rate inflation.

-   Complement statistical testing with contextual and semantic analysis
    to ensure accuracy.

Employing this statistical testing framework allows for the systematic
assessment of the significance of contextual word occurrences and
confidently categorizes terms based on statistical evidence.

## LLM Enrichment

The AI4ED Lex database documents several key fields for each skill tag
to ensure utility and thoroughness: Tag Name (the skill's identifier),
Definition (a brief description), and Class (categorized into six types:
Certification, Language, Job Title, Sector, Skill, Trait). Semantic
Relations covered include Synonymy (synsets for word senses), Antonymy
(opposites), Hyponymy and Hypernymy (specific vs. general), Meronymy and
Holonymy (part-whole relationships), and Troponymy (verb hierarchies).
Additionally, Acronyms and Spelling Variants are noted to recognize
abbreviations and alternate spellings. These elements collectively
enhance the AI4ED Lex, making it a rich resource for skill exploration
and application across various fields, such as job description analysis
and educational development.

The integration of Large Language Models (LLMs) into the AI4ED Lex
database workflow presents a sophisticated approach to ensuring the
completeness and accuracy of skill tag fields. LLMs can be harnessed to
fill missing data and verify existing information by systematically
interacting with an API designed for this purpose.

Here's an outline of how LLMs can be employed to enhance the database:

1.  **Identifying Missing or Incomplete Data:** The first step involves
    using scripts or manual inspection to identify skill tags with
    missing or incomplete fields within the AI4ED Lex database. These
    could include undefined acronyms, incomplete definitions, or
    unclassified tags.

2.  **Generating LLM Prompts:** For each identified gap, generate
    specific prompts that clearly describe what information is needed.
    For example, if a skill tag's definition is missing, the prompt
    could be: "Provide a concise definition for \[Skill Tag Name\].\"

3.  **API Integration with LLMs:** Set up an API integration with an LLM
    service. This API acts as the intermediary, sending prompts to the
    LLM and receiving the model's responses. The integration should be
    capable of handling batch requests to optimize the process.

4.  **Submitting Prompts and Receiving Responses:** Through the API,
    submit the generated prompts to the LLM. The LLM processes these
    prompts and returns responses that contain the requested information
    or corrections. This step may involve repeated API calls for
    different types of data needed.

5.  **Validating LLM Responses:** Incorporate a validation step to
    ensure the accuracy of the LLM-generated information. This could
    involve cross-referencing with trusted sources or a secondary review
    by human experts. Validation is crucial to maintain the integrity of
    the database.

6.  **Updating the AI4ED Lex Database:** Once the LLM responses are
    validated, update the database with the new or corrected
    information. This step should also include a timestamp or version
    control mechanism to track changes and updates made with the help of
    LLMs.

7.  **Continuous Monitoring and Improvement:** Establish a continuous
    monitoring system to regularly check the database for gaps or
    inaccuracies. LLMs can be re-engaged periodically or as new
    information becomes available to keep the database current and
    comprehensive.

Utilizing LLMs in this manner offers several advantages, including
automating the process of filling missing data, enhancing the accuracy
of skill tags, and reducing the manual effort required for database
maintenance. Moreover, LLMs can provide insights and information that
might not be readily available, thereby enriching the database with
nuanced understanding and coverage of skills, competencies, and
job-related terms.

By leveraging LLMs through API integration, the AI4ED Lex database can
achieve higher levels of completeness and accuracy. This method not only
streamlines the process of data verification and completion but also
ensures that the database remains a valuable resource for its users,
supporting a wide range of applications in job analysis and educational
content development.

## Tagging Kaggle Jobs Data

In our study, we gathered hundreds of thousands of job descriptions from
Kaggle, aiming for diversity across various fields, and systematically
tagged them using the AI4ED Lex semantic framework to categorize them
into specific classes like Certification, Language, Job Title, among
others. To ensure the accuracy of our tagging, we randomly selected a
subset of these descriptions for manual inspection, where experts
verified the tags correctness. This meticulous process of collection,
tagging, and validation, coupled with adjustments based on manual review
findings, not only reinforced the reliability of our dataset but also
provided an in-depth view of the skill demands across the labor market.
Through this comprehensive approach, we established a solid foundation
for our analysis, emphasizing precision in semantic tagging and the
importance of a diverse and representative dataset.

*Data Collection*

Our study initiated with an extensive data collection phase, wherein
hundreds of thousands of job descriptions were aggregated from Kaggle.
The platform, known for its vast repositories of datasets, served as a
critical resource for obtaining a diverse array of job descriptions
spanning a wide range of fields. This comprehensive collection aimed to
cover the broad spectrum of the labor market, ensuring the inclusivity
and representativeness of our dataset.

*Tagging Process* Upon the compilation of job descriptions, each entry
underwent a systematic tagging process. Utilizing the AI4ED Lex
databases semantic classification framework, we annotated the job
descriptions with relevant tags. These tags encapsulated key attributes
of each job, categorizing them into predefined classes such as
Certification, Language, Job Title, Sector, Skill, or Trait. This
tagging phase was instrumental in structuring the dataset for detailed
analysis, allowing for the nuanced exploration of skills and
qualifications demanded across various sectors.

*Random Sampling for Verification*

To validate the accuracy of our tagging process, we employed a rigorous
verification strategy. A random sample was drawn from the tagged
dataset, ensuring an unbiased selection of job descriptions for review.
The size of this sample was determined based on statistical principles
to represent the larger dataset accurately while remaining manageable
for manual inspection.

*Manual Inspection*

The selected job descriptions from the random sample were then subjected
to a meticulous manual review. This phase involved expert evaluators
cross-checking each tag for correctness and relevance. The manual
inspection aimed to identify and correct any inaccuracies or
inconsistencies in the tagging process, thereby enhancing the
reliability of the dataset. *Adjustments and Reiterations* Findings from
the manual inspection informed subsequent adjustments to the tagging
algorithm and process. In cases where systematic errors or biases were
identified, corrections were applied, and the affected portion of the
dataset was re-tagged. This iterative approach to quality assurance
underscored our commitment to maintaining a high standard of accuracy in
the classification and analysis of job descriptions.

This methodical approach to data collection, tagging, and verification
provided a robust foundation for our analysis. By leveraging a large,
diverse dataset of job descriptions from Kaggle, systematically tagging
them with the AI4ED Lex framework, and rigorously verifying a subset
through manual inspection, we ensured the integrity and utility of our
research. This process not only facilitated a granular understanding of
the labor markets skills landscape but also underscored the importance
of precision and reliability in semantic tagging endeavors.

## WGU Skills Library

We conduct comparative analyses with the WGU Skills Library to primarily
assess the recall and coverage of crucial skills terms within AI4ED Lex.
It's important to note that the WGU Skills Library functions as a skills
ontology, not a skill mapping tool. Thus, comparing it with AI4ED Lex
for NLP-related tasks would not be a direct comparison due to their
differing functionalities. Despite this, our comprehensive comparison
aims to understand how well AI4ED Lex aligns with the WGU Skills
Library, which is designed to synchronize educational content with labor
market needs. The WGU Skills Library offers well-structured skills data,
promoting a more equitable, skills-driven ecosystem. This ecosystem
enhances the ability of learners, workers, and employers to adapt and
thrive in an ever-evolving employment landscape.

## Evaluation Versus Commercial Skill Mapping Tools

To enhance the accuracy and comprehensiveness of the AI4ED Lex, we
engage in comparative analyses with commercial skill mapping tools. This
comparison serves two main purposes: to identify any critical tags that
AI4ED Lex might overlook and to pinpoint significant tags that
commercial tools fail to recognize. Despite our efforts, we've
encountered challenges in conducting these comparisons at scale due to
the limitations imposed by commercial tools. For instance, LightCast's
free tier permits tagging for only 50 documents, making it impractical
to generate meaningful comparisons without incurring substantial costs.

# Results

XXXXX

# Conclusion

XXXXX
