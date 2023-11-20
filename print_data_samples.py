
def print_sample(df, count):
    # Print sample entries
    sample_entries = df.sample(count)
    print("Sample Entries:\n", sample_entries)