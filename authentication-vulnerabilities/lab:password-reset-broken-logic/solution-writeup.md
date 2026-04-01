# Lab: Password Reset Broken Logic

## Overview
This lab's password reset functionality is vulnerable. The reset token is not properly validated, allowing an attacker to reset another user's password without a valid token.

## Objective
Reset Carlos's password, log in as Carlos, and access his account.

## Tools Used
- Burp Suite (Proxy, HTTP History, Repeater)
- Browser

## Vulnerability Explanation
The application uses a password reset token (`temp-forgot-password-token`) sent via email. However, when submitting the new password, the backend does not validate this token.

This allows an attacker to:
- Remove the token
- Modify the username
- Reset any user's password

This is a **broken authentication logic vulnerability**.

## Steps to Reproduce

1. Configure Burp Suite and log in using:
   - Username: `wiener`
   - Password: `peter`

2. Click on **"Forgot your password?"** and enter:
   ```
   wiener
   ```

3. Click **"Email client"** and open the reset link.

4. Reset your password to any value.

5. In Burp, go to:
   ```
   Proxy → HTTP History
   ```

6. Find the request:
   ```
   POST /forgot-password?temp-forgot-password-token=...
   ```

7. Observe:
   - Token is passed in URL
   - Username is passed as hidden parameter

8. Send this request to **Burp Repeater**.

9. In Repeater:
   - Remove the token value from:
     - URL
     - Request body

10. Send the request.

**Observation:**  
Password reset still works → Token is not validated.

11. Go back to browser and request another password reset.

12. Send the new POST request to Repeater again.

13. Modify the request:
   - Remove token value completely
   - Change:
     ```
     username=carlos
     ```
   - Set a new password

14. Send the request.

15. Go to login page and log in:
   - Username: `carlos`
   - Password: (your new password)

16. Access **"My account"** to complete the lab.

## Payload Used

### Modified Request
```
POST /forgot-password

username=carlos
new-password-1=yourpassword
new-password-2=yourpassword
```

## Proof of Concept

- Intercepted password reset request
- Removed token validation
- Changed username to victim (Carlos)
- Successfully reset Carlos's password
- Logged in as Carlos and accessed account

## Impact
- Full account takeover without valid token
- Authentication bypass
- Broken password reset mechanism

## Mitigation
- Properly validate reset tokens on submission
- Bind tokens to specific users and sessions
- Expire tokens after single use
- Use secure, unpredictable tokens
- Implement server-side validation checks

## Key Learnings
- Learned how broken logic can bypass authentication
- Understood importance of token validation
- Practiced using Burp Repeater for exploitation
- Identified risks in password reset mechanisms

