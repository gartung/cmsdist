### RPM cms cmssw-tool-conf CMS_148a11
# DO NOT MODIFY. This spec file is automatically generated by executing src/createConfSpecs.sh in the 
# main directory. Modify src/toolConfiguration.xsl if needed.
# We set a special variable TOOLCONF_VERSION which is then used by scram-build.file and scramv1-build.file to
# check out the correct toolbox. Notice that all the *-tool-conf.spec set the same variable so this is 
# relevant only for build time and not for runtime.
## INITENV SET TOOLCONF_VERSION %{v}
Source0: none 

Provides: tmp/slc3_ia32_gcc323/src/FWCore/TFWLiteSelector/test/libFWCoreTFWLiteSelectorTest.so
Provides: libboost_regex-gcc-mt.so 
Provides: libboost_signals-gcc-mt.so 
Provides: libboost_thread-gcc-mt.so

Requires: gcc
Requires: coral
Requires: pool
Requires: seal
Requires: xdaq
Requires: geant4
Requires: hepmc
Requires: heppdt
Requires: clhep
Requires: castor
Requires: dpm
Requires: zlib
Requires: python
Requires: boost
Requires: xerces-c
Requires: root
Requires: uuid
Requires: gsl
Requires: sqlite
Requires: oracle
Requires: mysqlpp
Requires: mysql
Requires: gccxml
Requires: python
Requires: boost
Requires: elementtree
Requires: sigcpp
Requires: mimetic
Requires: bz2lib
Requires: pcre
Requires: dcap
Requires: rulechecker
Requires: cppunit
Requires: qt
Requires: soqt
Requires: coin
Requires: curl
Requires: libjpg
Requires: libpng
Requires: libtiff
Requires: simage
Requires: openssl
Requires: expat
Requires: frontier_client
Requires: genser
Requires: tkonlinesw
Requires: doxygen
Requires: meschach
Requires: glimpse
Requires: oracle-env
Requires: p5-dbd-oracle
Requires: valgrind
Requires: fastjet
Requires: ktjet
Requires: ignominy
Requires: herwig
Requires: lhapdf
Requires: pythia6
Requires: pythia8
Requires: jimmy
Requires: hector
Requires: data-FastSimulation-MaterialEffects
Requires: data-FastSimulation-PileUpProducer
Requires: data-Geometry-CaloTopology
Requires: data-MagneticField-Interpolation
Requires: data-RecoParticleFlow-PFBlockProducer
Requires: data-RecoTracker-RingESSource
Requires: data-RecoTracker-RoadMapESSource
Requires: data-SimG4CMS-Calo
Requires: data-Validation-EcalDigis
Requires: data-Validation-EcalHits
Requires: data-Validation-EcalRecHits
Requires: data-Validation-Geometry
Requires: data-Validation-HcalHits
Requires: data-RecoMuon-MuonIdentification
Requires: data-CondCore-SQLiteData


%prep
%build
(echo "ARCHITECTURE:%{cmsplatf}"
 echo "SCRAM_BASEPATH:%{instroot}/external"

%if "%{?use_system_gcc:set}" == "set"
  echo "TOOL:cxxcompiler:"
       echo "  +GCC_BASE:/none"
       echo "  +CC:$(which gcc)"
       echo "  +CXX:$(which c++)"
       echo "  +PATH:/none"  # useless, toolbox says value=""
       echo "  +LD_LIBRARY_PATH:/none" # useless, toolbox says value=""
       echo "TOOL:g77gcc3:"
       echo "  +FC:$(which g77 | grep -v 'no g77')"
%endif
%if "%{?use_system_gcc:set}-%{?use_ccache:set}" == "-set"
echo "TOOL:cxxcompiler:"
       echo "  +GCC_BASE:$CCACHE_ROOT"
eval        "echo \"  +CC:$CCACHE_ROOT/bin/gcc\""
eval        "echo \"  +CXX:$CCACHE_ROOT/bin/c++\""
       echo "TOOL:g77gcc3:"
       echo "  +FC:$GCC_ROOT/bin/g77"
%endif
%if "%{?use_system_gcc:set}-%{?use_ccache:set}" == "-" 
echo "TOOL:cxxcompiler:"
       echo "  +GCC_BASE:$GCC_ROOT"
       echo "TOOL:g77gcc3:"
       echo "  +FC:$GCC_ROOT/bin/g77"
%endif

echo "TOOL:f77compiler:"
echo "  +G77_BASE:$GCC_ROOT"
echo "  +FC:$GCC_ROOT/bin/g77"

%if "%{?use_system_gcc:set}" == "set"
  echo "TOOL:ccompiler:"
       echo "  +GCC_BASE:/none"
       echo "  +CC:$(which gcc)"
       echo "  +CXX:$(which c++)"
       echo "  +PATH:/none"  # useless, toolbox says value=""
       echo "  +LD_LIBRARY_PATH:/none" # useless, toolbox says value=""
       echo "TOOL:g77gcc3:"
       echo "  +FC:$(which g77 | grep -v 'no g77')"
%endif
%if "%{?use_system_gcc:set}-%{?use_ccache:set}" == "-set"
echo "TOOL:ccompiler:"
       echo "  +GCC_BASE:$CCACHE_ROOT"
eval        "echo \"  +CC:$CCACHE_ROOT/bin/gcc\""
eval        "echo \"  +CXX:$CCACHE_ROOT/bin/c++\""
       echo "TOOL:g77gcc3:"
       echo "  +FC:$GCC_ROOT/bin/g77"
%endif
%if "%{?use_system_gcc:set}-%{?use_ccache:set}" == "-" 
echo "TOOL:ccompiler:"
       echo "  +GCC_BASE:$GCC_ROOT"
       echo "TOOL:g77gcc3:"
       echo "  +FC:$GCC_ROOT/bin/g77"
%endif

echo "TOOL:coral:"
echo "  +CORAL_BASE:$CORAL_ROOT"

echo "TOOL:pool:"
echo "  +POOL_BASE:$POOL_ROOT"

echo "TOOL:seal:"
echo "  +SEAL_BASE:$SEAL_ROOT"

echo "TOOL:ignominy:"
eval "echo \"  +IGNOMINY_BASE:\${IGNOMINY_ROOT}\""

echo "TOOL:xdaq:"
eval "echo \"  +XDAQ_BASE:\${XDAQ_ROOT}\""
eval "echo \"  +PATH:\${XDAQ_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${XDAQ_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${XDAQ_ROOT}/include\""

echo "TOOL:geant4:"
echo "  +GEANT4_BASE:$GEANT4_ROOT"
echo "  +GEANT4_SHARE_BASE:$GEANT4_ROOT/share"
echo "  +LIBDIR:$GEANT4_ROOT/lib/$(uname)-g++"
echo "  +INCLUDE:$GEANT4_ROOT/include"
echo "  +G4SRC:$GEANT4_ROOT/source"
echo "  +NeutronHPCrossSections:$G4NDL_PATH"
echo "  +G4LEVELGAMMADATA:$PHOTON_EVAPORATION_PATH"
echo "  +G4RADIOACTIVEDATA:$RADIATIVE_DECAY_PATH"
echo "  +G4LEDATA:$G4EMLOW_PATH"

echo "TOOL:hepmc:"
eval "echo \"  +HEPMC_BASE:\${HEPMC_ROOT}\""
eval "echo \"  +PATH:\${HEPMC_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${HEPMC_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${HEPMC_ROOT}/include\""

echo "TOOL:heppdt:"
eval "echo \"  +HEPPDT_BASE:\${HEPPDT_ROOT}\""
eval "echo \"  +PATH:\${HEPPDT_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${HEPPDT_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${HEPPDT_ROOT}/include\""

echo "TOOL:clhep:"
eval "echo \"  +CLHEP_BASE:\${CLHEP_ROOT}\""
eval "echo \"  +PATH:\${CLHEP_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${CLHEP_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${CLHEP_ROOT}/include\""

echo "TOOL:castor:"
eval "echo \"  +CASTOR_BASE:\${CASTOR_ROOT}\""
eval "echo \"  +PATH:\${CASTOR_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${CASTOR_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${CASTOR_ROOT}/include\""

echo "TOOL:dpm:"
eval "echo \"  +DPM_BASE:\${DPM_ROOT}\""
eval "echo \"  +LIBDIR:\${DPM_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${DPM_ROOT}/include\""

echo "TOOL:zlib:"
eval "echo \"  +ZLIB_BASE:\${ZLIB_ROOT}\""
eval "echo \"  +PATH:\${ZLIB_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${ZLIB_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${ZLIB_ROOT}/include\""

PYTHON_MAJOR=$(echo $PYTHON_VERSION | sed 's/\.[0-9]*$//')
echo "TOOL:python:"
echo "  +PYTHON_BASE:$PYTHON_ROOT"
echo "  +LIBDIR:$PYTHON_ROOT/lib"
echo "  +INCLUDE:$PYTHON_ROOT/include/python$PYTHON_MAJOR"
echo "  +PATH:$PYTHON_ROOT/bin"

echo "TOOL:boost:"
eval "echo \"  +BOOST_BASE:\${BOOST_ROOT}\""
eval "echo \"  +PATH:\${BOOST_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${BOOST_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${BOOST_ROOT}/include\""

echo "TOOL:xerces-c:"
eval "echo \"  +XERCESC_BASE:\${XERCES_C_ROOT}\""
eval "echo \"  +XERCES_C_BASE:\${XERCES_C_ROOT}\""
eval "echo \"  +PATH:\${XERCES_C_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${XERCES_C_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${XERCES_C_ROOT}/include\""

echo "TOOL:root:"
echo "  +ROOT_BASE:$ROOT_ROOT"
echo "  +ROOTSYS:$ROOT_ROOT"

echo "TOOL:rootrflx:"
echo "  +ROOTRFLX_BASE:$ROOT_ROOT"
echo "  +ROOTSYS:$ROOT_ROOT"
echo "  +GENREFLEX=$ROOT_ROOT/bin/genreflex"

echo "TOOL:rootcore:"
echo "  +ROOTCORE_BASE:$ROOT_ROOT"
echo "  +ROOTSYS:$ROOT_ROOT"

echo "TOOL:uuid:"
eval "echo \"  +UUID_BASE:\${UUID_ROOT}\""
eval "echo \"  +PATH:\${UUID_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${UUID_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${UUID_ROOT}/include\""

echo "TOOL:gsl:"
eval "echo \"  +GSL_BASE:\${GSL_ROOT}\""
eval "echo \"  +PATH:\${GSL_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${GSL_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${GSL_ROOT}/include\""

echo "TOOL:sqlite:"
eval "echo \"  +SQLITE_BASE:\${SQLITE_ROOT}\""
eval "echo \"  +PATH:\${SQLITE_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${SQLITE_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${SQLITE_ROOT}/include\""

echo "TOOL:oracle:"
echo "  +ORACLE_BASE:$ORACLE_ROOT"
echo "  +PATH:$ORACLE_ROOT/bin"
echo "  +LIBDIR:$ORACLE_ROOT/lib"
echo "  +INCLUDE:$ORACLE_ROOT/include"
echo "  +ORACLE_ADMINDIR:$ORACLE_ENV_ROOT/etc"

echo "TOOL:mysqlpp:"
eval "echo \"  +MYSQLPP_BASE:\${MYSQLPP_ROOT}\""
eval "echo \"  +PATH:\${MYSQLPP_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${MYSQLPP_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${MYSQLPP_ROOT}/include\""

echo "TOOL:mysql:"
eval "echo \"  +MYSQL_BASE:\${MYSQL_ROOT}\""
eval "echo \"  +PATH:\${MYSQL_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${MYSQL_ROOT}/lib/mysql\""
eval "echo \"  +INCLUDE:\${MYSQL_ROOT}/include/mysql\""

echo "TOOL:gccxml:"
eval "echo \"  +GCCXML_BASE:\${GCCXML_ROOT}\""
eval "echo \"  +PATH:\${GCCXML_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${GCCXML_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${GCCXML_ROOT}/include\""

echo "TOOL:boost_python:"
echo "  +BOOST_PYTHON_BASE:$BOOST_ROOT"
echo "  +LIBDIR:$BOOST_ROOT/lib"
echo "  +INCLUDE:$BOOST_ROOT/include"
echo "  +ELEMENTTREE_BASE:$ELEMENTTREE_ROOT"
echo "  +ELEMENTTREE_PYPATH=$ELEMENTTREE_ROOT/python$(echo $PYTHON_VERSION | cut -d. -f1,2)/site-packages"
echo "  +PYTHONPATH=$ELEMENTTREE_ROOT/lib/python$(echo $PYTHON_VERSION | cut -d. -f1,2)/site-packages"
echo "  +PYSTE_EXEC=$BOOST_ROOT/lib/python$(echo $PYTHON_VERSION | cut -d. -f1,2)/site-packages/Pyste/pyste.py"

echo "TOOL:sigcpp:"
echo "  +SIGCPP_BASE:$SIGCPP_ROOT"
echo "  +PATH:$SIGCPP_ROOT/bin"
echo "  +LIBDIR:$SIGCPP_ROOT/lib"
echo "  +INCLUDE:$SIGCPP_ROOT/include/sigc++-2.0"

echo "TOOL:mimetic:"
eval "echo \"  +MIMETIC_BASE:\${MIMETIC_ROOT}\""
eval "echo \"  +PATH:\${MIMETIC_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${MIMETIC_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${MIMETIC_ROOT}/include\""

echo "TOOL:bz2lib:"
eval "echo \"  +BZ2LIB_BASE:\${BZ2LIB_ROOT}\""
eval "echo \"  +PATH:\${BZ2LIB_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${BZ2LIB_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${BZ2LIB_ROOT}/include\""

echo "TOOL:pcre:"
eval "echo \"  +PCRE_BASE:\${PCRE_ROOT}\""
eval "echo \"  +PATH:\${PCRE_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${PCRE_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${PCRE_ROOT}/include\""

echo "TOOL:dcap:"
eval "echo \"  +DCAP_BASE:\${DCAP_ROOT}\""
eval "echo \"  +PATH:\${DCAP_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${DCAP_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${DCAP_ROOT}/include\""

echo "TOOL:rulechecker:"
echo "  +RULECHECKER_BASE:$RULECHECKER_ROOT"
echo "  +CLASSPATH:$RULECHECKER_ROOT:$CLASSPATH"
echo "  +RULECHECKER_PREPROCESS_EXT:i"
echo "  +RULECHECKER_VIOLATION_EXT:viol"

echo "TOOL:cppunit:"
eval "echo \"  +CPPUNIT_BASE:\${CPPUNIT_ROOT}\""
eval "echo \"  +PATH:\${CPPUNIT_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${CPPUNIT_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${CPPUNIT_ROOT}/include\""

echo "TOOL:qt:"
eval "echo \"  +QT_BASE:\${QT_ROOT}\""
eval "echo \"  +PATH:\${QT_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${QT_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${QT_ROOT}/include\""

echo "TOOL:soqt:"
eval "echo \"  +SOQT_BASE:\${SOQT_ROOT}\""
eval "echo \"  +PATH:\${SOQT_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${SOQT_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${SOQT_ROOT}/include\""

echo "TOOL:coin3d:"
eval "echo \"  +COIN3D_BASE:\${COIN_ROOT}\""
eval "echo \"  +PATH:\${COIN_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${COIN_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${COIN_ROOT}/include\""

echo "TOOL:curl:"
eval "echo \"  +CURL_BASE:\${CURL_ROOT}\""
eval "echo \"  +PATH:\${CURL_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${CURL_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${CURL_ROOT}/include\""

echo "TOOL:jpeg:"
echo "  +JPEG_BASE:$LIBJPG_ROOT"

echo "TOOL:png:"
echo "  +PNG_BASE:$LIBPNG_ROOT"

echo "TOOL:tiff:"
echo "  +TIFF_BASE:$LIBTIFF_ROOT"

echo "TOOL:simage:"
eval "echo \"  +SIMAGE_BASE:\${SIMAGE_ROOT}\""
eval "echo \"  +PATH:\${SIMAGE_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${SIMAGE_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${SIMAGE_ROOT}/include\""

echo "TOOL:openssl:"
eval "echo \"  +OPENSSL_BASE:\${OPENSSL_ROOT}\""
eval "echo \"  +PATH:\${OPENSSL_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${OPENSSL_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${OPENSSL_ROOT}/include\""

echo "TOOL:expat:"
eval "echo \"  +EXPAT_BASE:\${EXPAT_ROOT}\""
eval "echo \"  +PATH:\${EXPAT_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${EXPAT_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${EXPAT_ROOT}/include\""

echo "TOOL:frontier_client:"
eval "echo \"  +FRONTIER_CLIENT_BASE:\${FRONTIER_CLIENT_ROOT}\""
eval "echo \"  +PATH:\${FRONTIER_CLIENT_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${FRONTIER_CLIENT_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${FRONTIER_CLIENT_ROOT}/include\""

echo "TOOL:genser:"
eval "echo \"  +GENSER_BASE:\${GENSER_ROOT}\""
eval "echo \"  +PATH:\${GENSER_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${GENSER_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${GENSER_ROOT}/include\""

echo "TOOL:pythia6:"
eval "echo \"  +PYTHIA6_BASE:\${PYTHIA6_ROOT}\""
eval "echo \"  +LIBDIR:\${PYTHIA6_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${PYTHIA6_ROOT}/include\""

echo "TOOL:pythia8:"
eval "echo \"  +PYTHIA8_BASE:\${PYTHIA8_ROOT}\""
eval "echo \"  +LIBDIR:\${PYTHIA8_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${PYTHIA8_ROOT}/include\""

echo "TOOL:jimmy:"
eval "echo \"  +JIMMY_BASE:\${JIMMY_ROOT}\""
eval "echo \"  +LIBDIR:\${JIMMY_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${JIMMY_ROOT}/include\""

echo "TOOL:toprex421:"
eval "echo \"  +TOPREX421_BASE:\${TOPREX421_ROOT}\""
eval "echo \"  +PATH:\${TOPREX421_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${TOPREX421_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${TOPREX421_ROOT}/include\""

echo "TOOL:tauola27_121_1:"
eval "echo \"  +TAUOLA27_121_1_BASE:\${TAUOLA27_121_1_ROOT}\""
eval "echo \"  +PATH:\${TAUOLA27_121_1_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${TAUOLA27_121_1_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${TAUOLA27_121_1_ROOT}/include\""

echo "TOOL:charybdis1_002:"
eval "echo \"  +CHARYBDIS1_002_BASE:\${CHARYBDIS1_002_ROOT}\""
eval "echo \"  +PATH:\${CHARYBDIS1_002_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${CHARYBDIS1_002_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${CHARYBDIS1_002_ROOT}/include\""

echo "TOOL:herwig:"
eval "echo \"  +HERWIG_BASE:\${HERWIG_ROOT}\""
eval "echo \"  +LIBDIR:\${HERWIG_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${HERWIG_ROOT}/include\""

echo "TOOL:lhapdf:"
eval "echo \"  +LHAPDF_BASE:\${LHAPDF_ROOT}\""
eval "echo \"  +LHAPATH:\${LHAPDF_ROOT}/PDFsets\""
eval "echo \"  +LIBDIR:\${LHAPDF_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${LHAPDF_ROOT}/include\""

echo "TOOL:hector:"
eval "echo \"  +HECTOR_BASE:\${HECTOR_ROOT}\""
eval "echo \"  +LIBDIR:\${HECTOR_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${HECTOR_ROOT}/include\""

echo "TOOL:tkonlinesw:"
eval "echo \"  +TKONLINESW_BASE:\${TKONLINESW_ROOT}\""
eval "echo \"  +PATH:\${TKONLINESW_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${TKONLINESW_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${TKONLINESW_ROOT}/include\""

echo "TOOL:doxygen:"
eval "echo \"  +DOXYGEN_BASE:\${DOXYGEN_ROOT}\""
eval "echo \"  +PATH:\${DOXYGEN_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${DOXYGEN_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${DOXYGEN_ROOT}/include\""

echo "TOOL:meschach:"
eval "echo \"  +MESCHACH_BASE:\${MESCHACH_ROOT}\""
eval "echo \"  +PATH:\${MESCHACH_ROOT}/bin\""
eval "echo \"  +LIBDIR:\${MESCHACH_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${MESCHACH_ROOT}/include\""

echo "TOOL:fastjet:"
eval "echo \"  +FASTJET_BASE:\${FASTJET_ROOT}\""
eval "echo \"  +LIBDIR:\${FASTJET_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${FASTJET_ROOT}/include\""

echo "TOOL:ktjet:"
eval "echo \"  +KTJET_BASE:\${KTJET_ROOT}\""
eval "echo \"  +LIBDIR:\${KTJET_ROOT}/lib\""
eval "echo \"  +INCLUDE:\${KTJET_ROOT}/include\""

echo "TOOL:glimpse:"
eval "echo \"  +GLIMPSE_BASE:\${GLIMPSE_ROOT}\""
eval "echo \"  +PATH:\${GLIMPSE_ROOT}/bin\""

echo "TOOL:elementtree:"
echo "  +ELEMENTTREE_BASE:$ELEMENTTREE_ROOT"
echo "  +ELEMENTTREE_PYPATH:$ELEMENTTREE_ROOT/python$(echo $PYTHON_VERSION | cut -d. -f1,2)/site-packages"

echo "TOOL:CMSSWData:"
echo "  +CMSSWDATA_BASE:%{instroot}/%{cmsplatf}/cms"

echo "TOOL:valgrind:"
echo "  +VALGRIND_BASE:$VALGRIND_ROOT"

) > tools.conf
%install
mkdir %i/configurations/
cp tools.conf %i/configurations/tools-STANDALONE.conf
%post
%{relocateConfig}configurations/tools-STANDALONE.conf
#
