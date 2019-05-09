# Dropbox Paper Markdown to Real Markdown (with local image files)

**The problem:** Dropbox Paper exports to Markdown (nice), but all images still reference their Dropbox URLs rather than image downloads, making it poorly-suited for properly moving documentation out of Dropbox Paper into anywhere else (e.g. a GitHub repo).

`paper2md.py` is a simple Python script that solves that.

**Features:**

- Creates an `assets` folder and `README.md` next to the file you input and saves images from Dropbox URLs into this folder.
- Creates a `README.md` file which is a copy of the file you input, but with images pointing to your newly-downloaded assets. If there is already a `README.md` at the same level as your input file, it will instead create a file with the suffix `-local.md`.

**Use at your own risk.** This was a quick-n-dirty script made to solve an immediate need.

## Usage

This is a messy Python script made to solve an immediate, limited need. Use at your own risk.

### Step 1: Set up the project locally

Use a Python virtual environment to build this project. If you've never set up a virtual environment before, [read more about it in this guide](https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments).

You can set up a Python 3 virtual environment with:

```bash
python3 -m venv ./venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

Install requirements:

```bash
pip install -r requirements.txt
```

### Step 2: Export from Dropbox Paper to a markdown file

From the Drobox Paper docs:

> You can convert any of your existing docs to .docx (Microsoft Word), or .md (Markdown) file by following these steps:
>
> 1. Click "…" (ellipsis) in the Paper doc you're viewing.
> 1. Click Export.
> 1. Choose the file format for your download.
> 1. Click Download.

Then, move this into a folder in which you want to keep the notes (I'm moving this into a docs folder of another repo).

Retitle the document as something simple like `paper.md`, for simplicity later (Dropbox Paper tends to export with file names that don't paste to the terminal nicely).

### Step 3: Run the script!

With the venv activated in this project, run the script on your downloaded Dropbox Paper markdown:

```
python paper2md.py <your_file_path_here>/paper.md
```

This will create an `assets` folder with save images and an updated `README.md` markdown file next to the file you input.
