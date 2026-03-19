# Lab: Username enumeration via different responses

## Overview
This lab is vulnerable due to a logic flaw in its password brute-force protection.

## Objective
Brute-force the victim's password, then log in and access their account page. 

## Tools Used
Burp Suite, Browser(Firefox).

## Vulnerability Explanation
The application implements weak brute-force protection system i.e. IP block which can be bypassed easily.

When invalid credentials are entered 3-times in a row, then IP is blocked by the application; But counter is reset when valid credentials are submitted.

## Steps to Reproduce

1. Open the login page.
2. Enter a random username and password.
3. Observe the error message.
4. Use Burp Suite to intercept the request.
5. Send the request to Intruder.
6. Create an username wordlist by alternating valid username whose password is known and target.
7. Modify given password wordlist to match the valid username's password and place in parallely to that username to execute pitch-fork attack. This will help to avoid IP block as counter is reset when valid username and password is entered. 
8. In resouce pool tab create a custom resource pool and where set maximum concurrent requests to 1 to ensure that login attempts are sent to the server in correct order.
9. Start the attack and login successfully by useing credentials obtained in result.

## Payload Used

Username wordlist:
- carlos
- wiener
- carlos
- wiener
- carlos
- carlos
- wiener
- carlos
- carlos
- wiener
- carlos
- carlos
- wiener
- carlos
- carlos
- wiener
- carlos
- carlos
- wiener
- carlos
- carlos
- wiener
- carlos
- carlos
- wiener
- carlos
- carlos
- wiener
- carlos
- carlos
- wiener
- carlos
- carlos
- wiener
- carlos
- carlos
- wiener
- carlos
- carlos
- wiener
- carlos
- carlos
- wiener
- carlos
- carlos
- wiener
- carlos
- carlos
- wiener
- carlos
- carlos
- wiener
- carlos
- carlos
- wiener
- carlos
- carlos
- wiener
- carlos
- carlos
- wiener
- carlos
- carlos
- wiener
- carlos
- carlos
- wiener
- carlos
- carlos
- wiener
- carlos
- carlos
- wiener
- carlos
- carlos
- wiener
- carlos
- carlos
- wiener
- carlos
- carlos
- wiener
- carlos
- carlos
- wiener
- carlos
- carlos
- wiener
- carlos
- carlos
- wiener
- carlos
- carlos
- wiener
- carlos
- carlos
- wiener

Password wordlist:
- 123456
- peter
- password
- peter
- 12345678
- qwerty
- peter
- 123456789
- 12345
- peter
- 1234
- 111111
- peter
- 1234567
- dragon
- peter
- 123123
- baseball
- peter
- abc123
- football
- peter
- monkey
- letmein
- peter
- shadow
- master
- peter
- 666666
- qwertyuiop
- peter
- 123321
- mustang
- peter
- 1234567890
- michael
- peter
- 654321
- superman
- peter
- 1qaz2wsx
- 7777777
- peter
- 121212
- 000000
- peter
- qazwsx
- 123qwe
- peter
- killer
- trustno1
- peter
- jordan
- jennifer
- peter
- zxcvbnm
- asdfgh
- peter
- hunter
- buster
- peter
- soccer
- harley
- peter
- batman
- andrew
- peter
- tigger
- sunshine
- peter
- iloveyou
- 2000
- peter
- charlie
- robert
- peter
- thomas
- hockey
- peter
- ranger
- daniel
- peter
- starwars
- klaster
- peter
- 112233
- george
- peter
- computer
- michelle
- peter
- jessica
- pepper
- peter
- 1111
- zxcvbn
- peter
- 555555
- 11111111
- peter
- 131313
- freedom
- peter
- 777777
- pass
- peter
- maggie
- 159753
- peter
- aaaaaa
- ginger
- peter
- princess
- joshua
- peter
- cheese
- amanda
- peter
- summer
- love
- peter
- ashley
- nicole
- peter
- chelsea
- biteme
- peter
- matthew
- access
- peter
- yankees
- 987654321
- peter
- dallas
- austin
- peter
- thunder
- taylor
- peter
- matrix
- mobilemail
- peter
- mom
- monitor
- peter
- monitoring
- montana
- peter
- moon
- moscow
- peter

## Proof of Concept

Using Burp Suite Intruder, a valid username was alternatingly used with target username to avoid IP block.

After performing a brute-force attack on the password where also parallely matching password is used, the correct credentials were found and access to the user account was successfully obtained.

## Impact
- Attackers can easily bypass IP block if this kind of vulnerability is present
- Enables targeted brute-force attacks
- Can lead to account takeover

## Mitigation
- Avoid resetting even if the counter when valid credentials are submitted
- Implement rate limiting and account lockout

## Key Learnings
- Learned how IP block can be bypassed if small mistakes are made by developers
- Understood how to use Burp Suite Intruder's resouce pool feature
