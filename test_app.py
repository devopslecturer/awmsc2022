import datetime
import logging

#import pytest
from app import app


# Function to test login_signup page.html
def test_signup_page():

    """

    Description : Description : The "test_signup_page" function is used to test the register/sign up page from python test_app.py

    return : status_code
    
    rtype : integer

    """
 
    client = app.test_client()
    resp = client.get('/login_signup')
    print(resp.status_code)
    assert resp.status_code == 200


#def test_user_signup():
   # pass

# Function to test payment.html
def test_payment_page():

    """

    Description : Description : The "test_payment_page" function is used to test the payment page from python test_app.py

    return : status_code
    
    rtype : integer

    """
 
    client = app.test_client()
    resp = client.get('/payment.html')
    print(resp.status_code)
    assert resp.status_code == 200

# Function to test home.html
def test_home_page():

    """

    Description : Description : The "test_home_page" function is used to test the Home page from python test_app.py

    return : status_code
    
    rtype : integer

    """
 
    client = app.test_client()
    resp = client.get('/home.html')
    print(resp.status_code)
    assert resp.status_code == 200

# Function to test booking.html
def test_booking_page():

    """

    Description : Description : The "test_booking_page" function is used to test the Bookings/ Ride page from python test_app.py

    return : status_code
    
    rtype : integer

    """
 
    client = app.test_client()
    resp = client.get('/bookings.html')
    print(resp.status_code)
    assert resp.status_code == 200

# Function to test profile.html
def test_profile_page():

    """

    Description : Description : The "test_profile_page" function is used to test the profiles page from python test_app.py

    return : status_code
    
    rtype : integer

    """
 
    client = app.test_client()
    resp = client.get('/profile.html')
    print(resp.status_code)
    assert resp.status_code == 200

# Function to test paymentsuccess.html
#def test_payment_success_page():
    #client = app.test_client()
    #resp = client.get('/paymentsuccess.html')
    #print(resp.status_code)
    #assert resp.status_code == 200




