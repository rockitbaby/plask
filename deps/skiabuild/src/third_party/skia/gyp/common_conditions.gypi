# conditions used in both common.gypi and skia.gyp in chromium
#
{
  'conditions' : [

    ['skia_os == "win"',
      {
        'defines': [
          'SK_BUILD_FOR_WIN32',
          'SK_IGNORE_STDINT_DOT_H',
          '_CRT_SECURE_NO_WARNINGS',
        ],
        'msvs_cygwin_shell': 0,
        'msvs_settings': {
          'VCCLCompilerTool': {
            'WarningLevel': '1',
            'WarnAsError': 'false',
            'DebugInformationFormat': '3',
            'AdditionalOptions': [ '/MP' ],
          },
          'VCLinkerTool': {
            'AdditionalDependencies': [
              'OpenGL32.lib',
              'usp10.lib',
            ],
          },
        },
        'configurations': {
          'Debug': {
            'msvs_settings': {
              'VCCLCompilerTool': {
                'DebugInformationFormat': '4', # editAndContiue (/ZI)
                'ProgramDataBaseFileName': '$(OutDir)\\$(ProjectName).pdb',
                'Optimization': '0',           # optimizeDisabled (/Od)
                'PreprocessorDefinitions': ['_DEBUG'],
                'RuntimeLibrary': '3',         # rtMultiThreadedDebugDLL (/MDd)
                'ExceptionHandling': '0',
                'RuntimeTypeInfo': 'false',      # /GR-
                'WarningLevel': '3',             # level3 (/W3)
              },
              'VCLinkerTool': {
                'GenerateDebugInformation': 'true', # /DEBUG
                'LinkIncremental': '2',             # /INCREMENTAL
              },
            },
          },
          'Release': {
            'msvs_settings': {
              'VCCLCompilerTool': {
                'DebugInformationFormat': '3',   # programDatabase (/Zi)
                'ProgramDataBaseFileName': '$(OutDir)\\$(ProjectName).pdb',
                'Optimization': '3',             # full (/Ox)
                'WholeProgramOptimization': 'true', #/GL
               # Changing the floating point model requires rebaseling gm images
               #'FloatingPointModel': '2',       # fast (/fp:fast)
                'FavorSizeOrSpeed': '1',         # speed (/Ot)
                'PreprocessorDefinitions': ['NDEBUG'],
                'RuntimeLibrary': '2',           # rtMultiThreadedDLL (/MD)
                'ExceptionHandling': '0',
                'RuntimeTypeInfo': 'false',      # /GR-
                'WarningLevel': '3',             # level3 (/W3)
              },
              'VCLinkerTool': {
                'GenerateDebugInformation': 'true', # /DEBUG
                'LinkTimeCodeGeneration': '1',      # useLinkTimeCodeGeneration /LTCG
              },
              'VCLibrarianTool': {
                'LinkTimeCodeGeneration': 'true',   # useLinkTimeCodeGeneration /LTCG
              },
            },
          },
        },
      },
    ],

    ['skia_os in ["linux", "freebsd", "openbsd", "solaris"]',
      {
        'defines': [
          'SK_SAMPLES_FOR_X',
          'SK_BUILD_FOR_UNIX',
        ],
        'configurations': {
          'Debug': {
            'cflags': ['-g']
          },
          'Release': {
            'cflags': ['-O2']
          },
        },
        'cflags': [ '-Wall', '-Wextra', '-Wno-unused' ],
        'include_dirs' : [
          '/usr/include/freetype2',
        ],
      },
    ],

    ['skia_os == "mac"', 
      {
        'defines': [
          'SK_BUILD_FOR_MAC',
        ],
        'configurations': {
          'Debug': {
            'xcode_settings': {
              'GCC_OPTIMIZATION_LEVEL': '0',
            },
          },
          'Release': {
            'xcode_settings': {
              'GCC_OPTIMIZATION_LEVEL': '3',
            },
          },
        },
        'xcode_settings': {
          'SYMROOT': '<(DEPTH)/xcodebuild',
          'SDKROOT': 'macosx10.6',
        },
      },
    ],

    ['skia_os == "ios"', 
      {
        'defines': [
          'SK_BUILD_FOR_IOS',
        ],
        'configurations': {
          'Debug': {
            'xcode_settings': {
              'GCC_OPTIMIZATION_LEVEL': '0',
            },
          },
        },
        'xcode_settings': {
          'SYMROOT': '<(DEPTH)/xcodebuild',
        },
      },
    ],

  ], # end 'conditions'
}

# Local Variables:
# tab-width:2
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=2 shiftwidth=2: