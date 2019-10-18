## Installing bamboolib using virtualenv

### 1. Create a virtual environment for your project

In the terminal enter the following where `bamboolib_venv` is the name of the virtual environment. Please change it if you want name your virtual environment differently.

```bash
virtualenv bamboolib_venv
```

### 2. Activate your virtual environment

```bash
source bamboolib_venv/bin/activate
```

### 3. Install bamboolib

Use the `pip install` command we have send you via e-mail.

### 4. Setup Jupyter extensions

From the terminal, you need to setup the Jupyter Notebook extensions via the following command:

```bash
jupyter nbextension enable --py qgrid
```

### 5. Add the IPython kernel to Jupyter

`bamboolib_venv` is the name that will appear in the kernel list of your Jupyter Notebook. Please change it if you want to have a different kernel name.

```bash
ipython kernel install --user --name=bamboolib_venv
```

### 6. Test bamboolib

Go [here](https://github.com/tkrabel/bamboolib/blob/master/installation/bamboolib_test_run/with_virtual_environment.md#test-the-library).
