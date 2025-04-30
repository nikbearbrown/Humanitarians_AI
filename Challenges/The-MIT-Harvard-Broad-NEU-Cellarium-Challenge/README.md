# The MIT-Harvard Broad/NEU | Cellarium Challenge

## Description:
Dive into the world of AI and single-cell RNA annotation with "The MIT-Harvard Broad/NEU | Cellarium Challenge." This song encapsulates the excitement and complexity of cutting-edge scientific challenges. Join us in celebrating the fusion of technology, ethics, and collaborative effort in the quest for innovation. Let the music inspire you to harness the power of AI for good, with ethics bright and knowledge strong.

**Music by:** Liam Bear Brown

**Lyrics by:** Nik Bear Brown

- ['The MIT - Harvard Broad NEU  Cellarium Challenge (Nik Vocals NBB)’ on SoundCloud](https://soundcloud.com/liam-bear-brown/the-mit-harvard-broad-neu-cellarium-challenge-nik-vocals-nbb?si=f750af88f2564010b5a4f8ae1da99f69&utm_source=twitter&utm_medium=post&utm_campaign=social_sharing)
- ['The MIT - Harvard Broad NEU  Cellarium Challenge (Bobby Jo Vocals)’ on SoundCloud](https://soundcloud.com/liam-bear-brown/the-mit-harvard-broad-neu-cellarium-challenge-bobby-jo-vocals?si=82e27c0b236b409a98072228f1442cc1&utm_source=twitter&utm_medium=post&utm_campaign=social_sharing)

## The Cellarium Challenge
[Cellarium Challenge on GitHub](https://github.com/cellarium-ai/cellarium-neu-challenge)

---

Feel free to contribute, collaborate, and explore the exciting intersection of AI and single-cell RNA annotation with us!

# NEU | Cellarium Challenge
## Description

Cell Annotation Service (CAS) is a tool that can be used for a rapid search of the cells based on their raw count matrices. This service can be used by analysts to perform annotation and search of their cells.
## Data
The Raw Count Matrix in scRNA-seq data is a sparse, high-dimensional array where each column represents a gene, and each row represents a cell from the tissue. Each value in the matrix indicates the count of a particular gene expressed in a specific cell during the experiment, based on the RNA molecules captured by the sequencing machine. The scRNA-seq data is structured as follows:

![image](./assets/matrix_ex.png)

Typically, these matrices have 30,000 to 40,000 columns and can vary in the number of rows, sometimes reaching several millions. Most of the values represent 0, just a small portion of the values in the matrix has numbers other than 0.

## Data Flow of Cell Annotation
1. [Dimensionality reduction](https://en.wikipedia.org/wiki/Dimensionality_reduction)
   First scRNA-seq data comes from the client and goes through dimensionality reduction (PCA). As the output PCA gives us 512 dimension vectors.
2. [Nearest Neighbor Search](https://en.wikipedia.org/wiki/Nearest_neighbor_search)
   Then 512 dimension representations of the input cells go to a Nearest Neighbor Search engine, which returns an array of cells that are close to the querying cell (potentially meaningful biological context).
   Let’s say for our input example (Table 1) we have an output like this:
```JSON
[
 {
   "query_id": "Cell 1",
   "matches": [
     {"id": 12321, "cell_type": "T cell", "distance": 0.789},
     {"id": 123145, "cell_type": "lymphocyte", "distance": 0.790},
     {"id": 1231, "cell_type": "alpha-beta T cell", "distance": 0.80}
   ]
 },
 {
   "query_id": "Cell 2",
   "matches": [
     {"id": 113543, "cell_type": "MHC-II-negative non-classical monocyte", "distance": 0.812},
     {"id": 1908, "cell_type": "native cell", "distance": 0.701},
     {"id": 12, "cell_type": "leukocyte", "distance": 0.67}
   ]
 },
 {
   "query_id": "Cell 3",
   "matches": [
     {"id": 1012342, "cell_type": "MHC-II-negative non-classical monocyte", "distance": 0.93},
     {"id": 56753,"cell_type": "Gr1-low non-classical monocyte", "distance": 0.82},
     {"id": 623456, "cell_type": "leukocyte", "distance": 0.710221}
   ]
 }
]
```

This would help us to annotate the query cell with the cell type returned from the Nearest Neighbor engine.

3. Summarize context based on Nearest Neighbor Search output (the step that needs action)

## Problem
Cell Type is a categorical variable. Hierarchy of cell types is represented by [Ontology](https://en.wikipedia.org/wiki/Ontology_(information_science)). You can find the specific ontology used for the hierarchy of the data we work with [here](https://www.ebi.ac.uk/ols4/ontologies/cl?viewMode=tree). The main problem of this challenge lies in summarizing the Nearest Neighbor Search responses. 
Including all the neighbors in the response is difficult to interpret for annotation purposes, as the response sometimes contains multiple reasonable matches. Our reference datasets are annotated at different levels of the cell ontology.
As a result, a similarity query results in a mixture of annotations at different granularities.
Note: the complexity of the problem lies in the fact that higher level cell types belong to multiple lower cell types in hierarchy, however those lower level cell types (which are all parents for the lower level cell type) can have different parents and have no connection. Example:

Let’s take a look at [CD86-positive plasmablast](https://www.ebi.ac.uk/ols4/ontologies/cl/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCL_0001202?lang=en) in the ontology graph.
It has different branches of parents:

![image](./assets/cd86-positive_plasmablast.png)

It can be a leukocyte and a motile cell, and both of these will be true. If we go to a deeper level, we can see that it belongs to the antibody-secreting cell, B cell, and lymphocyte of B lineage. Having a result predicting any of these classes would be meaningful.
When the nearest neighbor search returns results with various cell types, we need to ensure that we aren't using cell types that are too granular, as this risks deviating too far from the ground truth. Similarly, we should avoid generalizing too much with a parent cell type that doesn't accurately represent the cell.

## Challenge
Develop an algorithm that, based on the response from the nearest neighbor search engine, can return a reasonable aggregation of cell types while ranking them.
You are required to propose the algorithm and describe it in detail. While the code for the prototype is not mandatory, it would be a valuable addition. Please include the resources you used, such as links to papers or articles. The most important criteria that we will look at are the approach you propose for the problem's solution and how well you can use online resources to develop one.

### Submission
Send your submission to:

fgrab@broadinstitute.org

and CC Prof Nik Bear Brown:

ni.brown@northeastern.edu

before June 6, 2024, 11:59 PM.

Please include "NEU-Cellarium-Challenge" in the email subject line.

Feel free to use the same email if you have any questions regarding the challenge task.

### Materials
Please find a jupyter notebook attached with examples of the data. You can use the notebook (NEU-Broad-Challenge.ipynb) as a starter point for the challenge.


The challenge is provided by the Cellarium team at the Data Sciences Platform, Broad Institute, and Professor Nik Bear Brown from Northeastern University's College of Engineering.


