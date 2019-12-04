## Installing bamboolib

### 1. Install bamboolib

From the terminal, execute the pip install:
```bash
pip install bamboolib
```

### 2. Setup Jupyter extensions

#### 2.1 Installation for Jupyter Notebook

From the terminal, you need to setup the Jupyter Notebook extensions via the following command:

```bash
jupyter nbextension enable --py qgrid --sys-prefix
jupyter nbextension enable --py widgetsnbextension --sys-prefix
jupyter nbextension install --py bamboolib --sys-prefix
jupyter nbextension enable --py bamboolib --sys-prefix
```

#### 2.2. Installation for Jupyter Lab >=1.0

**We only support Jupyter Lab version 1.0 or higher.**

First, you need to install the jupyterlab-manager. Make sure that the jupyterlab-manager version is [compatible with your Jupyter Lab version](https://github.com/jupyter-widgets/ipywidgets/tree/jupyterlab_branch/packages/jupyterlab-manager#version-compatibility).

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

### 3. Test bamboolib

__[Continue here](https://github.com/tkrabel/bamboolib/blob/jupyterlab_branch/installation/bamboolib_test_run/without_virtual_environment.md#test-the-library)__
