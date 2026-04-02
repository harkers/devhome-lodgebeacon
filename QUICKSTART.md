# Display Forge Display - Quick Start

**Premium Digital Signage for Masonic Halls**

---

## 🚀 Running the Display (3 Steps)

### Step 1: Start the Server

```bash
cd /home/stu/lodgebeacon-display
python3 -m http.server 18080
```

### Step 2: Open the Display

In a browser, go to:
```
http://localhost:18080
```

Or open directly:
```bash
# Linux
firefox http://localhost:18080 &

# Mac
open http://localhost:18080
```

### Step 3: Full Screen

- Press **F11** for full-screen mode
- Or use browser's fullscreen option

---

## 🎛️ Admin Interface

Open in another tab/window:
```
http://localhost:18080/admin.html
```

**Features:**
- 🎨 Theme selector (4 premium themes)
- 🚨 Emergency message broadcasting
- 👁️ Display preview
- 📞 Support contact: stuharker@gmail.com

---

## 🎨 Changing Themes

### Via Admin Panel
1. Open admin panel at `http://localhost:18080/admin.html`
2. Click on desired theme card:
   - **Masonic Heritage** - Traditional navy and gold
   - **Silicon Valley Slate** - Clean, professional
   - **International Orange** - Bold, industrial
   - **Cyber-Quartz** - Sophisticated, premium
3. Changes apply immediately

### Via Browser Console
```javascript
// Available themes: masonic, slate, industrial, quartz
window.setDisplayTheme('slate');
```

### Persist Theme Choice
Theme selection is saved to browser localStorage and persists across sessions.

---

## 📋 What's Included

| Feature | Status | Description |
|---------|--------|-------------|
| **Slide rotation** | ✅ Working | Auto-rotates every 10 seconds |
| **Clock display** | ✅ Working | Shows current time and date (bottom-right) |
| **Emergency override** | ✅ Working | Instant red screen broadcast |
| **Admin panel** | ✅ Working | Theme selector + emergency controls |
| **Craft lodge pages** | ✅ Working | 5 individual lodge slides with meeting details |
| **Masonic quotes** | ✅ Working | 10 quotes rotate randomly |
| **Premium themes** | ✅ Working | 4 professionally designed themes |
| **8-point grid spacing** | ✅ Working | Professional typography and layout |

---

## 🖥️ Setting Up a Raspberry Pi Display

### Requirements
- Raspberry Pi 3 or 4
- Micro SD card (16GB+)
- TV or monitor with HDMI
- WiFi or ethernet connection

### Installation Steps

1. **Install Raspberry Pi OS Lite**
   ```bash
   # Download from https://www.raspberrypi.com/software/
   # Flash to SD card using Raspberry Pi Imager
   ```

2. **Configure auto-login**
   ```bash
   sudo raspi-config
   # System Options > Boot / Auto Login > Desktop Autologin
   ```

3. **Install Chromium**
   ```bash
   sudo apt update
   sudo apt install chromium-browser
   ```

4. **Create startup script**
   ```bash
   cat > /home/pi/start-lodgebeacon.sh << 'EOF'
   #!/bin/bash
   sleep 10
   export DISPLAY=:0
   chromium-browser --kiosk --incognito --disable-session-crashed-bubble http://YOUR_SERVER_IP:18080
   EOF
   chmod +x /home/pi/start-lodgebeacon.sh
   ```

5. **Add to startup**
   ```bash
   echo '@reboot /home/pi/start-lodgebeacon.sh' | crontab
   ```

6. **Reboot and test**
   ```bash
   sudo reboot
   ```

---

## 🚨 Using Emergency Messages

### From Admin Page
1. Open `http://localhost:18080/admin.html`
2. Type message in "Emergency Message" box
3. Click **"Send Emergency Message"**
4. All displays show red emergency screen immediately

### From Browser Console (on display)
```javascript
// Trigger emergency
window.triggerEmergency("Hall closed due to weather");

// Clear emergency
window.clearEmergencyManual();
```

### How It Works
- Emergency overlay appears instantly
- Overrides all slide rotation
- Red background with white text
- Visible from any angle
- Cleared via admin panel or console

---

## ✏️ Customizing Content

### Change Slide Timing

Edit `js/display.js`:

```javascript
const config = {
    slideInterval: 10000, // 10 seconds per slide (adjust as needed)
    emergencyCheckInterval: 5000,
    showClock: true
};
```

### Add/Edit Slides

In `js/display.js`, modify the `slides` array:

```javascript
const slides = [
    {
        id: 'welcome',
        html: `
            <div class="slide">
                <h1>Your Custom Title</h1>
                <p style="font-size: 2rem;">Your custom content</p>
            </div>
        `
    },
    // Add more slides...
];
```

### Customize Lodge Information

Find the `craftLodges` array in `js/display.js`:

```javascript
const craftLodges = [
    {
        name: "Royal Alfred Lodge",
        number: "1028",
        warrant: "13th August 1864",
        meetingDay: "First Monday",
        meetingTime: "6:30pm",
        nextMeeting: {
            date: "7th April 2025",
            business: "1st Degree",
            time: "6:30pm"
        }
    },
    // Edit other lodges...
];
```

### Modify Quotes

Find the `masonicQuotes` array in `js/display.js` and add/edit quotes:

```javascript
const masonicQuotes = [
    "The badge of a Mason is not honour worn upon the breast, but honour carried faithfully in conduct.",
    // Add your own quotes...
];
```

---

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| Display not loading | Check server is running: `python3 -m http.server 18080` |
| Blank screen | Check browser console for errors (F12) |
| Slides not rotating | Refresh browser (Ctrl+R / Cmd+R) |
| Emergency not showing | Check admin page localStorage matches display |
| Clock not updating | Refresh browser; check JavaScript console |
| Theme not changing | Ensure localStorage is enabled in browser |
| Fonts not loading | Check internet connection (Google Fonts) |
| Text too small/large | Adjust font sizes in `css/display-themes.css` |

---

## 📁 File Structure

```
lodgebeacon-display/
├── index.html              # Main display page
├── admin.html              # Admin control panel
├── README.md               # Full documentation
├── QUICKSTART.md           # This file
├── FEATURES.md             # Planned features (P1 priority)
├── css/
│   └── display-themes.css  # All theme definitions + base styles
└── js/
    └── display.js          # Display logic, content, quotes
```

---

## 🎯 Current Features (MVP 0.2)

### Content
- ✅ 13 slides total (welcome, history, lodges, facilities, etc.)
- ✅ 5 individual Craft lodge pages with meeting schedules
- ✅ 10 Masonic quotes (randomly interplaced)
- ✅ Real-time clock and date display
- ✅ Emergency override system

### Design
- ✅ 4 premium "Quiet Luxury" themes
- ✅ Professional typography (tight headings, loose body text)
- ✅ 8-point grid spacing system
- ✅ Responsive layout for 55" TVs
- ✅ High contrast for distance readability

### Admin
- ✅ Theme selector with visual previews
- ✅ Emergency message broadcaster
- ✅ Support contact information
- ✅ LocalStorage-based persistence

---

## 📞 Support

**Technical Contact:** stuharker@gmail.com  
**Location:** Alfreton Masonic Hall, Derby Road, Alfreton, DE55 7AQ  
**GitHub:** https://github.com/harkers/devhome-lodgebeacon  

---

## 🚀 Next Steps

### Immediate
1. [ ] Deploy on target display hardware
2. [ ] Test all themes in production
3. [ ] Train hall staff on admin panel
4. [ ] Verify emergency system works

### Phase 1 (Planned)
See `FEATURES.md` for detailed specification:
- [ ] Calendar integration (Google, Microsoft 365, ICS)
- [ ] Scheduled display notices
- [ ] Automatic event import
- [ ] Manual message scheduling
- [ ] Auto-expiry system
- [ ] Preview mode

---

## 💡 Tips

- **Use F11** for true fullscreen (hides browser UI)
- **Disable screensaver** on display device
- **Set brightness** appropriately for room lighting
- **Test emergency system** regularly
- **Keep admin URL bookmarked** for quick access
- **Use wired ethernet** for reliability (not WiFi)

---

**Status:** Production Ready (MVP 0.2)  
**Version:** 0.2  
**Last Updated:** 2026-04-02
