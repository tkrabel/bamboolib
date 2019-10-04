## Test the library

First, start the Jupyter Kernel.

```bash
jupyter notebook
```

Afterwards, create a new notebook file.

Finally, run the following in a Jupyter Notebook code cell:

```python
import bamboolib as bam
df = bam.get_titanic_df()  # the titanic pd.DataFrame with 891 rows and 12 columns
# df = bam.get_1mio_rows_titanic_df()  # 1.079.001 rows and 12 columns
bam.show(df)
```

You should see a GUI if everything worked fine. If you don't see anything, please read [here](https://github.com/tkrabel/bamboolib/blob/master/installation/troubleshooting/troubleshooting.md#troubleshooting-installation-errors).
