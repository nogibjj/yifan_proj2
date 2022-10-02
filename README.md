# Customized Python CML tool
[![customized command line tool](https://github.com/nogibjj/yifan_proj2/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/yifan_proj2/actions/workflows/main.yml)

## How to use
### Python
- You can use it not only on one dataset(default) but also the one defined by yourself
```shell
Usage: py_cmd.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  count      Goup data with column name.
  load_data  Load data from existed csv file.
  sort       Sort data from cols with separator `,`.
  to_type    Transfer csv file to pkl or gdf file.
```
### shell script
- It will count the total number of source availble for each tv shows
- It will sort tv shows by sources into different file
- It will count the number of entry for each available source
```
sh ./process.sh
```

## Default Dataset
TV Shows Analysis: Netflix, Prime Video, Hulu and Disney+

The data scraped comprises a comprehensive list of tv shows available on various streaming platforms

Reference: https://www.kaggle.com/datasets/whenamancodes/netflix-prime-video-disney-hulu/code
