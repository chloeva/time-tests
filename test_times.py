from times import compute_overlap_time, time_range

def test_generic_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = short
    assert compute_overlap_time(large, short) == expected

def test_no_overlap():
    range1 = [("2025-10-27 10:00:00", "2025-10-27 11:00:00")]
    range2 = [("2025-10-27 12:00:00", "2025-10-27 13:00:00")]
    expected =[]
    assert compute_overlap_time(range1, range2) == expected

def test_multiple_interval_overlap():
    # Range 1: 4 intervals between 10:00 and 12:00 (so each 30 minutes)
    range1 = time_range("2025-10-27 10:00:00", "2025-10-27 12:00:00", number_of_intervals=4)

    # Range 2: 4 intervals between 11:00 and 13:00
    range2 = time_range("2025-10-27 11:00:00", "2025-10-27 13:00:00", number_of_intervals=4)

    overlaps = compute_overlap_time(range1, range2)

    expected = [
        ("2025-10-27 11:00:00", "2025-10-27 11:30:00"),
        ("2025-10-27 11:30:00", "2025-10-27 12:00:00"),
    ]

    assert overlaps == expected

def test_adjacent_intervals_no_overlap():

    range1 = [("2025-10-27 10:00:00", "2025-10-27 11:00:00")]
    range2 = [("2025-10-27 11:00:00", "2025-10-27 12:00:00")]

    overlaps = compute_overlap_time(range1, range2)

    # Expect no overlap, since 11:00:00 is the exact transition point.
    assert overlaps == []

