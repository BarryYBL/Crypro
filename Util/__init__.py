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

"""Miscellaneous modules

Contains useful modules that don't belong into any of the
other Crypro.* subpackages.

Crypro.Util.number        Number-theoretic functions (primality testing, etc.)
Crypro.Util.randpool      Random number generation
Crypro.Util.RFC1751       Converts between 128-bit keys and human-readable
                          strings of words.
Crypro.Util.asn1          Minimal support for ASN.1 DER encoding

"""

__all__ = ['randpool', 'RFC1751', 'number', 'strxor', 'asn1' ]

__revision__ = "$Id$"

