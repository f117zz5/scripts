#!/usr/bin/env python3
"""
Custom Terminal Calendar (gcal_cli)

A command-line tool to display a calendar with support for:
- Yearly and monthly views.
- ISO Week numbers (CW).
- Event management (stored in JSON).
- Highlighting for the current day and event days.

Author: Gemini (Refactored)
Date: 2026-01-11
"""

import calendar
import json
import os
import sys
import datetime
import argparse
from typing import Dict, List, Optional, Tuple

# Configuration
EVENTS_FILE = os.path.expanduser("~/.mycal_events.json")

# ANSI Colors Constants
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"

# Special Highlights
HL_TODAY_BG = "\033[30;103m"  # Black text on Bright Yellow background
HL_TODAY_EVENT_BG = "\033[31;103m" # Red text on Bright Yellow background


class CalendarEngine:
    """Handles data persistence and date calculations."""

    def __init__(self, storage_path: str):
        """
        Initialize the engine.

        Args:
            storage_path (str): Path to the JSON file storing events.
        """
        self.storage_path = storage_path
        self._events: Dict[str, List[str]] = self._load_events()

    def _load_events(self) -> Dict[str, List[str]]:
        """Loads events from the storage file."""
        if not os.path.exists(self.storage_path):
            return {}
        try:
            with open(self.storage_path, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}

    def _save_events(self) -> None:
        """Saves current events to the storage file."""
        with open(self.storage_path, 'w') as f:
            json.dump(self._events, f, indent=2)

    def add_event(self, date_str: str, text: str) -> bool:
        """
        Adds an event for a specific date.

        Args:
            date_str (str): Date in YYYY-MM-DD format.
            text (str): Description of the event.

        Returns:
            bool: True if successful, False if date format is invalid.
        """
        try:
            datetime.datetime.strptime(date_str, "%Y-%m-%d")
            if date_str not in self._events:
                self._events[date_str] = []
            self._events[date_str].append(text)
            self._save_events()
            return True
        except ValueError:
            return False

    def get_events(self) -> Dict[str, List[str]]:
        """Returns all stored events."""
        return self._events

    def get_week_number(self, year: int, month: int, day: int) -> int:
        """Returns the ISO calendar week number."""
        return datetime.date(year, month, day).isocalendar()[1]


class CalendarRenderer:
    """Handles visual rendering of the calendar."""

    def __init__(self, engine: CalendarEngine):
        """
        Initialize the renderer.

        Args:
            engine (CalendarEngine): The data source for events.
        """
        self.engine = engine
        self.cal = calendar.Calendar(firstweekday=0) # Monday is 0

    def _get_day_styled(self, year: int, month: int, day: int) -> str:
        """
        Returns the string representation of a day, styled with ANSI colors.

        Args:
            year (int): Year.
            month (int): Month.
            day (int): Day of the month.

        Returns:
            str: The 2-digit day string with ANSI codes.
        """
        date_obj = datetime.date(year, month, day)
        date_str = f"{year}-{month:02d}-{day:02d}"
        day_str = f"{day:2d}"
        
        events = self.engine.get_events()
        is_today = (date_obj == datetime.date.today())
        has_event = date_str in events

        if has_event:
            if is_today:
                return f"{HL_TODAY_EVENT_BG}{day_str}{RESET}"
            else:
                return f"{RED}{day_str}{RESET}"
        elif is_today:
            return f"{HL_TODAY_BG}{day_str}{RESET}"
        else:
            return day_str

    def render_month_lines(self, year: int, month: int, with_weeks: bool = True) -> List[str]:
        """
        Generates a list of strings representing the visual rows for a specific month.

        Args:
            year (int): The year.
            month (int): The month (1-12).
            with_weeks (bool): Whether to include the 'CW' column.

        Returns:
            List[str]: A list of exactly 8 strings (Title + Header + 6 Weeks).
        """
        lines = []
        month_days = self.cal.monthdayscalendar(year, month)
        month_name = calendar.month_name[month]
        
        # Geometry constants
        # Week col: 3 chars ("CW ")
        # Day cols: 7 * 3 = 21 chars ("Mo " ...)
        # Total Width: 24 (with weeks) or 21 (without)
        width = 24 if with_weeks else 21
        
        # 1. Title Line
        title = f"{month_name} {year}"
        pad_left = max(0, (width - len(title)) // 2)
        title_content = " " * pad_left + title
        title_content += " " * (width - len(title_content))
        lines.append(f"{BOLD}{title_content}{RESET}")
        
        # 2. Header Line
        header = "Mo Tu We Th Fr Sa Su"
        if with_weeks:
            header = "CW " + header
        
        # Pad header to match full width
        if len(header) < width:
            header += " " * (width - len(header))
        lines.append(f"{CYAN}{header}{RESET}")

        # 3. Week Lines
        for week in month_days:
            line = ""
            
            # Calendar Week Column
            if with_weeks:
                # Find the first non-zero day to determine the week number
                week_num_str = "   "
                for day in week:
                    if day != 0:
                        wk = self.engine.get_week_number(year, month, day)
                        week_num_str = f"{wk:2d} "
                        break
                line += f"{CYAN}{week_num_str}{RESET}"

            # Days Columns
            for day in week:
                if day == 0:
                    line += "   "
                else:
                    line += self._get_day_styled(year, month, day) + " "
            
            lines.append(line)
        
        # 4. Vertical Padding
        # Ensure we always return 8 lines (Title + Header + up to 6 weeks)
        while len(lines) < 8:
            lines.append(" " * width)
            
        return lines

    def print_year(self, year: int) -> None:
        """
        Prints the full calendar for the given year.

        Args:
            year (int): The year to display.
        """
        months = list(range(1, 13))
        # Process in blocks of 3 months
        for i in range(0, 12, 3):
            block_months = months[i:i+3]
            month_blocks = []
            
            for m in block_months:
                month_blocks.append(self.render_month_lines(year, m, with_weeks=True))
            
            # Print row by row
            max_lines = 8 
            for line_idx in range(max_lines):
                row_str = ""
                for m_idx, m_lines in enumerate(month_blocks):
                    if line_idx < len(m_lines):
                        row_str += m_lines[line_idx] + "   " # 3 spaces padding between months
                    else:
                        row_str += " " * 27 # 24 width + 3 padding
                print(row_str)
            print() # Spacer between quarters

    def list_events_list(self) -> None:
        """Prints all events sorted by date."""
        events = self.engine.get_events()
        if not events:
            print("No events found.")
            return
        
        print(f"{BOLD}Upcoming Events:{RESET}")
        for date_str in sorted(events.keys()):
            for event in events[date_str]:
                print(f"{CYAN}{date_str}{RESET}: {event}")


def main():
    """Main entry point for command line argument parsing."""
    engine = CalendarEngine(EVENTS_FILE)
    renderer = CalendarRenderer(engine)
    
    # 1. Handle "add" command
    if len(sys.argv) > 1 and sys.argv[1] == "add":
        if len(sys.argv) < 4:
            print("Usage: mycal add <YYYY-MM-DD> <text>")
            sys.exit(1)
        if engine.add_event(sys.argv[2], sys.argv[3]):
            print(f"{GREEN}Event added for {sys.argv[2]}: {sys.argv[3]}{RESET}")
        else:
            print(f"{RED}Invalid date format. Use YYYY-MM-DD.{RESET}")
        return

    # 2. Handle "list" command (flexible position)
    if "list" in sys.argv:
        renderer.list_events_list()
        return

    # 3. Handle Viewing (Year/Month)
    args = sys.argv[1:]
    now = datetime.datetime.now()
    year = now.year
    month = None

    # Simple heuristic parser for "mycal 2026", "mycal 1 2026", "mycal"
    if len(args) == 1:
        try:
            val = int(args[0])
            if val > 12:
                year = val
            else:
                month = val
        except ValueError:
            pass
    elif len(args) == 2:
        try:
            val1 = int(args[0])
            val2 = int(args[1])
            if val1 <= 12 and val2 > 12:
                month = val1
                year = val2
            elif val1 > 12 and val2 <= 12:
                year = val1
                month = val2
        except ValueError:
            pass
            
    if month:
        # Show specific month
        lines = renderer.render_month_lines(year, month, with_weeks=True)
        for line in lines:
            print(line)
    else:
        if len(args) == 0:
            # Default: Current month
            lines = renderer.render_month_lines(year, now.month, with_weeks=True)
            for line in lines:
                print(line)
        else:
            # Show full year
            renderer.print_year(year)

if __name__ == "__main__":
    main()