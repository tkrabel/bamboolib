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

Jupyter Lab is currently under heavy development, and APIs and dependencies change on a frequent basis. This is why **we only support Jupyter Lab version 1.0 or higher**.

You need the jupyterlab-manager extension version that is [compatible with your Jupyter Lab version](https://github.com/jupyter-widgets/ipywidgets/tree/master/packages/jupyterlab-manager#version-compatibility).

Replace the command below with the correct jupyterlab-manager versiona and enter it into your terminal:

```bash
# Click the link above to find the right version, e.g. 1.0, 1.1, 1.2, ...
jupyter labextension install @jupyter-widgets/jupyterlab-manager@MAJOR_VERSION.MINOR_VERSION --no-build
```

From the terminal, you then install the other Jupyter Lab extensions via the following command:

```bash
jupyter labextension install @8080labs/qgrid@1.1.1 --no-build
jupyter labextension install plotlywidget --no-build
jupyter labextension install jupyterlab-plotly --no-build
jupyter labextension install bamboolib --no-build

# This step may take a while
jupyter lab build --minimize=False
```

### 3. Test bamboolib

__[Continue here](https://github.com/tkrabel/bamboolib/blob/master/installation/bamboolib_test_run/without_virtual_environment.md#test-the-library)__
