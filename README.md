# LodgeBeacon Display for Alfreton Hall

**Simple Digital Signage System**

---

## Quick Start MVP

A simple web-based display system that can run on:
- Raspberry Pi + TV
- Any old computer with browser
- Smart TV with browser
- Tablet mounted on wall

---

## How It Works

1. **Content served** from a simple web server
2. **Display shows** full-screen webpage
3. **Updates automatically** via auto-refresh or WebSocket
4. **Managed via** simple admin interface or config file

---

## File Structure

```
lodgebeacon-alfreton/
├── display/
│   ├── index.html          # Main display page
│   ├── admin.html          # Simple admin interface
│   ├── slides/             # Slide content
│   │   ├── welcome.html
│   │   ├── events.html
│   │   ├── dining.html
│   │   └── emergency.html
│   ├── css/
│   │   └── display.css
│   ├── js/
│   │   └── display.js
│   └── config.json         # Display configuration
├── calendar/
├── continuity/
├── web/
└── docs/
```

---

## Running the Display

### Option 1: Python Simple Server (Easiest)

```bash
cd display
python3 -m http.server 8080
```

Then open `http://localhost:8080` in browser on display device.

### Option 2: Node.js (Better for production)

```bash
npm install -g http-server
cd display
http-server -p 8080
```

### Option 3: Docker

```bash
docker run -d -p 8080:80 -v $(pwd):/usr/share/nginx/html:ro nginx:alpine
```

---

## Display Configuration

Edit `config.json`:

```json
{
  "hallName": "Alfreton Masonic Hall",
  "slideInterval": 10000,
  "slides": [
    { "type": "welcome", "duration": 10000 },
    { "type": "events", "duration": 15000 },
    { "type": "dining", "duration": 10000 }
  ],
  "emergency": {
    "enabled": false,
    "message": ""
  }
}
```

---

## Setting Up Raspberry Pi

1. Install Raspberry Pi OS Lite
2. Enable auto-login
3. Install Chromium:
   ```bash
   sudo apt update
   sudo apt install chromium-browser
   ```
4. Create startup script:
   ```bash
   #!/bin/bash
   chromium-browser --kiosk http://your-server:8080
   ```
5. Add to crontab:
   ```
   @reboot /home/pi/start-display.sh
   ```

---

## Emergency Override

Send emergency message via simple HTTP request:

```bash
curl -X POST http://your-server:8080/api/emergency \
  -H "Content-Type: application/json" \
  -d '{"message": "Hall closed due to weather", "duration": 3600}'
```

---

## Next Steps

1. [ ] Create basic HTML/CSS/JS display
2. [ ] Add slide rotation
3. [ ] Add emergency override
4. [ ] Create simple admin page
5. [ ] Test on Raspberry Pi
6. [ ] Deploy at Alfreton Hall

---

**Status:** MVP Development  
**Target:** Test at Alfreton Hall within 2 weeks
