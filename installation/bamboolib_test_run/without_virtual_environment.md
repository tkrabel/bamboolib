## Test the library

First, start the Jupyter Kernel (**Jupyter Lab is currently not supported!**).

```bash
jupyter notebook
```

Afterwards, create a new notebook file.

Finally, run the following in a Jupyter Notebook code cell:

```python
import bamboolib as bam
import pandas as pd
df = pd.read_csv(bam.titanic_csv)
bam.show(df)
```

You should see a GUI if everything worked fine. If you don't see anything, please read [here](https://github.com/tkrabel/bamboolib/blob/master/installation/troubleshooting/troubleshooting.md#troubleshooting-installation-errors).
