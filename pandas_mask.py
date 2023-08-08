import pandas as pd

df = pd.DataFrame({
    "A": [12, 4, 5, 34, 1],
    "B": [5, 2, 100, 2, 34],
    "C": [12, 243, 3, 8, 9],
    "D": [64, 2, 67, 3, 19]
})

df_masked = df.mask(df > 10, "PUTIN" "\U0001f4aa" "\N{smiling face with sunglasses}")
print(df, "\n")
print(df_masked)
