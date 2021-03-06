# Copyright 2014 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'sources': [
    'src/celt/arm/fixed_armv4.h',
    'src/celt/arm/fixed_armv5e.h',
    'src/celt/arm/kiss_fft_armv4.h',
    'src/celt/arm/kiss_fft_armv5e.h',
    'src/silk/arm/SigProc_FIX_armv4.h',
    'src/silk/arm/SigProc_FIX_armv5e.h',
  ],
  'conditions': [
    ['winrt_platform=="win_phone" or winrt_platform=="win10_arm"', {
      'sources': [
        'src/celt/arm/pitch_arm.h',
        'src/silk/arm/macros_armv4.h',
        'src/silk/arm/macros_armv5e.h',
      ],
    },{
      'sources': [
        'src/celt/pitch_arm.h',
        'src/silk/arm/macro_armv4.h',
        'src/silk/arm/macro_armv5e.h',
      ],
    }] 
  ],
}
