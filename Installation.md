# Installation of bamboolib

**Please note: bamboolib currently only supports Jupyter Notebook.**

In order to install bamboolib, you only need to do one thing.

## pip install

From the terminal, you can install bamboolib with the pip install command that you received from us via mail.

## Test the library

To check whether everything went smoothly, start your Jupyter Notebook (`jupyter notebook`) in the terminal, create a new notebook file and run the following:

```python
import bamboolib as bam
df = bam.get_titanic_df()
df = pd.concat([df for i in range(0, 1211)])  # expand df to 1 mio rows
prep = bam.prep(df)
prep
```

You should see a GUI if everything worked fine. If you don't see anything, please continue reading.

## Manually install and enable Jupyter Extensions

As of Jupyter Notebook 5.3+, pip will not only install bamboolib, but also it's required notebook extensions. Sometimes however, this doesn't work automatically.

In such a case, you need to install and enable the bamboolib extension manually.

Open your terminal and run
```bash
# install the extension
jupyter nbextension install --py bamboolib --sys-prefix
# tell jupyter to load it everytime you start a jupyter notebook
jupyter nbextension enable --py bamboolib --sys-prefix
```

Then, restart your Jupyter notebook (make sure to shut down the server and start it over again) and try the code snippet from above again.
