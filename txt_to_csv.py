#%%
import csv

def detect_encoding(file_path):
    encodings = ['utf-8', 'iso-8859-1', 'ascii', 'cp1252']
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                f.read()
            return encoding
        except UnicodeDecodeError:
            continue
    raise Exception("無法使用任何編碼方式打開文件")

def txt_to_csv(txt_file, csv_file):
    encoding = detect_encoding(txt_file)
    with open(txt_file, 'r', encoding=encoding) as txtfile:
        with open(csv_file, 'w', newline='',encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            for line in txtfile:
                if line.startswith('#'):
                    line = line[1:]
                fields = line.strip().split()
                csv_writer.writerow(fields)
#%%
txtfile='/Users/jeremy/Desktop/Package_9809/*txt'
f_mseed = glob.glob(os.path.join(txtfile))
f_mseed.sort()
for path in f_mseed:
    txt_filename = path
    csv_filename = '/Users/jeremy/Desktop/2023project/cwb_csv/'+str(path[35:41])+'.cwb_hr.csv'
    txt_to_csv(txt_filename, csv_filename)


# %%
