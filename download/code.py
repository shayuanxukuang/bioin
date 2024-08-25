import pandas as pd
from Bio import Entrez
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from concurrent.futures import ThreadPoolExecutor, as_completed

# 设置NCBI的的邮箱
Entrez.email = "996297660@qq.com"

# CSV文件路径
csv_file = "split_BVBRC_phagegenome_part_1.xlsx"
# 读取CSV文件

#注意读取的文件格式
df = pd.read_excel(csv_file)

# 序列字典
fasta_sequences = {}


# 序列编号处理
def fetch_sequence(x):
    try:
        handle = Entrez.efetch(db="nucleotide", id=x, rettype="fasta", retmode="text")
        sequence = handle.read()
        handle.close()
        return sequence
    except Exception as e:
        # 打印错误信息
        print(f"Error retrieving sequence for {accession}: {e}")
        # 将出错的accession写入到文件中
        with open("failed_accessions1.txt", "a") as file:
            file.write(f"{accession}\n")
        return None

    finally:
        print(f"Finished fetching sequence for {x}")
    # 使用ThreadPoolExecutor来并发执行

#多线程执行，超过4就不行
with ThreadPoolExecutor(max_workers=3) as executor:
    # 准备future到accession的映射
    future_to_accession = {executor.submit(fetch_sequence, row["GenBank Accessions"]): row["GenBank Accessions"] for
                           index, row in df.iterrows()}

    # 遍历future对象，获取结果
    count = 0
    for future in as_completed(future_to_accession):
        accession = future_to_accession[future]
        sequence = future.result()
        if sequence is not None:
            fasta_sequences[accession] = sequence
        count += 1

        # 每下载一段存储一次
        #if count % 1000 == 0:
         #   df["FASTA Sequence"] = df["GenBank Accessions"].map(fasta_sequences.get)
          #  df.to_csv("updated_" + csv_file, index=False)
           # print(f"Saved {count} sequences to CSV.")


df["FASTA Sequence"] = df["GenBank Accessions"].map(fasta_sequences.get)

# DataFrame写入CSV文件
df.to_excel("updated_" + csv_file, index=False)

print("finish")