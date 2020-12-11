# Random password Generator
[![PyPI version](https://img.shields.io/badge/PYPI-V%202.1.0-blue.svg)](https://pypi.org/project/random-password-generator)
[![Build Status](https://travis-ci.org/suryasr007/random-password-generator.svg?branch=master)](https://travis-ci.org/suryasr007/random-password-generator)
[![Updates](https://pyup.io/repos/github/suryasr007/random-password-generator/shield.svg)](https://pyup.io/repos/github/suryasr007/random-password-generator/)

##### A simple and custom random password generator.
 * Generate a simple password of default length 6-16.
 * Generate a password with custom properties.
 * Generate a password from given characters.
 * Generate Non Duplicate Password.
 * Available at https://random-pg.herokuapp.com/

## API (GET Request)
 * Base_url: https://random-pg.herokuapp.com
 * Generate simple password ```/api/generate```
   * Optional Attributes can be provided as params  
     eg: 
     ```
      /api/generate?minlen=16  
      /api/generate?minlen=16&minlchars=5
     ```
 * Generate a custom password from givin characters
   * Mandatory attributes can be provided as params  
     eg: 
     ```
      /api/shuffle?password=sdjbfbfB&maxlen=14
     ```
 * Generate a non duplicate password.  
   * Mandatory Attribute 'maxlen'  
     eg:
     ``` 
      /nonduplicate?maxlen=14
     ```


## Usage
 * Install the package.
 * Import the package.
 * Create an instance
 * Modify the default properties. (Optional)
 * Generate the password (Default length of password 6-16 unless specified via properties).

``` bash
  pip install random-password-generator
```

``` python
  from password_generator import PasswordGenerator

  pwo = PasswordGenerator()
  pwo.generate()
```


## Configuration

| property   |                          Description                 | Default |
| ---------- |------------------------------------------------------| ------- |
| minlen     |   Minimum length of the password                     | 6 |
| maxlen     |   Maximum length of the password                     | 16 |
| minuchars  |   Minimum upper case characters required in password | 1 |
| minlchars  |   Minimum lower case characters required in password | 1 |
| minnumbers |   Minimum numbers required in password               | 1 |
| minschars  |   Minimum special characters in the password         | 1 |

## Update V2.1.0
Application uses [secrets](https://docs.python.org/3/library/secrets.html) module instaed of `random` module **whenever** possible.


## Update V2.0.1
Application is available at following link: https://random-pg.herokuapp.com/


## Update V1.1.0
From version 1.1.0, Characters can be excluded from the required password by setting the properties on PasswordGenerator object

example:
``` python
  pwo = PasswordGenerator()

  pwo.excludeuchars = "ABCDEFTUVWXY" # (Optional)
  pwo.excludelchars = "abcdefghijkl" # (Optional)
  pwo.excludenumbers = "012345" # (Optional)
  pwo.excludeschars = "!$%^" # (Optional)
```


## Generate a custom password
``` python
  pwo = PasswordGenerator()

  # All properties are optional
  pwo.minlen = 30 # (Optional)
  pwo.maxlen = 30 # (Optional)
  pwo.minuchars = 2 # (Optional)
  pwo.minlchars = 3 # (Optional)
  pwo.minnumbers = 1 # (Optional)
  pwo.minschars = 1 # (Optional)

  pwo.generate()
```

## Generate a password from given characters
``` python
  pwo = PasswordGenerator()

  # It takes two arguments
  # required characters and length of required password
  pwo.shuffle_password('sdafasdf#@&^#&234u8', 20)
```

## Generate Non Duplicate Password
``` python
  pwo = PasswordGenerator()

  # length of required password
  pwo.non_duplicate_password(20)
```

## Contributions
Contributions are welcomed via PR.

## License
 * [MIT](LICENSE)
