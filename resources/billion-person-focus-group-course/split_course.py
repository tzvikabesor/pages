#!/usr/bin/env python3
"""
Script to split the Maven course into individual lesson files.
"""

import re
from pathlib import Path

def parse_course_file(file_path):
    """Parse the course file and split into lessons."""

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lessons = []
    current_week = None
    current_lesson = None
    current_content = []

    lines = content.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i]

        # Detect week headers
        week_match = re.match(r'^# Week (\d+)', line)
        if week_match:
            # Save previous lesson if exists
            if current_lesson and current_content:
                lessons.append({
                    'week': current_week,
                    'lesson_num': current_lesson['num'],
                    'title': current_lesson['title'],
                    'content': '\n'.join(current_content)
                })
                current_content = []

            current_week = int(week_match.group(1))
            current_lesson = None
            i += 1
            continue

        # Detect lesson headers - various patterns
        lesson_patterns = [
            r'^# \*\*(.+?)\*\*\s*$',  # Bold headers
            r'^Lesson (\d+)[:\s•]',    # Lesson N:
        ]

        for pattern in lesson_patterns:
            match = re.match(pattern, line)
            if match:
                # Save previous lesson if exists
                if current_lesson and current_content:
                    lessons.append({
                        'week': current_week,
                        'lesson_num': current_lesson['num'],
                        'title': current_lesson['title'],
                        'content': '\n'.join(current_content)
                    })
                    current_content = []

                # Extract title from the next few lines
                title = ""
                if pattern == lesson_patterns[0]:  # Bold header
                    title = match.group(1)
                else:
                    # Look ahead for the title
                    for j in range(i, min(i+5, len(lines))):
                        if lines[j].startswith('#') and '**' in lines[j]:
                            title_match = re.search(r'\*\*(.+?)\*\*', lines[j])
                            if title_match:
                                title = title_match.group(1)
                                break

                # Try to extract lesson number
                lesson_num = None
                if pattern == lesson_patterns[1]:
                    lesson_num = int(match.group(1))
                else:
                    # Try to find lesson number nearby
                    for j in range(max(0, i-3), min(i+3, len(lines))):
                        num_match = re.search(r'Lesson (\d+)', lines[j])
                        if num_match:
                            lesson_num = int(num_match.group(1))
                            break

                if not lesson_num:
                    # Assign sequential number
                    lesson_num = len([l for l in lessons if l['week'] == current_week]) + 1

                current_lesson = {
                    'num': lesson_num,
                    'title': title or line.strip('#').strip('*').strip()
                }
                break

        # Add line to current content
        if current_lesson or current_week == 1:
            current_content.append(line)

        i += 1

    # Save final lesson
    if current_lesson and current_content:
        lessons.append({
            'week': current_week,
            'lesson_num': current_lesson['num'],
            'title': current_lesson['title'],
            'content': '\n'.join(current_content)
        })

    return lessons


def create_filename(week, lesson_num, title):
    """Create a sanitized filename for a lesson."""
    # Clean title for filename
    clean_title = re.sub(r'[^\w\s-]', '', title)
    clean_title = re.sub(r'[\s]+', '-', clean_title)
    clean_title = clean_title.lower().strip('-')[:50]  # Limit length

    if not clean_title:
        clean_title = "lesson"

    return f"week-{week:02d}-lesson-{lesson_num:02d}-{clean_title}.md"


def split_course(input_file, output_dir):
    """Split the course file into individual lesson files."""
    input_path = Path(input_file)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    print(f"Reading course from: {input_file}")
    lessons = parse_course_file(input_file)

    print(f"\nFound {len(lessons)} lessons")

    created_files = []
    for lesson in lessons:
        filename = create_filename(
            lesson['week'],
            lesson['lesson_num'],
            lesson['title']
        )
        filepath = output_path / filename

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(lesson['content'])

        created_files.append(filename)
        print(f"Created: {filename}")
        print(f"  Week {lesson['week']}, Lesson {lesson['lesson_num']}: {lesson['title']}")

    return created_files


if __name__ == '__main__':
    course_file = '/Users/tzvika.b/Documents/my-work-system/projects/billion-person-focus-group/Course/Maven course.md'
    output_dir = '/Users/tzvika.b/Documents/my-work-system/projects/billion-person-focus-group/Course'

    created = split_course(course_file, output_dir)
    print(f"\n✓ Created {len(created)} lesson files")
