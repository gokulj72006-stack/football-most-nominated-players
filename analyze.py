import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    df = pd.read_csv("data/ballon-d-or.csv")
    return df

def most_nominated(df):
    counts = df["player"].value_counts()
    return counts

def plot_top_players(counts, top_n=10):
    counts.head(top_n).plot(kind="bar", title=f"Top {top_n} Most Nominated Players")
    plt.ylabel("Number of Nominations")
    plt.xlabel("Player")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = load_data()
    counts = most_nominated(df)

    print(counts.head(10))
    print(f"\nMost nominated: {counts.idxmax()} with {counts.max()} nominations")

    plot_top_players(counts)