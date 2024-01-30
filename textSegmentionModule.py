from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import AgglomerativeClustering

# Split text by periods.
def customSentenceTokenizer(text):
    return [sentence.strip() for sentence in text.split('.') if sentence.strip()]

#hierarchical text clustering
def hierarchicalTextClustering(text, num_clusters=3):
    # Tokenize the text into sentences.
    sentences = customSentenceTokenizer(text)

    # Use TF-IDF Vectorization for text representation.
    vectorizer = TfidfVectorizer(stop_words='english')
    text_vectors = vectorizer.fit_transform(sentences)

    # Apply the Hierarchical Clustering algorithm.
    hierarchical = AgglomerativeClustering(n_clusters=num_clusters)
    cluster_labels = hierarchical.fit_predict(text_vectors.toarray())

    # Create a list of classifications based on clusters.
    clusters = [[] for _ in range(num_clusters)]
    for i, label in enumerate(cluster_labels):
        clusters[label].append(sentences[i])

    return [' '.join(cluster) for cluster in clusters]


#loading text
def loadingText(textAddress):
    filepath = Path(textAddress)
    return filepath.read_text()

#makeListOfSegments(original_text)
def makeListOfSegments(text):
    original_text = text.split("\n")
    return original_text

#find text title (suppose the first segment of the text as title)
def findTextTitle(listOfSegments):
    return(listOfSegments[0])

#find text body (suppose everything except title of the text)
def findTextBody(listOfSegments):
    return(listOfSegments[1:])

#text length
def findTextLength(text):
    return(len(text.split()))

#find position start (refers to the rank of the first word of the segment in the main text)
def findPositionStart(segment, listOfSegments):
    index = 0
    position = 1
    while (segment != listOfSegments[index]):
        position += findTextLength(listOfSegments[index])
        index += 1
    return position


#find position end (refers to the rank of the last word of the segment in the main text)
def findPositionEnd(segment, listOfSegments):
    position = findPositionStart(segment, listOfSegments) +findTextLength(segment) -1
    return position