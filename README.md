# haproxystat

CLI tool for HAProxy statistics. Gets the statistics CSV file from the statistics page (usually `http://localhost:1936/;csv`) and displays them on `stdout`.

## Usage

When viewing the CSV file, values can be read from left to right with the basic syntax of "pxname | svname | statistic" (e.g. `www_backend | server1 | bin`).

`haproxystat` uses this scheme by separating the column names with a dot.

```
haproxystat -s www_backend.server1.bin # Get value for specified statistic`
haproxystat                            # List all statistics
haproxystat -c                         # Get CSV content
```
