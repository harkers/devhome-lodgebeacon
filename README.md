# Display Forge Display

**Premium Digital Signage for Masonic Halls**

---

## Overview

Display Forge is a sophisticated digital signage system designed specifically for Masonic halls and lodges. It transforms any TV or display into an elegant noticeboard showing lodge information, meeting schedules, upcoming events, and important announcements.

**Current Deployment:** Alfreton Masonic Hall  
**Version:** MVP 0.2  
**Status:** Production Ready  

---

## Features

### 🎨 Premium Themes
Four professionally designed themes with "Quiet Luxury" aesthetics:

- **Masonic Heritage** - Traditional navy and gold (default)
- **Silicon Valley Slate** - Clean, professional, high-trust
- **International Orange** - Bold, industrial, high-performance
- **Cyber-Quartz** - Sophisticated, glass aesthetic

### 📊 Dynamic Content
- **Craft Lodge Pages** - Individual slides for each lodge with meeting details
- **Masonic Quotes** - Rotating inspirational quotes between content slides
- **Event Calendar** - Upcoming meetings and special events
- **Emergency Notices** - Override system for urgent announcements

### 🖥️ Admin Panel
- Theme selector with live preview
- Emergency message broadcasting
- Support contact integration
- Real-time display control

---

## Quick Start

### Run Locally

```bash
cd /home/stu/lodgebeacon-display
python3 -m http.server 18080
```

Then open `http://localhost:18080` in your browser.

### Deploy on Raspberry Pi / TV

1. **Install dependencies:**
   ```bash
   sudo apt update
   sudo apt install chromium-browser
   ```

2. **Set up auto-start:**
   ```bash
   # Create startup script
   cat > /home/pi/start-lodgebeacon.sh << 'EOF'
   #!/bin/bash
   chromium-browser --kiosk --incognito http://YOUR_SERVER_IP:18080
   EOF
   chmod +x /home/pi/start-lodgebeacon.sh
   ```

3. **Add to crontab:**
   ```bash
   crontab -e
   # Add: @reboot /home/pi/start-lodgebeacon.sh
   ```

---

## File Structure

```
lodgebeacon-display/
├── index.html              # Main display page
├── admin.html              # Admin control panel
├── css/
│   └── display-themes.css  # All theme definitions
├── js/
│   └── display.js          # Display logic and content
├── FEATURES.md             # Planned features (P1)
├── README.md               # This file
└── QUICKSTART.md           # Quick setup guide
```

---

## Display Content

### Current Slides (13 Total)

1. **Welcome** - Hall introduction
2. **History** - Building background
3. **Craft Lodges Overview** - All lodges listed
4. **Royal Alfred Lodge 1028** - Meeting details
5. **St Thomas Lodge 2583** - Meeting details
6. **Vulcan Lodge 4382** - Meeting details
7. **Morcar Lodge 8548** - Meeting details
8. **Pioneer Lodge 9065** - Meeting details
9. **Other Orders** - Royal Arch, Mark, etc.
10. **Facilities** - Hall amenities
11. **Visitors** - Welcome message
12. **Contact** - Location and info
13. **Masonic Quotes** - Rotating wisdom (interplaced)

### Quote System

10 Masonic quotes rotate randomly throughout the display cycle:

> "The badge of a Mason is not honour worn upon the breast, but honour carried faithfully in conduct."

> "He who governs himself with wisdom may one day help guide others with dignity."

> "The strongest lodge is built not merely by ritual well performed, but by men who live its virtues when no eye is upon them."

...and 7 more.

---

## Configuration

### Change Theme

**Via Admin Panel:**
1. Open `http://YOUR_DISPLAY:18080/admin.html`
2. Select desired theme
3. Changes apply immediately

**Via Browser Console:**
```javascript
window.setDisplayTheme('slate') // Options: masonic, slate, industrial, quartz
```

### Adjust Slide Timing

Edit `js/display.js`:

```javascript
const config = {
    slideInterval: 10000, // 10 seconds per slide
    emergencyCheckInterval: 5000,
    showClock: true
};
```

---

## Emergency System

### Send Emergency Message

**Via Admin Panel:**
1. Open admin panel
2. Enter message in Emergency section
3. Click "Send Emergency Message"

**Via Browser Console (on display):**
```javascript
window.triggerEmergency("Hall closed due to weather")
```

### Clear Emergency

**Via Admin Panel:**
- Click "Clear Emergency" button

**Via Browser Console:**
```javascript
window.clearEmergencyManual()
```

---

## Access URLs

| Service | URL |
|---------|-----|
| Display | http://192.168.10.80:18080 |
| Admin Panel | http://192.168.10.80:18080/admin.html |
| GitHub Repo | https://github.com/harkers/devhome-lodgebeacon |

---

## Support

**Contact:** stuharker@gmail.com  
**Location:** Alfreton Masonic Hall, Derby Road, Alfreton, DE55 7AQ  

---

## Planned Features (P1 Priority)

See `FEATURES.md` for detailed specification:

### Scheduled Display Notices
- Calendar integration (Google, Microsoft 365, ICS)
- Automatic event import with configurable display windows
- Manual message scheduling
- Auto-expiry after events
- Priority-based ordering
- Event suppression controls
- Preview mode

**Target Implementation:** Phase 1

---

## Technical Details

### Typography & Spacing

Built on "Quiet Luxury" design principles:

- **Headings:** Tight tracking (`letter-spacing: -0.03em`), tight leading (`line-height: 1.1`)
- **Body Text:** Relaxed spacing (`line-height: 1.65`, `letter-spacing: 0.01em`)
- **8-Point Grid:** All margins/padding in multiples of 8px
- **Line Length:** Max 65 characters for optimal readability

### Font Stack

```css
/* Headings */
font-family: 'Outfit', sans-serif; /* Geometric, premium feel */

/* Body */
font-family: 'Figtree', sans-serif; /* Clean, highly legible */
```

### Color Palettes

Each theme uses carefully selected colors for depth and contrast:

**Masonic Heritage:**
- Background: `#0a1628` (Deep Navy)
- Accent: `#c9a227` (Masonic Gold)

**Silicon Valley Slate:**
- Background: `#f8fafc` (Cool Off-White)
- Accent: `#38bdf8` (Sky Blue)

**International Orange:**
- Background: `#121212` (Matte Black)
- Accent: `#ff5f1f` (Safety Orange)

**Cyber-Quartz:**
- Background: `#0f0e17` (Deep Quartz)
- Accent: `#a78bfa` (Soft Violet)

---

## Development

### Local Development

```bash
# Clone repository
git clone https://github.com/harkers/devhome-lodgebeacon.git
cd devhome-lodgebeacon

# Start development server
python3 -m http.server 18080

# Open in browser
open http://localhost:18080
```

### Making Changes

1. Edit files in `css/` or `js/` directories
2. Refresh browser to see changes
3. Commit and push to deploy

### Git Workflow

```bash
git add .
git commit -m "Description of changes"
git push origin main
```

---

## License

Proprietary - Harker Systems

---

**Last Updated:** 2026-04-02  
**Version:** MVP 0.2
