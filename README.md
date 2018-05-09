# Random password Generator
##### A simple and custom random password generator.

## How to Use
 * Install the package.
``` bash
  pip install random-password-generator
```
 * Import the package.
``` python
  from random-password-generator import PasswordGenerator
```
 * Create an instance
``` python
  pwo = PasswordGenerator()
```
 * Simple generation
``` python
  pwo.generate()
```

## Configuration
We can set properties such as
| property   |                          Description                 | Default |
| ---------- |------------------------------------------------------| ------- |
| minlen     |   Minimum length of the password                     | 6 |
| maxlen     |   Maximum length of the password                     | 16 |
| minuchars  |   Minimum upper case characters required in password | 1 |
| minlchars  |   Minimum lower case characters required in password | 1 |
| minnumbers |   Minimum numbers required in password               | 1 |
| minschars  |   Minimum special characters in the password         | 1 |
