import sys
import pandas as pd

def turn_data(ip):
    return f'{ip}:443#JP'

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <file_path> <n>")
        sys.exit(1)

    file_path = sys.argv[1]
    n = int(sys.argv[2])

    # 读取 CSV 文件
    df = pd.read_csv(file_path)

    # 随机选取 n 行
    random_rows = df.sample(n)
    ipports = random_rows['IP 地址'].apply(turn_data)
    
    # 写入文件
    with open('addressesapi.txt', 'w') as f:
        for address in ipports:
            f.write(address + '\n')
    print(f"addressesapi.txt写入{n}个节点")
    
    random_rows = df.sample(n)
    ipports = random_rows['IP 地址'].apply(turn_data)
    
    # 写入文件
    with open('addressesapi_1.txt', 'w') as f:
        for address in ipports:
            f.write(address + '\n')
    print(f"addressesapi_1.txt写入{n}个节点")


    random_rows = df.sample(n)
    ipports = random_rows['IP 地址'].apply(turn_data)
    
    # 写入文件
    with open('addressesapi_2.txt', 'w') as f:
        for address in ipports:
            f.write(address + '\n')
    print(f"addressesapi_2.txt写入{n}个节点")



if __name__ == "__main__":
    main()
