# AI4ED Lex - A Lexical Database for Skills Mapping

In analyzing job descriptions within a dataset, we can predict the occurrence of specific job-related terms, such as "Node.js" or "Photographer," by employing a Poisson distribution. The formula is as follows:

(eq. 1) Poisson distribution: 
<img src="https://raw.githubusercontent.com/nikbearbrown/AI4ED_Lex/main/Art/equation_1.png">

Where:

- \( n \) denotes the frequency of the job-related term within a category of job descriptions.
- \( N \) signifies the total count of all terms within the job description category.
- \( f \) is the term's overall frequency within the entire corpus, which might be derived from a dataset such as Wikipedia articles for comparison (i.e., the frequency is the term count within Wikipedia divided by the total term count in Wikipedia).

To mitigate potential floating-point errors, the Poisson equation can be expressed in logarithmic form:

(eq. 2) 
<img src="https://raw.githubusercontent.com/nikbearbrown/AI4ED_Lex/main/Art/equation_2.png">

For larger term counts \( n \), the factorial \( n! \) is approximated using Stirling's approximation. By applying this method, we identify a set of terms, referred to as "Discriminating Terms," that are indicative of job-related content. These terms act as linear discriminators and are used to generate a likelihood statistic, which when combined with other features, can classify a job description. This approach adapts the traditional discriminant analysis technique, similar to the one employed by Mosteller and Wallace in their investigation of authorship attribution for The Federalist Papers.



