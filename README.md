# Paginate Pandas

A dead simple paginator for `pandas.Series` or `DataFrame`s that leverages on
`ipywidgets`:


```bash
pip install paginate_pandas
```

## Usage

```python
from paginate_pandas import paginate


data = ...  # Some DataFrame or Series
paginate(data)
```

See the demonstration in the 30s video below:

[screencast.webm](https://user-images.githubusercontent.com/1233486/204803747-fd4d00dd-5de8-4960-87eb-4d74bd5fb07e.webm)

You can also hide the NaN values to produce a neater frame visualization

```python
from paginate_pandas import paginate_fillna as paginate

paginate(data)  # NaN values are now empty cells
```
