#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------
# Application Name
# ------------------------------------------------------------------------------
app_name = 'Crypto'

# ------------------------------------------------------------------------------
# Version Number
# ------------------------------------------------------------------------------
major_version = "2"
minor_version = "0"
patch_version = "0"

# ------------------------------------------------------------------------------
# Debug Flag (switch to False for production release code)
# ------------------------------------------------------------------------------
debug = False

# ------------------------------------------------------------------------------
# Usage String
# ------------------------------------------------------------------------------
usage = """
Encrypt by explicit file path:
------------------------------
  Crypto <options> [file path] <file path 2...>


Encrypt all top level files in directory:
-----------------------------------------
  Crypto <options> [directory path] <directory path 2...>
  
  
Create a tar archive from directory and encrypt the archive:
-----------------------------------------------------------
  Crypto --tar [directory path] <directory path 2...>


Decrypt by explicit file path:
------------------------------
  deCrypto <options> [file path] <file path 2...>


Decrypt all top level encrypted files in directory:
---------------------------------------------------
  deCrypto <options> [directory path] <directory path 2...>


Enter `Crypto --help` or `deCrypto --help` to view the available options.

"""

# ------------------------------------------------------------------------------
# Help String
# ------------------------------------------------------------------------------
help = """
-------------------------------------------------
Crypto
Simple symmetric GPG file encryption
Copyright 2015 Christopher Simpkins
MIT license
Source: https://github.com/chrissimpkins/Crypto
Docs: https://chrissimpkins.github.io/Crypto/
-------------------------------------------------

ABOUT
Crypto provides a simple interface to symmetric Gnu Privacy Guard (gpg) encryption and decryption for one or more files.  gpg must be installed on your system in order to use the Crypto and deCrypto executables.

USAGE
  ENCRYPTION
    Crypto <options> [file path] <file path...>
    Crypto <options> [directory path] <directory path...>

  DECRYPTION
    deCrypto <options> [file path] <file path...>
    deCrypto <options> [directory path] <directory path...>

CRYPTO OPTIONS
   --armor | -a          Use a portable ASCII armored encryption format
   --hash                Generate SHA256 hash digest of encrypted file(s)
   --space               Favor reduced file size over encryption speed
   --speed               Favor encryption speed over reduced file size
   --tar                 Create tar archive of directory of files before encryption

DECRYPTO OPTIONS
   --nountar             Do not automatically unpack decrypted tar archives
   --overwrite | -o      Overwrite an existing file with the decrypted file
   --stdout    | -s      Print file contents to the standard output stream

OTHER OPTIONS
   --help | -h           Display Crypto and deCrypto help
   --usage               Display Crypto and deCrypto usage
   --version | -v        Display version number

DESCRIPTION
Use one or more explicit file path arguments to encrypt or decrypt the file(s).  Crypto and deCrypto will attempt to encrypt or decrypt (respectively) any explicit filepaths that you include irrespective of the file type.  Encrypted files are generated on the path '<original_filepath>.crypt'.  The original file is not modified or removed by Crypto.

Use one or more directory arguments with the Crypto executable to encrypt all files in the top level of each directory with the same passphrase. Previously encrypted files with a '.crypt' file type will not be generated again in a directory.  Remove them before you run the command if you intend to repeat encryption with a file.

Use one or more directory arguments with deCrypto to decrypt all .crypt, .gpg, .asc, and .pgp files in the top level of each directory.  deCrypto automatically unpacks decrypted tar archives.

Encryption is performed with the AES256 cipher algorithm.  Decryption will take place with any cipher algorithm that your version of gpg supports.
"""
