# LodgeBeacon Display - Quick Start

**Alfreton Masonic Hall Digital Signage**

---

## 🚀 Running the Display (3 Steps)

### Step 1: Start the Server

```bash
cd /home/stu/.openclaw/workspace/lodgebeacon-alfreton/display
python3 -m http.server 8080
```

### Step 2: Open the Display

In a browser, go to:
```
http://localhost:8080
```

Or open directly:
```bash
# Linux
firefox http://localhost:8080 &

# Mac
open http://localhost:8080
```

### Step 3: Full Screen

- Press **F11** for full-screen mode
- Or use browser's fullscreen option

---

## 🎛️ Admin Interface

Open in another tab/window:
```
http://localhost:8080/admin.html
```

**Features:**
- Send emergency messages
- Clear emergencies
- Open display window

---

## 📋 What's Included

| Feature | Status | Description |
|---------|--------|-------------|
| Slide rotation | ✅ Working | Auto-rotates every 10 seconds |
| Clock display | ✅ Working | Shows current time and date |
| Emergency override | ✅ Working | Instant message broadcast |
| Admin panel | ✅ Working | Simple web interface |
| 5 sample slides | ✅ Working | Welcome, meetings, dining, visitors, contact |

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
   # Flash to SD card
   ```

2. **Configure auto-login**
   ```bash
   sudo raspi-config
   # System Options > Boot / Auto Login > Console Autologin
   ```

3. **Install Chromium**
   ```bash
   sudo apt update
   sudo apt install chromium-browser
   ```

4. **Create startup script**
   ```bash
   cat > /home/pi/start-display.sh << 'EOF'
   #!/bin/bash
   sleep 10
   export DISPLAY=:0
   chromium-browser --kiosk --disable-infobars --disable-session-crashed-bubble http://your-server:8080
   EOF
   chmod +x /home/pi/start-display.sh
   ```

5. **Add to startup**
   ```bash
   echo '@reboot /home/pi/start-display.sh' | crontab
   ```

6. **Reboot**
   ```bash
   sudo reboot
   ```

---

## 🚨 Using Emergency Messages

### From Admin Page
1. Open `http://localhost:8080/admin.html`
2. Type message in Emergency Message box
3. Click "Send Emergency Message"
4. All displays show red emergency screen immediately

### From Browser Console
```javascript
// Trigger emergency
triggerEmergency("Hall closed due to weather");

// Clear emergency
clearEmergencyManual();
```

---

## ✏️ Customizing Slides

Edit `js/display.js`:

```javascript
const slides = [
    {
        id: 'welcome',
        html: `
            <div class="slide">
                <h1>Your Custom Title</h1>
                <p>Your custom content</p>
            </div>
        `
    },
    // Add more slides...
];
```

---

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| Display not loading | Check server is running on port 8080 |
| Slides not rotating | Refresh browser |
| Emergency not showing | Check admin page console for errors |
| Clock not updating | Refresh browser |
| Fullscreen not working | Press F11 manually |

---

## 📁 Files

```
display/
├── index.html       # Main display
├── admin.html       # Admin interface
├── css/
│   └── display.css  # Styles
├── js/
│   └── display.js   # Display logic
└── README.md        # This file
```

---

## 🎯 Next Steps

1. [ ] Customize slides for Alfreton Hall
2. [ ] Add actual event data (manual or from calendar)
3. [ ] Test on target display hardware
4. [ ] Set up auto-start on Raspberry Pi
5. [ ] Train hall staff on admin interface

---

## 📞 Support

For technical issues, contact:
- Hall Secretary: secretary@alfretonmasonichall.org.uk

---

**Status:** MVP Ready for Testing  
**Version:** 0.1
