#!/usr/bin/env python
# coding: utf-8

# In[21]:


# Data source: PhysioNet ERP-BCI dataset
# https://physionet.org/content/erpbci/1.0.0/
# Citi et al., Journal of Neural Engineering, 2010
# Goldberger et al., Circulation, 2000


# In[20]:


import requests
from pathlib import Path

base_url = "https://physionet.org/files/erpbci/1.0.0"
subjects = [f"s{i:02d}" for i in range(1, 13)]
runs = 20

def download_subject(subject,save_dir):
    save_dir = Path(save_dir)/subject
    save_dir.mkdir(parents=True, exist_ok=True)

    for i in range(1,runs+1):
        file_name = f"rc{i:02d}.edf"
        url = f"{base_url}/{subject}/{file_name}"
        out_path = save_dir/file_name

        if out_path.exists():
            print(f"Already exists: {subject}/{file_name}")
            continue

        r = requests.get(url,stream=True)
        if r.status_code == 200:
            with open(out_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"Downloaded:{subject}/{file_name}")
        else:
            print(f"Error code ({r.status_code}):{subject}/{file_name}")

if __name__ == "__main__":
    for subject in subjects:
        download_subject(subject, save_dir="data/raw")


# In[ ]:




