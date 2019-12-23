# -*- coding: utf-8 -*-
#
# ===================================================================
# The contents of this file are dedicated to the public domain.  To
# the extent that dedication to the public domain is not available,
# everyone is granted a worldwide, perpetual, royalty-free,
# non-exclusive license to exercise all rights associated with the
# contents of this file for any purpose whatsoever.
# No rights are reserved.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ===================================================================

"""Python CryProAESgraphy Toolkit

A collection of CryProAESgraphic modules implementing various algorithms
and protocols.

Subpackages:

CryProAES.Cipher
 Secret-key (AES, DES, ARC4) and public-key encryption (RSA PKCS#1) algorithms
CryProAES.Hash
 Hashing algorithms (MD5, SHA, HMAC)
CryProAES.Protocol
 CryProAESgraphic protocols (Chaffing, all-or-nothing transform, key derivation
 functions). This package does not contain any network protocols.
CryProAES.PublicKey
 Public-key encryption and signature algorithms (RSA, DSA)
CryProAES.Signature
 Public-key signature algorithms (RSA PKCS#1) 
CryProAES.Util
 Various useful modules and functions (long-to-string conversion, random number
 generation, number theoretic functions)
"""

__all__ = ['Cipher', 'Hash', 'Protocol', 'PublicKey', 'Util', 'Signature']

__version__ = '2.0.1'     # See also below and setup.py
__revision__ = "$Id$"

# New software should look at this instead of at __version__ above.
version_info = (2, 0, 1, 'final', 0)    # See also above and setup.py

