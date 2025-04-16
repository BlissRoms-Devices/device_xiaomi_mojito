#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'hardware/qcom-caf/sm8150',
    'hardware/xiaomi',
    'vendor/qcom/opensource/display',
    'vendor/xiaomi/sm6150-common',
]

def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'com.fingerprints.extension@1.0',
        'vendor.qti.hardware.camera.device@1.0',
    ): lib_fixup_vendor_suffix,
}

blob_fixups: blob_fixups_user_type = {
    'vendor/etc/sensors/hals.conf': blob_fixup()
         .regex_replace('sensors.touch.detect.so\n',''),
    'vendor/lib64/camera/components/com.qti.node.watermark.so': blob_fixup()
         .add_needed('libpiex_shim.so'),
}

module = ExtractUtilsModule(
     'mojito',
     'xiaomi',
     blob_fixups=blob_fixups,
     lib_fixups=lib_fixups,
     namespace_imports=namespace_imports,
 )

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm6150-common', module.vendor
    )
    utils.run()
