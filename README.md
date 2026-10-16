# ECON4310 Macroeconomic Theory: notebooks

Jupyter notebooks for [ECON4310 Macroeconomic Theory](https://www.uio.no/studier/emner/sv/oekonomi/ECON4310/) at the University of Oslo.

Run them in the browser, no installation needed:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mhaabeth/econ4310/HEAD)

## Notebooks

| Notebook | Content |
|---|---|
| `business_cycles.ipynb` | Mainland GDP from SSB. HP and Hamilton filters. Business cycle facts for output, consumption and investment. AR(1) simulation. |

## Data

Notebooks download data directly from [Statistics Norway's API](https://www.ssb.no/en/api) (PxWebApi v2) using the helper in `ssb.py`. A snapshot in `data/` is used when the API is unreachable. SSB data are licensed under CC BY 4.0.

## Running locally

```bash
git clone https://github.com/mhaabeth/econ4310.git
cd econ4310
conda env create -f environment.yml
conda activate econ4310
jupyter lab
```

Or with pip: `pip install numpy pandas matplotlib statsmodels requests jupyterlab`.

## Credits

Inspired by Karl Harmenberg's [uiogrowth](https://github.com/karlharmenberg/uiogrowth) notebooks.

Maintained by Morten Grindaker, Department of Economics, University of Oslo.
