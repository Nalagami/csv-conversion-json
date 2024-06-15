import sys

def main():
    
    # コマンドライン引数を取得
    args = sys.argv
    if len(args) != 2:
        print('Usage: python main.py <arg1>')
        return
    
    # 引数を取得
    csv_file_path = args[1]

    # ファイルを読み込む
    with open(csv_file_path, 'r') as f:
        header = []
        data = []
        for index, line in enumerate(f, start=0):
            # 1行目はヘッダーを取得
            if index == 0:
                header = line.strip().split(',')
            else:
                # 2行目以降はデータを取得
                data.append(line.strip().split(','))

        print('header:', header) 
        print('data:', data)

    csv_data = []

    for row in data:
        tmp_row = {}
        for index, string in enumerate(row, start=0):
            tmp_row[header[index]] = string
            print(string, end=' ')
        csv_data.append(tmp_row)

    print(csv_data)

    # TODO: データをオブジェクトにしてファイルに書き込む

    return

if __name__ == '__main__':
    main()