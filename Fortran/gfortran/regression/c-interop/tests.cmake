# This file was generated by update-test-config.py
#
# Each line in this file corresponds to a single test. The format of each line
# is:
#
#     <kind>;<sources>;<xfail>;<options>;<enabled-on>;<disabled-on>
#
# where
#
#     <kind>         is one of 'preprocess', 'assemble', 'compile', 'link' or
#                    'run'.
#
#     <sources>      is a space separated list of sources files that comprise
#                    the test. The first file is the "main" file. The rest
#                    of the files must be specified in program compilation
#                    order.
#
#     <xfail>        if present, must be 'xfail' which indicates that the test
#                    is expected to trigger a compile-time or runtime error.
#
#     <options>      is a space separated list of options to be passed to the
#                    compiler when building the test.
#
#     <enabled-on>   is a space-separated list of targets on which the test is
#                    enabled. Each element of the list will be a regular
#                    expression that is expected to match an LLVM target triple.
#                    If no targets are provided, the test is enabled on all
#                    targets.
#
#     <disabled-on>  is a space-separated list of targets on which the test is
#                    disabled. Each element of the list will be a regular
#                    expression that is expected to match an LLVM target triple.
#
compile;allocatable-optional-pointer.f90;;;;
compile;assumed-type-dummy.f90;xfail;;;
compile;c1255-1.f90;;;;
compile;c1255-2.f90;xfail;;;
compile;c1255a.f90;xfail;;;
compile;c407a-1.f90;;;;
compile;c407a-2.f90;xfail;-fcoarray=single;;
compile;c407b-1.f90;;;;
compile;c407b-2.f90;xfail;;;
compile;c407c-1.f90;xfail;;;
compile;c516.f90;xfail;;;
compile;c524a.f90;xfail;-fcoarray=single;;
compile;c535a-1.f90;;;;
compile;c535a-2.f90;xfail;-fcoarray=single;;
compile;c535b-1.f90;;-fcoarray=single;;
compile;c535b-2.f90;xfail;-fcoarray=single;;
compile;c535b-3.f90;xfail;-fcoarray=single;;
compile;c535c-1.f90;xfail;;;
compile;c535c-2.f90;xfail;;;
compile;c535c-3.f90;xfail;;;
compile;c535c-4.f90;xfail;;;
compile;deferred-character-1.f90;xfail;;;
compile;explicit-interface.f90;xfail;;;
compile;fc-descriptor-pr108621.f90;;-fdump-tree-original;;
compile;pr103287-1.f90;xfail;;;
compile;pr103287-2.f90;xfail;;;
compile;removed-restrictions-1.f90;;;;
compile;removed-restrictions-2.f90;;;;
compile;removed-restrictions-3.f90;;;;
compile;removed-restrictions-4.f90;;;;
compile;tkr.f90;xfail;;;
run;allocatable-dummy.f90 allocatable-dummy-c.c dump-descriptors.c;;-g;;
run;allocate-errors.f90 allocate-errors-c.c dump-descriptors.c;;-Wno-error -fcheck=all;;
run;allocate.f90 allocate-c.c dump-descriptors.c;;-g;;
run;argument-association-assumed-rank-1.f90;;;;
run;argument-association-assumed-rank-2.f90;;;;
run;argument-association-assumed-rank-3.f90;;;;
run;argument-association-assumed-rank-4.f90;;;;
run;argument-association-assumed-rank-5.f90;;;;
run;argument-association-assumed-rank-6.f90;;;;
run;argument-association-assumed-rank-7.f90;;;;
run;argument-association-assumed-rank-8.f90;;;;
run;cf-descriptor-1.f90 cf-descriptor-1-c.c dump-descriptors.c;;;;
run;cf-descriptor-2.f90 cf-descriptor-2-c.c dump-descriptors.c;;;;
run;cf-descriptor-3.f90 cf-descriptor-3-c.c dump-descriptors.c;;-g;;
run;cf-descriptor-4.f90 cf-descriptor-4-c.c dump-descriptors.c;;-g;;
run;cf-descriptor-5.f90 cf-descriptor-5-c.c dump-descriptors.c;;-g;;
run;cf-descriptor-6.f90 cf-descriptor-6-c.c dump-descriptors.c;;;;
run;cf-descriptor-7.f90 cf-descriptor-7-c.c dump-descriptors.c;;;;
run;cf-descriptor-8.f90 cf-descriptor-8-c.c dump-descriptors.c;;;;
run;cf-out-descriptor-1.f90 cf-out-descriptor-1-c.c dump-descriptors.c;;;;
run;cf-out-descriptor-2.f90 cf-out-descriptor-2-c.c dump-descriptors.c;;;;
run;cf-out-descriptor-3.f90 cf-out-descriptor-3-c.c dump-descriptors.c;;-g;;
run;cf-out-descriptor-4.f90 cf-out-descriptor-4-c.c dump-descriptors.c;;-g;;
run;cf-out-descriptor-5.f90 cf-out-descriptor-5-c.c dump-descriptors.c;;-g;;
run;cf-out-descriptor-6.f90 cf-out-descriptor-6-c.c dump-descriptors.c;;-g;;
run;contiguous-1.f90 contiguous-1-c.c dump-descriptors.c;;-g;;
run;contiguous-2.f90 contiguous-2-c.c dump-descriptors.c;;-g;;
run;contiguous-3.f90 contiguous-3-c.c dump-descriptors.c;;-g;;
run;deferred-character-2.f90;;;;
run;establish-errors.f90 establish-errors-c.c dump-descriptors.c;;-Wno-error -fcheck=all;;
run;establish.f90 establish-c.c dump-descriptors.c;;-g;;
run;fc-descriptor-1.f90 fc-descriptor-1-c.c dump-descriptors.c;;-g;;
run;fc-descriptor-2.f90 fc-descriptor-2-c.c dump-descriptors.c;;-g;;
run;fc-descriptor-3.f90 fc-descriptor-3-c.c dump-descriptors.c;;-g;;
run;fc-descriptor-4.f90 fc-descriptor-4-c.c dump-descriptors.c;;-g;;
run;fc-descriptor-5.f90 fc-descriptor-5-c.c dump-descriptors.c;;-g;;
run;fc-descriptor-6.f90 fc-descriptor-6-c.c dump-descriptors.c;;-g;;
run;fc-descriptor-7.f90 fc-descriptor-7-c.c dump-descriptors.c;;-g;;
run;fc-descriptor-8.f90 fc-descriptor-8-c.c dump-descriptors.c;;;;
run;fc-descriptor-9.f90 fc-descriptor-9-c.c dump-descriptors.c;;;;
run;fc-out-descriptor-1.f90 fc-out-descriptor-1-c.c dump-descriptors.c;;-g;;
run;fc-out-descriptor-2.f90 fc-out-descriptor-2-c.c dump-descriptors.c;;-g;;
run;fc-out-descriptor-3.f90 fc-out-descriptor-3-c.c dump-descriptors.c;;-g;;
run;fc-out-descriptor-4.f90 fc-out-descriptor-4-c.c dump-descriptors.c;;-g;;
run;fc-out-descriptor-5.f90 fc-out-descriptor-5-c.c dump-descriptors.c;;;;
run;fc-out-descriptor-6.f90 fc-out-descriptor-6-c.c dump-descriptors.c;;-g;;
run;fc-out-descriptor-7.f90 fc-out-descriptor-7-c.c dump-descriptors.c;;-g;;
run;ff-descriptor-1.f90;;;;
run;ff-descriptor-2.f90;;;;
run;ff-descriptor-3.f90;;;;
run;ff-descriptor-4.f90;;;;
run;ff-descriptor-5.f90;;;;
run;ff-descriptor-6.f90;;;;
run;ff-descriptor-7.f90;;;;
run;note-5-3.f90;;;;
run;note-5-4.f90 note-5-4-c.c;;;;
run;optional.f90 optional-c.c dump-descriptors.c;;-g;;
run;pr103390-1.f90;;-fdump-tree-original;;
run;pr103390-2.f90;;-fdump-tree-original;;
run;pr103390-3.f90;;-fdump-tree-original;;
run;pr103390-4.f90;;-fdump-tree-original;;
run;pr103390-5.f90;;-fdump-tree-original;;
run;pr103390-6.f90;;-fdump-tree-original;;
run;pr103390-7.f90;;-fdump-tree-original;;
run;pr103390-8.f90;;-fdump-tree-original;;
run;pr103390-9.f90;;-fdump-tree-original;;
run;rank-class.f90;;;;
run;rank.f90;;;;
run;section-1.f90 section-1-c.c dump-descriptors.c;;-g;;
run;section-1p.f90 section-1-c.c dump-descriptors.c;;-g;;
run;section-2.f90 section-2-c.c dump-descriptors.c;;-g;;
run;section-2p.f90 section-2-c.c dump-descriptors.c;;-g;;
run;section-3.f90 section-3-c.c dump-descriptors.c;;-g;;
run;section-3p.f90 section-3-c.c dump-descriptors.c;;-g;;
run;section-4.f90 section-4-c.c dump-descriptors.c;;-g;;
run;section-errors.f90 section-errors-c.c dump-descriptors.c;;-Wno-error -fcheck=all;;
run;select-errors.f90 select-errors-c.c dump-descriptors.c;;-Wno-error -fcheck=all;;
run;select.f90 select-c.c dump-descriptors.c;;;;
run;setpointer-errors.f90 setpointer-errors-c.c dump-descriptors.c;;-Wno-error -fcheck=all;;
run;setpointer.f90 setpointer-c.c dump-descriptors.c;;;;
run;shape-bindc.f90;;;;
run;shape-poly.f90;;;;
run;shape.f90;;;;
run;size-bindc.f90;;;;
run;size-poly.f90;;;;
run;size.f90;;;;
run;typecodes-array-basic.f90 typecodes-array-basic-c.c dump-descriptors.c;;-g;;
run;typecodes-array-char.f90 typecodes-array-char-c.c dump-descriptors.c;;-g;;
run;typecodes-array-float128.f90 typecodes-array-float128-c.c dump-descriptors.c;;-g;;
run;typecodes-array-int128.f90 typecodes-array-int128-c.c dump-descriptors.c;;-g;;
run;typecodes-array-longdouble.f90 typecodes-array-longdouble-c.c dump-descriptors.c;;-g;;
run;typecodes-sanity.f90 typecodes-sanity-c.c;;-g;;
run;typecodes-scalar-basic.f90 typecodes-scalar-basic-c.c dump-descriptors.c;;-g;;
run;typecodes-scalar-float128.f90 typecodes-scalar-float128-c.c dump-descriptors.c;;-g;;
run;typecodes-scalar-int128.f90 typecodes-scalar-int128-c.c dump-descriptors.c;;-g;;
run;typecodes-scalar-longdouble.f90 typecodes-scalar-longdouble-c.c dump-descriptors.c;;-g;;
run;ubound-bindc.f90;;;;
run;ubound-poly.f90;;;;
run;ubound.f90;;;;