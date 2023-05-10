import os,sys, csv

#引数が３つであることを確認
if len(sys.argv)!=4:
    print("使い方：ExportAnyColumns.py file1 file2 列番号")
    sys.exit()
#参照元のファイルが存在することを確認する
in_file = sys.argv[1]
if not os.path.exists(in_file):
    print("ファイルが存在しません")
    sys.exit()

#出力先のファイルが存在していた場合に上書きするかを確認する
out_file = sys.argv[2]
if os.path.exists(out_file):
    if input("上書きしますか？(y/n):")!="y":
        sys.exit()

#列番号
col_nums = (sys.argv[3])
print("column_no: ", col_nums, "を出力")
cols = col_nums.split(",")
# #書き出し最終行番号
# end_line = line_no + 20
# print("end_line: ",end_line)

with open(in_file,"r", newline="", encoding="utf_16") as in_f:
    with open(out_file, "w", encoding="utf_16") as out_f:
        #reader = csv.reader(in_f)
        for line in in_f:
            #line = line.rstrip("\n")
            # タブ区切りでリストに変換する
            line = line.split("\t")
            #書き出し用のファイルに指定列を出力
            for i, col_num in enumerate(cols):
                col = line[col_num]
                if col is None or col =="":
                    print("指定の列はありませんでした")
                    break
                else:
                    if len(cols) = 1 and rows is None:
                        rows = rows + col + "\n"
                    if i == 0:
                        col = col
                    elif i == len(col_num)
                    else:
                        col = col + "\t"
                    col col = col + "\n"
                out_f.write(col)
                i += 1

            
