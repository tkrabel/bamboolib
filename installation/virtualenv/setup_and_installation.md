## Installing bamboolib using virtualenv

### 1. Create a virtual environment for your project

In the terminal enter the following where `bamboolib_venv` is the name of the virtual environment. Please change it if you want name your virtual environment differently.

```bash
virtualenv bamboolib_venv
source bamboolib_venv/bin/activate

ipython kernel install --user --name=bamboolib_venv
```

### 2. Install bamboolib

```bash
pip install bamboolib
```

### 3. Setup Jupyter extensions

#### 3.1 Installation for Jupyter Notebook

From the terminal, you need to setup the Jupyter Notebook extensions via the following command:

```bash
jupyter nbextension enable --py qgrid --sys-prefix
jupyter nbextension enable --py widgetsnbextension --sys-prefix
jupyter nbextension install --py bamboolib --sys-prefix
jupyter nbextension enable --py bamboolib --sys-prefix
```

#### 3.2. Installation for Jupyter Lab >=1.0

**We only support Jupyter Lab version 1.0 or higher.**

First, you need to install the jupyterlab-manager. Make sure that the jupyterlab-manager version is [compatible with your Jupyter Lab version](https://github.com/jupyter-widgets/ipywidgets/tree/master/packages/jupyterlab-manager#version-compatibility).

Replace the command below with the correct jupyterlab-manager version and paste it into your terminal:

```bash
# Click the link above to find the right version, e.g. 1.0, 1.1, 1.2, ...
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

### 4. Test bamboolib

Go [here](https://github.com/tkrabel/bamboolib/blob/master/installation/bamboolib_test_run/with_virtual_environment.md#test-the-library).
