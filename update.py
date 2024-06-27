import sys
import pandas as pd
import random

def turn_data(ip):
    return f'{ip}:443#JP'

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <file_path> <n>")
        sys.exit(1)

    file_path = sys.argv[1]
    n = 10
    k = int(sys.argv[2])  # 每份文件的节点数量

    # 读取 CSV 文件
    df = pd.read_csv(file_path)

    # 随机选取 k*n 行
    random_rows = df.sample(k * n)
    ipports = random_rows['IP 地址'].apply(turn_data)

    # 分别写入 n 份文件
    for i in range(n):
        if i > 0:
            outname = f'addressesapi_{i}.txt'
        else:
            outname = 'addressesapi.txt'
        with open(outname, 'w') as f:
            for address in ipports[i * k: (i + 1) * k]:
                f.write(address + '\n')
        print(f"{outname} 写入 {k} 个节点")

if __name__ == "__main__":
    main()
