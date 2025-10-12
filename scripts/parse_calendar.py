#!/usr/bin/env python3
"""
Parse ICS calendar file and extract events into structured format
"""

import re
from datetime import datetime, timedelta
from collections import defaultdict

def parse_ics(file_path):
    """Parse ICS file and extract events"""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into individual events
    events = []
    current_event = {}
    in_event = False

    for line in content.split('\n'):
        line = line.strip()

        if line == 'BEGIN:VEVENT':
            in_event = True
            current_event = {}
        elif line == 'END:VEVENT':
            in_event = False
            if current_event:
                events.append(current_event)
            current_event = {}
        elif in_event:
            # Parse event properties
            if ':' in line:
                # Handle properties with parameters (e.g., DTSTART;TZID=...)
                if ';' in line.split(':')[0]:
                    key = line.split(';')[0]
                    value = ':'.join(line.split(':')[1:])
                else:
                    key = line.split(':')[0]
                    value = ':'.join(line.split(':')[1:])

                # Store the property
                current_event[key] = value

    return events

def format_datetime(dt_string):
    """Convert ICS datetime to readable format"""
    if not dt_string:
        return None

    # Remove timezone info for parsing
    dt_clean = dt_string.split(';')[0] if ';' in dt_string else dt_string
    dt_clean = dt_clean.replace('TZID=Asia/Jerusalem:', '')

    try:
        if 'T' in dt_clean:
            # Has time component
            if 'Z' in dt_clean:
                dt = datetime.strptime(dt_clean, '%Y%m%dT%H%M%SZ')
            else:
                dt = datetime.strptime(dt_clean, '%Y%m%dT%H%M%S')
            return dt.strftime('%Y-%m-%d %H:%M')
        else:
            # All-day event
            dt = datetime.strptime(dt_clean, '%Y%m%d')
            return dt.strftime('%Y-%m-%d')
    except:
        return dt_string

def analyze_events(events):
    """Analyze and summarize events"""

    # Filter to future/recent events (last 30 days and future)
    now = datetime.now()
    cutoff = datetime(now.year, now.month, now.day) - timedelta(days=30)

    future_events = []
    recurring_events = defaultdict(int)

    for event in events:
        dtstart = event.get('DTSTART', '')
        summary = event.get('SUMMARY', 'No Title')

        # Check if recurring
        if 'RRULE' in event:
            recurring_events[summary] += 1

        # Try to parse date
        try:
            dt_clean = dtstart.split(';')[-1].split(':')[-1]
            if 'T' in dt_clean:
                dt_clean = dt_clean.replace('Z', '')
                event_date = datetime.strptime(dt_clean[:8], '%Y%m%d')
            else:
                event_date = datetime.strptime(dt_clean, '%Y%m%d')

            if event_date >= cutoff:
                future_events.append({
                    'date': format_datetime(dtstart),
                    'summary': summary,
                    'description': event.get('DESCRIPTION', ''),
                    'location': event.get('LOCATION', ''),
                    'recurring': 'RRULE' in event
                })
        except:
            pass

    # Sort by date
    future_events.sort(key=lambda x: x['date'] if x['date'] else '')

    return future_events, recurring_events

def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: python parse_calendar.py <ics_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    print("Parsing calendar file...")
    events = parse_ics(file_path)
    print(f"Found {len(events)} total events")

    print("\nAnalyzing events...")
    future_events, recurring = analyze_events(events)

    # Print upcoming events
    print(f"\n{'='*80}")
    print(f"UPCOMING & RECENT EVENTS (Last 30 days + Future)")
    print(f"{'='*80}\n")

    for event in future_events[:50]:  # Show first 50
        print(f"📅 {event['date']}")
        print(f"   {event['summary']}")
        if event['location']:
            print(f"   📍 {event['location']}")
        if event['recurring']:
            print(f"   🔄 Recurring")
        print()

    # Print recurring event summary
    print(f"\n{'='*80}")
    print(f"RECURRING EVENTS SUMMARY")
    print(f"{'='*80}\n")

    for title, count in sorted(recurring.items(), key=lambda x: x[1], reverse=True)[:20]:
        print(f"🔄 {title} ({count} occurrences)")

    # Export to JSON
    import json
    output_file = file_path.replace('.ics', '_parsed.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({
            'total_events': len(events),
            'upcoming_events': future_events,
            'recurring_summary': dict(recurring)
        }, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Full data exported to: {output_file}")

if __name__ == '__main__':
    main()
