import pytest
from analyzer import analyze_novel

@pytest.fixture
def sample_text_file(tmp_path):
    """Create a sample text file for testing."""
    # Create a text with 600 words to test chunking into two chunks.
    content = "word " * 600
    file_path = tmp_path / "sample.txt"
    file_path.write_text(content)
    return file_path

def test_chunking(sample_text_file):
    """Test that the text is split into 500-word chunks."""
    sentiments, grade_levels = analyze_novel(sample_text_file)
    assert len(sentiments) == 2
    assert len(grade_levels) == 2

@pytest.fixture
def positive_text_file(tmp_path):
    """Create a text file with a known positive sentiment."""
    content = "I love this. It's fantastic and wonderful."
    file_path = tmp_path / "positive.txt"
    file_path.write_text(content)
    return file_path

def test_sentiment_analysis(positive_text_file):
    """Test that the sentiment is calculated correctly."""
    sentiments, _ = analyze_novel(positive_text_file)
    assert len(sentiments) == 1
    assert sentiments[0] > 0.5

@pytest.fixture
def grade_level_text_file(tmp_path):
    """Create a text file with a known grade level."""
    content = "The cat sat on the mat. The dog chased the cat. The cat ran away."
    file_path = tmp_path / "grade.txt"
    file_path.write_text(content)
    return file_path

def test_grade_level_calculation(grade_level_text_file):
    """Test that the grade level is calculated correctly."""
    _, grade_levels = analyze_novel(grade_level_text_file)
    assert len(grade_levels) == 1
    # Note: textstat calculates a Flesch-Kincaid grade of -1.05 for this text,
    # which rounds to -1.
    assert round(grade_levels[0]) == -1
