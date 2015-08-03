from distutils.core import setup
import py2exe, innosetup
import sys
# sys.argv.append('py2exe')
sys.argv.append('innosetup')
sys.path.append("C:\\lhq\\template-engine\\template-engine")
sys.path.append("template-engine")

py2exe_options = {
        "includes": ["sip", ],
        "dll_excludes": ["MSVCP90.dll",],
        "compressed": 1,
        "optimize": 2,
        "ascii": 0,
        # "bundle_files": 1,
        }

innosetup_options = {
        # user defined iss file path or iss stringi
        'inno_script': innosetup.DEFAULT_ISS, # default is ''
        # bundle msvc files
        'bundle_vcr': True, # default is True
        # zip setup file
        'zip': False, # default is False, bool() or zip file name
        # create shortcut to startup if you want.
        'regist_startup': True, # default is False
}

setup(
      name = 'PyQt Demo',
      version = '1.0',
      license = "PSF",
      author = "lhq",
      author_email = '415200973@qq.com',
      description = 'haha',
      url='www.baidu.com',
      # windows=[{"script":"template-engine/MainWindow.py"}],
      zipfile = None,
      options = {'py2exe': py2exe_options, 'innosetup': innosetup_options},
      data_files=[("action",
                   ["action_data/animation_opacity.json",
                    "action_data/animation_straightline.json",
                    "action_data/layer_layer.json",
                    "action_data/segment_segment.json",
                    "action_data/settings.json",
                    "action_data/subtitle_subtitle.json",
                   ]),
                  ],
      )