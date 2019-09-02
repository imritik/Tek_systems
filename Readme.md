<b>Problem Statement:</b>

Smart Front Desk Registration system is used to ease and quicker the process of  registration of the visitor coming to an organisation using Aadhaar card inorder to prevent the fake details given by visitor. 

In this web application we are going to auto fill the registration form using an android application, it will fetch the data from the aadhaar card directly by scanning the QR Code given. 

<i>There are five major modules in this project:</i>

•	Android Application used to fetch the data of Aadhaar card by scanning the QR Code given

•	Module to do the registration of visitor by autofilling the details fetched from android application to web form.

•	Already registered users should be recognized by Phone Number.

•	Module to update information (if changed) of already registered user.

•	Module to generate the various kinds of reports of interest for admin for last 3 months of data. 

•	Module for user management by admin.


<h2>Getting Started</h2>

<b>Requirements:</b>

<ul>
<li>MongoDB 4.0</li>
<li>Android Studio</li>
<li>Django</li>
<li>pip</li>
<li>Android version 4.4+</li>
</ul>

<b>Testing:</b>

1. pip install -r requirements.txt

2.Install Apk

3.Connect Both devices to the common server.

4.Make a collection named 'fda' in mongodb.

5.Run python manage.py runserver IP

6.Copy and Paste the url into your browser and visit /home.

<b>Notes:</b>
<ul>
<li>Scan your Aadhar QR code with the app and click submit.</li>
<li>If logged in, you will be redirected to a form with pre-filled details.</li>
<li>Enter the asked details(if any) & get temporary entry card.</li>
</ul>
