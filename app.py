import streamlit as st

option = st.sidebar.selectbox(
    "which one do you pick?",
    ("video", "image", "All"),
)

st.title("Dinosaurus")
st.write("Dinos are one of the smartest animals in the multiverse.(ecept stegosaurus.)They ruled over earth for many years.There's still some dinosaurus living among us.")

if option =="video" or option== "All":
    st.subheader("this is a real BBC video")
    st.video("https://www.youtube.com/watch?v=RBgFsVN3uR8")

if option =="image" or option== "All":
    st.subheader("These's are some of the dinosaurus")
    st.image("sussy dinosaur image 1.jpg")

st.sidebar.subheader("press the  button")
button = st.sidebar.button("pterodactyl")
if button:
 st.sidebar.markdown (""":rainbow[A 'pterodactyl' refers to a genus of extinct flying reptiles called Pterodactylus, though the term is often used informally to mean any pterosaur. These were not dinosaurs, but a distinct group of winged reptiles that lived during the Jurassic Period and had wings made of a membrane stretching from their elongated fourth finger to their bodies. They were mostly carnivorous and had lightweight bones. 
    About Pterodactylus
Pterodactylus antiquus was the first pterosaur to be scientifically identified and named. 
Appearance: It had a compact body, hollow bones, a long, slender beak, large eyes, and a wingspan of about 1 meter (3.3 feet). Some species had crests on their heads. 
Diet: Likely ate invertebrates like insects and mollusks when young, and potentially small fish and other small animals as adults. 
Flight: Its wings were made of a membrane of skin, muscle, and other tissues that stretched from its elongated fourth finger to its body. 
Pterosaurs vs. Pterodactyls
Pterosaur: This is the broad term for the entire order of extinct, flying reptiles. 
Pterodactylus: This is the name of a specific genus within the pterosaur group. 
Common Usage: The name 'pterodactyl' is often used incorrectly as a catch-all term for all pterosaurs, especially common ones like Pteranodon. 
Other meanings
Film: There is a 2005 American thriller film called Pterodactly.]""")