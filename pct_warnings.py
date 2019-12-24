# -*- coding: ascii -*-
#
#  pct_warnings.py : PyCrypro warnings file
#
# Written in 2008 by Dwayne C. Litzenberger <dlitz@dlitz.net>
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

#
# Base classes.  All our warnings inherit from one of these in order to allow
# the user to specifically filter them.
#

class CryproWarning(Warning):
    """Base class for PyCrypro warnings"""

class CryproDeprecationWarning(DeprecationWarning, CryproWarning):
    """Base PyCrypro DeprecationWarning class"""

class CryproRuntimeWarning(RuntimeWarning, CryproWarning):
    """Base PyCrypro RuntimeWarning class"""

#
# Warnings that we might actually use
#

class RandomPool_DeprecationWarning(CryproDeprecationWarning):
    """Issued when Crypro.Util.randpool.RandomPool is instantiated."""

class ClockRewindWarning(CryproRuntimeWarning):
    """Warning for when the system clock moves backwards."""

class GetRandomNumber_DeprecationWarning(CryproDeprecationWarning):
    """Issued when Crypro.Util.number.getRandomNumber is invoked."""

class PowmInsecureWarning(CryproRuntimeWarning):
    """Warning for when _fastmath is built without mpz_powm_sec"""

# By default, we want this warning to be shown every time we compensate for
# clock rewinding.
import warnings as _warnings
_warnings.filterwarnings('always', category=ClockRewindWarning, append=1)

# vim:set ts=4 sw=4 sts=4 expandtab:
