import textstat
from textblob import TextBlob

def analyze_novel(filepath):
    """
    Analyzes the sentiment and reading level of a novel.

    Args:
        filepath: The path to the text file to analyze.

    Returns:
        A tuple containing two lists: sentiments and grade_levels.
    """
    try:
        with open(filepath, 'r') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None, None

    # Strip formatting (replace newlines with spaces)
    text = text.replace('\n', ' ')

    # Split into 500-word chunks
    words = text.split()
    chunks = [' '.join(words[i:i + 500]) for i in range(0, len(words), 500)]

    sentiments = []
    grade_levels = []

    for chunk in chunks:
        # Calculate sentiment polarity
        sentiment = TextBlob(chunk).sentiment.polarity
        sentiments.append(sentiment)

        # Calculate Flesch-Kincaid grade level
        grade_level = textstat.flesch_kincaid_grade(chunk)
        grade_levels.append(grade_level)

    return sentiments, grade_levels
