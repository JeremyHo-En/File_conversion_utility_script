#%%
import pandas as pd
import glob
import os
#%%
def xls_to_csv(input_file, output_file):
    """
    將 .xls 文件轉換為 .csv 文件

    參數:
        input_file: str, .xls 文件路徑
        output_file: str, 輸出 .csv 文件路徑
    """
    try:
        df = pd.read_excel(input_file, engine='xlrd')
        df.to_csv(output_file, index=False, encoding='utf-8-sig')
        print(f"轉換成功！檔案已儲存為: {output_file}")
    except Exception as e:
        print(f"轉換失敗: {e}")


#%%
station_namelist = ['Songshan','Qianzhe','ChungMing']
for name in station_namelist:
    f_mseed = glob.glob(os.path.join(f'/Users/jeremy/Desktop/CVDs/Air_raw/{name}/*xls'))
    f_mseed.sort()

    for paths in f_mseed:
        filename = os.path.basename(paths)[0:4]
        filepath = os.path.dirname(paths)
        input_file = paths
        output_file = filepath+'/'+filename+'.csv'
        xls_to_csv(input_file, output_file)

