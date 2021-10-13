# Chat API

Basic REST API using relational DB for a chat system. 

## Installation
> pip install -r requirements.txt

## End-points

**{url}/**  
Type: GET  
Description: Welcome message  

**{url}/check/**  
Type: POST  
Description: Check the health of the system.  

**{url}/users/**  
Type: POST  
Description: Create a user in the system.  

**{url}/login/**  
Type: POST  
Description: Log in as an existing user.  
Security: basic authorization  

**{url}/messages/**  
Type: POST  
Description: Send a message from one user to another. Support types of messages: text, image and video.  
Security: token  

**{url}/messages/**  
Type: GET  
Description: Fetch all existing messages to a given recipient, within a range of message IDs.  
Security: token  



