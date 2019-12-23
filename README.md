# Crypto
Simple symmetric GPG file encryption and decryption

## About
Crypto provides a simple interface to symmetric Gnu Privacy Guard (gpg) encryption and decryption for one or more files on Unix and Linux platforms.  It runs on top of gpg and requires a gpg install on your system.  Encryption is performed with the AES256 cipher algorithm.

Encryption benchmarks vs. default gpg encryption are available [here](http://chrissimpkins.github.io/Crypto/benchmarks.html) with additional details for [text](http://chrissimpkins.github.io/Crypto/text-benchmarks.html), [pdf](http://chrissimpkins.github.io/Crypto/pdf-benchmarks.html), [mp3](http://chrissimpkins.github.io/Crypto/mp3-benchmarks.html), and [png](http://chrissimpkins.github.io/Crypto/png-benchmarks.html) mime types.

Crypto provides a number of options including automated tar archives of multiple files prior to encryption, portable ASCII armored encryption formatting, and SHA256 hash digest generation for your encrypted files.

## Documentation

Detailed documentation is available [here](http://chrissimpkins.github.io/Crypto/index.html).

## Quickstart

#### Encrypt a File
```
$ Crypto sometext.txt
```

#### Encrypt with Portable ASCII Armored Format
```
$ Crypto --armor sometext.txt
```

#### Encrypt Multiple Files with Same Passphrase
```
$ Crypto sometext.txt anotherimage.jpg
```

#### Encrypt Multiple Files with Wildcard Expansion
```
$ Crypto *.txt
```

#### Encrypt and Generate SHA256 Hash Digest of the Encrypted File
```
$ Crypto --hash sometext.txt
```

#### Encrypt All Top Level Files in Multiple Directories with Same Passphrase
```
$ Crypto imagedir privatedir
```

#### Pack Multiple Files in a Tar Archive, Then Encrypt the Archive
```
$ Crypto --tar privatedir
```

#### Decrypt a File
```
$ deCrypto sometext.txt.crypt
```

#### Decrypt All Encrypted Files in Top Level of Directory
```
$ deCrypto privatedir
```

#### Decrypt Text to Standard Output Stream
```
$ deCrypto --stdout sometext.txt.gpg
```


## Install

### 1) Install GPG

#### Mac OSX Users
Mac OSX users can install gpg from [source](https://www.gnupg.org/download/index.html), with [Homebrew](http://brew.sh/), or by installing the [Mac GPG Tools Suite](https://gpgtools.org/gpgsuite.html).

The Homebrew install command is:

```
brew install gpg
```

Please refer to the detailed documentation on the Gnu Privacy Guard and Mac GPG Tools suite sites for more information if you choose the source or GPG Tools approaches.

#### Linux Users
If gpg is not installed on your Linux distro, you can use your package manager to install it or compile and install it from the [source](https://www.gnupg.org/download/index.html).

### 2) Install Crypto
You can install Crypto with [pip](https://pypi.python.org/pypi/pip/):

```
pip install Crypto
```

or download the [Crypto source](https://github.com/chrissimpkins/Crypto/archive/master.zip), unpack it, navigate to the top level directory, and install with the command:

```
python setup.py install
```

## Options

### Crypto Options

#### `--armor | -a`

Encrypt in a portable ASCII armored format

#### `--hash`

Generate SHA256 hash digest of encrypted file(s)

#### `--space`

Favor reduced file size over encryption speed

#### `--speed`

Favor encryption speed over reduced file size

#### `--tar`

Create tar archives from directories of files, then encrypt

### deCrypto Options

#### `--nountar`

Do not automatically unpack tar archives after decryption

#### `--overwrite | -o`

Overwrite an existing file with the new decrypted file

#### `--stdout | -s`

Push the decrypted data to the standard output stream instead of generating a new file

### Other Options

#### `--help | -h`

View the help documentation

#### `--usage`

View the usage documentation

#### `--version | -v`

View the Crypto version number

## Project Contributors

- [Barry](https://github.com/BarryYBL) 

## Author contact information
 QQ:3165856425
 
 Email:YBL2652612315@126.com
