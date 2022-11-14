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
