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