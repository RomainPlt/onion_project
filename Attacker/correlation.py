import pandas as pd
import compare_data

table = pd.read_csv("dataframe.csv")
number_router = input("How many routers ? ")
out_message_len = input("Data length ? ")


def estimation(o_len, n_nodes):
    cipher = 0
    for i in range(n_nodes):
        pos = table.loc[table["message_len"] == cipher + 36]
        cipher = pos["cipher_len"].iloc[0]
        print(cipher)
    return o_len + cipher


if __name__ == "__main__":
    print(estimation(out_message_len, number_router))
