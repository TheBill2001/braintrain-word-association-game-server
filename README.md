# Embedding server

To run the server, create a virtual environment and activate. Then install the dependencies.

```
pip install -r requirements.txt
```

Copy the file `template.env` to `.env` and edit the configuration. Run the server:

```
python src/main.py
```

**NOTE:** Currently only Underthesea does not work with Python 3.12, [see](https://github.com/undertheseanlp/underthesea/issues/729). You can use Conda to install an isolated Python 3.11 environment.
