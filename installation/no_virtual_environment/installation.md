## Installing bamboolib

### 1. Install bamboolib

From the terminal, execute the pip install:
```bash
pip install bamboolib
```

### 2. Setup Jupyter extensions

From the terminal, you need to setup the Jupyter Notebook extensions via the following command:

```bash
jupyter nbextension enable --py qgrid --sys-prefix
jupyter nbextension enable --py widgetsnbextension --sys-prefix
jupyter nbextension install --py bamboolib --sys-prefix
jupyter nbextension enable --py bamboolib --sys-prefix
```

### 3. Test bamboolib

__[Continue here](https://github.com/tkrabel/bamboolib/blob/master/installation/bamboolib_test_run/without_virtual_environment.md#test-the-library)__
