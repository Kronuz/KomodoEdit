# Build PCRE
cd contrib/pcre
mkdir .libs
./configure --disable-shared --disable-dependency-tracking --enable-utf8 --enable-unicode-properties
cd ../../

# Build SilverCity
cd src
ln -fs ../contrib/scintilla .
cd ..

# Binaries for ST2:
export PYTHON=python

cd src/silvercity
ln -fs ../../contrib/pcre/.libs/libpcre.a .
CFLAGS='-I ../../contrib/pcre' $PYTHON setup.py build
cd ../../

cd contrib/sgmlop
$PYTHON setup.py build
cd ../../

cd contrib/cElementTree
$PYTHON setup.py build
cd ../../

cd contrib/ciElementTree
$PYTHON setup.py build
cd ../../

mkdir -p SublimeCodeIntel/arch/_local_arch_py2
find src -type f -name '*.so' -exec mv {} SublimeCodeIntel/arch/_local_arch_py2 \;
find contrib -type f -name '*.so' -exec mv {} SublimeCodeIntel/arch/_local_arch_py2 \;


# Binaries for ST3:
export PYTHON=python3

cd src/silvercity
ln -fs ../../contrib/pcre/.libs/libpcre.a .
CFLAGS='-I ../../contrib/pcre' $PYTHON setup.py build
cd ../../

cd contrib/sgmlop
$PYTHON setup.py build
cd ../../

cd contrib/iElementTree
$PYTHON setup.py build
cd ../../

find . -type f -name '*.so'

mkdir -p SublimeCodeIntel/arch/_local_arch_py3
find src -type f -name '*.so' -exec mv {} SublimeCodeIntel/arch/_local_arch_py3 \;
find contrib -type f -name '*.so' -exec mv {} SublimeCodeIntel/arch/_local_arch_py3 \;
