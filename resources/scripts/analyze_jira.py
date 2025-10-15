#!/usr/bin/env python3
"""
Analyze Jira tickets from CSV export

Usage:
    python3 scripts/analyze_jira.py [options]

Options:
    --active        Show only active (To Do, In Progress, To Discuss, Validation) tickets
    --recent        Show recently completed tickets (last 30 days)
    --project NAME  Filter by project (e.g., SQUAD, RND)
    --summary       Show summary statistics only
    --all           Show all tickets grouped by status (default)
"""

import csv
import sys
from datetime import datetime, timedelta
from collections import defaultdict

CSV_PATH = "Context/Sola/data/Jira.csv"

def parse_date(date_str):
    """Parse Jira date format to datetime"""
    if not date_str:
        return None
    try:
        # Try common Jira date formats
        for fmt in ["%Y-%m-%d %H:%M:%S", "%Y-%m-%d", "%d/%b/%y %I:%M %p"]:
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        return None
    except:
        return None

def load_tickets():
    """Load tickets from CSV"""
    tickets = []
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            tickets.append(row)
    return tickets

def analyze_by_status(tickets):
    """Group tickets by status"""
    by_status = defaultdict(list)
    for ticket in tickets:
        status = ticket.get('Status', 'Unknown')
        by_status[status].append(ticket)
    return by_status

def analyze_by_project(tickets):
    """Group tickets by project"""
    by_project = defaultdict(list)
    for ticket in tickets:
        project = ticket.get('Issue key', '').split('-')[0] if ticket.get('Issue key') else 'Unknown'
        by_project[project].append(ticket)
    return by_project

def get_active_tickets(tickets):
    """Get tickets that are currently active"""
    active_statuses = ['To Do', 'In Progress', 'To Discuss', 'Validation']
    return [t for t in tickets if t.get('Status') in active_statuses]

def get_recent_completed(tickets, days=30):
    """Get tickets completed in last N days"""
    cutoff = datetime.now() - timedelta(days=days)
    recent = []

    for ticket in tickets:
        if ticket.get('Status') == 'Done':
            # Try to get completion date from Updated or Resolved field
            date_str = ticket.get('Updated') or ticket.get('Resolved')
            if date_str:
                date = parse_date(date_str)
                if date and date >= cutoff:
                    recent.append(ticket)

    return recent

def format_ticket(ticket):
    """Format ticket for display"""
    key = ticket.get('Issue key', 'N/A')
    summary = ticket.get('Summary', 'N/A')
    status = ticket.get('Status', 'N/A')
    assignee = ticket.get('Assignee', 'Unassigned')

    # Truncate summary if too long
    if len(summary) > 70:
        summary = summary[:67] + "..."

    return f"  [{key}] {summary}\n          Status: {status} | Assignee: {assignee}"

def print_summary(tickets):
    """Print summary statistics"""
    by_status = analyze_by_status(tickets)
    by_project = analyze_by_project(tickets)

    print("=" * 70)
    print("JIRA TICKETS SUMMARY")
    print("=" * 70)
    print(f"\nTotal Tickets: {len(tickets)}")

    print("\n--- By Status ---")
    for status, status_tickets in sorted(by_status.items(), key=lambda x: -len(x[1])):
        count = len(status_tickets)
        pct = (count / len(tickets) * 100) if tickets else 0
        print(f"  {status:20s}: {count:3d} ({pct:5.1f}%)")

    print("\n--- By Project ---")
    for project, proj_tickets in sorted(by_project.items(), key=lambda x: -len(x[1])):
        count = len(proj_tickets)
        pct = (count / len(tickets) * 100) if tickets else 0
        print(f"  {project:20s}: {count:3d} ({pct:5.1f}%)")

    print("\n" + "=" * 70)

def print_tickets(tickets, title):
    """Print list of tickets"""
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

    if not tickets:
        print("  (No tickets)")
    else:
        for ticket in tickets:
            print(format_ticket(ticket))
            print()

def main():
    args = sys.argv[1:]

    # Load tickets
    try:
        tickets = load_tickets()
    except FileNotFoundError:
        print(f"Error: Could not find {CSV_PATH}")
        print("Make sure the Jira CSV export is in the correct location.")
        return 1

    # Parse options
    show_active = '--active' in args
    show_recent = '--recent' in args
    show_summary = '--summary' in args
    project_filter = None

    for i, arg in enumerate(args):
        if arg == '--project' and i + 1 < len(args):
            project_filter = args[i + 1].upper()

    # Apply project filter if specified
    if project_filter:
        tickets = [t for t in tickets if t.get('Issue key', '').startswith(project_filter)]
        if not tickets:
            print(f"No tickets found for project: {project_filter}")
            return 0

    # Show requested view
    if show_summary:
        print_summary(tickets)
    elif show_active:
        active = get_active_tickets(tickets)
        print_tickets(active, f"ACTIVE TICKETS ({len(active)} total)")
    elif show_recent:
        recent = get_recent_completed(tickets)
        print_tickets(recent, f"RECENTLY COMPLETED ({len(recent)} in last 30 days)")
    else:
        # Default: show all grouped by status
        by_status = analyze_by_status(tickets)

        # Active statuses first
        active_statuses = ['To Do', 'In Progress', 'To Discuss', 'Validation']
        for status in active_statuses:
            if status in by_status:
                print_tickets(by_status[status], f"{status.upper()} ({len(by_status[status])} tickets)")

        # Then done
        if 'Done' in by_status:
            print(f"\n\n{'=' * 70}")
            print(f"COMPLETED: {len(by_status['Done'])} tickets")
            print("(Use --recent to see recently completed)")

        # Then won't do and others
        other_statuses = [s for s in by_status.keys() if s not in active_statuses and s != 'Done']
        for status in other_statuses:
            print_tickets(by_status[status], f"{status.upper()} ({len(by_status[status])} tickets)")

    return 0

if __name__ == '__main__':
    sys.exit(main())
