# Installation of bamboolib

**Please note:** bamboolib currently only supports Jupyter Notebook.

This markdown will help you install bamboolib based on your computer setup. What does you setup look like?

- I am using [pip virtualenv](https://github.com/tkrabel/bamboolib/blob/master/Installation_walkthrough.md#installing-bamboolib-using-virtualenv)
- I am using [conda virtual environment](https://github.com/tkrabel/bamboolib/blob/master/Installation_walkthrough.md#installing-bamboolib-using-conda-environment)
- I don't use virtual environments / I don't know what a virtual environment is


In order to install bamboolib, you only need to do one thing.

## pip install

From the terminal, you can install bamboolib with the pip install command that you received from us via mail.

## Test the library

First, start the Jupyter Kernel ...

```bash
jupyter notebook
```

... and create a new notebook file. If you where using a virtual environment, choose the ipython kernel of your virtual environment.

Finally, run the following in a cell:

```python
import bamboolib as bam
df = bam.get_titanic_df()  # the titanic pd.DataFrame with 891 rows and 12 columns
# df = bam.get_1mio_rows_titanic_df()  # 1.079.001 rows and 12 columns
bam.show(df)
```

You should see a GUI if everything worked fine. If you don't see anything, please continue reading.

## Troubleshooting installation errors

Please make sure that the following is correct:
- you try to run bamboolib in a Jupyter Notebook. And not Jupyter Lab.
- you opened the Jupyter Notebook in the Chrome or Firefox browser. You don't use the Internet Explorer.

If the installation still doesn't work, you should try to [manually install the needed Jupyter Extensions](https://github.com/tkrabel/bamboolib/blob/master/Installation_walkthrough.md#manually-install-and-enable-jupyter-extensions).

## Manually install and enable Jupyter Extensions

As of Jupyter Notebook 5.3+, pip will not only install bamboolib, but also it's required notebook extensions. Sometimes however, this doesn't work automatically.

In such a case, you need to install and enable the bamboolib extension manually.

Open your terminal and run
```bash
jupyter nbextension enable --py widgetsnbextension --sys-prefix
jupyter nbextension install --py bamboolib --sys-prefix
jupyter nbextension enable --py bamboolib --sys-prefix
```

Then, restart your Jupyter notebook (make sure to shut down the server and start it over again) and try the code snippet from [above](https://github.com/tkrabel/bamboolib/blob/master/Installation_walkthrough.md#test-the-library) again.

---------

## Installing bamboolib using virtualenv

If you manage your python packages using `virtualenv`, then follow these steps to install and use bamboolib in your virtual environment.

### 0. pip install virtualenv if you haven't done already

```bash
pip install virtualenv
```

### 1. Create a virtual environment for your project

`<venv_name>` is the name you want to call your virtual environment.

```bash
virtualenv <venv_name>
```

### 2. Activate your virtual environment

`<venv_name>` is the name you gave your virtual environment at creation.

```bash
source <venv_name>/bin/activate
```

### 3. Install bamboolib

Use the pip install command we have send you via e-mail

### 4. Add the IPython kernel to Jupyter

`<display_name>` is the name that will appear in the kernel list of your Jupyter Notebook. You are not allowed to use spaces in `<display_name>`

```bash
ipython kernel install --user --name=<display_name>
```

### 5. Install the bamboolib jupyter extension

```bash
jupyter nbextension enable --py widgetsnbextension --sys-prefix
jupyter nbextension install --py bamboolib --sys-prefix
jupyter nbextension enable --py bamboolib --sys-prefix
```

### 6. Deactivate the virtual environment

This step is optional, but recommended if you have different Jupyter versions between your user and your virtual environment.

```bash
deactivate
```

### 7. Test bamboolib

Go [here](https://github.com/tkrabel/bamboolib/blob/master/Installation_walkthrough.md#test-the-library).

------------

## Installing bamboolib using conda environment

### 1. Create a virtual environment for your project

In the terminal client enter the following where <venv_name> is the name you want to call your environment.

```bash
conda create -n <venv_name>
```

Press y to proceed. This will install the Python version and all the associated anaconda packaged libraries at `<path_to_your_anaconda_location>/anaconda/envs/<venv_name>`

### 2. Activate your virtual environment

To activate or switch into your virtual environment, simply type the following where <venv_name> is the name you gave to your environement at creation.

```bash
source activate <venv_name>
```

### 3. Install pip in your virtual environment

```bash
conda install pip
```

At this point you have two versions of pip installed; a global version and a version specific to your virtual environment. Please make sure that the command `which pip` returns a ath to the pip version of your virtual environment. If it doesn't do so, you will need to find the directory of your virtual environment, which will be somewhere like `/anaconda/envs/<venv_name>/`. You can install packages into your virtual environment with `/anaconda/envs/<venv_name>/bin/pip install <package_name>`.

### 4. Install bamboolib

Use the pip install command we have send you via e-mail. Replace pip with your virtual environments pip version if necessary.

### 5. Deactivate your virtual environment

To end a session in the current environment, enter the following.

```bash
source deactivate
```

### 6. Test bamboolib

Go [here](https://github.com/tkrabel/bamboolib/blob/master/Installation_walkthrough.md#test-the-library).