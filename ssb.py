"""Minimal helper for Statistics Norway's PxWebApi v2.

Example
-------
>>> from ssb import get_quarterly
>>> df = get_quarterly("09190", {"Makrost": ["bnpb.nr23_9fn"],
...                              "ContentsCode": ["FastePriserSesJust"]})

Browse tables at https://www.ssb.no/statbank. Variable and value codes for a
table are listed at
https://data.ssb.no/api/pxwebapi/v2/tables/<table_id>/metadata?lang=en
"""

from pathlib import Path

import pandas as pd
import requests

BASE = "https://data.ssb.no/api/pxwebapi/v2/tables"
SNAPSHOT = Path(__file__).parent / "data" / "ssb_09190_snapshot.csv"


def get_table(table_id, value_codes, lang="en", timeout=30):
    """Download a table as JSON-stat2 and return a long DataFrame.

    value_codes maps each dimension id to a list of value codes.
    Time is always included in full ("*") unless given explicitly.
    """
    params = {"lang": lang, "outputFormat": "json-stat2"}
    for dim, codes in value_codes.items():
        params[f"valueCodes[{dim}]"] = ",".join(codes)
    params.setdefault("valueCodes[Tid]", "*")
    r = requests.get(f"{BASE}/{table_id}/data", params=params, timeout=timeout)
    r.raise_for_status()
    js = r.json()

    dims = js["id"]
    index = pd.MultiIndex.from_product(
        [sorted(js["dimension"][d]["category"]["index"],
                key=js["dimension"][d]["category"]["index"].get) for d in dims],
        names=dims,
    )
    return pd.DataFrame({"value": js["value"]}, index=index).reset_index()


def quarter_to_period(q):
    """'2024K3' -> pandas quarterly Period."""
    return pd.Period(q.replace("K", "Q"), freq="Q")


def get_quarterly(table_id, value_codes, series_dim="Makrost", **kwargs):
    """Return a wide quarterly DataFrame: one column per value of series_dim."""
    df = get_table(table_id, value_codes, **kwargs)
    wide = df.pivot_table(index="Tid", columns=series_dim, values="value")
    wide.index = wide.index.map(quarter_to_period)
    wide.columns.name = None
    return wide.sort_index()


def load_snapshot():
    """Offline copy of table 09190 (constant prices, seasonally adjusted)."""
    df = pd.read_csv(SNAPSHOT)
    df.index = df.pop("quarter").map(quarter_to_period)
    return df
