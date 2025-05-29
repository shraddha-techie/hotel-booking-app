import streamlit as st
from PIL import Image
import base64

# Get background image as base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

image_path = "images/background.jpg"
img_base64 = get_base64_of_bin_file(image_path)

# CSS Styling
page_bg_img = f"""
<style>
.stApp {{
    background-image: url("data:image/png;base64,{img_base64}") !important;
    background-size: cover !important;
    background-position: center !important;
    background-repeat: no-repeat !important;
    background-attachment: fixed !important;
}}
.content-container {{
    background-color: rgba(255, 255, 255, 0.85);
    padding: 25px 40px;
    border-radius: 12px;
    max-width: 1100px;
    margin: 50px auto;
    box-shadow: 0 0 20px rgba(0,0,0,0.25);
    color: #4B0082;
    font-weight: 600;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}}
.navbar {{
    display: flex;
    justify-content: space-around;
    background-color: rgba(255,255,255,0.95);
    padding: 10px 0;
    position: sticky;
    top: 0;
    z-index: 999;
    border-bottom: 2px solid #4B0082;
    margin-bottom:opx;
}}
.navbar a {{
    color: #4B0082;
    text-decoration: none;
    font-size: 18px;
    font-weight: bold;
}}
.navbar a:hover {{
    text-decoration: underline;
}}
</style>
"""

# Page Config and Top Bar
st.set_page_config(page_title="Hotel RoyalView", layout="centered")
st.markdown(page_bg_img, unsafe_allow_html=True)

# Navbar
st.markdown('''
<div class="navbar">
    <a href="#Decoration">Decoration</a>
    <a href="#Balcony">Balcony View</a>
    <a href="#Rooms">Rooms</a>
    <a href="#NightParty">Night Party</a>
    <a href="#Booking">Booking</a>
    <a href="#Contact">Contact</a>
</div>
''', unsafe_allow_html=True)

# Content Container
st.markdown('<div class="content-container">', unsafe_allow_html=True)

# Welcome
st.markdown('<h1 style="color:#4B0082;">Welcome to Hotel RoyalView 🏨</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#4B0082; font-size:18px;">Experience luxury and comfort at the heart of the city.</p>', unsafe_allow_html=True)

# Image Carousel with Arrows (full width)
from streamlit_carousel import carousel
slides = [
    {"img": "images/counter.jpg", "title": "Reception Area", "text": "Welcome to our reception"},
    {"img": "images/hotel.jpg", "title": "Front View", "text": "Beautiful front view of Hotel RoyalView"},
    {"img": "images/pool.jpg", "title": "Swimming Pool", "text": "Relax in our luxurious pool"},
    {"img": "images/view.jpg", "title": "Scenic View", "text": "Enjoy breathtaking scenic views"}
]
carousel(items=slides, width=1.0)  # width=1.0 means full width

# Decoration Section
st.markdown("---")
st.markdown('<h2 id="Decoration" style="color:#4B0082;">🎉 Decoration Corner</h2>', unsafe_allow_html=True)
st.markdown('<p style="color:#4B0082;">We offer special decoration packages for your celebrations!</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.image("images/birthday.jpg", caption="Birthday Setup", width=500)
    st.markdown('<p style="color:#4B0082;">🎂 Celebrate birthdays in style with custom decorations and cake arrangements.</p>', unsafe_allow_html=True)
with col2:
    st.image("images/anniversary.jpg", caption="Anniversary Setup", width=500)
    st.markdown('<p style="color:#4B0082;">💖 Make anniversaries memorable with romantic room decor and surprises.</p>', unsafe_allow_html=True)

# Balcony Section
st.markdown("---")
st.markdown('<h2 id="Balcony" style="color:#4B0082;">🌅 Balcony View</h2>', unsafe_allow_html=True)
st.image("images/balcony.jpg", caption="Enjoy serene balcony views", width=900)
st.markdown('<p style="color:#4B0082;">Relax and unwind with breathtaking views from our spacious balconies.</p>', unsafe_allow_html=True)

# Rooms Section
st.markdown("---")
st.markdown('<h2 id="Rooms" style="color:#4B0082;">🏨 Rooms</h2>', unsafe_allow_html=True)
st.image("images/rooms.jpg", caption="Comfortable and Spacious Rooms", width=900)
st.markdown('<p style="color:#4B0082;">Choose from a variety of rooms designed to meet your comfort and luxury needs.</p>', unsafe_allow_html=True)

# Night Party Section
st.markdown("---")
st.markdown('<h2 id="NightParty" style="color:#4B0082;">🌙 Night Party</h2>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.image("images/nightparty1.jpg", caption="Night Party Vibes 1", width=430)
with col2:
    st.image("images/nightparty2.jpg", caption="Night Party Vibes 2", width=430)
st.markdown('<p style="color:#4B0082;">Join us for an unforgettable night party with music, lights, and great vibes!</p>', unsafe_allow_html=True)

# Booking Section
st.markdown("---")
st.markdown('<h2 id="Booking" style="color:#4B0082;">📝 Booking Form</h2>', unsafe_allow_html=True)
with st.form("booking_form"):
    name = st.text_input("Full Name")
    phone = st.text_input("Phone Number")
    email = st.text_input("Email Address")
    room_type = st.selectbox("Room Type", ["Standard", "Deluxe", "Suite"])
    check_in = st.date_input("Check-in Date")
    check_out = st.date_input("Check-out Date")
    submitted = st.form_submit_button("Submit Booking")
    if submitted:
        st.success(f"Thank you {name}! Your booking request for a {room_type} room from {check_in} to {check_out} has been received. We will contact you shortly.")

# Contact Section
st.markdown("---")
st.markdown('<h2 id="Contact" style="color:#4B0082;">📞 Contact Us</h2>', unsafe_allow_html=True)
st.write("Get in touch with us for bookings or inquiries.")
st.write("🏨 **Hotel RoyalView**")
st.write("📍 123 City Center Road, Bhopal, MP - 462001")
st.write("📞 +91-9876543210")
st.write("📧 royalview@example.com")

# End of container
st.markdown('</div>', unsafe_allow_html=True)
