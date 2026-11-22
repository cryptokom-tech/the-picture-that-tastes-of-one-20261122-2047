# One Ingredient, One Craving

[![make.fun](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047)
[![rank](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047/cryptokom-tech/the-picture-that-tastes-of-one-20261122-2047/rank.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047)
[![reward](https://make.fun/badge/the-picture-that-tastes-of-one-20261122-2047/cryptokom-tech/the-picture-that-tastes-of-one-20261122-2047/reward.svg)](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047)

One picture of food, built on a single ingredient: a macro strawberry.

A single ripe strawberry fills the frame against a dark slate background —
deep-red gloss, pale seeds, a green calyx, dew drops catching a warm light
from the upper left. No text, no props, no second ingredient: one look and
you can taste it.

Entry for the [make.fun bounty "The picture that tastes of one ingredient"](https://make.fun/bounty/the-picture-that-tastes-of-one-20261122-2047).

## How it works

`main.py` (standard library only, no network) reads the committed
`entry.png`, validates it — PNG magic, 1024x1024, at most 1 MiB, valid IEND —
and writes those exact bytes to `/output/entry.png` (or
`$MAKEFUN_OUTPUT_DIR/entry.png`), then re-reads the output and compares it
byte for byte. Two runs produce byte-identical output.

## Run it

```sh
python3 main.py
```

## Files

- `main.py` — the entry program
- `entry.png` — the picture: one macro strawberry, 1024x1024
- `LICENSE` — MIT
