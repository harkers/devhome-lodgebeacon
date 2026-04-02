// LodgeBeacon Display for Alfreton Hall
// Customized with real content from alfretonmasonichall.org.uk
// Individual lodge pages with meeting schedules

// Configuration
const config = {
    hallName: "Alfreton Masonic Hall",
    slideInterval: 10000, // 10 seconds per slide
    emergencyCheckInterval: 5000,
    showClock: true
};

// Hall data from alfretonmasonichall.org.uk
const hallData = {
    name: "Alfreton Masonic Hall",
    address: "The Masonic Hall, Derby Road, Alfreton, Derbyshire, DE55 7AQ",
    website: "https://alfretonmasonichall.org.uk",
    history: "Originally built as the Abraham Lincoln Library in 1938 by American Philanthropist Robert Watchorn. Dedicated as a Masonic Temple on 2nd November 1970."
};

// Craft Lodges with fake meeting schedules
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
    {
        name: "St Thomas Lodge",
        number: "2583",
        warrant: "5th September 1895",
        meetingDay: "Second Tuesday",
        meetingTime: "7:00pm",
        nextMeeting: {
            date: "8th April 2025",
            business: "Installation",
            time: "7:00pm"
        }
    },
    {
        name: "Vulcan Lodge",
        number: "4382",
        warrant: "6th December 1921",
        meetingDay: "Third Wednesday",
        meetingTime: "6:30pm",
        nextMeeting: {
            date: "16th April 2025",
            business: "2nd Degree",
            time: "6:30pm"
        }
    },
    {
        name: "Morcar Lodge",
        number: "8548",
        warrant: "14th June 1972",
        meetingDay: "Fourth Thursday",
        meetingTime: "7:00pm",
        nextMeeting: {
            date: "24th April 2025",
            business: "Lecture Evening",
            time: "7:00pm"
        }
    },
    {
        name: "Pioneer Lodge",
        number: "9065",
        warrant: "10th November",
        meetingDay: "First Friday",
        meetingTime: "7:00pm",
        nextMeeting: {
            date: "4th April 2025",
            business: "3rd Degree",
            time: "7:00pm"
        }
    }
];

// Generate lodge slides
function generateLodgeSlide(lodge) {
    return {
        id: `lodge-${lodge.number}`,
        html: `
            <div class="slide">
                <h1 style="font-size: 2.5rem; margin-bottom: 0.5rem;">${lodge.name}</h1>
                <h2 style="font-size: 3.5rem; color: #c9a227; margin-bottom: 1.5rem;">No. ${lodge.number}</h2>
                
                <div style="background: rgba(26, 54, 93, 0.3); border-radius: 15px; padding: 1.5rem; margin: 1rem 0;">
                    <p style="font-size: 1.3rem; margin-bottom: 1rem;">
                        <strong style="color: #c9a227;">Next Meeting:</strong> ${lodge.nextMeeting.date}
                    </p>
                    <p style="font-size: 1.5rem; margin-bottom: 0.5rem;">
                        <strong>${lodge.nextMeeting.business}</strong>
                    </p>
                    <p style="font-size: 1.8rem; color: #c9a227;">${lodge.nextMeeting.time}</p>
                </div>
                
                <p style="font-size: 1.1rem; color: #94a3b8; margin-top: 1.5rem;">
                    Regular meetings: ${lodge.meetingDay} at ${lodge.meetingTime}<br/>
                    Warrant dated ${lodge.warrant}
                </p>
            </div>
        `
    };
}

// All slides
const slides = [
    // Welcome
    {
        id: 'welcome',
        html: `
            <div class="slide">
                <h1>Welcome to</h1>
                <h2 style="font-size: 4.5rem; color: #c9a227; margin-bottom: 2rem;">Alfreton Masonic Hall</h2>
                <p style="font-size: 1.8rem; max-width: 80%; margin: 0 auto;">Home to Four Craft Lodges and the headquarters of Derbyshire Freemasonry</p>
                <p style="margin-top: 3rem; color: #c9a227; font-size: 1.4rem;">Est. 1864 (Current Temple dedicated 1970)</p>
            </div>
        `
    },
    // History
    {
        id: 'history',
        html: `
            <div class="slide">
                <h1>Our History</h1>
                <p style="font-size: 1.5rem; max-width: 85%; margin: 2rem auto; line-height: 1.6;">
                    Built as the Abraham Lincoln Library in 1938 by American philanthropist Robert Watchorn, 
                    who was born in Alfreton and made his fortune in the USA before returning to give back to his hometown.
                </p>
                <p style="font-size: 1.4rem; color: #c9a227; margin-top: 2rem;">
                    Temple dedicated 2nd November 1970
                </p>
            </div>
        `
    },
    // Craft Lodges Overview
    {
        id: 'craft-lodges-overview',
        html: `
            <div class="slide">
                <h1>Our Craft Lodges</h1>
                <div style="font-size: 1.4rem; margin-top: 2rem; line-height: 2.2;">
                    <p><strong style="color: #c9a227;">Royal Alfred Lodge</strong> No. 1028</p>
                    <p><strong style="color: #c9a227;">St Thomas Lodge</strong> No. 2583</p>
                    <p><strong style="color: #c9a227;">Vulcan Lodge</strong> No. 4382</p>
                    <p><strong style="color: #c9a227;">Morcar Lodge</strong> No. 8548</p>
                    <p><strong style="color: #c9a227;">Pioneer Lodge</strong> No. 9065</p>
                </div>
                <p style="margin-top: 2rem; color: #94a3b8; font-size: 1.2rem;">See following slides for meeting details</p>
            </div>
        `
    },
    // Individual Lodge Slides
    generateLodgeSlide(craftLodges[0]), // Royal Alfred 1028
    generateLodgeSlide(craftLodges[1]), // St Thomas 2583
    generateLodgeSlide(craftLodges[2]), // Vulcan 4382
    generateLodgeSlide(craftLodges[3]), // Morcar 8548
    generateLodgeSlide(craftLodges[4]), // Pioneer 9065
    // Other Orders
    {
        id: 'other-orders',
        html: `
            <div class="slide">
                <h1>Other Orders</h1>
                <div style="font-size: 1.4rem; margin-top: 1.5rem; line-height: 2;">
                    <p><strong>Alfreton Holy Royal Arch Chapter 1028</strong></p>
                    <p><strong>St Martin Lodge of Mark Master Masons 414</strong></p>
                    <p><strong>Rose Croix - Alfreton Chapter 710</strong></p>
                    <p><strong>Royal Ark Mariners - Mt Ararat Lodge 414</strong></p>
                    <p><strong>Red Cross of Constantine</strong></p>
                    <p><strong>Royal & Select Masters</strong></p>
                </div>
                <p style="margin-top: 1.5rem; color: #c9a227; font-size: 1.2rem;">See website for meeting dates</p>
            </div>
        `
    },
    // Facilities
    {
        id: 'facilities',
        html: `
            <div class="slide">
                <h1>Our Facilities</h1>
                <ul style="font-size: 1.6rem; text-align: left; display: inline-block; margin-top: 1rem;">
                    <li style="margin-bottom: 0.8rem;">Temple with seating</li>
                    <li style="margin-bottom: 0.8rem;">Dining room with festive board</li>
                    <li style="margin-bottom: 0.8rem;">Bar facilities</li>
                    <li style="margin-bottom: 0.8rem;">Robing areas</li>
                    <li style="margin-bottom: 0.8rem;">Substantial car park</li>
                </ul>
                <p style="margin-top: 2rem; color: #c9a227; font-size: 1.3rem;">Facilities available for hire</p>
            </div>
        `
    },
    // Visitors
    {
        id: 'visitors',
        html: `
            <div class="slide">
                <h1>Visiting Brethren</h1>
                <p style="font-size: 2rem; margin: 2rem 0;">"There are no strangers in Freemasonry,<br/>only friends you've yet to meet."</p>
                <p style="font-size: 1.6rem; margin: 2rem 0;">You are always welcome at Alfreton</p>
                <p style="margin-top: 2rem; color: #c9a227;">Please contact the Secretary in advance</p>
            </div>
        `
    },
    // Contact
    {
        id: 'contact',
        html: `
            <div class="slide">
                <h1>Contact Information</h1>
                <p style="font-size: 2rem; margin: 2rem 0;"><strong>Alfreton Masonic Hall</strong></p>
                <p style="font-size: 1.5rem; line-height: 1.8;">
                    The Masonic Hall<br/>
                    Derby Road<br/>
                    Alfreton<br/>
                    Derbyshire, DE55 7AQ
                </p>
                <p style="margin-top: 2rem; font-size: 1.4rem; color: #c9a227;">alfretonmasonichall.org.uk</p>
            </div>
        `
    }
];

// State
let currentSlide = 0;
let slideTimer = null;
let isEmergency = false;

// Initialize
function init() {
    console.log('🏛️ LodgeBeacon Display initialized');
    console.log('Hall:', config.hallName);
    console.log('Craft lodges:', craftLodges.length);
    
    // Start clock
    if (config.showClock) {
        updateClock();
        setInterval(updateClock, 1000);
    }
    
    // Show first slide
    showSlide(0);
    
    // Start rotation
    startRotation();
    
    // Check for emergency
    setInterval(checkEmergency, config.emergencyCheckInterval);
    
    console.log('✅ Display running with lodge meeting schedules');
}

// Show specific slide
function showSlide(index) {
    const container = document.getElementById('slide-content');
    
    // Fade out
    container.style.opacity = '0';
    
    setTimeout(() => {
        // Update content
        container.innerHTML = slides[index].html;
        
        // Fade in
        container.style.opacity = '1';
        
        console.log('📺 Showing slide:', slides[index].id);
    }, 500);
}

// Start slide rotation
function startRotation() {
    if (slideTimer) clearInterval(slideTimer);
    
    slideTimer = setInterval(() => {
        if (!isEmergency) {
            currentSlide = (currentSlide + 1) % slides.length;
            showSlide(currentSlide);
        }
    }, config.slideInterval);
}

// Update clock
function updateClock() {
    const now = new Date();
    
    // Time
    const timeString = now.toLocaleTimeString('en-GB', {
        hour: '2-digit',
        minute: '2-digit'
    });
    const clockEl = document.getElementById('clock');
    if (clockEl) clockEl.textContent = timeString;
    
    // Date
    const dateString = now.toLocaleDateString('en-GB', {
        weekday: 'long',
        day: 'numeric',
        month: 'long',
        year: 'numeric'
    });
    const dateEl = document.getElementById('date');
    if (dateEl) dateEl.textContent = dateString;
}

// Check for emergency
function checkEmergency() {
    const emergencyData = localStorage.getItem('lodgebeacon_emergency');
    
    if (emergencyData) {
        const data = JSON.parse(emergencyData);
        if (data.active && !isEmergency) {
            showEmergency(data.message);
        } else if (!data.active && isEmergency) {
            clearEmergency();
        }
    }
}

// Show emergency
function showEmergency(message) {
    isEmergency = true;
    const msgEl = document.getElementById('emergency-message');
    const overlayEl = document.getElementById('emergency-overlay');
    if (msgEl) msgEl.textContent = message;
    if (overlayEl) overlayEl.classList.remove('hidden');
    console.log('🚨 EMERGENCY:', message);
}

// Clear emergency
function clearEmergency() {
    isEmergency = false;
    const overlayEl = document.getElementById('emergency-overlay');
    if (overlayEl) overlayEl.classList.add('hidden');
    console.log('✅ Emergency cleared');
}

// Manual emergency trigger
window.triggerEmergency = function(message) {
    const data = {
        active: true,
        message: message,
        timestamp: Date.now()
    };
    localStorage.setItem('lodgebeacon_emergency', JSON.stringify(data));
    showEmergency(message);
};

// Clear emergency manually
window.clearEmergencyManual = function() {
    localStorage.removeItem('lodgebeacon_emergency');
    clearEmergency();
};

// Calendar integration (future)
window.fetchCalendarEvents = async function() {
    console.log('📅 Calendar integration pending');
};

// Start
init();
