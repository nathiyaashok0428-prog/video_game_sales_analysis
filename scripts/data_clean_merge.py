# ============================================================
# data_clean_merge.py
# Video Game Sales – Robust Data Cleaning & Merge Pipeline
# ============================================================

import pandas as pd

# ------------------------------------------------------------
# 1. LOAD RAW DATA
# ------------------------------------------------------------

games_df = pd.read_csv("data/games.csv")
sales_df = pd.read_csv("data/vgsales.csv")

print("Initial Shapes:")
print("Games:", games_df.shape)
print("Sales:", sales_df.shape)


# ------------------------------------------------------------
# 2. STANDARDIZE COLUMN NAMES
# ------------------------------------------------------------

def normalize_columns(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df

games_df = normalize_columns(games_df)
sales_df = normalize_columns(sales_df)

print("\nGames Columns:", games_df.columns.tolist())
print("Sales Columns:", sales_df.columns.tolist())


# ------------------------------------------------------------
# 3. REMOVE DUPLICATES
# ------------------------------------------------------------

games_df = games_df.drop_duplicates()
sales_df = sales_df.drop_duplicates()


# ------------------------------------------------------------
# 4. HANDLE MISSING VALUES (SAFE & CONDITIONAL)
# ------------------------------------------------------------

# ---- Handle publisher ONLY if column exists ----
if "publisher" in games_df.columns:
    games_df["publisher"] = games_df["publisher"].fillna("Unknown")

# ---- Handle rating ONLY if column exists ----
if "rating" in games_df.columns:
    games_df["rating"] = games_df["rating"].fillna("Not Rated")

# ---- Handle year in sales ----
if "year" in sales_df.columns:
    sales_df = sales_df.dropna(subset=["year"])
    sales_df["year"] = sales_df["year"].astype(int)


# ------------------------------------------------------------
# 5. DATA TYPE STANDARDIZATION (SAFE)
# ------------------------------------------------------------

sales_columns = [
    "na_sales", "eu_sales", "jp_sales",
    "other_sales", "global_sales"
]

for col in sales_columns:
    if col in sales_df.columns:
        sales_df[col] = pd.to_numeric(sales_df[col], errors="coerce")

sales_df = sales_df.dropna(subset=["global_sales"])


# ------------------------------------------------------------
# 6. LOGICAL VALIDATION RULES
# ------------------------------------------------------------

# Global sales cannot be negative
sales_df = sales_df[sales_df["global_sales"] >= 0]

# Regional sales cannot exceed global sales
for region in ["na_sales", "eu_sales", "jp_sales", "other_sales"]:
    if region in sales_df.columns:
        sales_df = sales_df[sales_df[region] <= sales_df["global_sales"]]


# ------------------------------------------------------------
# 7. MERGE DATASETS (CORRECT JOIN KEYS)
# ------------------------------------------------------------

final_df = pd.merge(
    games_df,
    sales_df,
    left_on="title",
    right_on="name",
    how="inner"
)

print("After merge shape:", final_df.shape)


# ------------------------------------------------------------
# 8. FINAL COLUMN SELECTION (ONLY EXISTING)
# ------------------------------------------------------------

required_columns = [
    "name", "platform", "year", "genre",
    "publisher", "na_sales", "eu_sales",
    "jp_sales", "other_sales", "global_sales", "rating"
]

final_columns = [col for col in required_columns if col in final_df.columns]

final_df = final_df[final_columns]


# ------------------------------------------------------------
# 9. SAVE CLEAN DATA
# ------------------------------------------------------------

final_df.to_csv(
    "data/cleaned_video_game_data.csv",
    index=False
)

print("\n✅ Data cleaning & merge completed successfully")
print("📁 Saved: data/cleaned_video_game_data.csv")
