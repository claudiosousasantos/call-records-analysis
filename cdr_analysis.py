import json
import pandas as pd

cdr_json = '''
[
    {"call_id": "C001", "caller": "5551001", "receiver": "5552002", "start_time": "2024-01-15 08:05:00", "duration_seconds": 120, "status": "completed", "tower_id": "T10"},
    {"call_id": "C002", "caller": "5551001", "receiver": "5553003", "start_time": "2024-01-15 08:30:00", "duration_seconds": 45, "status": "completed", "tower_id": "T10"},
    {"call_id": "C003", "caller": "5552002", "receiver": "5551001", "start_time": "2024-01-15 09:15:00", "duration_seconds": 0, "status": "missed", "tower_id": "T11"},
    {"call_id": "C004", "caller": "5553003", "receiver": "5554004", "start_time": "2024-01-15 10:00:00", "duration_seconds": 300, "status": "completed", "tower_id": "T12"},
    {"call_id": "C005", "caller": "5551001", "receiver": "5554004", "start_time": "2024-01-15 10:45:00", "duration_seconds": 15, "status": "dropped", "tower_id": "T10"},
    {"call_id": "C006", "caller": "5554004", "receiver": "5552002", "start_time": "2024-01-15 11:20:00", "duration_seconds": 600, "status": "completed", "tower_id": "T12"}
]
'''

# Parse JSON
calls = json.loads(cdr_json)

# Print each call
for call in calls:
    print(f"{call['call_id']}: {call['caller']} -> {call['receiver']} | {call['duration_seconds']}s | {call['status']}")

# Total call time
total_seconds = 0
for call in calls:
    total_seconds += call['duration_seconds']
print(f"\nTotal call time: {total_seconds} seconds ({total_seconds / 60:.1f} minutes)")

# Count by status
status_counts = {}
for call in calls:
    status = call['status']
    if status in status_counts:
        status_counts[status] += 1
    else:
        status_counts[status] = 1
print("Status counts:", status_counts)

# Dropped call rate
dropped_rate = status_counts.get('dropped', 0) / len(calls)
print(f"Dropped call rate: {dropped_rate:.1%}")

# Pandas analysis
df = pd.DataFrame(calls)
df['start_time'] = pd.to_datetime(df['start_time'])
df['hour'] = df['start_time'].dt.hour

print("\nCalls and total seconds per caller:")
print(df.groupby('caller')['duration_seconds'].agg(['count', 'sum']))

print("\nCalls per hour:")
print(df.groupby('hour').size())

print("\nCalls per tower:")
print(df['tower_id'].value_counts())