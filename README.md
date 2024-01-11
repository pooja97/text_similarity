# Text Similarity Flask App | Bag Of Words and Cosine Similarity

## Introduction

Created a Flask app to check text similarity using Bag Of Words and Cosine Similarity metric. It does not consider punctuations and the position of the words. Takes two text inputs from the user and performs similarity check by creating Bag Of Words (dictionary of frequency of each word in the text; {word:frequency}) and using Cosine Similarity (a metric used to measure how similar two vectors are.) 

## Technologies Used
Programming Language:
    python3<br>
    HTML and JavaScript (for creating UI and sending the user data as a POST request) <br> 

## To Run: 
Method 1 - Cloning the GitHub repository:  
    Clone the repository 
    cd to the cloned folder and with that folder run command `docker build -t text-similarity .` using terminal 
    Once the docker image is created run command `docker run -p 80:80 text-similarity`

Method 2 - Pulling the image from DockerHub:


docker pull pooyadav209712/text-similarity:latest

