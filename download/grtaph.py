import pandas as pd


def split_excel_to_multiple_files(input_file, output_prefix, chunk_size=5000):
    # 读取整个Excel文件
    df = pd.read_excel(input_file, engine='openpyxl')

    # 初始化计数器
    chunk_number = 0

    # 如果数据帧数据少于或等于chunk_size，则直接写入单个文件
    if len(df) <= chunk_size:
        df.to_excel(f"{output_prefix}_part_1.xlsx", index=False, engine='openpyxl')
        return

        # 否则，分割DataFrame并写入多个文件
    for i in range(0, len(df), chunk_size):
        chunk = df.iloc[i:i + chunk_size]
        chunk.to_excel(f"{output_prefix}_part_{chunk_number + 1}.xlsx", index=False, engine='openpyxl')
        chunk_number += 1

    # 使用示例


input_file = 'G:/bioin/ncbi_dataset/BVBRC_phagegenome.xlsx'
output_prefix = 'G:/bioin/ncbi_dataset/split_BVBRC_phagegenome'
split_excel_to_multiple_files(input_file, output_prefix)