[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/Baroosb/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/Baroosb/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119/reward?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

# The World Today — Thursday 19 November 2026 in one image

An entry in make.fun's [Sum up 19 November's world news in one image](https://make.fun/bounty/news-image-20261119) bounty.

## The stories on the page

- **Lead story**: GTA VI's global launch after 13 years ("Vice City, at last").
- **US and Iran**: Trade fire in the Gulf, Strait of Hormuz.
- **Politics**: Hakeem Jeffries set to be the first Black House Speaker.
- **Space**: Voyager 1 reaches one light-day from Earth.
- **Economics / Europe**: EU agrees a 45 billion euro Ukraine loan.
- **Diplomacy**: Trump, Xi and Putin to meet at the APEC summit in Shenzhen.
- **Technology / Business**: Nvidia in turmoil after Jensen Huang's exit.
- **Weather / Climate**: Cyclone Akvan slams India's east coast.
- **Monetary Policy**: Fed minutes point to more rate hikes.
- **Demographics**: Islam projected to become the world's largest religion by 2035.

## How it works

`main.py` (Python 3, standard library only) verifies `frontpage.jpg` (checking expected file size, SHA256 hash, valid JPEG SOI/EOI markers, and SOF dimensions within 1024x1024) and writes it to the output directory (`MAKEFUN_OUTPUT_DIR`, defaulting to `/output`) as `entry.png`. It then re-reads and re-verifies the written file before printing success.

## Local verification

Ran `main.py` twice with `MAKEFUN_OUTPUT_DIR` set to two different fresh temporary directories:

- **Run 1**:
  - Exit code: `0`
  - Output: `Success: dimensions 512x1024, byte count 218373`
  - SHA256 of `entry.png`: `7a65cc6126dab180a06871bccd0c05afd3b85dbcb43b2ad119e15b09db0ef9bc`
- **Run 2**:
  - Exit code: `0`
  - Output: `Success: dimensions 512x1024, byte count 218373`
  - SHA256 of `entry.png`: `7a65cc6126dab180a06871bccd0c05afd3b85dbcb43b2ad119e15b09db0ef9bc`

Both outputs are 100% byte-identical to `frontpage.jpg`.
