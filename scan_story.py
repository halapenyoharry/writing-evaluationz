import sys
from analyzer import analyze_novel
from plotting import plot_analysis

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        filepath = 'draft.txt'
        print(f"No file specified. Using default: {filepath}")
        # Create a dummy draft.txt for demonstration
        with open(filepath, 'w') as f:
            f.write("This is a simple sentence. This is another sentence. " * 250)

    sentiments, grade_levels = analyze_novel(filepath)

    if sentiments and grade_levels:
        plot_analysis(sentiments, grade_levels)
