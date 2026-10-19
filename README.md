# ECON4310 Macroeconomic Theory: notebooks

Jupyter notebooks for [ECON4310 Macroeconomic Theory](https://www.uio.no/studier/emner/sv/oekonomi/ECON4310/) at the University of Oslo.

## Run in the browser

Click a badge. Nothing to install.

| Notebook | Colab (fast, needs a Google account) | Binder (no account, slower start) |
|---|---|---|
| `business_cycles.ipynb` | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mhaabeth/Econ-4310/blob/main/business_cycles.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mhaabeth/Econ-4310/HEAD?labpath=business_cycles.ipynb) |

In Colab, choose **Runtime → Run all**. Changes are not saved unless you choose **File → Save a copy in Drive**.

## Notebooks

| Notebook | Content |
|---|---|
| `business_cycles.ipynb` | Mainland GDP from SSB. HP and Hamilton filters. Business cycle facts for output, consumption and investment. AR(1) simulation. |

## Data

Notebooks download data directly from [Statistics Norway's API](https://www.ssb.no/en/api) (PxWebApi v2) using the helper in `ssb.py`. A snapshot in `data/` is used when the API is unreachable. SSB data are licensed under CC BY 4.0.

## Running locally

```bash
git clone https://github.com/mhaabeth/Econ-4310.git
cd Econ-4310
conda env create -f environment.yml
conda activate econ4310
jupyter lab
```

Or with pip: `pip install numpy pandas matplotlib statsmodels requests jupyterlab`.

## Credits

Inspired by Karl Harmenberg's [uiogrowth](https://github.com/karlharmenberg/uiogrowth) notebooks.

Maintained by Morten Grindaker, Department of Economics, University of Oslo.
