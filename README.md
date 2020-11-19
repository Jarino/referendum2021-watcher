# referendum2021-watcher
Script to scrape the count of votes from DiscoPelle's referendum

## Deployment

Currently using crontab:
```
0,5,10,15,20,25,30,35,40,45,50,55 * * * * /path/to/refwatch.py >> /path/to/refwatch.log 2>&1
```

Some notes on that:
- depending on the system, the python executable might need to be specified via shebang
- the `DB_NAME` variable in `db.py` is relative, but it might need to be changed to absolute
