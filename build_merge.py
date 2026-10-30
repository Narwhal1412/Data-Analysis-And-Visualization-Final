# Short python script, that goes down one folder deep,
# To stitch multiple notebooks together in a predefined order
import glob, os
import nbformat

# Define the order of which to stitch the file together
folder_order = ["giaHuy","anhTuan","giaViet"]

# Go down one folder deep, and get all the notebooks with the glob /.
files = glob.glob("*/524H*.ipynb")
# Lambda function to split into a list of strings, from giaHuy/test.ipynb -> ["giaHuy","test.ipynb"],
# And grabs the first item from the list which is the folder
# Then they'll be indexed(From custom order) and sorted.
files = sorted(files, key=lambda x: folder_order.index(x.split('/')[0]))

# Create a new notebook to store the cells of all other notebooks.
out = nbformat.v4.new_notebook()
# Add each cells from other notebooks to the new one.
for f in files:
    out.cells += nbformat.read(f, as_version=4).cells # type:ignore

os.makedirs("build",exist_ok=True) # Makes absolutely sure the folder build exists.
# Then write to build/final.ipynb
nbformat.write(out, "build/final.ipynb")
