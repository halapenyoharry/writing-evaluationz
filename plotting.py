import matplotlib.pyplot as plt

def plot_analysis(sentiments, grade_levels):
    """
    Generates a plot of the sentiment and grade level analysis.

    Args:
        sentiments: A list of sentiment polarity values.
        grade_levels: A list of Flesch-Kincaid grade level values.
    """
    fig, ax1 = plt.subplots()

    # Left Axis (Sentiment)
    ax1.set_xlabel('Chunk (500 words)')
    ax1.set_ylabel('Emotional Volatility (Sentiment)', color='blue')
    ax1.plot(sentiments, color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.axhline(y=0.0, color='blue', linestyle='--', label='Boring')

    # Right Axis (Grade Level)
    ax2 = ax1.twinx()
    ax2.set_ylabel('Readability (Grade Level)', color='orange')
    ax2.plot(grade_levels, color='orange')
    ax2.tick_params(axis='y', labelcolor='orange')
    ax2.axhline(y=12, color='orange', linestyle='--', label='Pretentious')

    plt.title('Novel Pacing Analysis')
    fig.tight_layout()
    plt.show()
