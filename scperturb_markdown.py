from mdutils.mdutils import MdUtils
import pandas as pd

df = pd.read_excel('media-1.xlsx', index_col=False)

i = 0

prefix = df['Index (=FirstauthorLastauthorYear)'].iloc[i]
title = df['Title'].iloc[i]
abstract = df['Mini-Abstract (loosely summarized original Abstract)'].iloc[i]
yaml_header = f"---\nlayout: post\ntitle: {prefix}\n---\n"
h5ad_prefix = "AdamsonWeissman2016_GSM2406675_10X001"

img_text = "QC1.png"
img_path = "qc_image_1.png"

file_name = prefix + '.md'

md_file = MdUtils(file_name=file_name, title=title)

md_file.new_header(level=1, title='Abstract')
md_file.new_paragraph(abstract)
md_file.new_paragraph()

md_file.new_header(level=1, title='Quality Control')
md_file.write(f"![{img_text}]({img_path})")
md_file.new_paragraph()

md_file.new_header(level=1, title='Download')
md_file.insert_code(f"wget https://zenodo.org/record/7041849/files/{h5ad_prefix}.h5ad?download=1 -O {h5ad_prefix}.h5ad")

tmp_str = md_file.get_md_text()

md_str = yaml_header + tmp_str

with open(file_name, "w") as f:
    f.write(md_str)
