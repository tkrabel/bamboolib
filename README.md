# Community repository of bamboolib - the Fastest and Easiest Way to Work with pandas DataFrames 🐼🐍
[![](https://img.shields.io/badge/python->=3.6-blue.svg)](https://bamboolib.com)

This is the community repository of [bamboolib](https://bamboolib.8080labs.com/). There are no source files because bamboolib is closed source. However, you can [use bamboolib for free on Open Data](https://bamboolib.8080labs.com/get-started). If you have any issues or feature requests, please open an issue.

bamboolib is a python package for easy data exploration & transformation with pandas. You can use it with Jupyter Notebook or JupyterLab. bamboolib adds an interactive UI to your pandas output, which allows you to quickly prepare and visualize your data. All transformations come with **full keyboard control**, making bamboolib loved both by pandas-savvy users as well as Python novices.

## Main features and benefits of bamboolib

### 90% less working time

- Focus on what you want to do instead of how
- No more digging through StackOverflow
- Use your keyboard or mouse – whatever is fastest

### Easy to use

- Quick onboarding with minimal learning curve
- Find all features via an intuitive search bar
- Created by professional Data Scientists

### 100% compatible and flexible

- Seamless integration into your existing working environment
- Work from within Jupyter Notebook or JupyterLab
- Live code export for reproducibility and full customization

### Private, secure, local

- All your data remains private and secure
- Use it on your local machine without the need for cloud access
- Satisfies the requirements of your IT department

__[🔍Try bamboolib live on Binder](https://bamboolib.com/demo)__

## Quick installation for Jupyter Notebook

Install bamboolib for Jupyter Notebook by running the code below in your terminal (or Anaconda Prompt for Windows)

```bash
pip install bamboolib

# Jupyter Notebook extensions
jupyter nbextension install --py qgrid --sys-prefix
jupyter nbextension enable --py qgrid --sys-prefix
jupyter nbextension enable --py widgetsnbextension --sys-prefix
jupyter nbextension install --py bamboolib --sys-prefix
jupyter nbextension enable --py bamboolib --sys-prefix
```

Note that in order to avoid potential conflicts with other packages it is strongly recommended to use a virtual environment, e.g. [virtualenv](https://docs.python.org/3/tutorial/venv.html) or conda environments. Using an isolated environment makes it possible to install a specific version of bamboolib and its dependencies independently of any previously installed Python packages. If you are already using Anaconda, you can create an environment and install bamboolib with:

```bash
# Create conda environment
conda create -n bamboolib_venv python=3.7 -y

# Activate the environment
conda activate bamboolib_venv

# Add the IPython kernel to Jupyter
conda install ipykernel -y
python -m ipykernel install --user --name bamboolib_venv

# Install bamboolib ...
pip install bamboolib

# ... and Jupyter Notebook extensions
jupyter nbextension install --py qgrid --sys-prefix
jupyter nbextension enable --py qgrid --sys-prefix
jupyter nbextension enable --py widgetsnbextension --sys-prefix
jupyter nbextension install --py bamboolib --sys-prefix
jupyter nbextension enable --py bamboolib --sys-prefix
```

For installations using virtualenv or JupyterLab, go [here](https://github.com/tkrabel/bamboolib/tree/master/installation).

## Documentation

You find out how to get started along with tutorials and an API reference on our [docs](https://docs.bamboolib.8080labs.com/).

## Further links

- [Official Website](https://bamboolib.8080labs.com/)
- [bamboolib tutorial on Medium](https://towardsdatascience.com/bamboolib-learn-and-use-pandas-without-coding-23a7d3a94e1b).