import pandas as pd
from pybaseball import statcast

try:
    from google.colab import files
except ImportError:
    files = None


# ============================================================
# SETTINGS
# ============================================================
START_DATE = "2025-03-25"
END_DATE = "2025-04-05"

OUTPUT_ALL = "statcast_raw_data.csv"
OUTPUT_CALLED = "statcast_called_pitches_raw.csv"
OUTPUT_TRACKED = "statcast_called_pitches_tracked_only.csv"

TRACKING_COLUMNS = ["plate_x", "plate_z", "sz_bot", "sz_top"]


def show_dataframe(name, df, rows=10):
    print(f"\n{name}")
    print(f"Rows: {len(df):,}")
    print(df.head(rows).to_string(index=False))


def tracking_summary(df):
    available = [col for col in TRACKING_COLUMNS if col in df.columns]
    if not available:
        return "Tracking fields not present in returned data."

    complete_mask = df[available].notna().all(axis=1)
    summary = [
        f"Rows with all tracking fields present: {int(complete_mask.sum()):,} / {len(df):,} ({complete_mask.mean():.1%})"
    ]
    for col in available:
        non_null = int(df[col].notna().sum())
        summary.append(f"{col}: {non_null:,} non-null / {len(df):,} ({non_null / len(df):.1%})")
    return "\n".join(summary)


# ============================================================
# DOWNLOAD RAW STATCAST DATA
# ============================================================
print(f"Downloading Statcast data from {START_DATE} to {END_DATE}...")
all_pitches = statcast(start_dt=START_DATE, end_dt=END_DATE)
print(f"Downloaded {len(all_pitches):,} total pitches")


# ============================================================
# KEEP ONLY RAW CALLED PITCH SUBSETS
# ============================================================
called_pitches = all_pitches[
    all_pitches["description"].isin(["called_strike", "ball"])
].copy()

called_pitches_tracked = called_pitches[
    called_pitches[TRACKING_COLUMNS].notna().all(axis=1)
].copy()


# ============================================================
# SAVE RAW DATAFRAMES TO CSV
# ============================================================
all_pitches.to_csv(OUTPUT_ALL, index=False)
called_pitches.to_csv(OUTPUT_CALLED, index=False)
called_pitches_tracked.to_csv(OUTPUT_TRACKED, index=False)

print(f"Saved {OUTPUT_ALL}")
print(f"Saved {OUTPUT_CALLED}")
print(f"Saved {OUTPUT_TRACKED}")


# ============================================================
# DISPLAY DATAFRAME SUMMARIES
# ============================================================
print("\nTRACKING FIELD SUMMARY FOR CALLED PITCHES")
print(tracking_summary(called_pitches))

show_dataframe("ALL RAW STATCAST DATA", all_pitches)
show_dataframe("RAW CALLED PITCHES", called_pitches)
show_dataframe("TRACKED-ONLY CALLED PITCHES", called_pitches_tracked)


# ============================================================
# DOWNLOAD CSV FILES IN COLAB
# ============================================================
if files is not None:
    files.download(OUTPUT_ALL)
    files.download(OUTPUT_CALLED)
    files.download(OUTPUT_TRACKED)
else:
    print("\nColab download helper not available outside Google Colab.")
