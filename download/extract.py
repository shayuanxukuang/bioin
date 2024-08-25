import pandas as pd
# 读取CSV文件
df = pd.read_excel('BVBRC_genome1.xlsx')  # 替换为你的文件名

# 遍历DataFrame的每一行
for index, row in df.iterrows():
    fasta_seq = row['FASTA Sequence']
    # 检查数据类型
    if isinstance(fasta_seq, str):
        # 打印FASTA序列的一部分
        print(f"FASTA Sequence (truncated): {fasta_seq[:100]}...")
        # 这里可以添加代码来处理CDS序列
    else:
        print(f"Warning: Non-string data type found for FASTA Sequence at index {index}. Skipping...")

    # ...（其他代码）


# 定义一个函数来提取CDS序列
def extract_cds_sequence(fasta_seq):
    if pd.isnull(fasta_seq) or 'partial cds' not in fasta_seq:
        return None
        # 分割字符串以找到'partial cds'的位置
    parts = fasta_seq.split('partial cds')
    if len(parts) > 1:
        # 提取'partial cds'之后的部分，并去除前导空白字符
        cds_seq = parts[1].strip()
        # 如果需要，可以在这里进一步处理cds_seq，例如去除尾随的换行符等
        return cds_seq
    return None


# 应用函数到DataFrame的相应列
df['CDS_Sequence'] = df['FASTA Sequence'].apply(extract_cds_sequence)

# 打印出几个示例以检查


# 写入新的CSV文件（或覆盖原文件）
df.to_csv('updated_fil.xlsx', index=False)  # 替换为你的文件名