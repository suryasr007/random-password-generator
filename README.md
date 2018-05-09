# Random password Generator
##### A simple and custom random password generator.
 * Generate a simple password of default length 6-16.
 * Generate a password with custom properties.
 * Generate a password from given characters.
 * Generate Non Duplicate Password

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
  from random-password-generator import PasswordGenerator

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


## Generate a custom password
``` python
  pwo = PasswordGenerator()

  # All properties are optional
  pwo.minlen = 30
  pwo.maxlen = 30
  pwo.minuchars = 2
  pwo.minlchars = 3
  pwo.minnumbers = 1
  pwo.minschars = 1

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
  pwo.shuffle_password(20)
```

## License
 * MIT
