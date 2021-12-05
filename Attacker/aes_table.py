import simple_aes
import pandas as pd

aes = pd.DataFrame(columns={"message_len", "cipher_len"})

keys = []
message = []
size = []

for i in range(1, 10000):
    m = "m" * i
    k = "keykey"
    size = len(simple_aes.encrypt(m, k))
    aes = aes.append({"message_len": len(m), "cipher_len": size}, ignore_index=True)


aes.to_csv("dataframe.csv", index=False)
print(aes)
