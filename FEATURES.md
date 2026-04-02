# Feature Request: Scheduled Messages and Calendar-Driven Display Notices

**Product:** Display Forge // Display  
**Status:** Draft  
**Priority:** P1  
**Author:** Stuart  
**Created:** 2026-04-02  
**Version:** 1.0  

---

## 1. Summary

Add an inbuilt scheduling system for short on-screen messages designed for a 55-inch TV display.

The system must support:
- Automatic import of upcoming events from connected calendars
- Manual creation of scheduled display messages
- Defined appearance dates
- Automatic expiry after the relevant event or end date
- Default visibility beginning one week before the event

This feature will allow the display screen to act as a live internal noticeboard for meetings, events, reminders, deadlines, and important lodge or hall communications without requiring constant manual updates.

---

## 2. Problem Statement

The display system currently lacks a structured way to manage time-based notices.

Operators need a reliable method to:
- Automatically surface upcoming events from calendar sources
- Manually schedule short announcements for display
- Control when messages start appearing
- Ensure old notices disappear automatically after the relevant event
- Avoid stale, cluttered, or outdated information remaining on the screen

Without this, the screen becomes harder to trust, more labour-intensive to manage, and less useful as a communication channel.

---

## 3. Goals

The feature should:
- Turn the display into a trusted live noticeboard
- Reduce manual maintenance of TV messaging
- Ensure event notices appear at the right time
- Automatically remove expired items
- Support both automated and manual communications workflows
- Provide clean, readable, large-format output suitable for a 55-inch screen viewed at distance

---

## 4. Core Use Cases

### Use Case 1 — Calendar-driven event notice
As an operator, I want the system to import events from a connected calendar so that upcoming meetings and activities appear automatically on the display.

### Use Case 2 — Manual announcement scheduling
As an operator, I want to manually create a short message with a start date and end date so that I can schedule non-calendar notices such as reminders, warnings, or special announcements.

### Use Case 3 — Automatic display window
As an operator, I want calendar events to begin showing one week before the event date so that members have sufficient notice.

### Use Case 4 — Automatic expiry
As an operator, I want notices to disappear automatically after the related event or expiry date so that the screen stays current and uncluttered.

### Use Case 5 — Mixed schedule sources
As an operator, I want manually scheduled notices and calendar-imported notices to coexist in one timeline so that the display reflects all important communications in one place.

---

## 5. Functional Requirements

### FR-001 Calendar import
The system must support importing events from one or more calendar sources.

Supported sources should include:
- Google Calendar
- Microsoft 365 / Outlook Calendar
- ICS feed / shared calendar URL

### FR-002 Calendar sync
The system must refresh imported calendar data on a configurable sync interval.

**Default:** every 15 minutes

### FR-003 Event display window
Imported calendar events must appear on the display starting 7 days before the event start time by default.

**Configurable options:**
- 1 day before
- 3 days before
- 7 days before
- Custom number of days

### FR-004 Event expiry
Imported calendar notices must automatically expire once the event end time has passed.

**Optional setting:**
- Keep visible until end of day
- Expire immediately after end time
- Retain for custom number of hours after the event

### FR-005 Manual scheduling
The system must allow operators to manually create short display messages with:
- Title
- Short body text
- Optional category
- Start date/time
- End date/time
- Priority
- Target display or display group
- Publish status

### FR-006 Manual appearance rules
Manual messages must support:
- Immediate publish
- Scheduled future appearance
- Scheduled expiry
- Recurring schedule (optional phase 2)

### FR-007 Expiry handling
Expired manual messages must automatically stop appearing on the display without requiring manual removal.

### FR-008 Display formatting
Messages shown on the TV must be rendered in a large-format, high-legibility design suitable for a 55-inch screen.

**Requirements:**
- Large title text
- Short, readable body copy
- Optional event date/time line
- Optional icon/category marker
- High-contrast presentation
- Responsive safe margins for TV overscan and varied display layouts

### FR-009 Priority logic
Where multiple notices are active at the same time, the system must support ordering by:
- Priority
- Event date
- Creation date
- Pinned/manual override

### FR-010 Admin interface
The operator must have an admin screen to:
- View all scheduled notices
- View imported calendar events
- Edit manual notices
- Suppress imported events
- Override display windows
- Preview what will appear on screen

### FR-011 Event suppression
Operators must be able to hide individual imported calendar events without deleting them from the source calendar.

### FR-012 Preview mode
The system must provide a preview mode showing:
- What is live now
- What is due to appear in the next 7 days
- What is scheduled to expire soon

### FR-013 Fallback behavior
If a calendar source fails to sync, the system must:
- Keep the last known valid imported events
- Show sync failure status in admin
- Log the failure for troubleshooting

---

## 6. Suggested Data Model

### Message / Notice
```
- id
- source_type (`manual` | `calendar`)
- source_id
- title
- body
- category
- event_start
- event_end
- display_start
- display_end
- priority
- status (`draft` | `scheduled` | `live` | `expired` | `suppressed`)
- target_display
- created_by
- created_at
- updated_at
- sync_metadata
```

---

## 7. Business Rules

### Calendar items
- Imported events should default to `display_start = event_start - 7 days`
- Imported events should default to `display_end = event_end`
- If no event end exists, `display_end` should default to `event_start + 2 hours` unless overridden
- All-day events should expire at 23:59 local time on the event date unless configured otherwise

### Manual items
- A manual message must not go live before its `display_start`
- A manual message must expire automatically once `display_end` passes
- A message with no end date must require explicit confirmation before publishing

### Conflict handling
- Pinned notices may override normal ordering
- Higher-priority items should be shown more frequently where rotation is used
- Suppressed imported events must remain hidden unless manually re-enabled

---

## 8. UI / UX Requirements

### Admin experience
The admin area should include:
- Calendar feed configuration
- Notice list view
- Timeline or schedule view
- Manual notice creation form
- Status badges for live / upcoming / expired / suppressed
- Quick preview of TV output

### TV display experience
The TV presentation should:
- Cycle through active notices cleanly
- Show event date/time clearly
- Avoid excessive text
- Maintain strong readability from across a room
- Support branded themes and hall/lodge identity

**Recommended layout blocks:**
- Header
- Featured notice / current notice
- Upcoming event strip
- Optional footer with date/time or venue branding

---

## 9. Acceptance Criteria

### Calendar import
- Given a valid connected calendar, when events are synced, then future events are imported successfully
- Given an imported event, when it is 7 days before the event, then the event is eligible to appear on screen
- Given an imported event has ended, when the expiry condition is reached, then it no longer appears on the display

### Manual scheduling
- Given a manual message with a future start date, when the start date arrives, then the message appears automatically
- Given a manual message with an expiry date, when that date passes, then the message is removed automatically
- Given a manual message is marked draft, then it must not appear on the live display

### Admin controls
- Operators can suppress an imported event without removing it from the source calendar
- Operators can preview all messages scheduled for live display
- Operators can edit manual notices and save changes successfully

### Resilience
- If calendar sync fails, the admin panel shows the failure state
- Previously synced valid events remain available until the next successful sync or expiry

---

## 10. Non-Functional Requirements

- Calendar sync must be reliable and recover gracefully from connection failures
- Display rendering must remain readable on a 55-inch screen at room distance
- Scheduling must respect local timezone settings
- The admin interface must be usable on desktop and tablet
- Event and notice updates should propagate to the live display without requiring a full restart

---

## 11. Future Enhancements

### Phase 2
- Recurring manual notices
- Approval workflow for publishing notices
- Multiple display zones per screen
- Different notice templates by category
- Weather, dining, festive board, or service notices
- Per-screen targeting across multiple halls or rooms

### Phase 3
- AI-assisted summarisation of long calendar event titles into display-safe notices
- Smart priority suggestions based on event type
- Automatic branding and themed event cards
- Support for QR codes on selected notices

---

## 12. Suggested Feature Name Options

- Scheduled Display Notices
- Smart Noticeboard Scheduler
- Event and Message Scheduler
- Calendar-Driven Display Messaging
- Display Timeline Manager

**Recommended internal name:** `LB-DISPLAY-FR-001 — Scheduled Display Notices`

---

## 13. Implementation Notes

This feature should be designed as a unified scheduling layer rather than two separate systems.

The same display engine should handle:
- Imported calendar events
- Manually scheduled messages
- Future extensible content types

This keeps the logic clean and prevents the classic software sin of building two half-clever systems that immediately start arguing with each other.

---

## 14. Success Metrics

- Reduction in manual display updates
- Percentage of upcoming events automatically shown on screen
- Zero stale notices remaining after expiry
- Operator satisfaction with scheduling workflow
- Increased usage of the display as a trusted noticeboard

---

## 15. Technical Implementation Approach

### Backend Requirements
- Node.js/Express API for schedule management
- SQLite database for notice storage
- Google Calendar API integration
- Microsoft Graph API integration
- ICS feed parser
- Cron/scheduler for sync intervals

### Frontend Requirements
- React/Vue admin panel
- REST API for display client
- WebSocket for real-time updates
- LocalStorage fallback for offline operation

### Display Client Updates
- New slide type for notices/events
- Priority-based rotation logic
- Auto-expiry checking
- Sync status indicator

---

*Document Version: 1.0 | Last Updated: 2026-04-02*
