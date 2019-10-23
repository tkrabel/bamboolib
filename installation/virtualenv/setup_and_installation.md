## Installing bamboolib using virtualenv

### 1. Create a virtual environment for your project

In the terminal enter the following where `bamboolib_venv` is the name of the virtual environment. Please change it if you want name your virtual environment differently.

```bash
virtualenv bamboolib_venv
source bamboolib_venv/bin/activate

ipython kernel install --user --name=bamboolib_venv
```

### 2. Install bamboolib

Use the `pip install` command we have send you via e-mail.

```bash
USE PIP COMMAND FROM E-MAIL
```

### 3. Setup Jupyter extensions

From the terminal, you need to setup the Jupyter Notebook extensions via the following command:

```bash
jupyter nbextension enable --py qgrid --sys-prefix
jupyter nbextension enable --py widgetsnbextension --sys-prefix
jupyter nbextension install --py bamboolib --sys-prefix
jupyter nbextension enable --py bamboolib --sys-prefix
```

### 4. Test bamboolib

Go [here](https://github.com/tkrabel/bamboolib/blob/master/installation/bamboolib_test_run/with_virtual_environment.md#test-the-library).
