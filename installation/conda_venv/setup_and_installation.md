## Installing bamboolib using conda environment

### 1. Create a virtual environment for your project

In the terminal enter the following where `bamboolib_venv` is the name of the virtual environment. Please change it if you want name your virtual environment differently.

```bash
conda create -n bamboolib_venv -y
```

### 2. Activate your virtual environment

```bash
conda activate bamboolib_venv
```

### 3. Install pip and ipykernel in your virtual environment

```bash
conda install pip -y
conda install ipykernel -y
```

### 4. Install bamboolib

Use the `pip install` command we have send you via e-mail.

#### bamboolib wasn't installed into your conda env?

In this case you need to replace `pip` with the absolute path to your conda env's pip

```bash
<path_to_your_anaconda_location>/envs/bamboolib_venv/bin/pip install ...  # use the rest from the e-mail
```

### 5. Setup Jupyter extensions

From the terminal, you need to setup the Jupyter Notebook extensions via the following command:

```bash
jupyter nbextension enable --py qgrid
```

### 6. Add the IPython kernel to Jupyter

```bash
python -m ipykernel install --user --name bamboolib_venv
```

### 7. Test bamboolib

Go [here](https://github.com/tkrabel/bamboolib/blob/master/installation/bamboolib_test_run/with_virtual_environment.md#test-the-library).
