// LodgeBeacon Display Configuration
// Edit this file to customize for your lodge/hall

const LODGEBEACON_CONFIG = {
    // Hall/Lodge Information
    hallName: "Your Masonic Hall",
    hallAddress: "Your Address Here",
    hallWebsite: "https://your-hall-website.org",
    
    // Display Settings
    slideInterval: 10000, // milliseconds per slide (10 seconds)
    showClock: true,
    
    // Craft Lodges (add/edit/remove as needed)
    craftLodges: [
        {
            name: "Example Lodge",
            number: "1234",
            warrant: "1st January 1900",
            meetingDay: "First Monday",
            meetingTime: "7:00pm",
            nextMeeting: {
                date: "TBD",
                business: "Regular Meeting",
                time: "7:00pm"
            }
        }
        // Add more lodges here...
    ],
    
    // Other Orders (Royal Arch, Mark, etc.)
    otherOrders: [
        { name: "Holy Royal Arch Chapter", number: "1234" },
        { name: "Mark Master Masons", number: "5678" }
    ],
    
    // Facilities (edit to match your hall)
    facilities: [
        "Temple with seating",
        "Dining room with festive board",
        "Bar facilities",
        "Car parking"
    ]
};
