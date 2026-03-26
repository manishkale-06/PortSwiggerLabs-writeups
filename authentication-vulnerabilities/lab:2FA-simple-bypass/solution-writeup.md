# Lab: 2FA simple bypass

## Overview
This lab's two-factor authentication can be bypassed. You have already obtained a valid username and password, but do not have access to the user's 2FA verification code. 

## Objective
Access Carlos's account page.

## Tools Used
Browser(Firefox).

## Vulnerability Explanation
The application does not verify 2-factor-authentication throughly.

When a valid username and password is entered user is redirected to 2FA page but user is alredy logged in despite of verification process is still due.

## Steps to Reproduce

1. Open the login page.
2. Enter a Carlos's username and password which is provided.
3. Sipmly go to home page when redirected to 2FA page.
4. Login successfully.

## Payload Used

Username: carlos
Password: montoya

## Proof of Concept

Target username and password entered then application redirected to the 2FA page, from there 'back to home page'
button is clicked. This bypassed 2FA because it was not developed properly. 

## Impact
- Attackers can access other users account.
- Brute-Force attack can be performed.
- 2FA does not have negative impact on security.

## Mitigation
- Proper verification of 2FA.
- Must have valid and secure 2FA methods.

## Key Learnings
- Learned how poorly implemented 2FA system can be bypassed easily.
