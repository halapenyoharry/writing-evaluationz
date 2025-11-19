import sys
import textstat
from textblob import TextBlob
import matplotlib.pyplot as plt

def analyze_novel(filepath):
    """
    Analyzes the sentiment and reading level of a novel.

    Args:
        filepath: The path to the text file to analyze.
    """
    try:
        with open(filepath, 'r') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return

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

    # Visualization
    fig, ax1 = plt.subplots()

    # Left Axis (Sentiment)
    ax1.set_xlabel('Chunk (500 words)')
    ax1.set_ylabel('Emotional Volatility (Sentiment)', color='blue')
    ax1.plot(sentiments, color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.axhline(y=0.0, color='blue', linestyle='--', label='Boring')

    # Right Axis (Grade Level)
    ax2 = ax1.twinx()
    ax2.set_ylabel('Fartiness (Grade Level)', color='orange')
    ax2.plot(grade_levels, color='orange')
    ax2.tick_params(axis='y', labelcolor='orange')
    ax2.axhline(y=12, color='orange', linestyle='--', label='Pretentious')

    plt.title('Novel Pacing Analysis')
    fig.tight_layout()
    plt.show()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        filepath = 'draft.txt'
        print(f"No file specified. Using default: {filepath}")
        # Create a dummy draft.txt for demonstration
        with open(filepath, 'w') as f:
            f.write("This is a simple sentence. This is another sentence. " * 250)

    analyze_novel(filepath)
