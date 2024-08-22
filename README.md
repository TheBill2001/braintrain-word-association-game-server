# Embedding server

This repo used [Git LFS](https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage) to store the embeddings model. Install Git LFS and then run the following command in the repo to pull the model binary.

```
git lfs install
git lfs pull
```

To run the server, create a virtual environment and activate. Then install the dependencies.

```
pip install -r requirements.txt
```

Copy the file `template.env` to `.env` and edit the configuration. Run the server:

```
python src/main.py
```

**NOTE:** Currently only Underthesea does not work with Python 3.12, [see](https://github.com/undertheseanlp/underthesea/issues/729). You can use Conda to install an isolated Python 3.11 environment.
