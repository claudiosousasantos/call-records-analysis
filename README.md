# Call Records Analysis

A Python script that analyzes telecom call detail records (CDRs) to answer common network and usage questions.

## How it works
- Parses call records (caller, receiver, start time, duration, status, tower) from JSON
- **Plain Python section:** totals call time, counts calls by status with a dictionary, and calculates the dropped call rate
- **pandas section:** converts start times to datetimes, then summarizes calls and total duration per caller, calls per hour of day, and calls per cell tower

## Example results (sample data)
- 6 calls, 18.0 minutes of total call time
- Status counts: 4 completed, 1 missed, 1 dropped
- Dropped call rate: 16.7%
- Busiest hours: 8:00 and 10:00 (2 calls each)
- Busiest tower: T10 (3 calls)

## How to run
```bash
python cdr_analysis.py
```

## What I learned
- Counting items by category with a dictionary, using the check-then-increment pattern
- Using `.get(key, 0)` to safely read a count that might not exist
- Using `pd.to_datetime()` and `.dt.hour` to pull the hour out of a timestamp
- Using `.groupby().agg(['count', 'sum'])` to calculate several statistics in one step
- Using `.value_counts()` for quick frequency rankings
- How the same analysis looks with loops versus pandas

## Note on data
All phone numbers in this script are fictional sample values. Real call records are personal data, so never commit them to a public repository.

## Dependencies
Requires pandas:
```bash
pip install pandas
```
