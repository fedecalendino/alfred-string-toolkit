## ALFRED-STRING-TOOLKIT

[Alfred Workflow](https://www.alfredapp.com/workflows/) to run different sets of string manipulation tools 🔤️


### FUNCTIONS

#### *️⃣ str base

Apply a base to a string.

![parameters](screenshots/base-parameters.png)

![clipboard](screenshots/base-clipboard.png)

Also decode a base when possible!

![decode](screenshots/base-decode.png)


#### 🔠 str case

Change the case of a string.

![parameters](screenshots/case-parameters.png)

![clipboard](screenshots/case-clipboard.png)


#### #️⃣ str hash

Apply a hash to a string.

![parameters](screenshots/hash-parameters.png)

![clipboard](screenshots/hash-clipboard.png)


#### ℹ️ str info

Get information about a string.

![parameters](screenshots/info-parameters.png)

![clipboard](screenshots/info-clipboard.png)


#### 🔀 str lipsum

Generate a random amount of lorem ipsum paragraphs, sentences or words. 

![default](screenshots/lipsum-default.png)

![parameters](screenshots/lipsum-parameters.png)


#### 🔣️ str utils

Execute different string manipulation utilities on a string

![parameters](screenshots/utils-parameters.png)

![clipboard](screenshots/utils-clipboard.png)


##### Decode JWT

![decode jwt](screenshots/utils-decode-jwt.png)

**input**
`eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c`

**result**
```json
{
  "header": {
    "alg": "HS256",
    "typ": "JWT"
  },
  "payload": {
    "sub": "1234567890",
    "name": "John Doe",
    "iat": 1516239022
  },
  "signature": "SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
}
```