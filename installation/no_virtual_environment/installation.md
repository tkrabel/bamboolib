## Installing bamboolib

There are 2 steps:
1) pip install
2) install Jupyter extensions

### 1. pip install

From the terminal (or Anaconda Prompt if you use Windows), execute the pip install:
```bash
pip install bamboolib
```
Afterwards, you need to install Jupyter extensions for the interactive output.

### 2. Install Jupyter extensions

The installations are different for Jupyter Notebook and Jupyter Lab.

#### 2.1 Jupyter Notebook

From the terminal, you need to setup the Jupyter Notebook extensions via the following command:

```bash
jupyter nbextension enable --py qgrid --sys-prefix
jupyter nbextension enable --py widgetsnbextension --sys-prefix
jupyter nbextension install --py bamboolib --sys-prefix
jupyter nbextension enable --py bamboolib --sys-prefix
```

Afterwards, you can __[test bamboolib](https://github.com/tkrabel/bamboolib/blob/master/installation/bamboolib_test_run/without_virtual_environment.md#test-the-library)__


#### 2.2. Jupyter Lab >=1.0

> bamboolib supports Jupyter Lab version 1.0 or higher

First, you need to install the jupyterlab-manager which needs to be [compatible with your Jupyter Lab version](https://github.com/jupyter-widgets/ipywidgets/tree/master/packages/jupyterlab-manager#version-compatibility).

You can determine your Jupyter Lab version via typing in the following in your terminal:
```bash
jupyter labextension list
```

Then, replace the command below with the [compatible jupyterlab-manager version](https://github.com/jupyter-widgets/ipywidgets/tree/master/packages/jupyterlab-manager#version-compatibility) and execute it from your terminal.

For example, for JupyterLab 1.0.x and 1.1.x, you need to install jupyterlab-manager 1.0

```bash
# Click the link above to find the right version of jupyterlab-manager
# MAJOR_VERSION.MINOR_VERSION IS NOT NECESSARILLY EQUAL TO YOUR JUPYTERLAB VERSION
jupyter labextension install @jupyter-widgets/jupyterlab-manager@MAJOR_VERSION.MINOR_VERSION --no-build
```

From the terminal, install the other Jupyter Lab extensions via the following commands:

```bash
jupyter labextension install @8080labs/qgrid@1.1.1 --no-build
jupyter labextension install plotlywidget --no-build
jupyter labextension install jupyterlab-plotly --no-build
jupyter labextension install bamboolib --no-build

# This step may take a while
jupyter lab build --minimize=False
```

Afterwards, you can __[test bamboolib](https://github.com/tkrabel/bamboolib/blob/master/installation/bamboolib_test_run/without_virtual_environment.md#test-the-library)__


### 3. Test bamboolib

After the 2 installation steps, you can:


__[Continue to test bamboolib](https://github.com/tkrabel/bamboolib/blob/master/installation/bamboolib_test_run/without_virtual_environment.md#test-the-library)__
