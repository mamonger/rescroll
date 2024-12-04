import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Hebrew character counts for all books of the Hebrew Bible, including spaces (approx. 20% added)
character_counts_with_spaces = {
    "Genesis": 93677,
    "Exodus": 76442,
    "Leviticus": 53747,
    "Numbers": 69294,
    "Deuteronomy": 62882,
    "Joshua": 34053,
    "Judges": 33034,
    "Ruth": 12222,
    "1 Samuel": 45854,
    "2 Samuel": 42058,
    "1 Kings": 41453,
    "2 Kings": 36980,
    "Isaiah": 80242,
    "Jeremiah": 83238,
    "Ezekiel": 69086,
    "Hosea": 14350,
    "Joel": 3643,
    "Amos": 6353,
    "Obadiah": 1238,
    "Jonah": 2357,
    "Micah": 5079,
    "Nahum": 1943,
    "Habakkuk": 2620,
    "Zephaniah": 2972,
    "Haggai": 1657,
    "Zechariah": 7274,
    "Malachi": 2117,
    "Psalms": 180209,
    "Proverbs": 57924,
    "Job": 47882,
    "Song of Songs": 6822,
    "Ecclesiastes": 27847,
    "Lamentations": 17395,
    "Daniel": 25644,
    "Ezra": 16922,
    "Nehemiah": 23548,
    "1 Chronicles": 44990,
    "2 Chronicles": 47799,
}

def calculate_columns_and_length(total_characters, lines_per_column, characters_per_line, column_width_cm, right_margin, left_margin, inter_column_margin):
    """
    Calculate the total number of columns and the total manuscript length,
    accounting for margins (right before first column, left after last column, and inter-column).
    """
    try:
        # Calculate total columns
        characters_per_column = lines_per_column * characters_per_line
        total_columns = total_characters / characters_per_column

        # Total length includes column widths, inter-column margins, and outer margins
        total_length_cm = (
            total_columns * column_width_cm  # Width of all columns
            + (total_columns - 1) * inter_column_margin  # Inter-column margins
            + right_margin  # Margin before the first column
            + left_margin   # Margin after the last column
        )
        return round(total_columns, 2), round(total_length_cm, 2)
    except ZeroDivisionError:
        return 0, 0
